
$$
\newcommand{\tcr}[1]{\textcolor{red}{#1}}
\newcommand{\tcy}[1]{\textcolor{yellow}{#1}}
\newcommand{\tclg}[1]{\textcolor{lightgreen}{#1}}
\newcommand{\tclb}[1]{\textcolor{lightblue}{#1}}
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

Il **metodo di Gauss** (o **eliminazione gaussiana**) è uno degli algoritmi fondamentali per risolvere sistemi lineari della forma

$$ Ax=b $$

dove $A\in\R^{n\times n}$ è la matrice dei coefficienti, $x\in\R^n$ il vettore delle incognite e $b\in\R^n$ il vettore dei termini noti.

L’idea principale dell’algoritmo è **trasformare il sistema originale in uno equivalente ma più semplice da risolvere**. In particolare, attraverso *opportune combinazioni lineari* delle righe della matrice $A$, il metodo trasforma la matrice dei coefficienti in una matrice triangolare, per la quale la soluzione del sistema diventa immediata tramite gli algoritmi di sostituzione.

Dal punto di vista teorico il procedimento può essere interpretato come una **fattorizzazione della matrice**

$$ A=LU $$

dove:
- $L$ è una matrice **triangolare inferiore**,
- $U$ è una matrice **triangolare superiore**.

#### Struttura dell’algoritmo

Il metodo di Gauss si divide in **due fasi principali**.

Nella **prima fase**, detta **eliminazione gaussiana** o **fattorizzazione**, si trasformano progressivamente le righe della matrice $A$ fino ad ottenere una matrice triangolare superiore $U$. Durante questo processo si determinano anche i coefficienti che costituiranno la matrice triangolare inferiore $L$, ottenendo così la fattorizzazione

$$ A=LU. $$

Nella **seconda fase** si utilizza questa fattorizzazione per risolvere il sistema lineare. Sostituendo $A$ con $LU$ nel sistema originale si ottiene

$$ LUx=b. $$

Introducendo un nuovo vettore intermedio $y$, il sistema può essere riscritto come

$$ Ax = LUx = b \Rightarrow \begin{cases} Ly &=& b \\ Ux &=& y \end{cases} $$

Il problema viene quindi scomposto in **due sistemi triangolari**, molto più semplici da risolvere:

- il sistema $Ly=b$ viene risolto tramite **sostituzione in avanti**;
- il sistema $Ux=y$ viene risolto tramite **sostituzione all’indietro**.

#### Fase 1 $-$ Eliminazione gaussiana

La fase di eliminazione consiste nel **trasformare progressivamente la matrice** $A$ fino a ottenere una matrice triangolare superiore.

L’algoritmo procede per passi successivi. Se la matrice è di ordine $n$, il numero totale di passi di eliminazione è

$$ n−1. $$

Si parte dalla matrice iniziale

$$ A_1=A $$

e ad ogni passo si costruisce una nuova matrice

$$ A_{k+1},\quad k=1,\dots,n-1 $$

ottenuta tramite **combinazioni lineari delle righe** della matrice precedente.

L’obiettivo del passo $k$ è **annullare tutti gli elementi sotto la diagonale nella colonna** $k$. In questo modo, procedendo colonna dopo colonna, si costruisce gradualmente una matrice triangolare superiore.

#### Idea operativa dell’eliminazione

Per annullare gli elementi sotto la diagonale si utilizza l’elemento diagonale della colonna considerata, chiamato **elemento pivot** (o **perno**).

Supponiamo di lavorare sulla colonna $k$. L’elemento pivot è

$$ a_{kk} $$

Per eliminare l’elemento $a_{ik}$ con $i>k$ si costruisce un **moltiplicatore**

$$ m_{ik} = \frac{a_{ik}}{a_{kk}} $$

Successivamente si modifica la riga $i$ sottraendo alla riga stessa la riga $k$ moltiplicata per il moltiplicatore:

$$ \text{riga}_i \leftarrow \text{riga}_i - m_{ik}\cdot\text{riga}_k $$

Questa operazione produce uno **zero nella posizione** $(i,k)$ senza alterare l’equivalenza del sistema lineare. Ripetendo il procedimento per tutte le righe sotto la diagonale, la colonna $k$ diventa

$$ \begin{pmatrix}*\\0\\\vdots\\0\end{pmatrix}. $$

Procedendo successivamente sulle colonne $k+1,k+2,\dots$ si ottiene infine una matrice triangolare superiore $U$.

#### Fase 2 $-$ Risoluzione dei sistemi triangolari

Una volta ottenuta la fattorizzazione $A=LU$, il sistema lineare originale viene risolto in due passaggi. Nel primo passaggio si risolve $Ly=b$ con **sostituzione in avanti**. Nel secondo passaggio si risolve $Ux=y$ con **sostituzione all'indietro**, ottenendo infine il vettore soluzione $x$.

---

### Esempio della fase di eliminazione gaussiana

Consideriamo una matrice dei coefficienti

$$
A \in \mathbb{R}^{n\times n}.
$$

L’obiettivo della **fase di eliminazione** è trasformare progressivamente la matrice $A$ in una **matrice triangolare superiore**, annullando gli elementi sotto la diagonale principale. Questo viene fatto tramite **combinazioni lineari delle righe**, utilizzando opportuni coefficienti chiamati **moltiplicatori**.

#### Primo passo dell’eliminazione

Si parte dalla matrice iniziale

$$
A \equiv A_1 =
\begin{pmatrix}
\tcr{a_{11}} & a_{12} & a_{13} & \cdots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \cdots & a_{2n} \\
a_{31} & a_{32} & a_{33} & \cdots & a_{3n} \\
\vdots & \vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & a_{n3} & \cdots & a_{nn}
\end{pmatrix}.
$$

Nel primo passo si sceglie come **pivot** l’elemento sulla diagonale principale $\tcr{a_{11}}$ assumendo che $a_{11} \neq 0.$

L’obiettivo è **annullare tutti gli elementi sotto il pivot nella prima colonna**, cioè $a_{21}, a_{31}, \dots, a_{n1}$. Per farlo si introducono i **moltiplicatori**

$$
m_{i1} = \frac{a_{i1}}{a_{11}}\qquad i=2,\dots,n.
$$

Questi coefficienti indicano quanta parte della **prima riga** deve essere sottratta alla riga $i$ per eliminare l’elemento $a_{i1}$. Infatti si esegue la combinazione lineare

$$
\text{riga}_i
\leftarrow
\text{riga}_i - m_{i1}\,\text{riga}_1 \qquad i=2,\dots,n.
$$

Dopo questa operazione si ottiene una nuova matrice $A_2$ nella quale la prima colonna, sotto il pivot, contiene solo zeri:

$$
A_2 =
\begin{pmatrix}
a_{11} & a_{12} & a_{13} & \cdots & a_{1n} \\
0 & \tclb{a_{22}^{(2)}} & \tclb{a_{23}^{(2)}} & \tclb{\cdots} & \tclb{a_{2n}^{(2)}} \\
0 & \tclb{a_{32}^{(2)}} & \tclb{a_{33}^{(2)}} & \tclb{\cdots} & \tclb{a_{3n}^{(2)}} \\
\vdots & \tclb{\vdots} & \tclb{\vdots} & & \tclb{\vdots} \\
0 & \tclb{a_{n2}^{(2)}} & \tclb{a_{n3}^{(2)}} & \tclb{\cdots} & \tclb{a_{nn}^{(2)}}
\end{pmatrix}.
$$

Gli elementi aggiornati della matrice si calcolano tramite

$$
\tclb{a_{ij}^{(2)}} = a_{ij} - m_{i1}a_{1j}\qquad i,j=2,\dots,n.
$$

Questo primo passo può essere interpretato anche in termini di prodotto tra matrici:

$$
A_2 = L_1 A_1
$$

dove $L_1$ è una matrice triangolare inferiore che contiene i moltiplicatori della prima colonna

$$
L_1 = \begin{pmatrix}
1             &   &        &        & \\
\tcy{-m_{21}} & 1 &        &        & \\
\tcy{-m_{31}} & 0 & 1      &        & \\
\tcy{\vdots}  &   &        & \ddots & \\
\tcy{-m_{n1}} & 0 & \cdots & 0      & 1 \\
\end{pmatrix}
$$

---

#### Secondo passo dell’eliminazione

Una volta annullata la prima colonna sotto la diagonale, si passa alla **seconda colonna**.

Il nuovo pivot diventa $\tcr{a_{22}^{(2)}}$, con l’ipotesi $a_{22}^{(2)} \neq 0$.

Anche in questo caso l’obiettivo è **annullare tutti gli elementi sotto il pivot nella seconda colonna**, cioè $a_{32}^{(2)}, a_{42}^{(2)}, \dots, a_{n2}^{(2)}$. Si introducono quindi i **nuovi moltiplicatori**

$$
m_{i2} = \frac{a_{i2}^{(2)}}{a_{22}^{(2)}}
\qquad i=3,\dots,n.
$$

Le righe vengono modificate con la combinazione lineare

$$
\text{riga}_i
\leftarrow
\text{riga}_i - m_{i2}\,\text{riga}_2
\qquad i=3,\dots,n.
$$

Si ottiene così una nuova matrice $A_3$:

$$
A_3 =
\begin{pmatrix}
a_{11} & a_{12} & a_{13} & \cdots & a_{1n} \\
0 & \tcr{a_{22}^{(2)}} & a_{23}^{(2)} & \cdots & a_{2n}^{(2)} \\
0 & 0 & \tclb{a_{33}^{(3)}} & \tclb{\cdots} & \tclb{a_{3n}^{(3)}} \\
\vdots & \vdots & \tclb{\vdots} & & \tclb{\vdots} \\
0 & 0 & \tclb{a_{n3}^{(3)}} & \tclb{\cdots} & \tclb{a_{nn}^{(3)}}
\end{pmatrix}.
$$

Gli elementi aggiornati si calcolano con

$$
\tclb{a_{ij}^{(3)}} = a_{ij}^{(2)} - m_{i2}a_{2j}^{(2)} \qquad i,j=3,\dots,n.
$$

Anche questo passo può essere scritto come

$$
A_3 = L_2 A_2
$$

dove $L_2$ è una matrice triangolare inferiore che contiene i moltiplicatori della seconda colonna

$$
L_2 = \begin{pmatrix}
1      &               &        &        & \\
0      & 1             &        &        & \\
0      & \tcy{-m_{32}} & 1      &        & \\
\vdots & \tcy{\vdots}  &        & \ddots & \\
0      & \tcy{-m_{n2}} & \cdots & 0      & 1 \\
\end{pmatrix}
$$

---

#### Prosecuzione dell’algoritmo

Il procedimento continua nello stesso modo per le colonne successive. Al passo $k$:

- si sceglie come pivot l’elemento $a_{kk}^{(k)}$;
- si calcolano i moltiplicatori $m_{ik}$;
- si annullano gli elementi sotto il pivot tramite combinazioni lineari delle righe.

Dopo $n-1$ passi si ottiene una **matrice triangolare superiore $U$**. I moltiplicatori utilizzati durante l’eliminazione costituiscono invece gli elementi della **matrice triangolare inferiore $L$**.

In questo modo si ottiene la fattorizzazione fondamentale del metodo di Gauss:

$$
A = LU.
$$

Questa fattorizzazione permette poi di risolvere il sistema lineare tramite due sistemi triangolari molto più semplici.

---

### Studio implementazione dell’algoritmo di Gauss

Le **formule di aggiornamento** viste nella fase di eliminazione costituiscono di fatto l’**algoritmo di Gauss**. Per implementarlo è sufficiente tradurre queste formule in cicli sugli indici della matrice.

L’algoritmo può essere organizzato tramite **tre cicli annidati**.  
Il ciclo più esterno rappresenta il **passo di eliminazione**. Ad ogni passo si sceglie il pivot sulla diagonale principale e si eliminano gli elementi sotto di esso.

Per una matrice $A \in \mathbb{R}^{n\times n}$ l’algoritmo procede quindi nel seguente modo:

- il **ciclo esterno** scorre i passi dell’eliminazione ($k=1,\dots,n-1$);
- il **secondo ciclo** considera le righe sotto il pivot ($i=k+1,\dots,n$) e calcola il moltiplicatore
  $$
  m_{ik} = \frac{a_{ik}}{a_{kk}};
  $$
- il **terzo ciclo** aggiorna gli elementi della riga $i$ a destra del pivot ($j=k+1,\dots,n$) secondo la formula

  $$
  a_{ij} \leftarrow a_{ij} - m_{ik} a_{kj}.
  $$

Dal punto di vista implementativo, l’algoritmo **sovrascrive progressivamente la matrice** durante i vari passi dell’eliminazione. In questo modo non è necessario memorizzare tutte le matrici intermedie $A_1, A_2, \dots, A_n$, ma si aggiorna direttamente la matrice corrente. Questo rende il metodo **più efficiente in termini di memoria**.

Durante l’eliminazione vengono inoltre calcolati i **moltiplicatori** $m_{ik}$. Questi valori non devono essere scartati, perché costituiscono gli elementi della matrice triangolare inferiore $L$.

Una strategia molto comune consiste nel **memorizzare i moltiplicatori nella parte inferiore della matrice**, al posto degli zeri che si generano durante l’eliminazione. In questo modo, una volta completato il procedimento:

- la parte **triangolare superiore** della matrice contiene $U$;
- la parte **triangolare inferiore** contiene i moltiplicatori che definiscono $L$.

#### Costo computazionale della fattorizzazione

Durante la fattorizzazione di Gauss si eseguono due tipi principali di operazioni: il **calcolo dei moltiplicatori** e l’**aggiornamento degli elementi della matrice**.

I moltiplicatori sono

$$
m_{ik}=\frac{a_{ik}}{a_{kk}}, \qquad i=k+1,\dots,n.
$$

Il numero totale di quozienti è

$$
\sum_{k=1}^{n-1} (n-k) = \frac{n(n-1)}{2}
\approx \mathcal{O}\!\left(\frac{n^2}{2}\right).
$$

Questo corrisponde anche al numero di elementi del **triangolo inferiore** della matrice.

L’aggiornamento della sottomatrice richiede invece

$$
\sum_{k=1}^{n-1} (n-k)^2
=
\frac{n(n-1)(2n-1)}{6}
\approx \mathcal{O}\!\left(\frac{n^3}{3}\right)
$$

**somme e prodotti**.

Il costo dominante è quindi cubico e la **complessità complessiva della fattorizzazione di Gauss** è

$$
\mathcal{O}(n^3).
$$

---

### Interpretazione matriciale del passo di eliminazione

Consideriamo una matrice $3\times3$:

$$
A =
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}.
$$

Nel primo passo il pivot è $a_{11}$. Dopo aver calcolato i moltiplicatori

$$
m_{21} = \frac{a_{21}}{a_{11}}, 
\qquad
m_{31} = \frac{a_{31}}{a_{11}},
$$

si aggiornano le righe inferiori sottraendo un multiplo della prima riga.

L’aggiornamento della sottomatrice in basso a destra può essere scritto come

$$
\begin{pmatrix}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{pmatrix}
-
\begin{pmatrix}
m_{21}a_{12} & m_{21}a_{13} \\
m_{31}a_{12} & m_{31}a_{13}
\end{pmatrix}.
$$

Questa operazione può essere riscritta in forma compatta come **prodotto tra vettori**:

$$
\begin{pmatrix}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{pmatrix}
-
\begin{pmatrix}
m_{21} \\
m_{31}
\end{pmatrix}
\begin{pmatrix}
a_{12} & a_{13}
\end{pmatrix}.
$$

Il risultato è la nuova sottomatrice aggiornata:

$$
\begin{pmatrix}
a_{22}^{(2)} & a_{23}^{(2)} \\
a_{32}^{(2)} & a_{33}^{(2)}
\end{pmatrix}.
$$

Questa scrittura mostra che il passo di eliminazione può essere interpretato come una **operazione matriciale di tipo prodotto esterno**.

Dal punto di vista implementativo ciò permette di sostituire parte dei cicli con **operazioni vettoriali o matriciali**, migliorando l’efficienza dell’algoritmo nelle implementazioni numeriche (come quelle utilizzate nei software scientifici).

---

### Fattorizzazione di Gauss come Trasformazione Matriciale

#### Trasformazione elementare di Gauss

Nel procedimento di eliminazione gaussiana abbiamo visto che, partendo dalla matrice iniziale $A_1 = A$, vogliamo costruire una nuova matrice $A_2$ in cui gli elementi **sotto il primo pivot** $a_{11}$ siano nulli.   Per ottenere questo risultato si calcolano i **moltiplicatori** e si eseguono le **combinazioni lineari delle righe**. Questa operazione produce una nuova matrice $A_2$ equivalente alla precedente ma con la **prima colonna triangolarizzata** (zeri sotto la diagonale).

Lo stesso procedimento può essere interpretato in modo alternativo: invece di descrivere le operazioni riga per riga, possiamo rappresentarle come il **prodotto tra una matrice speciale e la matrice originale**.  

In particolare, esiste una matrice con **1 sulla diagonale principale** e i **moltiplicatori con segno negativo** nella prima colonna sotto la diagonale:

$$
A_2 =
\begin{pmatrix}
1       &   &        &        & \\
-m_{21} & 1 &        &        & \\
-m_{31} & 0 & 1      &        & \\
\vdots  &   &        & \ddots & \\
-m_{n1} & 0 & \cdots & 0      & 1
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{12} & a_{13} & \cdots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \cdots & a_{2n} \\
a_{31} & a_{32} & a_{33} & \cdots & a_{3n} \\
\vdots & \vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & a_{n3} & \cdots & a_{nn}
\end{pmatrix}
= L A_1 .
$$

Questa rappresentazione **non modifica l’algoritmo** né la sua implementazione: le operazioni da eseguire sono esattamente le stesse viste prima. Tuttavia è concettualmente importante perché mostra che ogni passo dell’eliminazione di Gauss può essere interpretato come una **trasformazione matriciale**, cioè come il prodotto tra una matrice elementare e la matrice corrente.  

Questa osservazione sarà fondamentale per comprendere come l’eliminazione gaussiana porti naturalmente alla **fattorizzazione $\mathbf{A = LU}$**.

---

#### Esempio di trasformazione elementare di Gauss

Consideriamo una matrice $3\times3$. Dopo aver scelto come pivot $a_{11}$, si calcolano i moltiplicatori

$$
m_{21} = \frac{a_{21}}{a_{11}}, \qquad 
m_{31} = \frac{a_{31}}{a_{11}} .
$$

Utilizzando questi moltiplicatori si eseguono le combinazioni lineari delle righe

$$
r_i \leftarrow r_i - m_{i1} r_1 ,
$$

ottenendo una nuova matrice in cui gli elementi sotto il pivot sono nulli:

$$
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}
\Rightarrow
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
0 & a_{22} - m_{21}a_{12} & a_{23} - m_{21}a_{13} \\
0 & a_{32} - m_{31}a_{12} & a_{33} - m_{31}a_{13}
\end{pmatrix}.
$$

La stessa operazione può essere espressa come **prodotto matriciale** con una matrice triangolare inferiore con 1 sulla diagonale:

$$
\begin{pmatrix}
1 & 0 & 0 \\
-m_{21} & 1 & 0 \\
-m_{31} & 0 & 1
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}.
$$

Queste matrici sono chiamate **trasformazioni elementari di Gauss**. Ogni passo dell’eliminazione corrisponde alla moltiplicazione della matrice corrente per una di queste matrici.

---

#### Fattorizzazione LU tramite eliminazione di Gauss

Applicando l’algoritmo di eliminazione di Gauss a una matrice $A$, e assumendo che **tutti i pivot siano diversi da zero**, si ottiene una matrice **triangolare superiore** $U$ e una serie di **moltiplicatori**

$$
m_{ik}, \qquad k = 1,\dots,n-1,\quad i = k+1,\dots,n
$$

Questi moltiplicatori definiscono le **Trasformazioni Elementari di Gauss** $L_1, L_2, \dots, L_{n-1}$. L’intero processo di eliminazione è quindi un susseguirsi di $n-1$ prodotti matriciali, che porta alla matrice triangolare superiore $U$:

$$
L_{n-1} L_{n-2} \cdots L_2 L_1 A = U
$$

Le matrici $L_k$ sono **triangolari inferiori con diagonale unitaria**, quindi sono **nonsingolari** (invertibili). Moltiplicando entrambi i membri per le inverse delle trasformazioni elementari otteniamo

$$
A = \underbrace{L_1^{-1} L_2^{-1} \cdots L_{n-2}^{-1} L_{n-1}^{-1}}_{L}U
$$

Definendo

$$
L = L_1^{-1} L_2^{-1} \cdots L_{n-2}^{-1} L_{n-1}^{-1}
$$

si ottiene la **fattorizzazione LU** della matrice:

$$ A = LU $$

dove $L$ è una matrice **triangolare inferiore con diagonale unitaria** e $U$ è **triangolare superiore**.

---

### Teorema di fattorizzazione di Gauss

Sia $A \in \mathbb{R}^{n\times n}$. Se durante l’eliminazione di Gauss tutti i pivot risultano diversi da zero,

$$
a_{kk}^{(k)} \ne 0, \qquad k=1,\dots,n-1,
$$

allora la matrice $A$ ammette una **fattorizzazione LU**

$$
A = LU
$$

dove $U$ è una **matrice triangolare superiore** e $L$ è una **matrice triangolare inferiore con diagonale unitaria**.

La matrice $U$ si ottiene applicando in sequenza le trasformazioni elementari di Gauss alla matrice iniziale:

$$
U = L_{n-1}\cdots L_1A =
\begin{pmatrix}
a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
0 & a_{22}^{(2)} & a_{23}^{(2)} & \dots & a_{2n}^{(2)} \\
0 & 0 & a_{33}^{(3)} & \dots & a_{3n}^{(3)} \\
\vdots & & & \ddots & \vdots \\
0 & \dots & \dots & 0 & a_{nn}^{(n)}
\end{pmatrix}.
$$

La matrice $L$ è invece costruita a partire dai **moltiplicatori** $m_{ik}$ utilizzati durante l’eliminazione:

$$
L = L_1^{-1}\cdots L_{n-1}^{-1} =
\begin{pmatrix}
1 & & & & \\
m_{21} & 1 & & & \\
m_{31} & m_{32} & 1 & & \\
\vdots & & \ddots & \ddots & \\
m_{n1} & m_{n2} & \dots & m_{n,n-1} & 1
\end{pmatrix}.
$$

In pratica, i moltiplicatori calcolati durante l’eliminazione costituiscono proprio gli elementi della parte inferiore della matrice $L$.

---

#### Interpretazione delle trasformazioni $L_k$

Ogni trasformazione elementare di Gauss può essere interpretata come una **modifica dell’identità**.  

Ad esempio, nel caso $3\times3$:

$$
L_1 =
\begin{pmatrix}
1 & 0 & 0 \\
-m_{21} & 1 & 0 \\
-m_{31} & 0 & 1
\end{pmatrix}.
$$

Questa matrice può essere riscritta come

$$
L_1 =
I -
\begin{pmatrix}
0 \\
m_{21} \\
m_{31}
\end{pmatrix}
\begin{pmatrix}
1 & 0 & 0
\end{pmatrix}.
$$

Il termine sottratto è il **prodotto diadico** (o prodotto esterno) tra due vettori.  
In generale quindi una trasformazione elementare può essere vista come

$$
L_k = I - uv^T
$$

dove $u$ e $v$ sono vettori opportuni che determinano le combinazioni lineari tra le righe.

---

#### Inversa delle trasformazioni elementari

Un risultato importante è che l’inversa di una trasformazione elementare di Gauss ha **la stessa struttura**, ma con i moltiplicatori di segno opposto.

Ad esempio:

$$
L_1^{-1} =
\begin{pmatrix}
1 & 0 & 0 \\
-m_{21} & 1 & 0 \\
-m_{31} & 0 & 1
\end{pmatrix}^{-1}
=
\begin{pmatrix}
1 & 0 & 0 \\
m_{21} & 1 & 0 \\
m_{31} & 0 & 1
\end{pmatrix}.
$$

Questo risultato permette di costruire la matrice $L$ della fattorizzazione LU come prodotto delle inverse delle trasformazioni elementari applicate durante l’eliminazione.

---

### Fallimento dell’algoritmo di Gauss e condizione sui minori principali

L’algoritmo di eliminazione di Gauss richiede che i **pivot** utilizzati durante i vari passi dell’eliminazione siano diversi da zero. In altre parole, al passo $k$ deve valere

$$
a_{kk}^{(k)} \ne 0.
$$

Una condizione teorica sufficiente affinché questo accada è che la matrice $A$ abbia **tutti i minori principali non nulli**.

Un **minore principale** è il determinante della sottomatrice ottenuta prendendo le prime $k$ righe e le prime $k$ colonne della matrice.

Ad esempio, per una matrice $3\times3$

$$
A =
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}
$$

i minori principali sono

$$
\det
\begin{pmatrix}
a_{11}
\end{pmatrix},
\qquad
\det
\begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{pmatrix},
\qquad
\det(A).
$$

Se tutti questi determinanti sono diversi da zero, allora l’eliminazione di Gauss può essere eseguita senza incontrare pivot nulli.

Tuttavia verificare esplicitamente questa condizione richiederebbe il **calcolo di molti determinanti**, operazione computazionalmente costosa. Per questo motivo tale condizione viene usata principalmente a **livello teorico**, mentre nella pratica si modifica direttamente l’algoritmo.

---

#### Modifica dell’algoritmo: scambio delle equazioni

Se durante l’eliminazione compare un pivot nullo (o numericamente sfavorevole), è possibile **scambiare due righe** della matrice dei coefficienti. Poiché ogni riga rappresenta un’equazione del sistema, questo equivale semplicemente a **cambiare l’ordine delle equazioni**, ottenendo comunque un sistema equivalente.

Lo scambio viene scelto in modo da portare nella posizione di pivot un elemento più adatto, cioè **non nullo**. Dal punto di vista implementativo questa operazione è semplice: basta scambiare le due righe della matrice dei coefficienti e, contemporaneamente, le corrispondenti componenti del vettore dei termini noti.

Durante l’esecuzione dell’algoritmo i moltiplicatori sono memorizzati nella parte inferiore della matrice, quindi lo scambio delle righe coinvolge automaticamente anche questi valori.

---

#### Matrici di permutazione

Dal punto di vista teorico, lo scambio di due righe può essere rappresentato come il prodotto tra la matrice corrente e una **matrice di permutazione elementare**.  

Se indichiamo con $P_k$ la matrice di permutazione utilizzata al passo $k$ e con $L_k$ la trasformazione di Gauss corrispondente, l’eliminazione può essere descritta come una successione di prodotti matriciali:

$$
A_2 = L_1 P_1 A_1
$$

e, proseguendo nei passi successivi,

$$
U = L_{n-1} P_{n-1} \cdots L_2 P_2 L_1 P_1 A.
$$

Questa rappresentazione è utile soprattutto dal punto di vista teorico; nell’implementazione pratica ci si limita semplicemente a **scambiare le righe della matrice**.

È comunque necessario che nella colonna considerata esista **almeno un elemento non nullo**, altrimenti la matrice sarebbe **singolare** e il sistema non avrebbe soluzione unica.

---

### Scelta del pivot: pivoting parziale

Non è sufficiente richiedere che il pivot sia diverso da zero. Se il pivot è **molto piccolo**, i moltiplicatori calcolati durante l’eliminazione possono diventare molto grandi, causando **instabilità numerica** a causa degli errori di arrotondamento.

Per migliorare la stabilità dell’algoritmo si utilizza quindi una strategia chiamata **pivoting parziale**.  

Al passo $k$ si sceglie come pivot l’elemento di **valore assoluto massimo nella colonna $k$**, tra le righe da $k$ a $n$. Successivamente si scambia la riga corrente con quella che contiene tale elemento.

In questo modo si evita di dividere per numeri troppo piccoli e si riduce la propagazione degli errori numerici. In **aritmetica esatta** questa precauzione non sarebbe necessaria (basterebbe che il pivot fosse non nullo), ma in **aritmetica floating-point** è fondamentale per la stabilità dell’algoritmo.

Questa strategia è adottata anche nelle implementazioni pratiche delle librerie numeriche, come ad esempio quelle utilizzate da **NumPy**.

#### Costo computazionale scelta

La scelta del pivot avviene ad ogni passo $k$ dell’algoritmo, individuando il massimo tra i $n-k+1$ elementi candidati nella colonna corrente.

Operativamente si confrontano gli elementi uno alla volta, mantenendo il massimo corrente e aggiornandolo quando si trova un valore maggiore.

Il costo della ricerca del pivot è complessivamente $\mathcal{O}(n^2/2)$, poiché viene ripetuta per ogni colonna su un numero decrescente di elementi.

Questo costo è inferiore rispetto alla fattorizzazione completa, che richiede $\mathcal{O}(n^3/3)$, quindi non è il termine dominante dell’algoritmo.

---

### Librerie numeriche utilizzate da NumPy

Le funzioni di risoluzione dei sistemi lineari, come `np.linalg.solve`, si basano su routine numeriche altamente ottimizzate provenienti da librerie storiche sviluppate originariamente in Fortran, in particolare **LAPACK** (Linear Algebra PACKage).

Nel caso di sistemi lineari generali, la routine utilizzata è tipicamente `_gesv`, che implementa la fattorizzazione $LU$ con pivoting per matrici dense. Questo significa che, dietro le quinte, NumPy non calcola l’inversa ma utilizza algoritmi numericamente stabili ed efficienti basati sulla decomposizione della matrice.

LAPACK fornisce diverse routine specializzate a seconda della struttura della matrice. Ad esempio, esistono metodi dedicati per matrici a banda, che sfruttano la presenza di molti zeri per ridurre il costo computazionale e l’uso di memoria.

Inoltre, sono disponibili algoritmi specifici per matrici con proprietà particolari, come matrici simmetriche o simmetriche definite positive. In questi casi si possono utilizzare fattorizzazioni più efficienti (ad esempio la fattorizzazione di Cholesky), migliorando sia le prestazioni che la stabilità numerica.

Questa suddivisione in casi specifici è fondamentale nel calcolo numerico: riconoscere la struttura della matrice permette di scegliere l’algoritmo più adatto e ottenere soluzioni più veloci e affidabili.

---

### Matrici sparse e problemi di inpainting

Nel contesto del *data filling* (o *inpainting*), le matrici che emergono hanno una struttura particolare: oltre alla **diagonale principale** e alle **diagonali immediatamente adiacenti**, possono comparire altre **diagonali più lontane**, separate da blocchi di zeri. Per questo motivo non sempre è corretto considerarle matrici a banda in senso stretto.

Una matrice quadrata di ordine $n$ si dice *sparsa* quando il numero di elementi non nulli è molto piccolo rispetto al totale $n^2$. In questi casi, memorizzare esplicitamente tutti gli zeri è inefficiente sia in termini di memoria che di tempo di calcolo.

Per questo motivo si utilizzano formati di memorizzazione compressa, che conservano solo le informazioni rilevanti. I più comuni sono:
- **CCS (Compressed Column Storage)**: compressione per colonne
- **CRS (Compressed Row Storage)**: compressione per righe

L’idea di base è memorizzare in un vettore tutti gli elementi non nulli della matrice. A questo si affiancano strutture ausiliarie che permettono di ricostruire la posizione di ciascun elemento, tipicamente tramite indici di riga e colonna. 

Una ulteriore ottimizzazione consiste nel raggruppare gli elementi per riga o colonna: invece di salvare ogni indice singolarmente, si memorizza la posizione iniziale di ciascun gruppo, sfruttando il fatto che gli elementi sono ordinati. Questo riduce ulteriormente lo spazio necessario.

Nel problema di inpainting visto in laboratorio, la matrice viene convertita in formato sparso proprio per motivi di efficienza: la maggior parte degli elementi è nulla o non informativa, quindi lavorare con una rappresentazione densa sarebbe inutilmente costoso.

Infine, nel caso di matrici sparse, anche la scelta del pivot e l’ordine delle operazioni diventano cruciali. Esistono algoritmi specifici che cercano non solo stabilità numerica, ma anche di preservare la sparsità, evitando la creazione di nuovi elementi non nulli (*fill-in*) durante la fattorizzazione.

Librerie specializzate, come quelle presenti nell’**HSL Software Index**, forniscono metodi avanzati per la risoluzione efficiente di sistemi lineari sparsi, sfruttando queste tecniche.

---

### Matrici speciali e algoritmi di risoluzione

Quando una matrice possiede una struttura o proprietà particolari, è possibile progettare algoritmi di risoluzione più efficienti rispetto al caso generale. L’idea è sfruttare tali proprietà per ridurre sia il costo computazionale sia l’uso di memoria.

---

### Matrici simmetriche

Una matrice $A$ è simmetrica se $A = A^T$. In questo caso, le informazioni contenute sopra e sotto la diagonale principale coincidono, quindi è sufficiente memorizzare solo metà matrice. Questo comporta un risparmio significativo in memoria e, di conseguenza, anche nelle operazioni computazionali.

Se la matrice è simmetrica, non singolare e con tutti i minori principali diversi da zero, allora è possibile utilizzare una fattorizzazione più efficiente della classica $LU$, ovvero:

$$ A = LDL^T $$

dove $L$ è triangolare inferiore con diagonale unitaria e $D$ è una matrice diagonale.

Il vantaggio principale è che non è necessario calcolare una matrice triangolare superiore indipendente: $U$ viene sostituita da $L^T$, riducendo il numero di operazioni. Il costo computazionale passa da $\mathcal{O}\left(\frac{n^3}{3}\right)$ nel caso generale a circa la metà $\mathcal{O}\left(\frac{1}{2}\cdot\frac{n^3}{3}\right)$.

#### Risoluzione del sistema

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

### Matrici simmetriche definite positive (fatt. di Cholesky)

Se una matrice $A$ è simmetrica ($A = A^T$), allora i suoi autovalori sono reali. Se inoltre tutti gli autovalori sono positivi, la matrice si dice *definita positiva*. Questa proprietà è molto importante perché garantisce l’esistenza di algoritmi di risoluzione particolarmente efficienti e numericamente stabili.

Nel caso simmetrico, come visto, il costo computazionale si riduce rispetto al caso generale. Se in più la matrice è definita positiva, è possibile utilizzare la **fattorizzazione di Cholesky**, che rappresenta il metodo più efficiente e stabile in questo contesto.

In questo caso, la matrice si fattorizza come:

$$ A = LL^T $$

dove $L$ è una matrice triangolare inferiore con elementi reali e diagonale positiva.

#### Idea dell’algoritmo (costruzione di $L$)

L’algoritmo di Cholesky costruisce la matrice $L$ elemento per elemento, imponendo l’uguaglianza $A = LL^T$. Considerando, ad esempio, il caso $3 \times 3$:

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

#### Vantaggi

La fattorizzazione di Cholesky è più efficiente della fattorizzazione $LU$, con un costo computazionale di circa

- **Simmetria**: La complessità si riduce della metà: $\mathcal{O}(\frac{n^3}{6})$.
- **Positività**: Algoritmo + stabile di tutti (algoritmo di Cholesky).

ovvero circa la metà rispetto al caso generale. Inoltre, è numericamente più stabile, grazie alla struttura della matrice e all’assenza di pivoting.

Per questo motivo, quando una matrice è simmetrica definita positiva, Cholesky è la scelta migliore per la risoluzione del sistema lineare.

---

### Fattorizzazione QR

La fattorizzazione $QR$ è una tecnica che consente di decomporre una matrice $A$ non singolare come prodotto di due matrici:

$$ A = QR $$

dove $Q \in \mathbb{R}^{n \times n}$ è una matrice **ortogonale** e $R \in \mathbb{R}^{n \times n}$ è una matrice **triangolare superiore**.

#### Matrici ortogonali

Una matrice $Q$ si dice ortogonale se soddisfa:

$$ Q^T Q = QQ^T = I $$

Questa proprietà implica che $Q$ è non singolare e che la sua inversa coincide con la trasposta:

$$ Q^{-1} = Q^T $$

Dal punto di vista computazionale, questo è estremamente vantaggioso, perché evitare il calcolo esplicito dell’inversa migliora sia l’efficienza sia la stabilità numerica.

#### Risoluzione di sistemi con matrici ortogonali

Se si considera un sistema del tipo:

$$ Qy = b $$

moltiplicando a sinistra per $Q^T$ si ottiene:

$$ Q^T Q y = Q^T b \quad \Rightarrow \quad y = Q^T b $$

Quindi la soluzione si riduce a un semplice prodotto matrice-vettore.

#### Idea della fattorizzazione QR

1. Applicando la fattorizzazione $A = QR$ al sistema lineare $Ax = b$, si ottiene:

    $$ QRx = b $$

2. Ponendo $y = Rx$, il sistema diventa:

    $$ Qy = b $$

3. che si risolve facilmente moltiplicando a sinistra per $Q^T$:

    $$ y = Q^T b $$

4. A questo punto si risolve il sistema triangolare superiore:

    $$ Rx = y $$

mediante sostituzione all’indietro.

#### Algoritmo di Householder

Esistono diversi metodi per calcolare la fattorizzazione $QR$. Tra questi, l’algoritmo di **Householder** è il più utilizzato in pratica, perché è numericamente stabile ed efficiente.

L’idea è costruire una sequenza di trasformazioni ortogonali che annullano progressivamente gli elementi sotto la diagonale, trasformando la matrice $A$ in una matrice triangolare superiore $R$. La matrice $Q$ è il prodotto delle trasformazioni ortogonali applicate.

---

### Algoritmo di Householder per la fattorizzazione $QR$

L’algoritmo di Householder consente di costruire la fattorizzazione $A = QR$ attraverso una sequenza di trasformazioni ortogonali che riducono progressivamente la matrice $A$ in forma triangolare superiore.

#### Confronto con il metodo di Gauss

Nel metodo di Gauss si applicano trasformazioni elementari triangolari inferiori:

$$ L_{n-1} \cdots L_1 A = U $$

dove ogni passo annulla gli elementi sotto il pivot utilizzando combinazioni lineari di righe. Le matrici $L_k$ sono triangolari inferiori, mentre il risultato finale $U$ è triangolare superiore.

Nel metodo di Householder, invece, si utilizzano trasformazioni ortogonali:

$$ U_{n-1} \cdots U_1 A = R $$

dove le matrici $U_k$ sono ortogonali e il risultato $R$ è triangolare superiore. La differenza fondamentale è che le trasformazioni non sono più combinazioni lineari di righe, ma riflessioni (o rotazioni) nello spazio.

#### Interpretazione geometrica

L’idea alla base dell’algoritmo è trasformare ogni colonna della matrice in modo da annullare tutti gli elementi sotto il primo.

Considerando la prima colonna $a_1$ di $A$:

$$
a_1 =
\begin{pmatrix}
a_{11} \\ a_{21} \\ \vdots \\ a_{n1}
\end{pmatrix}
$$

si costruisce una matrice ortogonale $U_1$ tale che:

$$
U_1 a_1 =
\begin{pmatrix}
-\|a_1\| \\ 0 \\ \vdots \\ 0
\end{pmatrix}
$$

Geometricamente, questa operazione corrisponde a una riflessione che allinea il vettore $a_1$ con il primo asse canonico. In questo modo, tutte le componenti sotto la prima vengono annullate in un solo passo.

#### Costruzione della trasformazione di Householder

Per costruire $U_1$, si procede come segue.

Si calcola la norma del vettore:

$$ \sigma_1 = \|a_1\| $$

Si definisce quindi il vettore:

$$ v_1 = a_1 + \sigma_1 e_1 $$

dove $e_1 = (1,0,\dots,0)^T$ è il primo vettore della base canonica.

Si introduce poi lo scalare:

$$ \alpha_1 = \frac{1}{2} \|v_1\|^2 $$

Infine, la matrice di Householder è definita come:

$$ U_1 = I - \frac{1}{\alpha_1} v_1 v_1^T $$

Questa matrice è ortogonale e simmetrica, e realizza la riflessione desiderata.

#### Idea generale dell’algoritmo

Applicando successivamente trasformazioni analoghe alle sottomatrici ottenute, si annullano progressivamente tutti gli elementi sotto la diagonale. Dopo $n-1$ passi si ottiene una matrice triangolare superiore $R$.

La matrice $Q$ della fattorizzazione si ottiene come prodotto delle trasformazioni ortogonali:

$$ Q = U_1^T U_2^T \cdots U_{n-1}^T $$

Poiché ogni $U_k$ è ortogonale e simmetrica, vale $U_k^T = U_k$, quindi:

$$ Q = U_1 U_2 \cdots U_{n-1} $$

Questo metodo è numericamente molto stabile, perché utilizza solo trasformazioni ortogonali, che preservano le norme e non amplificano gli errori di arrotondamento.

---
