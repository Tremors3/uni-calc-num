## Inversa di una matrice

Una matrice quadrata

$$
A\in\mathbb{R}^{n\times n}
$$

si dice **invertibile** (o **non singolare**) se esiste una matrice

$$
A^{-1}\in\mathbb{R}^{n\times n}
$$

tale che

$$
AA^{-1}=A^{-1}A=I_n,
$$

dove ($I_n$) è la matrice identità di ordine (n).

La matrice ($A^{-1}$) prende il nome di **matrice inversa** di (A). Se una matrice non ammette inversa, viene detta **singolare**.

L'inversa di una matrice svolge un ruolo analogo all'inverso di un numero reale:

$$
a\cdot\frac{1}{a}=1,
\qquad
AA^{-1}=I_n.
$$

La possibilità di invertire una matrice è strettamente legata al **determinante**. Una matrice quadrata è invertibile **se e solo se il suo determinante è diverso da zero**.

Il determinante può essere calcolato tramite procedure ricorsive, anche se in pratica si utilizzano algoritmi numericamente più efficienti.

---

### ▸ Proprietà dell'inversa

L'operazione di inversione soddisfa alcune proprietà fondamentali.

L'inversa dell'inversa restituisce la matrice di partenza:

$$
(A^{-1})^{-1}=A.
$$

L'inversa della trasposta coincide con la trasposta dell'inversa:

$$
(A^T)^{-1}=(A^{-1})^T=A^{-T}.
$$

Questo significa che **trasposizione e inversione possono essere applicate in qualsiasi ordine**.

Se due matrici sono invertibili, allora anche il loro prodotto è invertibile e vale

$$
(AB)^{-1}=B^{-1}A^{-1}.
$$

È importante osservare che **l'ordine delle matrici si inverte**.

---

## Determinante

Il **determinante** è una funzione che associa ad ogni matrice quadrata un numero reale.

Data una matrice

$$
A\in\mathbb{R}^{n\times n},
$$

il suo determinante si indica con

$$
\det(A).
$$

Esso fornisce importanti informazioni sulla matrice, in particolare sulla sua invertibilità.

---

### ▸ Definizione ricorsiva (Regola di Laplace)

Il determinante può essere definito ricorsivamente mediante lo sviluppo di Laplace.

Per una matrice di ordine 1,

$$
\det(A)=a_{11}
$$

Per una matrice di ordine superiore,

$$
\det(A)=
\sum_{j=1}^{n}
(-1)^{i+j}
\;
a_{ij}
\;
\det(A_{ij})
$$

dove:

* (i) è una qualsiasi riga scelta per lo sviluppo;
* ($A_{ij}$) è la matrice ottenuta eliminando la riga (i) e la colonna (j).

ed è valida scegliendo qualsiasi riga oppure qualsiasi colonna.

---

### ▸ Complessità computazionale

Il calcolo del determinante mediante la definizione ricorsiva richiede il calcolo di un grande numero di determinanti di ordine inferiore.

La complessità computazionale è

$$
\mathcal{O}(n!),
$$

che cresce troppo rapidamente all'aumentare della dimensione della matrice.

Per questo motivo, nella pratica, il determinante viene calcolato mediante la **fattorizzazione LU** o l'**eliminazione di Gauss**, ottenendo una complessità

$$
\mathcal{O}(n^3).
$$

---

### ▸ Proprietà del determinante

La proprietà più importante collega direttamente determinante e invertibilità:

$$
A \text{ è invertibile}
\iff
\det(A)\neq0.
$$

Equivalentemente,

$$
\det(A)=0
\iff
A \text{ è singolare}.
$$

---

## Autovalori e autovettori

Sia una matrice e uno scalare

$$
A\in\mathbb{R}^{n\times n},
\qquad
\lambda\in\mathbb{C}
$$

e un vettore non nullo

$$
x\in\mathbb{C}^n,\qquad x\neq0,
$$

si dicono rispettivamente **autovalore** e **autovettore** della matrice (A) se soddisfano

$$
Ax=\lambda x.
$$

Gli autovalori possono essere interpretati come una sorta di **"carta di identità" della matrice**, perché descrivono proprietà strutturali profonde dell’operatore lineare rappresentato dalla matrice.

Una matrice di ordine (n) possiede esattamente (n) autovalori, contando anche le molteplicità.

---

### ▸ Raggio spettrale

Il **raggio spettrale** di una matrice misura il modulo dell'autovalore di valore assoluto massimo.

Se gli autovalori della matrice sono

$$
\lambda_1,\lambda_2,\ldots,\lambda_n,
$$

si definisce

$$
\rho(A)=\max_{i=1,\ldots,n}|\lambda_i|.
$$

Il raggio spettrale è sempre un numero reale non negativo.

Nel calcolo numerico riveste un ruolo fondamentale nello studio della convergenza dei metodi iterativi e nella stabilità degli algoritmi.
