
$$
\newcommand{\tcr}[1]{\textcolor{red}{#1}}
\newcommand{\tcy}[1]{\textcolor{yellow}{#1}}
\newcommand{\tclg}[1]{\textcolor{lightgreen}{#1}}
$$

# Sistemi Lineari

## Studio dei Sistemi Lineari

### Generalità

Uno dei problemi fondamentali del calcolo numerico consiste nel risolvere **sistemi lineari di equazioni**. Data una matrice $A\in\R^{n\times n}$, detta matrice dei coefficienti, ed il vettore dei termini noti $b\in\R^n$:

$$ A =
\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn} \\
\end{pmatrix}
,\quad b =
\begin{pmatrix}
b_1 \\ b_2 \\ \vdots \\ b_n \\
\end{pmatrix}
$$

si vuole calcolare il vettore incognito $x\in\R^n$ che soddisfa l'equazione matriciale

$$ Ax=b. $$

Scrivendo l'equazione matriciale componente per componente si ottiene il sistema di $n$ equazioni lineari in $n$ incognite

$$
\begin{cases}
a_{11}x_1 + a_{12}x_2 + a_{13}x_3 + \dots + a_{1n}x_n = b_1 \\
a_{21}x_1 + a_{22}x_2 + a_{23}x_3 + \dots + a_{2n}x_n = b_1 \\
\dots \\
a_{n1}x_1 + a_{n2}x_2 + a_{n3}x_3 + \dots + a_{nn}x_n = b_1 \\
\end{cases}
$$

che rappresenta la forma classica di un sistema lineare.

### Esistenza e unicità della soluzione

Il **teorema di Rouché–Capelli** fornisce una condizione fondamentale per stabilire se un sistema lineare ammette soluzione. Nel caso particolare dei sistemi quadrati $n\times n$, una conseguenza importante del teorema è la seguente:

se la matrice dei coefficienti $A$ è **non singolare**, cioè **invertibile**, allora il sistema $Ax=b$ ammette un'**unica soluzione**.

Una matrice quadrata è non singolare se e solo se $\text{det}(A)\ne 0$. In questo caso la soluzione può essere espressa formalmente come

$$ x = A^{-1}b. $$

Dal punto di vista del calcolo numerico, questa condizione garantisce che il problema sia ben posto, cioè che la soluzione esista ed sia unica.

Purtroppo l'operazione di **calcolo della matrice inversa** di $A$ è **molto costosa computazionalmente**, ha una **pessima stabilità**, e da evitare in ogni modo. Vedremo metodi alternativi e più efficienti per la risoluzione di sistemi lineari.

### Studio del condizionamento di un sistema lineare

Consideriamo i seguendi sistemi:

1) **Sistema non perturbato**

    $$
    \begin{cases}
    x_1 &+& 2x_2 &=& 3 \\
    0.499x_1 &+& 1.001x_2 &=& 1.5 \\
    \end{cases}
    \quad\text{Soluzione corretta:}\;
    \begin{pmatrix}
    1 \\ 1
    \end{pmatrix}
    $$

2) **Sistema con coefficienti perturbati**

    $$
    \begin{cases}
    x_1 &+& 2x_2 &=& 3 \\
    \tcr{0.5}x_1 &+& \tcr{1.002}x_2 &=& 1.5 \\
    \end{cases}
    \quad\text{Soluzione corretta:}\;
    \begin{pmatrix}
    3 \\ 0
    \end{pmatrix}
    $$

3) **Sistema con termine noto perturbato**

    $$
    \begin{cases}
    x_1 &+& 2x_2 &=& 3 \\
    0.499x_1 &+& 1.001x_2 &=& \tcr{1.4985} \\
    \end{cases}
    \quad\text{Soluzione corretta:}\;
    \begin{pmatrix}
    2 \\ 0.5
    \end{pmatrix}
    $$

Osservando i tre sistemi si nota un fatto importante.

Le modifiche apportate ai dati del problema sono **molto piccole**, dell'ordine di $10^{-3}$. Tuttavia la variazione nelle soluzioni è **molto più grande**, dell'ordine di $10^0$.

Questo significa che **piccole perturbazioni nei dati possono produrre grandi variazioni nella soluzione**. Un sistema con questa caratteristica si dice **mal condizionato**.

#### Interpretazione geometrica del mal condizionamento

Analizzando il sistema si nota che i coefficienti della seconda equazione sono circa **la metà di quelli della prima equazione**. In altre parole, le due righe della matrice dei coefficienti sono quasi proporzionali.

Quando le righe (o le colonne) di una matrice sono quasi linearmente dipendenti, la matrice è **vicina alla singolarità** e il sistema diventa molto sensibile alle perturbazioni.

In un sistema $n\times n$ è sufficiente che **due righe della matrice dei coefficienti siano quasi dipendenti** per rendere il problema numericamente instabile.

In questi casi si dice che il sistema è **mal condizionato**, cioè la soluzione dipende in modo molto sensibile dagli errori nei dati iniziali.

### Numero di condizionamento di una matrice

Per misurare quantitativamente quanto un sistema lineare sia **sensibile a perturbazioni nei dati**, si introduce il concetto di **numero di condizionamento**.

Sia dato il sistema lineare $Ax=b$ con $A\in\R^{n\times n}$. Il numero di condizionamento della matrice $A$, rispetto ad una norma scelta, è definito come

$$ k(A) = \|A\|\cdot\|A^{-1}\| $$

Questa quantità misura quanto la soluzione del sistema può **amplificare gli errori presenti nei dati**.

#### Interpretazione del numero di condizionamento

Il numero di condizionamento fornisce un'indicazione della **stabilità numerica del problema**.

- Se $\quad k(A)\approx 1$

    la matrice è **ben condizionata** e piccoli errori nei dati producono piccoli errori nella soluzione.

- Se $\quad k(A)>> 1$

    la matrice è **mal condizionata** e anche errori molto piccoli nei dati possono produrre errori molto grandi nella soluzione.

In generale vale la relazione

$$ \frac{\|\delta x\|}{\|x\|} \le k(A)\frac{\|\delta b\|}{\|b\|} $$

che mette in relazione:
- errore relativo sulla soluzione $x$
- errore relativo sui dati $b$

Questa disuguaglianza mostra che il **numero di condizionamento rappresenta il fattore massimo di amplificazione dell'errore**.

## Metodi risolutivi per sistemi lineari **semplici**

### 1) Sistema diagonale $\mid$ $n$ equazioni indipendenti

Consideriamo un sistema lineare in cui la matrice dei coefficienti è **diagonale**

$$ A=
\begin{pmatrix}
d_1 \\ & d_2 \\ && \ddots \\ &&& d_n \\
\end{pmatrix}
,\quad\text{det}(A)=d_1\cdot d_2\cdot...\cdot d_n
$$

Il sistema $Ax=b$ può essere scritto esplicitamente come

$$ d_ix_i = b_i,\space i=1,...,n \quad\Rightarrow\quad x_i=\frac{b_i}{d_i},\space i=1,...,n $$

La caratteristica principale di un sistema diagonale è che **le equazioni sono completamente indipendenti tra loro**: ciascuna incognita può essere calcolata senza utilizzare le altre.

Dal punto di vista computazionale sono necessari soltanto $n$ quozienti, quindi il costo dell'algoritmo è

$$ \mathcal{O}(n). $$

### 2) Sistema triangolare $-$ Sostituzione in avanti e all'indietro

Un caso leggermente più complesso è quello dei **sistemi triangolari**, nei quali la matrice dei coefficienti contiene zeri sopra o sotto la diagonale.

Queste strutture permettono comunque di risolvere il sistema in modo efficiente tramite algoritmi chiamati **sostituzione in avanti** e **sostituzione all'indietro**.

#### Sistema triangolare inferiore $-$ sostituzione in avanti

Consideriamo una matrice triangolare **inferiore**, ossia $A_{ij} = 0$ per $i > j$

$$ R=
\begin{pmatrix}
r_{11} & & & \\
r_{21} & r_{22} & & \\
\vdots &        & \ddots & \\
r_{n1} & r_{n2} & \cdots & r_{nn} \\
\end{pmatrix}
,\quad b=\begin{pmatrix}b_1 \\ b_2 \\ \vdots \\ b_n\end{pmatrix}
$$

Il sistema $Rx=b$ diventa

$$
\begin{cases}
r_{11}x_1 && && &= b_1 &\to& x_1 = \frac{b_1}{r_{11}} \\
r_{21}x_1 &+& r_{22}x_2 && &= b_2 &\to& x_2 = \frac{b_2 - r_{21}x_1}{r_{22}} \\
\dots \\
r_{n1}x_1 &+& r_{n2}x_2 &+\cdots+& r_{nn} &= b_n &\to& x_n = \frac{b_n - \sum_{j=1}^{n-1}r_{nj}x_j}{r_{nn}} \\
\end{cases}
$$

Quindi la formula generica per un'incognita $x_i$ è

$$ x_i = \frac{b_i - \sum_{j=1}^{i-1}r_{ij}x_j}{r_{ii}},\quad i=1,\dots,n $$

Questo procedimento prende il nome di **sostituzione in avanti** perché le incognite vengono calcolate nell'ordine naturale $x_1,x_2,\dots,x_n$.

#### Sistema triangolare superiore $-$ sostituzione all'indietro

Nel caso di una matrice triangolare superiore la situazione è analoga, ma il calcolo procede in direzione opposta.

La formula generale diventa

$$ x_i = \frac{b_i - \sum_{j=i+1}^{n}r_{ij}x_j}{r_{ii}},\quad i=n,\dots,1 $$

In questo caso le incognite vengono determinate partendo dall'ultima equazione e procedendo verso l'alto. Per questo motivo l'algoritmo prende il nome di **sostituzione all'indietro**.

#### Costo computazionale

Per determinare il costo dell’algoritmo si osserva quante operazioni sono necessarie per calcolare ogni incognita.

Alla riga $i$ è necessario calcolare una somma che coinvolge $i-1$ termini, cioè

$$ \sum_{j=1}^{i-1} r_{ij}x_i $$

Sommando il numero di operazioni per tutte le righe si ottiene

$$ \sum_{i=1}^n (i-1) = \frac{n(n-1)}{2} $$

Il costo computazionale è quindi dell’ordine di

$$ \mathcal{O}\Big(\frac{n^2}{2}\Big)\approx\mathcal{O}(n^2) $$

Ad ogni passo si effettuano inoltre una divisione e alcune operazioni elementari. Tuttavia il numero totale di divisioni è dell’ordine di $n$, molto inferiore rispetto alle operazioni quadratiche, e quindi non influisce sull’ordine di complessità complessivo.

#### Instabilità degli algoritmi di sostituzione

> Per instabilità numerica si intende una situazione in cui un errore molto piccolo, introdotto durante una delle operazioni dell’algoritmo, si propaga e viene amplificato nei passi successivi, producendo un errore finale molto più grande.

Gli algoritmi di **sostituzione in avanti e all’indietro** sono efficienti dal punto di vista computazionale, ma possono diventare **numericamente instabili** quando gli elementi della matrice triangolare assumono particolari configurazioni.

**Esempio**: Quando gli elementi del triangolo inferiore sono molto grandi rispetto agli elementi diagonali (errore di troncamento).

Consideriamo il primo passo dell’algoritmo di sostituzione per un sistema triangolare inferiore. Il calcolo della prima incognita è

$$ x_1 = \frac{b_1}{l_{11}} $$

Nel calcolo numerico reale questa operazione viene eseguita in **aritmetica floating-point**, quindi il risultato effettivo è affetto da un piccolo errore di arrotondamento. Indichiamo con $\tilde x_1$ il valore calcolato dalla macchina:

$$ \tilde x_1 = \frac{b_1}{l_{11}}(1 + \epsilon_1) = x_1^*(1 + \epsilon_1), $$

dove:
- $x_1^*$ è il valore esatto
- $\epsilon_1$ rappresenta l’errore relativo introdotto dall’aritmetica floating-point
- $|\epsilon_1|\le u$, con $u$ **precisione di macchina**.

Nel passo successivo utilizziamo questo valore approssimato per calcolare la seconda incognita. Sostituendo $\tilde x_1$ nella seconda equazione si ottiene

$$ \tilde x_2 = x_2^* + \frac{l_{21}x_1^*}{l_{22}}\epsilon_1 $$

Questo risultato mostra che l’errore iniziale $\epsilon_1$ **viene moltiplicato dal fattore**

$$ \frac{l_{21}}{l_{22}} $$

Se questo rapporto è molto grande (ad esempio quando $l_{21}$ è molto più grande di $l_{22}$), anche un errore inizialmente molto piccolo può diventare **significativamente amplificato** già nel calcolo della seconda componente.

In generale, quando i coefficienti della matrice triangolare generano **rapporti molto grandi tra gli elementi**, gli errori di arrotondamento possono propagarsi lungo l’algoritmo rendendo la soluzione numericamente poco affidabile.

## Metodi risolutivi per sistemi lineari **generici**

### 1) Calcolo esplicito dell'inversa della matrice

Dato il sistema lineare $Ax=b$ con $A\in\R^{n\times n}$ invertibile, dal punto di vista teorico la soluzione può essere scritta come

$$ x=A^{-1}b. $$

Questo suggerisce un possibile metodo risolutivo: calcolare prima l'inversa della matrice $A$ e poi moltiplicarla per il vettore dei termini noti $b$.

Tuttavia questo approccio **non viene utilizzato nel calcolo numerico**. Il calcolo esplicito dell'inversa è infatti computazionalmente costoso e può introdurre **problemi di stabilità numerica**, soprattutto quando la matrice contiene coefficienti molto grandi o i termini noti sono molto piccoli.

Per questo motivo, nella pratica si preferiscono **metodi più efficienti e stabili** che permettono di risolvere direttamente il sistema $Ax=b$ senza calcolare l'inversa della matrice.

### 2) Metodo di Cramer

Il **metodo di Cramer** è un procedimento teorico per risolvere un sistema lineare $Ax=b$ basato sul **calcolo dei determinanti**. La soluzione si ottiene calcolando $n+1$ determinanti di matrici di ordine $n$: uno per la matrice $A$ e $n$ determinanti ottenuti sostituendo, una alla volta, le colonne di $A$ con il vettore $b$.

Tuttavia il calcolo di un determinante con l’algoritmo diretto ha costo dell’ordine di $n!$, che cresce molto rapidamente con la dimensione della matrice. Di conseguenza il metodo di Cramer risulta **computazionalmente troppo costoso** e non è utilizzato nella pratica per risolvere sistemi lineari di grandi dimensioni.

### 3) Metodo di Gauss

