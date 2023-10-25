""" 
    Exemple d'exercice de travail sur les fractions pouvant utiliser la classe `rational` :

    |  L'application f prend un rationnel x, écrit son écriture décimale et remplace tous les 5 par des 4,
    |  et le remet sous forme rationnelle.
    |    1) Ecrire cette fonction en Python (à l'aide de rational).
    |    2) Calculer f(1/2), f(1/4), f(17/14). 
    |    3) Combien l'équation f(x)=73/495 a-t-elle de solutions ? Combien l'équation f(x)=541/990 a-t-elle de solutions ?
"""

from typing import List
from rationals import rational
from random import randint

# -- Veillez à avoir installé la suivante pour lancer ce fichier :
from prettytable import PrettyTable

# -- 1) --
def f(x: rational, replace: tuple = (5, 4)) -> rational:
    dec = x.as_decimal()

    new_dec = str(dec[0]).replace(str(replace[0]), str(replace[1]))
    new_dec = float(new_dec) if isinstance(dec[0], float) else int(new_dec)

    new_period = int(str(dec[1]).replace(str(replace[0]), str(replace[1])))

    return rational.from_decimal(new_dec, new_period)

# -- 2) --
def question_2():
    Lx: List[rational] = [
        rational(1, 2),
        rational(1, 4),
        rational(17, 14),
        rational(12, 33)
    ]

    pt = PrettyTable()
    pt.field_names = ['x', 'f(x)']
    pt.add_rows([[f'{x}', f'{f(x)}'] for x in Lx])
    print(pt.get_string())

# -- 3) --
def question_3():
    Lx: List[rational] = [
        rational(73, 495),
        rational(541, 990)
    ]
    
    pt = PrettyTable()
    pt.field_names = ['f(x)', 'x']
    pt.add_rows([[f'{x}', f'{f(x, (4, 5))}'] for x in Lx])
    print(pt.get_string())

if __name__ == '__main__':
    print(rational(7, 8) + 1.65)