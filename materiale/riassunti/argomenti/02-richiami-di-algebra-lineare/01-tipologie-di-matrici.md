# Calcolo Matriciale

## Matrice

Una **matrice** è una tabella rettangolare di numeri reali organizzati in **righe** e **colonne**. Una matrice si indica generalmente con una lettera maiuscola, ad esempio

$$
A = (a_{ij}) \in \mathbb{R}^{m \times n}
$$

dove (m) rappresenta il **numero di righe**, (n) il **numero di colonne** e ($a_{ij}$) indica l'elemento appartenente alla riga (i) e alla colonna (j).

Il numero totale degli elementi contenuti nella matrice è pari a $m\cdot n$.

Dal punto di vista informatico, una matrice è rappresentata mediante un **array bidimensionale**.

Se gli elementi sono memorizzati nel formato **double**, ciascun elemento occupa 8 byte; di conseguenza una matrice di dimensione (m\times n) richiede complessivamente $8mn \text{ byte}$ di memoria.

---

## Tipologie di matrici

### ▸ Rettangolare, Quadrata, Vettori Riga/Colonna

▹ Una matrice è detta **rettangolare** quando il numero di righe è diverso dal numero di colonne, cioè

$$
A = (a_{ij}) \in \mathbb{R}^{m \times n}, \qquad m \neq n
$$

▹ Se invece il numero di righe coincide con il numero di colonne,

$$
A = (a_{ij}) \in \mathbb{R}^{n \times n}
$$

la matrice è detta **quadrata** e il valore comune prende il nome di **ordine** (o **dimensione**) della matrice. Molti concetti del calcolo matriciale, come il determinante, l'inversa e la simmetria, sono definiti esclusivamente per matrici quadrate.

▹ Quando una matrice possiede una sola colonna, cioè $n=1,$ prende il nome di **vettore colonna** ed appartiene allo spazio vettoriale ($\mathbb{R}^m$).

$$
\mathbf{x} \in \mathbb{R}^{m \times 1}
$$

▹ Quando invece possiede una sola riga, $m=1,$ si parla di **vettore riga**.

$$
\mathbf{x}^T \in \mathbb{R}^{1 \times n}
$$

▹ Infine, se la matrice è costituita da un solo elemento,

$$
m=n=1,
$$

essa coincide semplicemente con uno **scalare**.

---

### ▸ Diagonale principale

Gli elementi della forma

$$
a_{11},a_{22},\ldots,a_{nn}
$$

sono chiamati **elementi diagonali** e costituiscono la **diagonale principale** della matrice. Più in generale, se la matrice non è quadrata, gli elementi diagonali sono

$$
a_{ii},\qquad i=1,\ldots,\min(m,n).
$$

La diagonale principale riveste un ruolo fondamentale nella definizione di numerose classi di matrici.

---

### ▸ Matrice trasposta

Data una matrice

$$
A\in\mathbb{R}^{m\times n},
$$

la sua **trasposta**, indicata con

$$
A^T \in \mathbb{R}^{n \times m},
$$

si ottiene scambiando tra loro righe e colonne. In altre parole, la riga (i)-esima della matrice originale diventa la colonna (i)-esima della matrice trasposta.

---

### ▸ Matrice simmetrica

Una matrice quadrata è detta **simmetrica** quando coincide con la propria trasposta, cioè

$$
A=A^T.
$$

Ciò equivale ad affermare che ogni elemento è uguale al suo elemento simmetrico rispetto alla diagonale principale:

$$
a_{ij}=a_{ji},\qquad \forall \; i,j.
$$

La simmetria può essere definita solamente per matrici quadrate, poiché una matrice rettangolare e la sua trasposta hanno dimensioni differenti.

---

### ▸ Matrice identità

La **matrice identità**, indicata con (I) oppure ($I_n$) se si vuole specificarne l'ordine, è una matrice quadrata che presenta tutti gli elementi della diagonale principale uguali a 1 e tutti gli altri elementi uguali a 0.

Formalmente,

$$
I_{ij}=
\begin{cases}
1 & \text{se } i=j, \\
0 & \text{se } i\neq j.
\end{cases}
$$

La matrice identità rappresenta l'elemento neutro del prodotto tra matrici: moltiplicare una matrice per la matrice identità, a destra o a sinistra, non ne modifica il valore,

$$
AI=IA=A.
$$

---

### ▸ Matrice diagonale

Una matrice quadrata è detta **diagonale** quando tutti gli elementi esterni alla diagonale principale sono nulli, ossia

$$
d_{ij}=0,\qquad i\neq j.
$$

Gli unici elementi che possono essere diversi da zero sono quelli appartenenti alla diagonale principale.

Poiché una matrice diagonale di ordine (n) può contenere al massimo (n) elementi non nulli, è sufficiente memorizzare soltanto tali elementi, ottenendo un notevole risparmio di memoria rispetto alla memorizzazione completa della matrice.

---

### ▸ Matrice triangolare superiore

Una matrice quadrata è detta **triangolare superiore** quando tutti gli elementi situati al di sotto della diagonale principale sono uguali a zero. Formalmente,

$$
u_{ij}=0,\qquad i>j.
$$

Possono quindi assumere valori qualsiasi solamente gli elementi appartenenti alla diagonale principale e quelli situati sopra di essa.

---

### ▸ Matrice triangolare inferiore

Una matrice quadrata è detta **triangolare inferiore** quando tutti gli elementi situati al di sopra della diagonale principale sono uguali a zero. In formule,

$$
l_{ij}=0,\qquad i<j.
$$

In questo caso gli unici elementi potenzialmente diversi da zero sono quelli della diagonale principale e quelli posti al di sotto di essa.

---

### ▸ Matrici con struttura

Le matrici diagonali e triangolari sono esempi di **matrici con struttura**, cioè matrici nelle quali una parte degli elementi è nota a priori perché necessariamente uguale a zero.

Conoscere la struttura di una matrice è molto importante nel calcolo numerico, poiché consente di progettare algoritmi più efficienti e di ridurre significativamente l'occupazione di memoria. Infatti non è necessario memorizzare esplicitamente gli elementi che si conoscono essere nulli.

Nel caso di una matrice diagonale di ordine (n), è sufficiente memorizzare soltanto i (n) elementi della diagonale principale. Una matrice triangolare, invece, contiene circa

$$
\frac{n^2}{2}
$$

elementi potenzialmente non nulli; anche in questo caso è quindi possibile evitare di memorizzare metà della matrice, ottenendo un considerevole risparmio di memoria e una maggiore efficienza negli algoritmi numerici che operano su tali strutture.

---

## Struttura delle matrici e rappresentazione in memoria

Conoscere la **struttura di una matrice** può permettere di rappresentarla in memoria in modo molto più efficiente.

Ad esempio:

- una **matrice diagonale** può essere rappresentata semplicemente tramite il vettore contenente i suoi elementi diagonali;

- una **matrice triangolare** può essere memorizzata salvando soltanto gli elementi sopra o sotto la diagonale principale.

Questo tipo di rappresentazione riduce lo **spazio di memoria** necessario e spesso rende anche più efficienti le operazioni numeriche.
