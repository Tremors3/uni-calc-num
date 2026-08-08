# Fattorizzazione QR

La **fattorizzazione QR** è una tecnica che permette di decomporre una matrice quadrata non singolare $A\in\mathbb{R}^{n\times n}$ nel prodotto di una matrice ortogonale e di una matrice triangolare superiore:

$$
\boxed{A=QR}
$$

dove

$$
Q\in\mathbb{R}^{n\times n}
$$

è una matrice **ortogonale**, mentre

$$
R\in\mathbb{R}^{n\times n}
$$

è una matrice **triangolare superiore**.

L'idea fondamentale della fattorizzazione QR è quindi trasformare la matrice $A$ in una matrice triangolare superiore mediante trasformazioni ortogonali. Questo la rende particolarmente interessante dal punto di vista della stabilità numerica.

## Matrici ortogonali

Una matrice quadrata $Q$ si dice **ortogonale** se soddisfa

$$
Q^TQ=QQ^T=I.
$$

Da questa proprietà segue immediatamente che $Q$ è non singolare e che la sua inversa coincide con la trasposta:

$$
\boxed{Q^{-1}=Q^T}.
$$

Le matrici ortogonali hanno una proprietà particolarmente importante nell'analisi numerica: **preservano le norme**. Infatti, per ogni vettore $x$,

$$
|Qx|_2=|x|_2.
$$

Di conseguenza, l'applicazione di trasformazioni ortogonali non amplifica la norma dei vettori e contribuisce alla stabilità numerica degli algoritmi che le utilizzano.

### ▸ Risoluzione di un sistema con matrice ortogonale

Se si considera il sistema

$$
Qy=b,
$$

poiché $Q^{-1}=Q^T$, è sufficiente moltiplicare entrambi i membri per $Q^T$:

$$
Q^TQy=Q^Tb.
$$

Essendo

$$
Q^TQ=I,
$$

si ottiene

$$
\boxed{y=Q^Tb}.
$$

La soluzione richiede quindi solamente un prodotto matrice-vettore, senza dover calcolare esplicitamente l'inversa di $Q$.

## Risoluzione di un sistema mediante fattorizzazione QR

Consideriamo il seguente sistema lineare e supponiamo di aver calcolato la fattorizzazione $QR$ di $A$.

$$
Ax=b
,\qquad
A=QR.
$$

Sostituendo nella precedente equazione si ottiene

$$
QRx=b.
$$

Introducendo la variabile ausiliaria $y=Rx,$ il sistema diventa

$$
\begin{cases}
Q y = b & \quad\rightarrow & \text{Sistema Ortogonale} \\
R x = y & \quad\rightarrow & \text{Sistema Triangolare Superiore}
\end{cases}
$$

1. Poiché $Q$ è ortogonale,

    $$
    y=Q^Tb.
    $$

2. A questo punto resta da risolvere il sistema triangolare superiore

    $$
    Rx=y,
    $$

    che può essere risolto mediante **sostituzione all'indietro**.

La risoluzione completa consiste quindi nei due passaggi

$$
Qy=b
\quad\Longrightarrow\quad
y=Q^Tb,
\quad\Longrightarrow\quad
Rx=y.
$$

Il vantaggio è che non è necessario calcolare esplicitamente né $A^{-1}$ né $Q^{-1}$.

# Algoritmo di Householder

Esistono diversi metodi per calcolare la fattorizzazione QR. Tra questi, il metodo basato sulle **trasformazioni di Householder** è particolarmente importante perché utilizza trasformazioni ortogonali ed è quindi numericamente stabile.

L'obiettivo è costruire una successione di trasformazioni ortogonali

$$
U_1,U_2,\ldots,U_{n-1}
$$

che trasformino progressivamente $A$ in una matrice triangolare superiore $R$.

Dopo l'applicazione di tutte le trasformazioni si ottiene

$$
\boxed{
U_{n-1}\cdots U_2U_1A=R
}
$$

dove $R$ è triangolare superiore.

## Confronto con il metodo di Gauss

L'idea è simile a quella della fattorizzazione di Gauss: in entrambi i casi si applicano trasformazioni successive per annullare gli elementi sotto la diagonale e ottenere una matrice triangolare superiore.

Nel metodo di Gauss si utilizzano trasformazioni triangolari inferiori:

$$
L_{n-1}\cdots L_1A=U.
$$

Le trasformazioni sono basate su combinazioni lineari delle righe e il risultato è una matrice triangolare superiore $U$.

Nel metodo di Householder, invece, si utilizzano trasformazioni **ortogonali**:

$$
U_{n-1}\cdots U_1A=R.
$$

Le trasformazioni $U_k$ sono riflessioni ortogonali che annullano contemporaneamente tutti gli elementi sotto la diagonale nella colonna considerata.

La differenza fondamentale è quindi che Gauss utilizza trasformazioni triangolari legate all'eliminazione, mentre Householder utilizza trasformazioni ortogonali che preservano le norme.

## Trasformazione di Householder

### ▸ Idea geometrica

Data una colonna

$$
a=
\begin{pmatrix}
a_1\\
a_2\\
\vdots\\
a_n
\end{pmatrix},
$$

l'obiettivo è costruire una matrice ortogonale $U$ tale che

$$
Ua=
\begin{pmatrix}
-|a|_2\\
0\\
\vdots\\
0
\end{pmatrix}.
$$

In questo modo tutte le componenti del vettore, ad eccezione della prima, vengono annullate in un unico passaggio.

Geometricamente, la trasformazione di Householder è una **riflessione** che porta il vettore $a$ nella direzione del primo vettore della base canonica.

## Costruzione della matrice di Householder

Si considera il vettore $a$ e si calcola la sua norma euclidea:

$$
\sigma=|a|_2.
$$

Indicando con

$$
e_1=
\begin{pmatrix}
1\\
0\\
\vdots\\
0
\end{pmatrix}
$$

il primo vettore della base canonica, si definisce

$$
v=a+\sigma e_1.
$$

Il vettore $v$ determina la direzione rispetto alla quale viene effettuata la riflessione.

Si introduce quindi

$$
\alpha=\frac{1}{2}|v|_2^2.
$$

La matrice di Householder è definita da

$$
\boxed{
U=I-\frac{1}{\alpha}vv^T
}
$$

che, equivalentemente, può essere scritta come

$$
U
=

I-\frac{2}{|v|_2^2}vv^T.
$$

Questa matrice è **ortogonale e simmetrica**:

$$
U^TU=I,
$$

e

$$
U^T=U.
$$

Di conseguenza,

$$
\boxed{U^{-1}=U^T=U}.
$$

La matrice di Householder è quindi anche **auto-inversa**: applicare due volte la stessa riflessione restituisce il vettore iniziale.

Con la costruzione precedente, la trasformazione ha l'effetto

$$
Ua=
\begin{pmatrix}
-|a|_2\\
0\\
\vdots\\
0
\end{pmatrix}.
$$

Il segno della prima componente può essere scelto in modo equivalente modificando opportunamente la definizione di $v$.

## Esempio di Fattorizzazione QR con Householder

L'algoritmo applica successivamente trasformazioni di Householder alle colonne della matrice, lavorando ogni volta sulla sottomatrice che rimane dopo aver fissato le colonne precedenti.

### ▸ Primo passo

Si prende quindi il vettore formato dagli elementi sotto la diagonale della prima colonna di $A$:

$$
a_1=
\begin{pmatrix}
a_{11}\\
a_{21}\\
\vdots\\
a_{n1}
\end{pmatrix}.
$$

Si costruisce la trasformazione di Householder:

$$
\sigma_1=|a_1|_2,
$$

$$
v_1=a_1+\sigma_1e_1,
$$

$$
\alpha_1=\frac12|v_1|_2^2,
$$

$$
U_1
=
I-\frac{1}{\alpha_1}v_1v_1^T.
$$

tale che

$$
U_1a_1=
\begin{pmatrix}
a_{11}^{(2)}\\
0\\
\vdots\\
0
\end{pmatrix}.
$$

Applicando $U_1$ all'intera matrice si ottiene la nuova matrice $A_2$ dove la prima colonna presenta zeri sotto il primo elemento:

$$
A_2=U_1A=
\begin{pmatrix}
a_{11}^{(2)} & a_{12}^{(2)} & \cdots & a_{1n}^{(2)}\\
0 & a_{22}^{(2)} & \cdots & a_{2n}^{(2)}\\
\vdots & \vdots & \ddots & \vdots\\
0 & a_{n2}^{(2)} & \cdots & a_{nn}^{(2)}
\end{pmatrix}.
$$

### ▸ Secondo passo

Dopo il primo passo si considera la sottomatrice ottenuta eliminando la prima riga e la prima colonna. Si prende quindi il vettore formato dagli elementi sotto la diagonale della seconda colonna:

$$
a_2=
\begin{pmatrix}
a_{22}^{(2)}\\
a_{32}^{(2)}\\
\vdots\\
a_{n2}^{(2)}
\end{pmatrix}
\in\mathbb{R}^{n-1}.
$$

Si costruisce una nuova trasformazione di Householder, questa volta di dimensione $n-1$:

$$
\sigma_2=|a_2|_2,
$$

$$
v_2=a_2+\sigma_2e_1,
$$

$$
\alpha_2=\frac12|v_2|_2^2,
$$

$$
\widetilde U_2
=
I_{n-1}
\frac{1}{\alpha_2}v_2v_2^T.
$$

La trasformazione viene poi inserita nella parte inferiore destra della matrice di dimensione $n\times n$, in modo da non modificare gli elementi già sistemati nel primo passo.

Si ottiene così una matrice $A_3$ della forma

$$
A_3=
\begin{pmatrix}
a_{11}^{(2)} & a_{12}^{(2)} & \cdots & a_{1n}^{(2)}\\
0 & a_{22}^{(3)} & \cdots & a_{2n}^{(3)}\\
0 & 0 & \cdots & a_{3n}^{(3)}\\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \cdots & a_{nn}^{(3)}
\end{pmatrix}.
$$

In questo modo vengono annullati tutti gli elementi sotto il secondo elemento diagonale della seconda colonna.

### ▸ ...Passi successivi

Il procedimento continua nello stesso modo. Al passo $k$ si considera la sottomatrice che parte dalla riga e dalla colonna $k$ e si costruisce una trasformazione di Householder che annulla tutti gli elementi sotto la diagonale nella colonna $k$.

$$
\boxed{
U_{n-1}\cdots U_2U_1A=R
}
$$

dove $R$ è triangolare superiore.

### ▸ Costruzione della matrice $Q$

Dalla relazione

$$
U_{n-1}\cdots U_1A=R
$$

si può ricavare $A$ moltiplicando a sinistra per le inverse delle trasformazioni:

$$
A=
U_1^{-1}U_2^{-1}\cdots U_{n-1}^{-1}R.
$$

Poiché ogni trasformazione di Householder è ortogonale,

$$
U_k^{-1}=U_k^T.
$$

Pertanto

$$
A=
U_1^TU_2^T\cdots U_{n-1}^TR.
$$

Definendo

$$
\boxed{
Q=U_1^TU_2^T\cdots U_{n-1}^T
}
$$

si ottiene

$$
\boxed{A=QR}.
$$

Poiché ogni trasformazione di Householder è anche simmetrica,

$$
U_k^T=U_k,
$$

e quindi, in questo caso,

$$
\boxed{
Q=U_1U_2\cdots U_{n-1}.
}
$$

Essendo prodotto di matrici ortogonali, $Q$ è a sua volta ortogonale.

## Implementazione efficiente: forma matrix-free

Nella pratica non è conveniente costruire e memorizzare esplicitamente ciascuna matrice di Householder $U$. Una matrice $n\times n$ richiederebbe infatti $\mathcal{O}(n^2)$ memoria.

Si utilizza invece direttamente la rappresentazione

$$
U=
I-\frac{1}{\alpha}vv^T.
$$

Per applicare $U$ a un vettore $y$ si calcola

$$
z=Uy.
$$

Sostituendo la definizione di $U$,

$$
z=
\left(
I-\frac{1}{\alpha}vv^T
\right)y,
$$

da cui

$$
\boxed{
z=y-\frac{1}{\alpha}v(v^Ty).
}
$$

L'applicazione può quindi essere effettuata senza costruire la matrice $U$.

Il calcolo richiede innanzitutto il prodotto scalare

$$
p=v^Ty,
$$

che ha costo $\mathcal{O}(n)$, seguito dal prodotto tra lo scalare $p/\alpha$ e il vettore $v$, anch'esso di costo $\mathcal{O}(n)$, e infine dalla sottrazione tra vettori.

Pertanto l'applicazione di una trasformazione di Householder a un vettore ha costo

$$
\mathcal{O}(n).
$$

Questa rappresentazione consente di ottenere un'implementazione molto più efficiente dal punto di vista della memoria.

## Costo computazionale

Per una matrice quadrata $A\in\mathbb{R}^{n\times n}$, la fattorizzazione QR mediante Householder ha costo complessivo dell'ordine di

$$
\boxed{
\frac{2}{3}n^3
}
$$

La fattorizzazione di Gauss $LU$, nel caso considerato, ha invece un costo dell'ordine di

$$
\frac{1}{3}n^3.
$$

Pertanto, dal punto di vista del solo costo computazionale, la fattorizzazione QR mediante Householder è circa **due volte più costosa** della fattorizzazione di Gauss.

Questo maggior costo viene compensato dalle migliori proprietà di stabilità numerica delle trasformazioni ortogonali.

## Stabilità numerica

Il principale vantaggio della fattorizzazione QR rispetto alla fattorizzazione di Gauss è la **stabilità numerica**.

Le trasformazioni di Householder sono ortogonali e quindi preservano la norma euclidea:

$$
|Ux|_2=|x|_2.
$$

Di conseguenza, le trasformazioni utilizzate durante l'algoritmo non amplificano la norma degli errori nello stesso modo in cui possono farlo le trasformazioni della fattorizzazione di Gauss.

La fattorizzazione QR risulta quindi utile nei problemi numericamente delicati, ad esempio quando la matrice è mal condizionata o quando si vuole ridurre l'amplificazione degli errori di arrotondamento.

Nonostante il costo computazionale maggiore rispetto a Gauss, QR viene quindi preferita in diverse situazioni in cui la **stabilità numerica** è più importante del semplice costo computazionale.

---

# Dimostrazioni viste a lezione

## Dimostrazioni proprietà della matrice $U$

Consideriamo una matrice di Householder nella forma

$$
U = I - \frac{1}{\alpha} vv^T
\qquad \text{con} \qquad \alpha = \frac{1}{2}\|v\|^2
$$

da cui segue immediatamente

$$
\|v\|^2 = 2\alpha
$$

---

### ▸ Simmetria

Verifichiamo che $U$ è simmetrica, cioè $U = U^T$.

$$
\begin{aligned}
U^T &= \left(I - \frac{1}{\alpha} vv^T\right)^T \\
&= I^T - \frac{1}{\alpha}(vv^T)^T \\
&= I - \frac{1}{\alpha}(v^T)^T v^T \\
&= I - \frac{1}{\alpha} vv^T \\
&= U
\end{aligned}
$$

Quindi $U$ è **simmetrica**.

---

### ▸ Ortogonalità

Verifichiamo ora che $U$ è ortogonale, cioè $U^T U = I$.

Dato che $U$ è simmetrica, vale $U^T = U$, quindi basta calcolare:

$$
\begin{aligned}
U^T U &= \left(I - \frac{1}{\alpha} vv^T\right)\left(I - \frac{1}{\alpha} vv^T\right) \\
&= I - \frac{1}{\alpha} vv^T - \frac{1}{\alpha} vv^T + \frac{1}{\alpha^2} vv^T vv^T \\
&= I - \frac{2}{\alpha} vv^T + \frac{1}{\alpha^2} v (v^T v) v^T
\end{aligned}
$$

Osserviamo che $v^T v = \|v\|^2$, quindi:

$$
\begin{aligned}
U^T U &= I - \frac{2}{\alpha} vv^T + \frac{1}{\alpha^2} \|v\|^2 vv^T \\
&= I - \frac{2}{\alpha} vv^T + \frac{1}{\alpha^2} (2\alpha) vv^T \\
&= I - \frac{2}{\alpha} vv^T + \frac{2}{\alpha} vv^T \\
&= I
\end{aligned}
$$

Quindi $U$ è **ortogonale**.

---

## Dimostrazioni costruzione della trasformazione di Householder

Sia $a \in \mathbb{R}^n$, con $\sigma = \|a\| \neq 0$. Definiamo:

$$
v = a + \sigma e_1, \qquad
\alpha = \frac{1}{2}\|v\|^2, \qquad
U = I - \frac{1}{\alpha} vv^T
$$

### ▸ Obiettivo

$$
\text{Mostrare che:}\qquad
Ua =
\begin{pmatrix}
-\sigma \\ 0 \\ \vdots \\ 0
\end{pmatrix}
= -\sigma e_1
$$

---

### 1) Calcolo di $\mathbf\alpha$

$$\begin{aligned}
\alpha &= \frac{1}{2} \|v\|^2 = \frac{1}{2} v^T v \\
&= \frac{1}{2}(a + \sigma e_1)^T(a + \sigma e_1) \\
&= \frac{1}{2}\left(a^T a + \sigma a^T e_1 + \sigma e_1^T a + \sigma^2 e_1^T e_1 \right)
\end{aligned}
$$

Osservazioni:

- $a^T a = \|a\|^2 = \sigma^2$
- $e_1^T e_1 = 1$
- $a^T e_1 = e_1^T a$

Quindi:

$$
\begin{aligned}
\alpha &= \frac{1}{2}\left(\sigma^2 + 2\sigma e_1^T a + \sigma^2 \right) \\
&= \frac{1}{2}\left(2\sigma^2 + 2\sigma e_1^T a \right) \\
&= \sigma^2 + \sigma e_1^T a
\end{aligned}
$$

Abbiamo trovato che:

$$\boxed{
\alpha = \frac{1}{2}\|v\|^2 = \frac{1}{2}vv^T = \sigma^2 + \sigma e_1^Ta
}$$

---

### 2) Applicazione della trasformazione

$$
\begin{aligned}
Ua &= \left(I - \frac{1}{\alpha} vv^T\right)a \\
&= a - \frac{1}{\alpha} v (v^T a)
\end{aligned}
$$

Calcoliamo $v^T a$:

$$
\begin{aligned}
v^T a &= (a + \sigma e_1)^T a \\
&= a^T a + \sigma e_1^T a \\
&= \sigma^2 + \sigma e_1^T a \\
&= \alpha
\end{aligned}
$$

Sostituendo:

$$
\begin{aligned}
Ua &= a - \frac{1}{\alpha} v \cdot \alpha \\
&= a - v \\
&= a - (a + \sigma e_1) \\
&= -\sigma e_1
\end{aligned}
$$

Abbiamo dimostrato che:

$$ \boxed{Ua=-\sigma e_1} $$

---