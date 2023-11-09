# Documentation
## Rationals
### Initialisation

```py
>>> from rationals import rational
>>> r = rational(1, 2) # Numérateur : 1, Dénominateur : 2
>>> print(r)
1/2 = 0.5[0]
>>> print(rational(1, 3))
1/3 = 0.[3]
```


### Opérations

#### Addition / soustraction
```py
>>> rational(1, 2) + rational(1, 3)
rational(5, 6)
>>> 2 - rational(1, 5)
rational(9, 5)
>>> rational(7, 8) + 1.65
rational(101, 40)
```

#### Multiplication / division
```py
>>> rational(1, 2) * rational(1, 3)
rational(1, 6)
>>> 9 / rational(1, 9)
rational(81, 1)
>>> rational(3, 4) / 1.3
rational(15, 26)
```

#### Exponentiation
```py
>>> rational(1, 2) ** 3
rational(1, 8)
>>> 2 ** rational(1, 2)
1.4142135623730951 # Ce n'est plus rationnel, donc converti en float.
```

### Méthodes

#### Transformer un rationnel écrit sous sa forme décimale en sa forme fractionnaire.
@classmethod
`rational.from_decimal(d: float | int, period: int = 0)`

Prend en paramètres une partie (entière ou décimale) `d` et une période `period`. Si le rationnel considéré n'a pas de partie infinie, alors `period=0`.
```python
>>> rational.from_decimal(1.45, 6) # 1.456666...
rational(437, 300) # 437/300=1.45666...
```

#### Obtenir la partie décimale et la période d'un rationnel écrit sous sa forme fractionnaire.

`.as_decimal()`

Ne prend pas de paramètre, renvoie un tuple contenant la partie décimale finie du rationnel et sa période s'il est infini.
```python
>>> rational(1, 3).as_decimal()
(1, 3)
>>> rational(7, 30).as_decimal() 
(0.2, 3) # 7/30 = 0.2333...
```