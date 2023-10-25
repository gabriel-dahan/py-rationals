$\text{Formule de transformation de rationnels sous leur écriture fractionnaire.}$

Soit $\Delta$ la fonction qui à tout $n\in\mathbb{N}$ associe la représentation sous forme de fraction du nombre $0.\overline{n}\in\mathbb{Q}$.

$$\boxed{\Delta\underset{\text{def}}=\left(n\mapsto\frac{n}{10^{\lceil\log_{10}(n)\rceil}-1}\right)}$$

---

__Démonstration :__

Soit $q=0.\overline{n}$ et $c\in\mathbb{N}$ le nombre de chiffres de $n$.
$$10^{c-1}<n<10^c$$
$$\log_{10}(10^{c-1})<log_{10}(n)<\log_{10}(10^{c})$$
$$c-1<log_{10}(n)<c$$
On en déduit que $c$ est l'entier directement supérieur à $\log_{10}(n)$, d'où $c=\lceil\log_{10}(n)\rceil$.

$$q=0.\overline{n}$$
$$10^cq=n.\overline{n}=n+q$$
$$10^{\lceil\log_{10}(n)\rceil}q=n+q$$
$$q=\frac{n}{10^{\lceil\log_{10}(n)\rceil}-1}=\Delta(n)$$

---

On en déduit que n'importe quel rationnel peut être écrit en fonction de $\Delta(n)$.

*Exemples* : 
- $2.\overline{37}=2+\Delta(37)$
- $8.133\overline{9}=8+\Delta(9)\cdot 10^{-3}$