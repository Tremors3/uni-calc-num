
# Minimi Quadrati e fattorizzazione QR

## Modelli lineari e non lineari nei parametri

La formulazione

$$
Q(\alpha)=\|A\alpha-y\|_2^2
$$

è possibile quando il modello dipende **linearmente dai parametri**.

Ad esempio,

$$
f(x)=a_0+a_1x+a_2x^2
$$

è lineare nei parametri $a_0,a_1,a_2$, così come

$$
f(x)
=
a_0\phi_0(x)
+\dots
+a_{n-1}\phi_{n-1}(x)
$$

è lineare nei parametri $a_0,\dots,a_{n-1}$.

Questo permette di raccogliere i parametri nel vettore $\alpha$ e costruire una matrice $A$ che dipende dai dati $x_i$ e dalle funzioni di base, ma non dai parametri.

## Modelli non lineari nei parametri

Non tutti i modelli possiedono questa proprietà.

Consideriamo, ad esempio,

$$
f(x)=a_0e^{a_1x}
$$

Il parametro $a_1$ compare all’interno dell’esponenziale e quindi non compare linearmente. Non è quindi possibile scrivere il modello nella forma

$$
f(x)=A\alpha
$$

con una matrice $A$ indipendente dai parametri.

Il problema non può quindi essere trattato direttamente come un problema di **minimi quadrati lineari** e richiede tecniche di regressione non lineare.

## Problema generale dei minimi quadrati

Consideriamo quindi

$$
A\in\mathbb R^{m\times n},
\qquad
y\in\mathbb R^m
$$

e il problema

$$
\boxed{
\min_{\alpha\in\mathbb R^n}
\|A\alpha-y\|_2^2
}
$$

Generalmente si considera il caso

$$
m\ge n
$$

cioè un numero di dati almeno pari al numero di parametri.

Se inoltre le colonne di $A$ sono linearmente indipendenti, allora

$$
\operatorname{rank}(A)=n
$$

e il problema dei minimi quadrati possiede una **soluzione unica**.

Nel caso polinomiale, se i punti $x_i$ sono distinti, le colonne della matrice di Vandermonde sono linearmente indipendenti.

## Fattorizzazione QR

Per risolvere il problema dei minimi quadrati possiamo utilizzare la fattorizzazione QR.

Per una matrice $A\in\mathbb R^{m\times n}$ con $m\ge n$, nel caso di rango pieno sulle colonne, possiamo scrivere

$$
\boxed{
A
=
Q
\begin{pmatrix}
R\\
0
\end{pmatrix}
}
$$

dove

$$
Q\in\mathbb R^{m\times m}
$$

è ortogonale,

$$
R\in\mathbb R^{n\times n}
$$

è triangolare superiore e il blocco $0$ ha dimensione $(m-n)\times n$.

La matrice $Q$ soddisfa

$$
Q^TQ=I
$$

e quindi preserva la norma euclidea.

## Proprietà delle matrici ortogonali

Sia $Q$ una matrice ortogonale e sia $z\in\mathbb R^m$. Allora

$$
\begin{aligned}
\|Qz\|_2^2
&=(Qz)^T(Qz)\\
&=z^TQ^TQz\\
&=z^Tz\\
&=\|z\|_2^2
\end{aligned}
$$

e quindi

$$
\boxed{
\|Qz\|_2=\|z\|_2
}
$$

Una matrice ortogonale quindi rappresenta una trasformazione che non modifica la norma euclidea.

Un’altra proprietà che utilizzeremo è che, se un vettore viene suddiviso in due blocchi

$$
y=
\begin{pmatrix}
y_1\\
y_2
\end{pmatrix}
$$

allora

$$
\boxed{
\|y\|_2^2
=
\|y_1\|_2^2+\|y_2\|_2^2
}
$$

## Applicazione della QR al problema dei minimi quadrati

Partiamo da

$$
\|A\alpha-y\|_2^2
$$

e sostituiamo la fattorizzazione QR:

$$
A=
Q
\begin{pmatrix}
R\\
0
\end{pmatrix}
$$

ottenendo

$$
\|A\alpha-y\|_2^2
=
\left\|
Q
\begin{pmatrix}
R\\
0
\end{pmatrix}
\alpha-y
\right\|_2^2
$$

Poiché $Q$ è ortogonale, possiamo moltiplicare l’argomento della norma per $Q^T$ senza modificarne il valore:

$$
\begin{aligned}
\|A\alpha-y\|_2^2
&=
\left\|
Q^T
\left(
Q
\begin{pmatrix}
R\\
0
\end{pmatrix}
\alpha-y
\right)
\right\|_2^2\\
&=
\left\|
\begin{pmatrix}
R\\
0
\end{pmatrix}
\alpha-Q^Ty
\right\|_2^2
\end{aligned}
$$

Definiamo

$$
\tilde y=Q^Ty
$$

e suddividiamo $\tilde y$ in due blocchi:

$$
\tilde y=
\begin{pmatrix}
\tilde y_1\\
\tilde y_2
\end{pmatrix}
$$

Allora

$$
\begin{aligned}
\|A\alpha-y\|_2^2
&=
\left\|
\begin{pmatrix}
R\alpha\\
0
\end{pmatrix}
-
\begin{pmatrix}
\tilde y_1\\
\tilde y_2
\end{pmatrix}
\right\|_2^2\\
&=
\left\|
\begin{pmatrix}
R\alpha-\tilde y_1\\
-\tilde y_2
\end{pmatrix}
\right\|_2^2
\end{aligned}
$$

Applicando la proprietà della norma a blocchi otteniamo

$$
\boxed{
\|A\alpha-y\|_2^2
=
\|R\alpha-\tilde y_1\|_2^2
+
\|\tilde y_2\|_2^2
}
$$

Il secondo termine,

$$
\|\tilde y_2\|_2^2
$$

dipende solamente dai dati e non dai parametri $\alpha$. Non possiamo quindi modificarlo.

L’unico termine che possiamo minimizzare è

$$
\|R\alpha-\tilde y_1\|_2^2
$$

Essendo una norma quadratica, il suo valore minimo è $0$ e viene raggiunto imponendo

$$
R\alpha-\tilde y_1=0
$$

cioè

$$
\boxed{
R\alpha=\tilde y_1
}
$$

Abbiamo quindi trasformato il problema di minimizzazione in un **sistema lineare triangolare**.

Poiché $R$ è triangolare superiore, il sistema viene risolto mediante **sostituzione all’indietro**.

> **Nota.** La fattorizzazione QR esiste anche quando $A$ non ha rango pieno. Tuttavia, la semplice soluzione tramite il sistema triangolare $R\alpha=\tilde y_1$ presuppone il rango pieno delle colonne e quindi l’unicità della soluzione dei minimi quadrati. Nel caso di rango non pieno è necessario gestire opportunamente le colonne linearmente dipendenti, e la SVD fornisce un approccio particolarmente generale.

---