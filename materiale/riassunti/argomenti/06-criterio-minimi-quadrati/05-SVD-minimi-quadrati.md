# Risoluzione dei Minimi Quadrati tramite SVD

Consideriamo il problema

$$
\boxed{
\min_{\alpha\in\mathbb R^n}
\|A\alpha-y\|_2^2
}
$$

e supponiamo di avere

$$
A=U\Sigma V^T
$$

Sostituendo la SVD otteniamo

$$
\|A\alpha-y\|_2^2
=
\|U\Sigma V^T\alpha-y\|_2^2
$$

Poiché $U$ è ortogonale, possiamo moltiplicare per $U^T$ senza modificare la norma:

$$
\begin{aligned}
\|A\alpha-y\|_2^2
&=
\|U^T(U\Sigma V^T\alpha-y)\|_2^2\\
&=
\|\Sigma V^T\alpha-U^Ty\|_2^2
\end{aligned}
$$

Introduciamo

$$
\boxed{
\gamma=V^T\alpha
}
$$

e

$$
\boxed{
z=U^Ty
}
$$

Il problema diventa

$$
\boxed{
\|\Sigma\gamma-z\|_2^2
}
$$

Abbiamo quindi trasformato il problema originale in un problema più semplice, nel quale la matrice $\Sigma$ è diagonale.

## Espansione del problema

Poiché $A$ ha rango $k$, i primi $k$ valori singolari sono positivi e quelli successivi sono nulli.

Pertanto

$$
\Sigma\gamma
=
\begin{pmatrix}
\sigma_1\gamma_1\\
\sigma_2\gamma_2\\
\vdots\\
\sigma_k\gamma_k\\
0\\
\vdots\\
0
\end{pmatrix}
$$

e quindi

$$
\Sigma\gamma-z
=
\begin{pmatrix}
\sigma_1\gamma_1-z_1\\
\sigma_2\gamma_2-z_2\\
\vdots\\
\sigma_k\gamma_k-z_k\\
-z_{k+1}\\
\vdots\\
-z_m
\end{pmatrix}
$$

La norma quadratica diventa

$$
\begin{aligned}
\|\Sigma\gamma-z\|_2^2
&=
\sum_{i=1}^{k}
(\sigma_i\gamma_i-z_i)^2
+
\sum_{i=k+1}^{m}z_i^2
\end{aligned}
$$

Il secondo termine dipende esclusivamente dai dati e non può essere modificato scegliendo $\gamma$.

Per minimizzare il primo termine imponiamo

$$
\sigma_i\gamma_i-z_i=0
$$

per $i=1,\dots,k$.

Poiché $\sigma_i>0$,

$$
\boxed{
\gamma_i=\frac{z_i}{\sigma_i},
\qquad i=1,\dots,k
}
$$

Le componenti

$$
\gamma_{k+1},\dots,\gamma_n
$$

non compaiono nel valore di $\Sigma\gamma$, perché vengono moltiplicate dai valori singolari nulli.

Di conseguenza, se $k<n$, esistono infinite soluzioni minimizzanti.

## Soluzione a norma minima

Le componenti

$$
\gamma_{k+1},\dots,\gamma_n
$$

sono libere. Possiamo quindi scegliere

$$
\gamma=
\begin{pmatrix}
\dfrac{z_1}{\sigma_1}\\
\dfrac{z_2}{\sigma_2}\\
\vdots\\
\dfrac{z_k}{\sigma_k}\\
\gamma_{k+1}\\
\vdots\\
\gamma_n
\end{pmatrix}
$$

e ricavare $\alpha$ dalla relazione

$$
\gamma=V^T\alpha
$$

Poiché $V$ è ortogonale,

$$
V^TV=I
$$

e quindi

$$
\boxed{
\alpha=V\gamma
}
$$

Tra tutte le soluzioni minimizzanti scegliamo normalmente quella di **norma euclidea minima**.

Per ottenerla poniamo a zero tutte le componenti libere:

$$
\boxed{
\gamma=
\begin{pmatrix}
\dfrac{z_1}{\sigma_1}\\
\dfrac{z_2}{\sigma_2}\\
\vdots\\
\dfrac{z_k}{\sigma_k}\\
0\\
\vdots\\
0
\end{pmatrix}
}
$$

La scelta delle componenti libere nulle minimizza $\|\gamma\|_2$. Poiché $V$ è ortogonale,

$$
\|\alpha\|_2
=
\|V\gamma\|_2
=
\|\gamma\|_2
$$

e quindi minimizzare la norma di $\gamma$ equivale a minimizzare la norma di $\alpha$.

La soluzione di norma minima è dunque

$$
\boxed{
\alpha_{\min}=V\gamma
}
$$

con

$$
\gamma_i=
\begin{cases}
\dfrac{z_i}{\sigma_i}, & i=1,\dots,k\\
0, & i=k+1,\dots,n
\end{cases}
$$

Se $A$ ha rango pieno sulle colonne, cioè $k=n$, non ci sono componenti libere e la soluzione dei minimi quadrati è unica.

## Schema della soluzione tramite SVD

Data

$$
A=U\Sigma V^T
$$

il problema

$$
\min_\alpha\|A\alpha-y\|_2^2
$$

può essere risolto in tre passaggi:

$$
\boxed{
1
.\quad z=U^Ty
,\qquad
\gamma=V^T\alpha
\qquad\Rightarrow\qquad
\|\Sigma\gamma-z\|_2^2
}
$$

$$
\boxed{
2.\quad
\gamma_i=
\frac{z_i}{\sigma_i}
\quad i=1,\dots,k,
\qquad
\gamma_i=0
\quad i=k+1,\dots,n
}
$$

$$
\boxed{
3.\quad \alpha=V\gamma
}
$$

Il risultato è la soluzione ai minimi quadrati di **norma euclidea minima**.

---