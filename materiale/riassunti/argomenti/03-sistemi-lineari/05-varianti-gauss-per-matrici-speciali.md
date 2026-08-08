# Varianti della fattorizzazione di Gauss per matrici speciali

La fattorizzazione di Gauss con pivoting parziale è applicabile, in generale, a qualsiasi matrice quadrata nonsingolare. Tuttavia, molte matrici che derivano da problemi applicativi presentano una **struttura particolare**, ad esempio una struttura a banda o una struttura sparsa.

Conoscere la struttura della matrice permette di costruire varianti dell'algoritmo di Gauss che sfruttano le proprietà della matrice, evitando di eseguire operazioni su elementi sicuramente nulli. In questo modo è possibile ridurre sia la **complessità computazionale** sia l'**occupazione di memoria**.

## 1) Matrici a banda

Una matrice quadrata $A\in\mathbb{R}^{n\times n}$ si dice **a banda** con ampiezza inferiore $r$ e superiore $s$ se

$$
a_{ij}=0
\qquad
\text{se } j-i>s
\quad\text{oppure}\quad
i-j>r.
$$

In altre parole, gli elementi non nulli possono trovarsi solamente nella diagonale principale, nelle $s$ diagonali immediatamente superiori e nelle $r$ diagonali immediatamente inferiori.

Le matrici a banda sono particolarmente importanti perché molti problemi differenziali provenienti da applicazioni scientifiche e ingegneristiche, dopo la discretizzazione, portano alla soluzione di sistemi lineari caratterizzati proprio da questa struttura.

### ▹ Memorizzazione

Una matrice densa di ordine $n$ richiede la memorizzazione di $n^2$ elementi. Per una matrice a banda, invece, la maggior parte degli elementi è sicuramente nulla e non è necessario memorizzarla.

Il numero di elementi potenzialmente non nulli è dell'ordine di $n(r+s+1),$ per cui una matrice a banda può essere memorizzata in

$$
\mathcal{O}\bigl(n(r+s+1)\bigr)
$$

locazioni, anziché nelle $n^2$ locazioni necessarie per una matrice densa. Se $r$ e $s$ sono molto più piccoli di $n$, il risparmio di memoria può quindi essere considerevole.

### ▹ Fattorizzazione di Gauss di una matrice a banda

Se i **minori principali** della matrice sono tutti non nulli, la fattorizzazione di Gauss può essere eseguita senza scambi di righe e la struttura a banda viene preservata. In particolare, nella fattorizzazione

$$
A=LU,
$$

la matrice $L$ mantiene la banda inferiore di ampiezza $r$, mentre $U$ mantiene la banda superiore di ampiezza $s$.

Questo significa che durante l'eliminazione non è necessario calcolare o memorizzare elementi al di fuori delle bande.

La struttura permette quindi di ridurre notevolmente il costo rispetto alla fattorizzazione di una matrice densa. In particolare, il costo della fattorizzazione è dell'ordine di

$$
\mathcal{O}(nrs).
$$

### ▹ Effetto del pivoting

La situazione cambia quando è necessario effettuare **scambi di righe** durante la fattorizzazione. Uno scambio di righe può infatti distruggere la struttura a banda, introducendo elementi non nulli al di fuori della banda originaria.

Per questo motivo, nelle implementazioni specializzate per matrici a banda, si cerca di sfruttare la struttura evitando, quando possibile, operazioni che la distruggano.

---

## 2) Matrici sparse

Una matrice quadrata $A\in\mathbb{R}^{n\times n}$ si dice **sparsa** quando il numero di elementi non nulli è molto piccolo rispetto al numero totale di elementi,

$$
\operatorname{nnz}(A)\ll n^2,
$$

dove $\operatorname{nnz}(A)$ indica il numero di elementi non nulli della matrice.

### ▹ Memorizzazione delle matrici sparse

Per una matrice sparsa non è conveniente utilizzare la normale rappresentazione densa, poiché si finirebbe per memorizzare un numero enorme di zeri.

Si utilizzano quindi **formati di memorizzazione sparsi**, che memorizzano solamente gli elementi non nulli insieme alle informazioni necessarie per determinarne la posizione.

Tra i formati più comuni vi sono:

- il **CRS (Compressed Row Storage)**, che organizza gli elementi non nulli per righe;

- il **CCS (Compressed Column Storage)**, che li organizza per colonne.

Nel formato CRS gli elementi non nulli vengono memorizzati in un vettore, mentre strutture ausiliarie permettono di determinare per ciascun elemento la colonna di appartenenza e l'inizio di ogni riga.

Nel formato CCS l'idea è analoga, ma gli elementi vengono organizzati per colonne: si memorizzano gli elementi non nulli, i relativi indici di riga e le posizioni iniziali delle diverse colonne.

In entrambi i casi, la memoria richiesta è legata principalmente al numero di elementi non nulli $\operatorname{nnz}(A)$, anziché a $n^2$.

### ▹ Matrici sparse e problema di inpainting

Nel problema di **inpainting** si vuole ricostruire una parte mancante di un'immagine a partire dai dati disponibili. La discretizzazione del problema porta alla costruzione di sistemi lineari la cui matrice presenta una particolare struttura sparsa.

Gli elementi non nulli possono trovarsi sulla diagonale principale, sulle diagonali immediatamente adiacenti e, a seconda della discretizzazione e del problema considerato, anche su diagonali più lontane. Per questo motivo la matrice dell'inpainting non deve necessariamente essere considerata una semplice matrice a banda: la caratteristica fondamentale è la **sparsità**.

In questi problemi è quindi conveniente utilizzare una rappresentazione sparsa della matrice. Memorizzare l'intera matrice in formato denso significherebbe infatti occupare memoria e svolgere operazioni anche sugli elementi nulli, con un costo inutilmente elevato.

### ▹ Fill-in

Nelle matrici sparse è particolarmente importante considerare il fenomeno del **fill-in**.

Durante la **fattorizzazione di Gauss**, un elemento inizialmente nullo può diventare non nullo a causa delle operazioni di eliminazione. Questi nuovi elementi non nulli prendono il nome di **fill-in**.

Il fill-in modifica la struttura sparsa della matrice e può aumentare notevolmente sia la memoria necessaria sia il costo computazionale della fattorizzazione.

Per questo motivo, negli algoritmi per matrici sparse non è sufficiente considerare solamente la stabilità numerica. È necessario anche scegliere opportunamente l'ordine delle operazioni e dei pivot in modo da **limitare la quantità di fill-in**.

Il problema della scelta dell'ordine di eliminazione è quindi fondamentale: un ordinamento opportuno può mantenere una buona sparsità durante la fattorizzazione, mentre un ordinamento sfavorevole può produrre molti nuovi elementi non nulli.

---

## 3) Matrici simmetriche

Una matrice $A$ è simmetrica se $A = A^T$. In questo caso, le informazioni contenute sopra e sotto la diagonale principale coincidono, quindi è sufficiente memorizzare solo metà matrice.

Se la matrice è **simmetrica**, **non singolare** e con tutti i **minori principali diversi da zero**, allora è possibile utilizzare una fattorizzazione più efficiente della classica $LU$, ovvero:

$$ A = LDL^T $$

dove $L$ è triangolare inferiore con diagonale unitaria e $D$ è una matrice diagonale.

Il vantaggio principale è che non è necessario calcolare una matrice triangolare superiore indipendente:
- $U$ viene sostituita da $L^T$, riducendo il numero di operazioni;
- Il costo computazionale passa da $\mathcal{O}\left(\frac{n^3}{3}\right)$ nel caso generale a circa la metà $\mathcal{O}\left(\frac{1}{2}\cdot\frac{n^3}{3}\right)$.

### ▹ Risoluzione del sistema

Dato il sistema $Ax = b$ e la fattorizzazione $A = LDL^T$, si ottiene:

$$ LDL^T x = b $$

Introducendo le variabili intermedie $z$ e $y$, il problema si risolve in tre passi:

$$
\begin{cases}
L z = b     &\to \textit{Triangolo inferiore} \\
D y = z     &\to y_i = \frac{z_i}{d_{ii}}\quad i=1,\dots,n \\
L^T x = y   &\to \textit{Triangolo superiore} \\
\end{cases}
$$

Il primo e il terzo sistema sono triangolari (inferiore e superiore), quindi si risolvono rispettivamente con sostituzione in avanti e all’indietro. Il sistema con $D$ è invece immediato, poiché $D$ è diagonale:

$$ y_i = \frac{z_i}{d_{ii}}, \quad i = 1, \dots, n $$

Questa struttura rende l’algoritmo più efficiente e numericamente stabile rispetto al caso generale, a patto che la matrice soddisfi le ipotesi richieste.

---

## 4) Matrici simmetriche definite positive $-$ Fattorizzazione di Cholesky

Una matrice $A\in\mathbb{R}^{n\times n}$ si dice **simmetrica definita positiva** se è **simmetrica** ($A=A^T$), e tutti i suoi **autovalori sono positivi** ($\lambda_i>0,\quad i=1,\ldots,n$).

Questa proprietà è particolarmente importante perché permette di utilizzare la **fattorizzazione di Cholesky**, un algoritmo più semplice, efficiente e numericamente stabile rispetto alla fattorizzazione $LU$ generale.

### ▹ Fattorizzazione di Cholesky

Se $A$ è simmetrica definita positiva, allora esiste un'unica matrice triangolare inferiore $L$ con diagonale positiva tale che

$$
\boxed{A=LL^T}.
$$

La matrice $L$ ha quindi la forma

$$
L=
\begin{pmatrix}
l_{11} & 0 & \cdots & 0\\
l_{21} & l_{22} & \cdots & 0\\
\vdots & \vdots & \ddots & \vdots\\
l_{n1} & l_{n2} & \cdots & l_{nn}
\end{pmatrix},
$$

mentre $L^T$ è triangolare superiore.

La fattorizzazione sfrutta direttamente la simmetria di $A$: non è necessario calcolare separatamente due fattori triangolari, poiché il secondo è semplicemente la trasposta del primo.

### ▹ Costruzione di $L$

Considerando, ad esempio, il caso $3 \times 3$:

$$
A =
\begin{pmatrix}
a_{11} & a_{21} & a_{31} \\
a_{21} & a_{22} & a_{32} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}
=
L L^T
$$

con

$$ L L^T =
\begin{pmatrix}
l_{11} &        &  \\
l_{21} & l_{22} &  \\
l_{31} & l_{32} & l_{33} \\
\end{pmatrix}
\cdot
\begin{pmatrix}
l_{11} & l_{21} & l_{31} \\
       & l_{22} & l_{32} \\
       &        & l_{33} \\
\end{pmatrix}
$$

Sviluppando il prodotto $LL^T$, si ottengono relazioni tra gli elementi di $A$ e quelli di $L$. In particolare:

$$ a_{11} = l_{11}^2 \quad \Rightarrow \quad l_{11} = \sqrt{a_{11}} $$

$$ a_{21} = l_{21} l_{11} \quad \Rightarrow \quad l_{21} = \frac{a_{21}}{l_{11}} $$

$$ a_{31} = l_{31} l_{11} \quad \Rightarrow \quad l_{31} = \frac{a_{31}}{l_{11}} $$

e così via per gli elementi successivi, procedendo per colonne.

### ▹ Risoluzione del sistema lineare

Una volta calcolata la fattorizzazione $A=LL^T$, il sistema diventa

$$
LL^Tx=b.
$$

Si risolve quindi in due passaggi:

$$
\begin{cases}
L y = b     &\to \textit{Triangolo inferiore} \\
L^T x = y   &\to \textit{Triangolo superiore} \\
\end{cases}
$$

### ▹ Vantaggi

La fattorizzazione di Cholesky è particolarmente conveniente quando la matrice è simmetrica definita positiva perché sfrutta contemporaneamente **simmetria** e **definita positività**.

- **Simmetria**: Permette di evitare il calcolo e la memorizzazione di informazioni ridondanti. La complessità si riduce della metà rispetto alla fattorizzazione $LU$: $\mathcal{O}(\frac{n^3}{6})$.

- **Positività**: Garantisce l'esistenza della fattorizzazione con diagonale positiva e permette di evitare il pivoting. Algoritmo + stabile di tutti (algoritmo di Cholesky).

Inoltre, è **numericamente più stabile**, grazie alla struttura della matrice e all’assenza di pivoting.

---