from __future__ import annotations
from typing import Union, Tuple
from math import gcd, ceil, log10

AnyNum = Union['rational', Union[int, float]]

class rational(object):

    """ Classe permettant la représentation formelle et le calcul avec des rationnels, sous forme de fractions.
        REPO & DOCS : https://github.com/gabriel-dahan/py-rationals """

    def __init__(self, numerator: int, denominator: int) -> None:
        assert denominator != 0, 'Le dénominateur doit être non-nul.'

        self._num: int = numerator
        self._den: int = denominator
        self.__simplify()

    def __simplify(self) -> None:
        d = gcd(self._num, self._den) # gcd -> pgcd (en anglais)
        self._num //= d
        self._den //= d

    def __convert(self, entry: AnyNum) -> rational:
        if isinstance(entry, rational):
            return entry
        elif isinstance(entry, int):
            return rational(entry, 1)
        elif isinstance(entry, float):
            return rational.from_decimal(entry)

    def __add__(self, other: AnyNum) -> rational:
        other = self.__convert(other)
        return rational(
            self._num * other._den + other._num * self._den, 
            other._den * self._den
        )
    
    def __radd__(self, other: AnyNum) -> rational:
        return self + other
    
    def __mul__(self, other: AnyNum) -> rational:
        other = self.__convert(other)
        return rational(
            self._num * other._num,
            self._den * other._den
        )
    
    def __rmul__(self, other: AnyNum) -> rational:
        return self * other
    
    def __sub__(self, other: AnyNum) -> rational:
        other = self.__convert(other)
        return rational(
            self._num * other._den - other._num * self._den, 
            other._den * self._den
        )
    
    def __rsub__(self, other: AnyNum) -> rational:
        return -self + other
    
    def __div__(self, other: AnyNum) -> rational:
        other = self.__convert(other)
        return rational(
            self._num * other._den, 
            self._den * other._num
        )
    
    def __truediv__(self, other: AnyNum) -> rational:
        return self.__div__(other)
    
    def __rdiv__(self, other: AnyNum) -> rational:
        other = self.__convert(other)
        return rational(
            self._den * other._num,
            self._num * other._den
        )

    def __rtruediv__(self, other: AnyNum) -> rational:
        return self.__rdiv__(other)
    
    def __pow__(self, other: AnyNum) -> Union[rational, float]:
        if isinstance(other, int):
            return rational(self._num ** other, self._den ** other)
        elif isinstance(other, float):
            pnum, pden = self._num ** other, self._den ** other
            if float(int(pnum)) == pnum and float(int(pden)) == pden:
                return rational(int(pnum), int(pden))
        return float(self) ** float(other)
    
    def __rpow__(self, other: AnyNum) -> Union[rational, float]:
        return float(other) ** float(self)

    def __neg__(self) -> rational:
        return -1 * self
    
    def __lt__(self, other) -> bool:
        """ a < b """
        return float(self) < float(other)

    def __gt__(self, other) -> bool:
        """ a > b """
        return float(self) > float(other)

    def __le__(self, other) -> bool:
        """ a <= b """
        return float(self) <= float(other)

    def __ge__(self, other) -> bool:
        """ a >= b """
        return float(self) >= float(other)

    def __eq__(self, other) -> bool:
        return float(self) == float(other)

    def __repr__(self) -> str:
        return f'rational({self._num}, {self._den})'
    
    def __str__(self) -> str:
        d = self.as_decimal()
        return f'{self._num}/{self._den} = {d[0]}{"." if isinstance(d[0], int) else ""}[{d[1]}]'

    def __int__(self) -> int:
        return self._num // self._den

    def __float__(self) -> float:
        return self._num / self._den

    @classmethod
    def from_decimal(cls, d: Union[float, int], period: int = 0) -> rational:
        """ Renvoie l'écriture fractionnaire d'un rationnel depuis son écriture décimale.
            - d (float)  : nombre sous forme décimale.
            - period (int) : entier correspondant à la période du nombre rationnel si son développement décimal est infini (sinon 0). 
        """

        int_part = int(d)
        if isinstance(d, float):
            decimal_part = int(str(d).split('.')[1])
        else:
            decimal_part = -1

        if decimal_part in (-1, 0) and period == 0:
            return rational(int_part, 1)
        
        # ------
        # Pour mieux comprendre le code écrit ci-dessous, voir ma démonstration de la formule 
        # générale utilisée, écrite dans le fichier RATIONAL_FRAC.pdf.
        # ------
        
        if decimal_part > 1:
            c_dec = ceil(log10(decimal_part)) # Nombre de chiffres de la partie décimale
        elif decimal_part in (0, 1):
            c_dec = 1
        else:
            c_dec = 0

        if period > 0:

            c_rep = ceil(log10(period)) # Nombre de chiffres de la période

            frac = cls(period, 10 ** c_rep - 1) # Rationnel sans la partie entière.
            return d + frac / (10 ** c_dec)

        return cls(int_part * 10 ** c_dec + decimal_part, 10 ** c_dec)

    def get_period(self) -> Tuple[int, int]:
        """ Renvoie la période du rationnel considéré et la position dans la partie décimale à partir de laquelle la période commence. """
        last_remainder = self._num % self._den
        remainders = [last_remainder]
        while last_remainder not in remainders[:-1]:
            last_remainder = (last_remainder * 10) % self._den
            remainders.append(last_remainder)

        # On prend la liste des restes de la divison euclidienne depuis le premier élément qui s'est répété, jusqu'à la fin.
        # On obtient ainsi la liste des restes correspondant aux décimales de la période du nombre rationnel.
        period = ''
        start_remainder = remainders.index(remainders[-1])
        for remainder in remainders[start_remainder:-1]: 
            # Il ne reste qu'à effectuer la division entière de chacun de ces restes (multipliés par 10 !) 
            # par le diviseur pour obtenir chaque chiffre de la période de self.
            period += str((remainder * 10) // self._den)
        return int(period), start_remainder
    
    def as_decimal(self) -> Tuple[Union[float, int], int]:
        # Renvoie l'écriture sous forme décimale du rationnel, sous la forme d'un tuple contenant la partie finie et l'éventuelle période.
        period = self.get_period()
        as_float_str = str(float(self))
        # Compte le nombre de chiffres de la partie finie de self comme la somme du nombre de chiffres de la partie entière et de la position de début de la période. 
        finite_digits = ceil(log10(int(self) if self > 1 else 1)) + (period[1] + 1)
        finite_part_as_str = as_float_str[:finite_digits + 1] # Supprime tout ce qu'il y a à partir du début la période, ne gardant ainsi que la partie finie.

        s = finite_part_as_str.split('.')
        if len(s) == 1 or (len(s) == 2 and s[1] == ''):
            finite_part = int(s[0])
        else:
            finite_part = float(finite_part_as_str) 

        return (
            finite_part,
            period[0]
        )

if __name__ == '__main__':
    print(rational.from_decimal(1, 23).as_decimal())