
# Interpolazione polinomiale

In generale, non esiste un’unica funzione che passi per un insieme finito di punti: **infinite funzioni** possono interpolare gli stessi dati.

Per rendere il problema ben posto è quindi necessario **restringere la classe di funzioni** tra cui cercare l’interpolante.

Una scelta particolarmente importante è quella dei **polinomi**, poiché sono semplici da gestire dal punto di vista computazionale, garantiscono, sotto opportune condizioni, esistenza e unicità della soluzione e sono facili da valutare e derivare.

Il problema dell’interpolazione diventa quindi quello di costruire un **polinomio interpolante** $p(x)$ tale che

$$
\boxed{
p(x_i)=y_i,
\qquad i=0,\ldots,n
}
$$

Il polinomio $p(x)$ rappresenta quindi una funzione che interpola esattamente tutti i dati assegnati.

---

## Intermezzo sui polinomi

Un **polinomio** è una funzione espressa come combinazione di monomi, nella forma

$$
p(x)=a_0+a_1x+a_2x^2+\dots+a_nx^n,
\qquad a_0,a_1,\dots,a_n\in\mathbb{R}.
$$

I valori $a_i$ sono detti **coefficienti** del polinomio. Se $a_n\neq0$, il polinomio ha **grado $n$**. Un polinomio di grado al più $n$ è quindi completamente determinato dai suoi $n+1$ coefficienti

$$
a_0,a_1,\dots,a_n.
$$

### ▸ Perché utilizzare i polinomi nell'interpolazione?

I polinomi sono particolarmente adatti al problema dell’interpolazione perché permettono di trasformarlo in un problema algebrico: invece di cercare direttamente una funzione, si determinano i coefficienti del polinomio interpolante.

Considerando $n+1$ dati $(x_i,y_i)$, il polinomio di grado al più $n$ possiede esattamente $n+1$ coefficienti. Si può quindi imporre che il polinomio passi per tutti i dati, ottenendo le condizioni

$$
p(x_i)=y_i,
\qquad i=0,\dots,n.
$$

Sotto l’ipotesi che le ascisse $x_i$ siano tutte distinte, queste condizioni determinano **un unico polinomio di grado al più $n$**.

### ▸ Esistenza e unicità del polinomio interpolante

Il risultato fondamentale dell’interpolazione polinomiale afferma che, dati $n+1$ punti $(x_i,y_i)$ con ascisse $x_i$ tutte distinte, **esiste ed è unico** un polinomio $p_n(x)$ di grado al più $n$ che interpola i dati:

$$
\boxed{
p_n(x_i)=y_i,
\qquad i=0,\dots,n.
}
$$

Ad esempio, dati tre punti con ascisse distinte, esiste un unico polinomio di grado al più $2$, cioè una parabola, che passa esattamente per tutti e tre i punti.

Questo risultato rende il problema dell’interpolazione ben posto: tra le infinite funzioni che potrebbero passare per i dati, restringendo la ricerca alla classe dei polinomi si ottiene una **soluzione unica**, rappresentata completamente dai suoi coefficienti.

---

## 1) Metodo dei coefficienti indeterminati

Il **metodo dei coefficienti indeterminati** consiste nel determinare direttamente i coefficienti del polinomio interpolante. Si parte dalla forma generale del polinomio di grado al più $n$:

$$
p_n(x)=a_0+a_1x+a_2x^2+\dots+a_nx^n
$$

e si impongono le **condizioni di interpolazione**

$$
p_n(x_i)=y_i,
\qquad i=0,\dots,n.
$$

che corrispondono a:

$$\begin{aligned}
i=0) &\quad p_n(x_0) = y_0 \quad\Leftrightarrow\quad a_0 + a_1x_0 + a_2x_0^2 + \dots + a_nx_0^n = y_0 \\
i=1) &\quad p_n(x_1) = y_1 \quad\Leftrightarrow\quad a_0 + a_1x_1 + a_2x_1^2 + \dots + a_nx_1^n = y_1 \\ 
\dots \\
i=n) &\quad p_n(x_n) = y_n \quad\Leftrightarrow\quad a_0 + a_1x_n + a_2x_n^2 + \dots + a_nx_n^n = y_n \\ 
\end{aligned}$$

Sostituendo ciascuna ascissa $x_i$ nel polinomio si ottengono $n+1$ equazioni nelle $n+1$ incognite $a_0,\dots,a_n$:

$$
\begin{cases}
a_0+a_1x_0+a_2x_0^2+\dots+a_nx_0^n=y_0 \\
a_0+a_1x_1+a_2x_1^2+\dots+a_nx_1^n=y_1 \\
\vdots \\
a_0+a_1x_n+a_2x_n^2+\dots+a_nx_n^n=y_n
\end{cases}
$$

I valori $x_i$ e $y_i$ sono noti, mentre le incognite sono i coefficienti $a_0,a_1,\dots,a_n$.

### ▸ Forma matriciale

Il sistema può essere scritto in forma compatta come

$$
\boxed{V\alpha=y}
$$

dove

$$
V=
\begin{pmatrix}
1 & x_0 & x_0^2 & \dots & x_0^n \\
1 & x_1 & x_1^2 & \dots & x_1^n \\
\vdots & \vdots & \vdots & & \vdots \\
1 & x_n & x_n^2 & \dots & x_n^n
\end{pmatrix},
\qquad
\alpha=
\begin{pmatrix}
a_0 \\
a_1 \\
\vdots \\
a_n
\end{pmatrix},
\qquad
y=
\begin{pmatrix}
y_0 \\
y_1 \\
\vdots \\
y_n
\end{pmatrix}.
$$

La matrice $V\in\mathbb{R}^{(n+1)\times(n+1)}$ è detta **matrice di Vandermonde**.

Il problema dell’interpolazione polinomiale viene quindi trasformato nella **risoluzione di un sistema lineare** con $n+1$ equazioni e $n+1$ incognite. Una volta determinato il vettore $\alpha$, cioè i coefficienti $a_0,\dots,a_n$, il polinomio $p_n(x)$ è completamente determinato.

### ▸ Condizionamento della matrice di Vandermonde

Il metodo dei coefficienti indeterminati è una formulazione semplice e diretta del problema di interpolazione. Tuttavia, per valori grandi di $n$, la matrice di Vandermonde può risultare **numericamente mal condizionata**, rendendo la determinazione dei coefficienti poco stabile.

Per questo motivo, nella pratica si utilizzano anche formulazioni alternative dell’interpolazione, come le forme di **Lagrange** e **Newton**.

---

## 2) Metodo di Lagrange

Il metodo di Lagrange permette di costruire il polinomio interpolante senza determinare esplicitamente i coefficienti della forma canonica

$$
p_n(x) = a_0 + a_1x + \dots + a_nx^n
$$

L’idea è costruire una nuova base di polinomi, detta **base di Lagrange**, in cui ogni polinomio è associato a uno dei nodi $x_i$ e ha un comportamento particolarmente semplice nei nodi di interpolazione.

### ▸ Costruzione dei polinomi $L_i(x)$

Dati $n+1$ nodi distinti

$$
x_0,x_1,\dots,x_n
$$

si vuole costruire, per ogni $i$, un polinomio $L_i(x)$ che valga $1$ nel nodo $x_i$ e $0$ in tutti gli altri nodi:

$$
L_i(x_j) =
\begin{cases}
1 & \text{se } j=i \\
0 & \text{se } j\neq i
\end{cases}
$$

Per ottenere questo comportamento, si costruisce $L_i(x)$ come prodotto dei fattori

$$
x-x_j
$$

per tutti i nodi diversi da $x_i$:

$$
L_i(x) =
\prod_{\substack{j=0\,j\neq i}}^n
\frac{x-x_j}{x_i-x_j}
$$

Il numeratore contiene quindi un fattore $x-x_j$ per ogni $j\neq i$. Di conseguenza, se valutiamo $L_i$ nel nodo $x_j$ con $j\neq i$, uno dei fattori del prodotto diventa nullo e quindi

$$
L_i(x_j)=0
$$

Nel punto $x_i$, invece, il numeratore coincide con il denominatore:

$$
L_i(x_i)
= \prod_{\substack{j=0\,j\neq i}}^n
\frac{x_i-x_j}{x_i-x_j}
=1
$$

I denominatori sono costanti e servono quindi semplicemente a **normalizzare** il polinomio affinché il suo valore in $x_i$ sia esattamente $1$.

### ▸ Costruzione del polinomio interpolante

Una volta costruiti tutti i polinomi $L_i(x)$, il polinomio interpolante si ottiene combinandoli linearmente utilizzando come coefficienti i valori $y_i$ dei dati:

$$
\boxed{
p_n(x)=\sum_{i=0}^n y_iL_i(x)
}
$$

Il motivo per cui questa combinazione interpola i dati è immediato. Valutando il polinomio nel generico nodo $x_k$ si ottiene

$$
p_n(x_k)
= \sum_{i=0}^n y_iL_i(x_k)
$$

Per la proprietà dei polinomi di Lagrange, tutti i termini sono nulli tranne quello corrispondente a $i=k$. Pertanto

$$
p_n(x_k)
= y_kL_k(x_k)
=
y_k
$$

e quindi

$$
p_n(x_k)=y_k,
\qquad k=0,\dots,n
$$

Le condizioni di interpolazione sono dunque soddisfatte automaticamente.

### ▸ Interpretazione algebrica

Il metodo di Lagrange può essere visto come un cambiamento della **base dello spazio dei polinomi di grado al più $n$**. Invece della base canonica

$$
1,x,x^2,\dots,x^n
$$

si utilizzano i polinomi

$$
L_0(x),L_1(x),\dots,L_n(x)
$$

che sono costruiti direttamente a partire dai nodi $x_i$.

In questa nuova base, i coefficienti del polinomio interpolante sono semplicemente i valori $y_i$:

$$
p_n(x)
= y_0L_0(x)+y_1L_1(x)+\dots+y_nL_n(x)
$$

Quindi, a differenza del metodo dei coefficienti indeterminati, non è necessario risolvere un sistema lineare per determinare i coefficienti $a_i$. Si costruiscono direttamente i polinomi $L_i(x)$ e si combinano con i valori $y_i$.

### ▸ Esempio con due nodi

Nel caso di due soli punti $(x_0,y_0)$ e $(x_1,y_1)$, si costruiscono due polinomi di grado $1$:

$$
L_0(x)=\frac{x-x_1}{x_0-x_1},
\qquad
L_1(x)=\frac{x-x_0}{x_1-x_0}
$$

Essi soddisfano

$$
L_0(x_0)=1,\qquad L_0(x_1)=0
$$

e

$$
L_1(x_0)=0,\qquad L_1(x_1)=1
$$

Il polinomio interpolante è quindi

$$
p_1(x)=y_0L_0(x)+y_1L_1(x)
$$

ossia

$$
p_1(x)
=
y_0\frac{x-x_1}{x_0-x_1}
+
y_1\frac{x-x_0}{x_1-x_0}
$$

La costruzione mostra chiaramente il principio del metodo: **ogni $L_i$ “seleziona” il valore $y_i$ nel proprio nodo e annulla tutti gli altri valori nei restanti nodi**.

### ▸ Metodo di Lagrange nella forma di Newton

La forma di Newton permette di costruire il polinomio interpolante **in modo iterativo**, aggiungendo un nodo alla volta. Si parte da $p_0(x)=y_0$ e, a ogni nuovo nodo, si aggiunge un termine:

$$
p_{k+1}(x)=p_k(x)+y[x_0x_1\ldots x_k]\prod_{i=0}^{k-1}(x-x_i)
$$

dove $y[x_0x_1\ldots x_k]$ è una **differenza divisa**. In questo modo si ottengono progressivamente $p_1(x),p_2(x),\ldots,p_n(x)$ senza dover ricostruire ogni volta il polinomio da zero.

Il vantaggio principale della forma di Newton è quindi la sua **costruzione incrementale**: se viene aggiunto un nuovo nodo, è sufficiente calcolare la nuova differenza divisa e aggiungere il corrispondente termine al polinomio già costruito.

---