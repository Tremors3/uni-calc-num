
# Decomposizione ai Valori Singolari (SVD)

La **decomposizione ai valori singolari**, o **SVD** (*Singular Value Decomposition*), si applica a qualunque matrice reale rettangolare.

Sia

$$
A\in\mathbb R^{m\times n}
$$

una matrice di rango $k$. Allora esistono matrici ortogonali $U$ e $V$ tali che

$$
\boxed{
A=U\Sigma V^T
}
$$

dove

$$
U\in\mathbb R^{m\times m},
\qquad
V\in\mathbb R^{n\times n}
$$

sono ortogonali e

$$
\Sigma\in\mathbb R^{m\times n}
$$

è una matrice diagonale rettangolare.

I valori sulla diagonale di $\Sigma$ sono i **valori singolari**:

$$
\sigma_1,\sigma_2,\dots,\sigma_k
$$

ordinati in modo decrescente:

$$
\boxed{
\sigma_1\ge\sigma_2\ge\dots\ge\sigma_k>0
}
$$

Gli eventuali valori singolari successivi sono nulli.

La matrice $\Sigma$ ha quindi la struttura

$$
\Sigma=
\begin{pmatrix}
\sigma_1 & & & & 0\\
& \sigma_2 & & & \vdots\\
& & \ddots & & \vdots\\
& & & \sigma_k & 0\\
& & & & \ddots
\end{pmatrix}
$$

con dimensioni $m\times n$.

## Relazione con gli autovalori

I valori singolari sono strettamente legati agli autovalori di

$$
A^TA
$$

Infatti, gli autovalori non nulli di $A^TA$ sono

$$
\sigma_1^2,\dots,\sigma_k^2
$$

e quindi

$$
\boxed{
\sigma_i=\sqrt{\lambda_i(A^TA)}
}
$$

per gli autovalori positivi.

Le colonne di $V$ sono autovettori di $A^TA$, mentre le colonne di $U$ sono autovettori di $AA^T$.

Poiché

$$
\operatorname{rank}(A)=k
$$

anche $A^TA$ ha rango $k$ e quindi possiede $k$ autovalori positivi e $n-k$ autovalori nulli.