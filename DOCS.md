# Documentation :
## rational
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