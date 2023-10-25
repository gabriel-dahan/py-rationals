from typing import List

""" 
    Exemple d'exercice de travail sur les fractions pouvant utiliser la classe `rational` :
    
    Exercice :
    |  L'application f prend un rationnel x, écrit son écriture décimale, remplace tous les 5 par des 4
    |  et le remet sous forme rationnelle.
    |    1) Ecrire cette fonction en Python (à l'aide de rational).
    |    2) Calculer f(1/2), f(1/4), f(17/14). 
    |    3) Combien l'équation f(x)=73/495 a-t-elle de solutions ? Combien l'équation f(x)=541/990 a-t-elle de solutions ?
"""

# -- Pour lancer ce fichier, veillez à avoir installé la librairie suivante :
from prettytable import PrettyTable # pip install --user prettytable

from rationals import rational

# -- 1) --
# On s'autorise de rajouter un paramètre 'replace' à la fonction, spécifiant les valeurs à interchanger dans le développement décimal de x
# (on utilise ce paramètre dans la question 3, pour faire la réciproque de f en prenant replace = (4, 5)).
def f(x: rational, replace: tuple = (5, 4)) -> rational:
    a, b = replace
    dec, period = x.as_decimal() # Renvoie un tuple contenant la partie décimale finie de x et sa période si elle existe (sinon 0).

    new_dec = str(dec).replace(str(a), str(b))
    # Spécificité de mon implémentation : une partie décimale égale à 1 n'est pas égale à 1.0. La précision est prise en compte, ainsi rational(4, 3) = 4/3 = 1.333... != 1.0333...
    new_dec = float(new_dec) if isinstance(dec, float) else int(new_dec) 

    new_period = int(str(period).replace(str(a), str(b)))

    return rational.from_decimal(new_dec, new_period)

# -- 2) --
def question_2():
    # On fait une liste des valeurs à évaluer, puis on les évalue tout en les affichant dans un beau tableau créé par PrettyTable :)
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
    # De même que dans la question 2, à la seule différence ici qu'on prend la réciproque de f : replace = (4,5) à la place de (5, 4).
    # On répond alors implicitement à la question posée : il n'y a qu'une solution à n'importe quelle équation posée avec f.
    Lx: List[rational] = [
        rational(73, 495),
        rational(541, 990)
    ]
    
    pt = PrettyTable()
    pt.field_names = ['f(x)', 'x']
    pt.add_rows([[f'{x}', f'{f(x, (4, 5))}'] for x in Lx])
    print(pt.get_string())

if __name__ == '__main__':
    question_3()