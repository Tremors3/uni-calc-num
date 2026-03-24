# (7) Lezione 09-03-2026 | s 120..134 | Sistemi Lineari

## Studio sistemi lineari

### Condizione necessaria

Possiamo andare avanti con il calcolo di un sistema se la matrice dei coefficienti è non singolare. Il teorema di Rouchè-Capellì ci dice che se la matrice è invertibile, allora esiste una soluzione unica $Ax = b$.

### Studio del Condizionamento di un Sistema Lineare

Valutiamo la distanza tra le due soluzioni del sistema con dati perfetti e sistema con dati corrotti (slide 125).

$$ \begin{pmatrix} 1 \\ 1 \end{pmatrix} \hspace{20px} \begin{pmatrix} 2 \\ 0.5 \end{pmatrix} $$

$$ \| \begin{pmatrix} 1 \\ 1 \end{pmatrix} - \begin{pmatrix} 2 \\ 0.5 \end{pmatrix} \|_\infin = \| \begin{pmatrix} 1 \\ 0.5 \end{pmatrix} \|_\infin $$

Un problema si dice **mal condizionato** se leggere variazioni sui dati portano ad importanti variazioni sui risultati.

I problemi mal condizionati prevedono tecniche chiamate "**di regolarizzazione" specifiche**. In generale vogliamo cercare di evitare di incontrare problemi mal condizionati.

$$\begin{cases}
    x_1 & + & x_2 & = & 3 \\
    .499x_1 & + & 1.001x_2 & = & 1.5
\end{cases}$$


Notiamo che i coefficienti sono più o meno la metà rispetto a quelli nella prima riga. Questo indica che il problema è mal condizionato. In un sistema $n\times n$ basta che ci siano due di queste $n$ righe in una situazione simile a questa ed il problema è mal condizionato.

### Numero di condizionamento

Il caso del mal condizionamento si verifica quando $k(A)$ diventa grande.
Si dimostra che il numero di mal condizionamento è $\ge 1$ (slide 130).

Il **numero di condizionamento** fa da amplificatore all'errore sui dati.

Dimostrazione numero di condizionamento. Nella formula a slide 130 si denota come il fattore k amplifica l'errore sulle soluzioni. La disequazione mostra come l'errore relativo sui dati è maggiorato dall'errore sull seoluzioni aplificate per il $k(A)$.

Supponiamo che l'errore si trovi tutto nel termine noto. In realtà un'analisi simile la può fare anche quando gli errori li abbiamo sugli elementi della matrice. Quindi abbiamo errori sui termini noti e sulla matrice (slide 132). C'è sempre di mezzo l'indice di condizionamento.

Esprime il fattore di amplificazione sui dati che si riflette sulle soluzioni.

# (8) Lezione 10-03-2026 | s 135..139 | Sistemi Lineari Facili

### Strategia Sbagliata: Calcolare l'inversa di una matrice

In generale l'operazione di calcolo dell'inversa di una matrice è una operazione molto costosa computazionalmente (inutile) e instabile (esempio slide 137). Non calcoleremo mai l'inversa di una matrice.

### Come risolviamo un sistema lineare

Qual'è la struttura della matrice dei coefficienti?

Prima di partire a testa bassa con un algoritmo per risolvere un problema dobbiamo prima raccogliere più informazioni possibile riguardo ai dati del problema.

Il primo discriminante per arrivare ad un opportuno algoritmo è la **Matrice dei Coefficienti**.

Possono presentarsi dei casi facili:

#### 1) Caso matrice dei coefficienti **Diagonale** (slide 138)

Controllare se una matrice dei coefficienti è diagonale, è banale. Basta moltiplicare le componenti della diagonale.

La cosa bella di un sistema diagonale è che ogni equazione contiene una sola incognita; allora ciascuna equazione si può trattare in maniera indipendente da tutte le altre.

Per ogni incognita basta dividere $b_i$ per il coefficiente dell'incognita $x_i$

$$ x_i = \frac{b_i}{d_i} $$

Costo computazionale: abbiamo $n$ divisioni floating point.

#### 2) Caso matrice dei coefficienti **Diagonale** (slide 139)

$$\begin{pmatrix}
r_{11} \\ r_{21} & r_{22} \\ r_{31} & \cdots & r_{33} \\ \vdots &&& \ddots \\ r_{n1} && \cdots && r_{nn}
\end{pmatrix}\begin{pmatrix} b_1 \\ \vdots \\ \vdots \\ b_n \end{pmatrix} \\

\begin{cases}
    r_{11}x_1 & & & = b_1 & \to x_1 = \frac{b_1}{r_{11}} \\
    r_{21}x_1 & + r_{22}x_2 & & = b_2 & \to x_2 = \frac{b_2 - r_{21}x_1}{r_{22}} \\ \vdots \\

    r_{n1}x_1 & + r_{n2}x_2 & + \cdots + & r_{nn}x_n = b_n & \to x_i = \frac{b_i - r_{i1}x_1 - r_{i2}x_2 - \dots - r_{ii-1}x_{i-1}}{r_{ii}}  = \frac{b_i - \sum_{i=1}^{i-1} r_{ij}x_j}{r_{ii}}\\
\end{cases}$$

Il costo computazionale dell'algoritmo lo deriviamo considerando i calcoli a ciascun livello. Abbiamo che:

$$ \sum_{j=1}^{n} (j-1) = \frac{n(n-1)}{2} \quad\to\quad O\Big(\frac{n^2}{2}\Big) $$

Al passo i si effettuano $i$ somme e $i - 1$ prodotti, ed un quoziente. Le divisioni sono solo $i$ di un ordine inferiore a $i^2$, quindi non le riportiamo.

# (9) Lezione 11-03-2026 | s 140..152 | Sistemi Lineari Generici

### Instabilità metodo di sostituzione

Gli algoritmi di sostituzione possono diventare instabile quando gli elementi della matrice triangolare sono fatti in un certo modo (slide 140).

Instabilità: errore introdotto da un'operazione dell'algoritmo si propaga ed aumenta in modo ingente. L'errore piccolo commesso sul calcolo della prima componente potrebbe venir amplificato durante il calcolo delle componenti successive.

$$ \tilde x_1 = fl(b_1/l_{11}) = \frac{b_1}{l_{11}}(1 + \varepsilon_1) = x_1^*(1 + \varepsilon_1) $$

Dove $\varepsilon_1 \le u$, minore rispetto alla precisione di macchina. Sostituendo al valore con la tilde il valore di $x_1^*$ con compreso l'errore. Vediamo che troviamo la soluzione esatt apiù un errore. Errore dovuto al primo passo dell'algoritmo più il coefficiente.

$$ \tilde x_2 = x_2^* + \frac{l_{21}x_1^*}{l_{22}}\varepsilon_1 $$

Il coefficiente che moltiplica l'errore nel secondo passo potrebbe diventare molto grande. Già al calcolo della seconda componente, se $l_{21}$ è molto più grande di quello che sta sotto $l_{22}$ allora potremmo introdurre un errore ancora più grande.

### Sistemi qualsiasi $\mid$ 1) Metodo di Cramer

Basato sul calcolo di $n+1$ determinanti di matrici di ordine $n$. Il calcolo di un singolo determinante di una matrice costa tanto ($n!$). Dobbiamo trovare una soluzione più efficiente. Quello che ci impedisce di sfruttare questo algoritmo è la sua complessità computazionale.

### Sistemi qualsiasi $\mid$ 2) Metodo di Eliminazione di Gauss

$$
\newcommand{\tcr}[1]{\textcolor{red}{#1}}
\newcommand{\tcy}[1]{\textcolor{yellow}{#1}}
\newcommand{\tclg}[1]{\textcolor{lightgreen}{#1}}
\newcommand{\tclb}[1]{\textcolor{lightblue}{#1}}
$$

$$ Ax = b $$

Calcolare due nuove matrici $L,U$ che sono rispettivamente matrici triangolari Inferiore e Superiore. La loro proprietà è che il loro prodotto è uguale alla matrice di partenza.

$$ A = LU $$

La soluzione del sistema tramite il metodo di Gaus prevede lo scomponimento del sistema originale in due sistemi triangolari.

$$ Ax = LUx = b \Rightarrow \begin{cases} Ly &=& b \\ Ux &=& y \end{cases} $$

Come abbiamo ottenuto questo risultato? Partiamo da:

$$
Ax = b \quad A = LU
$$

Introduciamo una nuova variabile $y = Ux$, ed otteniamo:

$$
L\underbrace{Ux}_{y} = b \quad\Rightarrow\quad Ly = b \quad\Rightarrow\quad \begin{cases} Ly &=& b &\text{1° passo}\\ Ux &=& y &\text{2° passo} \end{cases}
$$

Idea del metodo di Gauss (metodo di Fattorizzazione):

- Fase 1:
    - Scomposizione di $A$ come prodotto di $LU$. Si tratta della fase più costosa.
- Fase 2:
    - `1° passo`: Metodo di **Sostituzione in Avanti**;
    - `2° Passo`: Metodo di **Sostituzione in all'Indietro**;

L'idea generale anche di altri metodi si basa sempre su questo concetto.
Suddividere la matrice di partenza in sotto matrici facili da risolvere.

#### Algoritmo di Fattorizzazione (Prima fase Gauss)

L'unico dato in questo caso è la Matrice dei Coefficienti $A$.

$$A = \begin{pmatrix}
a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \dots & a_{2n} \\
a_{31} & a_{32} & a_{33} & \dots & a_{3n} \\
\vdots & \vdots & \vdots &       & \vdots \\
a_{n1} & a_{n2} & a_{n3} & \dots & a_{nn}
\end{pmatrix}$$

Vogliamo calcolare un'altra matrice che sia Triangolare Superiore. Lo faremo un $n-1$ passi. Ciascuno di questi passi consisterà in...

$$
A = \begin{pmatrix}
\tcr{a_{11}} & a_{12} & a_{13} & \dots & a_{1n} \\
\tclg{a_{21}} & a_{22} & a_{23} & \dots & a_{2n} \\
\tclg{a_{31}} & a_{32} & a_{33} & \dots & a_{3n} \\
\tclg{\vdots} & \vdots & \vdots &       & \vdots \\
\tclg{a_{n1}} & a_{n2} & a_{n3} & \dots & a_{nn}
\end{pmatrix}$$

1) Vogliamo ricavare una nuova matrice in cui nella prima colonna, sotto la diagonale principale, vogliamo avere solamente zeri.

    1) Dobbiamo individuare l'elemento perno del primo passo. Si tratta dell'elemento con indici $11$ quindi $a_{11}$.

    2) Se il perno è == 0. L'algoritmo che stiamo descrivendo si ferma.

    3) Se il perno è != 0. L'algoritmo continua.

    4) Ad ogni passo calcoleremo un certo numero di moltiplicatori. Che utilizzeremo per fare le trasformazioni che ci servono per rendere 0 gli elementi evidenziati in verde.

#### PASSO 1

1. perno $\leftarrow a_{11}$
    
    Hp $\quad a_{11} \ne 0$

2. moltiplicatori

    $m_{21} = a_{21} / a{11} \\ m_{i1} = a_{i1} / a_{11} \\ m_{n1} = a_{n1} / a_{11}$

$$
A_2 = \begin{pmatrix}
1^a \text{ riga } \\
2^a \text{ riga } - m_{21} \cdot 1° \text{ riga } \\
i^a \text{ riga } - m_{i1} \cdot 1° \text{ riga } \\
n^a \text{ riga } - m_{n1} \cdot 1° \text{ riga } \\
\end{pmatrix}
= 
\begin{pmatrix}
a_{11} & a_{12} & a_{13} & \dots & a{1n} \\
\tclg{0} & a_{22}^{(2)} & a_{23}^{(2)} & \dots & a_{2n}^{(2)} \\
\tclg{0} & a_{32}^{(2)} & a_{33}^{(2)} & \dots & a_{3n}^{(2)} \\
\tclg{\vdots} & \vdots & \vdots &       & \vdots \\
\tclg{0} & a_{n2}^{(2)} & a_{n3}^{(2)} & \dots & a_{nn}^{(2)}
\end{pmatrix}
$$

Formule per la prima riga:

$$
a_{21}^{(2)} = a_{21} - m_{21} \cdot a_{21} - \frac{a_{21}}{a_{11}} \bar{a_{11}}= 0 \\
a_{2j}^{(2)} = a_{2j} - m_{21} \cdot a_{2j} \text{ per } j=2,\dots,n
$$

Formule per le righe successive:

#### PASSO 2

Rieseguire lo stesso algoritmo svolto sulla matrice A al primo passo sulla sottomatrice evidenziata in giallo.

$$
A_2 =
\begin{pmatrix}
a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
0 & \tcy{a_{22}^{(2)}} & \tcy{a_{23}^{(2)}} & \tcy{\dots} & \tcy{a_{2n}^{(2)}} \\
0 & \tcy{a_{32}^{(2)}} & \tcy{a_{33}^{(2)}} & \tcy{\dots} & \tcy{a_{3n}^{(2)}} \\
\vdots & \tcy{\vdots} & \tcy{\vdots} &      & \tcy{\vdots} \\
0 & \tcy{a_{n2}^{(2)}} & \tcy{a_{n3}^{(2)}} & \tcy{\dots} & \tcy{a_{nn}^{(2)}}
\end{pmatrix}
$$

Lavoriamo su:

$$
A_2 =
\begin{pmatrix}
a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
0 & \tcr{a_{22}^{(2)}} & {a_{23}^{(2)}} & {\dots} & {a_{2n}^{(2)}} \\
0 & \tclg{a_{32}^{(2)}} & {a_{33}^{(2)}} & {\dots} & {a_{3n}^{(2)}} \\
\vdots & \tclg{\vdots} & {\vdots} &      & {\vdots} \\
0 & \tclg{a_{n2}^{(2)}} & {a_{n3}^{(2)}} & {\dots} & {a_{nn}^{(2)}}
\end{pmatrix}
$$

1. perno $\leftarrow a_{22}^{(2)}$
    
    Hp $\quad a_{22}^{(2)} \ne 0 \quad$ Ci fermiamo se il perno è nullo ($= 0$)

2. moltiplicatori.

    Vogliamo ottenere una nuova matrice $A_3$ e che abbia degli zeri in corrispondenza 

    $m_{32} = a_{32} / a_{22} \\ 
    m_{i2} = a_{i2} / a_{22} \\ 
    m_{n2} = a_{n2} / a_{22}$

$$
A_2 = \begin{pmatrix}
1^a \text{ riga di } A_2 \\
2^a \text{ seconda di } A_2 \\
3^a \text{ riga di } A_2 - m_{31} \cdot 2° \text{ riga di } A_2 \\
\vdots \\
n^a \text{ riga di } A_2 - m_{n2} \cdot 2° \text{ riga di } A_2 \\
\end{pmatrix}
= 
\begin{pmatrix}
a_{11} & a_{12} & a_{13} & \dots & a{1n} \\
0 & a_{22}^{(2)} & a_{23}^{(2)} & \dots & a_{2n}^{(2)} \\
0 & \tclg{0} & a_{33}^{(3)} & \dots & a_{3n}^{(3)} \\
\vdots & \tclg{\vdots} & \vdots &       & \vdots \\
0 & \tclg{0} & a_{n3}^{(3)} & \dots & a_{nn}^{(3)}
\end{pmatrix}
$$

Formula di aggiornamento: $a_{ij}^{(3)} = a_{ij}^{(2)} - m_{i2}a_{2j}^{(2)}$ per $i,j = \dots$.

---

Esempio:
Data la matrice $A\in\R^{n\times n}$

**PASSO 1**:

1. Scelgo come elemento perno (o pivot): $a_{11}$.
2. Ipotesi: $a_{11}\ne 0$.
3. Calcolo i moltiplicatori:
    $$ m_{i1} = \frac{a_{i1}}{a_{11}},\quad i=2,\dots,n $$

    La formula per il calcolo dei moltiplicatori deriva da:

    $$ a_{i1} = m\cdot a_{ii} $$

    Vogliamo sapere qual'è il valore di m per cui $a_{ii}$ è uguagliato ad $a_{i1}$ che vogliamo azzerare. Notare come si trovano sulla stessa colonna perchè poi sottrarremo la riga del perno a quella indicizzata da $i$, annullando il valore nella posizione $i1$. Questo viene fatto per ogni riga:
4. Combinazioni lineare: riga $i$ con la riga 1 e coefficiente $-m_{i1},\quad i=2,\dots,n$.

$$
A\equiv A_1 = \begin{pmatrix}
a_{11} & a_{12} & a_{13} & \cdots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \cdots & a_{2n} \\
a_{31} & a_{32} & a_{33} & \cdots & a_{3n} \\
\vdots & \vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & a_{n3} & \cdots & a_{nn} \\
\end{pmatrix}\Rightarrow A_2 = \begin{pmatrix}
\tcr{a_{11}} & a_{12} & a_{13} & \cdots & a_{1n} \\
\tclb{0}      & \tclb{a_{22}^{(2)}} & \tclb{a_{23}^{(2)}} & \tclb{\cdots} & \tclb{a_{2n}^{(2)}} \\
\tclb{0}      & \tclb{a_{32}^{(2)}} & \tclb{a_{33}^{(2)}} & \tclb{\cdots} & \tclb{a_{3n}^{(2)}} \\
\tclb{\vdots} & \tclb{\vdots}       & \tclb{\vdots}       &               & \tclb{\vdots} \\
\tclb{0}      & \tclb{a_{n2}^{(2)}} & \tclb{a_{n3}^{(2)}} & \tclb{\cdots} & \tclb{a_{nn}^{(2)}} \\
\end{pmatrix}
$$

Formula per il calcolo di $a_{ij}^{(2)}$:

$$ \tclb{a_{ij}^{(2)}} = a_{ij} - m_{i1}a_{1j}\quad i,j=2,\dots,n $$

A questo punto:

$$
A_2 = \begin{pmatrix}
1       &   &        &        & \\
-m_{21} & 1 &        &        & \\
-m_{31} & 0 & 1      &        & \\
\vdots  &   &        & \ddots & \\
-m_{n1} & 0 & \cdots & 0      & 1 \\
\end{pmatrix}\begin{pmatrix}
a_{11} & a_{12} & a_{13} & \cdots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \cdots & a_{2n} \\
a_{31} & a_{32} & a_{33} & \cdots & a_{3n} \\
\vdots & \vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & a_{n3} & \cdots & a_{nn} \\
\end{pmatrix} = LA_1
$$

**PASSO 2**:

1. Scelgo come elemento perno (o pivot): $a_{22}^{(2)}$.
2. Ipotesi: $a_{22}^{(2)}\ne 0$.
3. Calcolo i moltiplicatori:
    $$ m_{i2} = \frac{a_{i2}^{(2)}}{a_{22}^{(2)}},\quad i=3,\dots,n $$
4. Combinazioni lineare: riga $i$ con la riga 2 e coefficiente $-m_{i2},\quad i=3,\dots,n$.

$$
A_2 = \begin{pmatrix}
a_{11} & a_{12} & a_{13} & \cdots & a_{1n} \\
\tclb{0}      & \tclb{a_{22}^{(2)}} & \tclb{a_{23}^{(2)}} & \tclb{\cdots} & \tclb{a_{2n}^{(2)}} \\
\tclb{0}      & \tclb{a_{32}^{(2)}} & \tclb{a_{33}^{(2)}} & \tclb{\cdots} & \tclb{a_{3n}^{(2)}} \\
\tclb{\vdots} & \tclb{\vdots}       & \tclb{\vdots}       &               & \tclb{\vdots} \\
\tclb{0}      & \tclb{a_{n2}^{(2)}} & \tclb{a_{n3}^{(2)}} & \tclb{\cdots} & \tclb{a_{nn}^{(2)}} \\
\end{pmatrix}\Rightarrow A_3 = \begin{pmatrix}
a_{11} & a_{12} & a_{13} & \cdots & a_{1n} \\
\tclb{0}      & \tcr{a_{22}^{(2)}}  & \tclb{a_{23}^{(2)}} & \tclb{\cdots} & \tclb{a_{2n}^{(2)}} \\
\tclb{0}      & \tclb{0}      & \tclg{a_{33}^{(3)}} & \tclg{\cdots} & \tclg{a_{3n}^{(3)}} \\
\tclb{\vdots} & \tclb{\vdots} & \tclg{\vdots}       &               & \tclg{\vdots} \\
\tclb{0}      & \tclb{0}      & \tclg{a_{n3}^{(3)}} & \tclg{\cdots} & \tclg{a_{nn}^{(3)}} \\
\end{pmatrix}
$$

Formula per il calcolo di $a_{ij}^{(2)}$:

$$ \tclg{a_{ij}^{(3)}} = \tclb{a_{ij}} - m_{i2}\tclb{a_{2j}}\quad i,j=3,\dots,n $$

A questo punto:

$$
A\equiv A_1 = \begin{pmatrix}
1      &         &   &        & \\
0      & 1       &   &        & \\
0      & -m_{32} & 1 &        & \\
\vdots &         &   & \ddots & \\
0      & -m_{n2} & 0 & \cdots & 1 \\
\end{pmatrix}\begin{pmatrix}
a_{11} & a_{12} & a_{13} & \cdots & a_{1n} \\
\tclb{0}      & \tclb{a_{22}^{(2)}} & \tclb{a_{23}^{(2)}} & \tclb{\cdots} & \tclb{a_{2n}^{(2)}} \\
\tclb{0}      & \tclb{a_{32}^{(2)}} & \tclb{a_{33}^{(2)}} & \tclb{\cdots} & \tclb{a_{3n}^{(2)}} \\
\tclb{\vdots} & \tclb{\vdots}       & \tclb{\vdots}       &               & \tclb{\vdots} \\
\tclb{0}      & \tclb{a_{n2}^{(2)}} & \tclb{a_{n3}^{(2)}} & \tclb{\cdots} & \tclb{a_{nn}^{(2)}} \\
\end{pmatrix} = L_2A_2
$$

---


#### In generale

Ad un generico passo $k$. Abbiamo in ingresso la matrice $A_k$ (dai passi precedenti) e dobbiamo produrre la matrice $A_{k+1}$. Prendo gli elementi che stavano nella vecchia matrice, meno i moltiplicatori di quella riga li moltiplicati per gli elementi che stavano sulla stessa riga e colonna del moltiplicatore.

Iteriamo l'algoritmo $n-1$ volte. Alla fine ritrovaremo la matrice trasformata nella forma triangolare superiore.

#### Studio dell'algoritmo

Le formule di aggiornamento sono l'algoritmo di Gauss. Prendere queste formule ed implementarle per i vari indici.

Tre cicli annidati:
- **Cilo esterno**: ciclo del passo.
    - **Secondo ciclo**: Combinazioni lineari (da j+1 --> n (colonna)) perchè lavoriamo sotto. Calcoliamo il moltiplicatore ad ogni passaggio.
        - **Terzo ciclo**: Aggiorniamo gli elementi da k+1 a --> (riga).

Questo metodo va a sovrascrivere gli elementi della matrice precedente ad ogni passo. Efficiente in modo da non dover memorizzare $n-1$ matrici.

Ad ogni passo abbiamo un moltiplicatore in meno da calcolare naturalmente. Li dobbiamo memorizzare perchè ci forniranno l'informazione necessaria per calcolare la sottomatrice inferiore $L$.

Ricavata al primo punto la matrice triangolare $U$, possiamo memorizzare i moltiplicatori al posto degli zeri nella parte inferiore della matrice.

**Implementazione in Laboratorio**.

$$ A = 
\begin{pmatrix}
\tcr{a_{11}} & a_{12} & a_{13} \\
a_{21} & \tcy{a_{22}} & \tcy{a_{23}} \\
a_{31} & \tcy{a_{32}} & \tcy{a_{33}} \\
\end{pmatrix}
$$

$$ A = 
\begin{pmatrix}
a_{12} & a_{13} \\
a_{22} & a_{23} \\
\end{pmatrix}
-
\begin{pmatrix}
m_{21}a_{12} & m_{21}a_{13} \\
m_{31}a_{12} & m_{31}a_{13} \\
\end{pmatrix}
= \\
\begin{pmatrix}
a_{12} & a_{13} \\
a_{22} & a_{23} \\
\end{pmatrix}
-
\begin{pmatrix}
m_{21} \\ m_{31}
\end{pmatrix}
\cdot
\begin{pmatrix}
a_{12} & a_{13}
\end{pmatrix}
=
\begin{pmatrix}
a_{22}^{(2)} & a_{23}^{(2)} \\
a_{32}^{(2)} & a_{33}^{(2)} \\
\end{pmatrix}
$$

Quindi possiamo sostituire il secondo ciclo con un'operazione che prevede la moltiplicazione della matrice. 

---

# (10) Lezione 16-03-2026 | s 153..178 | Metodo di Gauss - continuo

### Eliminazione Gaussiana $-$ Aggiunta sul costo computazionale 

I costi computazionali di ogni passo dell'algoritmo si calcolano con facilità considerando che:

- Il numero di moltiplicatori e quindi di quozienti è pari al numero di elementi nella matrice diagonale inferiore della matrice originale, quindi:

    $$ \mathcal{O}\Big(\frac{n^2}{2}\Big) = \mathcal{O}\Big(\frac{n(n-1)}{2}\Big) $$

- Per le somme ed i prodotti il metodo di calcolo è l ostesso ma consideriamo il numero totale di iterazioni e quindi di sottomatrici:

    $$ \mathcal{O}\Big(\frac{n^3}{3}\Big) =\mathcal{O}\Big(\frac{n(n-1)(2n-1)}{6}\Big) $$

### Fattorizzazione

E' dimostrabile che, rendendo ad 1 la diagonale principale delle due matrici $U$ ed $L$, e moltiplicate tra loro riotteniamo la matrice orignale $A$

$$ A = L\cdot U. $$

#### Trasformazione elementare di Gauss

L'altra volta abbiamo detto che per passare dalla matrice iniziale $A_1$ vogliamo trovarne un'altra che è quella chiamata $A_2$. Per trovare questa seconda matrice troviamo i moltiplicatori adatti ad annullare le righe sottostanti e eseguire le combinazioni lineari delle righe successive con la prima (formula vista). 

Alternativamente possiamo **riesprimere questo algoritmo come un prodotto matriciale** tra una matrice che ha come diagonale principale degli 1, come colonna interessata i moltiplicatori calcolati e la matrice precedente $A_1$.

Quindi:

$$
A_2 = \begin{pmatrix}
1       &   &        &        & \\
-m_{21} & 1 &        &        & \\
-m_{31} & 0 & 1      &        & \\
\vdots  &   &        & \ddots & \\
-m_{n1} & 0 & \cdots & 0      & 1 \\
\end{pmatrix}\begin{pmatrix}
a_{11} & a_{12} & a_{13} & \cdots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \cdots & a_{2n} \\
a_{31} & a_{32} & a_{33} & \cdots & a_{3n} \\
\vdots & \vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & a_{n3} & \cdots & a_{nn} \\
\end{pmatrix} = LA_1
$$

Questo risultato non ci dice niente di nuovo. L'implementazione non cambia rispetto a quella vista in precedenza (l'algoritmo rimane invariato). Ma è interessante come risultato perchè possiamo vedere l'algoritmo come un prodotto matriciale.

**Esempio**:

Calcolati

$$
m_{21} = \frac{a_{21}}{a_{11}},\quad m_{31} = \frac{a_{31}}{a_{11}}
$$

Abbiamo:

$$
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33} \\
\end{pmatrix}\Rightarrow\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
0 & a_{22} - m_{21}a_{12} & a_{23} - m_{21}a_{13} \\
0 & a_{32} - m_{31}a_{12} & a_{33} - m_{31}a_{13} \\
\end{pmatrix}
$$

In modo alternativo ed equivalente:

$$
\begin{pmatrix}
1 & & \\
\tcy{-m_{21}} & \tcy{1} & \\
-m_{31} & 0 & 1 \\
\end{pmatrix}\begin{pmatrix}
\tcy{a_{11}} & a_{12} & a_{13} \\
\tcy{a_{21}} & a_{22} & a_{23} \\
\tcy{a_{31}} & a_{32} & a_{33} \\
\end{pmatrix} = \begin{pmatrix}
a_{11}               & a_{12} & a_{13} \\
\tclg{-m_{21}a_{11}+a_{21}} & \tclb{-m_{21}a_{12}+a_{22}} & \tcr{-m_{21}a_{13}+a_{23}} \\
& & & \\
\end{pmatrix}
$$

Sulle slides troviamo il passo generico di questo algoritmo. **Il risultato è quindi un susseguirsi di $\mathbf{n-1}$ prodotti matriciali**.

Le **Trasformazioni Elementari di Gauss** sono le matrici intermedie dell'algoritmo di Fattorizzazione. Otteniamo che:

$$ U = L_{n-1}L_{n-1}\cdots L_2L_1A $$

---

#### Vedere la matrice $L$ come prodotto

Vogliamo vedere la matrice $L$ come **prodotto dell'inversa delle Trasformazioni Elementari di Gauss**. Qiesto moltiplichiamo per le inverse delle trasformazioni elementari entrambi i lati dell'uguaglianza $A=LU$:

$$
L_{n-1}^{-1}\Big( L_{n-1}L_{n-2}\cdots L_2L_1 \Big)A = L_{n-1}^{-1}U \\
L_{n-2}^{-1}\Big( L_{n-2}\cdots L_2L_1 \Big)A = L_{n-1}^{-1}L_{n-1}^{-2}U \\
$$

Ripetendo i passaggi otteniamo:

$$
A = \underbrace{L_1^{-1}L_2^{-1}\cdots L_{n-2}^{-1}L_{n-1}^{-1}}_{L} U
$$

---

#### Modo alternativo di vedere le $L_k$

La matrice di Trasformazione $k$-esima la si può vedere come una generalizzazione dei seguenti passaggi (slide 154), esempio:

$$
\begin{aligned}
    L_1 =
    \begin{pmatrix}
    1 & & \\
    -m_{21} & 1 & \\
    -m_{31} & 0 & 1 \\
    \end{pmatrix}
    &=
    \begin{pmatrix}
    1 & & \\
    & 1 & \\
    &   & 1 \\
    \end{pmatrix}
    -
    \begin{pmatrix} 0 \\ m_{21} \\ m_{31} \end{pmatrix}
    \begin{pmatrix} 1 & 0 & 0 \end{pmatrix}
    \\
    &= 
    \begin{pmatrix}
    1 & & \\
    & 1 & \\
    &   & 1 \\
    \end{pmatrix} - \begin{pmatrix}
    0 & 0 & 0 \\
    m_{21} & 0 & 0 \\
    m_{31} & 0 & 0 \\
    \end{pmatrix}
\end{aligned}
$$

Si possono scrivere l'Identità meno il Prodotto Diadico (prodotto diade tra due vettori). Segnarsi il caso generico presente sulle slides.

### Risultato dei passaggi

Notiamo che l'inversa di ciascuna delle **Trasformazioni Elementari di Gauss** è uguale alla stessa matrice ma con i moltiplicatori invertiti di segno. Questo è dimostrato sulle slides (slide 153-157).

$$ L_1^{-1} =
\begin{pmatrix}
1 & & \\
-m_{21} & 1 & \\
-m_{31} & 0 & 1 \\
\end{pmatrix}^{-1}
=
\begin{pmatrix}
1 & & \\
m_{21} & 1 & \\
m_{31} & 0 & 1 \\
\end{pmatrix}
$$

Dimostrazione sulle slides.

---

### Fallimento dell'algoritmo $-$ Condizione sui **Minori Principali**

L'ipotesi del problema è che gli elementi perno $a_{ii}$ siano $\ne 0$.
La matrice su cui applichiamo l'algoritmo abbia tutti i **minori principali** $\ne 0$.

Un minore principale è il determinante della sotto matrice... Esempio:


$$
A =
\begin{pmatrix}
\tcr{a_{11}} & \tclg{a_{12}} & \tclb{a_{13}} \\
\tclg{a_{21}} & \tclg{a_{22}} & \tclb{a_{23}} \\
\tclb{a_{31}} & \tclb{a_{32}} & \tclb{a_{33}} \\
\end{pmatrix}
$$

I determinanti di queste sotto matrici in teori adovrebbero essere calcolati e controllati che siano $\ne 0$. Ma il calcolo di tutti questi determinanti è **molto costoso computazionalmente**. Questa è solamente un'**ipotesi teorica**.

### Modificare Gauss

Come possiamo modificare l'algoritmo di Gauss in modo da renderlo più generico? Da consentire la sua applicazione anche su matrici a cui non sarebbe possibile applicarlo.

#### Scambio delle equazioni

Scambiare le righe della matrice dei coefficienti e di conseguenza quele dei termini noti in modo da ottenere un sistema equivalente ma con valori di perno non nulli.

Questo equivale a scambiare l'ordine delle equazioni.

L'idea è di scambiare solo le righe delle matrici che sono compatibili, in modo da ottenere il perno che mi piace di più ad un passo generico $k$. Vedi slide 165.

Dal punto di vista implementativo è una banalità. Basta prendere l'algoritmo e aggiungere una logica di scambio. Anche i moltiplicatori devono essere scambiati, ma questo viene fatto in automatico dato che sono salvati nella matrice triangolare inferiore.

Dal punto di vista matriciale, anche qua tutto può essere visto come un susseguirsi di prodotto matriciale. Vogliamo tenere affiancati i procedimenti di triangolazione con un susseguirsi di prodotti matriciali. Anche gli scambi tra due righe si possono vedere come prodotti matriciali.

Anche qua solo dal punto di vista formale ci è utile questa informazione. Dal punto di vista algoritmico affettuiamo semplicemente lo scambio.

Dobbiamo introdurre le **Matrici di Permutazione Elementari**. Slide 166. Segnati le cose spiegate a questa slide.

**Procedimento**

Prima di ogni passo di eliminazione gaussiana controlliamo se il perno ci piace. Se non ci piace ne cerchiamo un'altro che ci piaccia di più ($\ne 0$) e se lo troviamo effettuiamo lo scambio di riga.

Avremo quindi Matrici di Permutazioni Elementari (teoricamente) per ogni passo dell'algoritmo ($P_k$).

Teniamo conto che almeno uno elemento diverso da zero ci deve essere, altrimenti la matrice sarebbe singolare. Si può dimostrare ma non l'abbiamo dimostrato, solo citato.

Otteniamo quindi:

$$ A_2 = L_1P_1A_1 $$

Abbiamo aggiunto una permutazione. Questo lo facciamo in tutti i passi successivi:

$$ \begin{aligned} A_k &= L_kP_kA_k \\ &= A_{n-1}\cdot ...\cdot L_2P_2L_1P_1A \end{aligned}$$

### Criterio di scelta del perno $-$ Strategia di Pivoting-Parziale

Scegliere un certo perno aumenta la stabilità dell'algoritmo.

Resoconto slide 175.

Scegliersi un pivo troppo piccolo, potrebbe portare a instabilità nella fase successiva dell'algoritmo.

Conviene quindi non solo controllare che il pivo sia $\ne 0$, ma prendere anche il più grande possibile. Si vede bene a slide 177. Regola: Trovate qualcosa di piccolo e scambiatelo con qualcosa di grande. Per la stabilità. In aritmentica esatta questo discorso non ha senso, ha senso solo che il pivo sia $\ne 0$. Implementato anche da Numpy.

---

# (11) Lezione 17-03-2026 | s 179..182 | Metodo di Gauss - continuo

### Costo e implementazione Pivoting Parziale

Scelta del pivot ad ogni passo dell'algoritmo. Richede di individuare il massimo tra i $n-k+1,\quad per k=1,\dots,n-1$ elementi candidati. Per individuare il massimo effetuiamo la differenza e vedere se il risultato è positivo o negativo. Ciclo che tiene traccia del massimo valore corrente; eventualmente lo aggiorna.

Costo computazionale: $\mathcal{O}(\frac{n^2}{2})$. Comunque di una dimensione in meno rispetto al costo di $\mathcal{O}(\frac{n^3}{3})$ della fattorizzazione.

Implementazione e appunti in laboratorio.

---

# (12) Lezione 18-03-2026 | s 182..200 | Varianti della fattorizzazione di Gauss per matrici speciali

### Librerie usate da NumPy

Tutti i metodi di linalg.solve sono basati su una libreria "_gesv". Routine storiche implementate originariamente in fortran. La documentazione riguarda (LAPAK) proprio alle matrici generali (fattorizzazione LU).

Esiste una sezione per la risoluzione di matrici a banda. In generale ci sono librerie suddivise a seconda della tipologia specifica di problema che devono risolvere.

Altre funzioni specifiche per matrici ricorrenti (con proprietà speciali):
- Matrici simmetriche
- Matrici simmetriche $-$ definite positive
- Data filling di un vettore/di una matrice

### Matrici Sparse (data filling/inpainting)

La matrice inpainting ha la diagonale principale, la prima superiore, la prima inferiore, e altre 2 diagonali che non sono adiacenti alle altre, in mezzo ci sono diagonali nulle. Quindi non può essere considerata a banda.

Una matrice quadrata di ordine $n$ si considera *sparsa* se il numero di elementi diversi da zero è una priccola percentuale rispetto ad $n^2$.

Si adottano dei formati di rappresentazione compressi. Compressi per righe o per colonne:
- CCS: Compressed Column Storage;
- CRS: Compressed Row Storage.

Vettore destinato a contenere tutti gli elementi diversi da zero della matrice.
Gli altri due vettori contengono rispettivamente l'indice di riga e di colonna di ogni elemento del primo vettore. Efficiente se il numero elementi non nulli è molto basso rispetto alla dimensione della matrice.

L'informazione può essere compressa ulteriormente raggruppando gli elementi che fanno barte della stessa colonna (o riga per CRS); memorizzando solamente il numero di elementi di ciascun gruppo (dato che gli elementi sono ordinati).

Nel caso dell'inpainting che abbiamo visto in laboratorio la prof traduce la matrice a banda in una matrice sparsa per motivi di efficienza. Dato che la gran parte della matrice a banda era sconosciuta (elementi nulli).

HSL Software Index - Sezione "FORTRAN/LINEAR ALGEBRA": Contiene una libreria di metodi per la risoluzione di matrici sparse.

Algoritmi per far si che non solo il pivot sia scelto con cura, ma in modo che le matrici dei coefficienti ecc... abbiano il maggior numero di zeri.

### Matrici speciali $-$ Specializzazione algoritmi di solving

E' possibile specializzare un algoritmo risolutivo per matrici che si sa avere una certa forma/certe proprietà? SI!

### Matrici speciali $-$ Proprietà di Simmetria

Dal punto di vista della memoria, se le righe e le colonne sono uguali, non c'è bisogno di memorizzarle entrambe. Anche qui il risparmio non è banale, si risparmia la metà. Anche la complessità computazionale si può ridurre alla metà.

Si può dimostrare che nel caso in cui una matrice sia simmetrica/non singolare, e con tutti i minori principali $\ne 0$. La fattorizzazione può diventare:

$$ A = LDL^T $$

Il risparmio è: invece di avere $L$ e $U$, due matrici triangolari i quali elementi sono indipendenti e slegati. Qui abbiamo $L$ e $L^T$, ed una matrice diagonale $D$. 

- **Matrice non simmetrica**: La forma $LU$ ha un costo di $\mathcal{O}(\frac{n^3}{3})$.
- **Matrice simmetrica**: La forma $LDL^T$ richiede di calcolare solamente la matrice $L$. La complessità si dimezza: $\mathcal{O}(\frac{1}{2}\cdot\frac{n^3}{3})$.

Procedimento algoritmico (*slide 196*):

$$ Ax = b \quad\Leftrightarrow\quad L\underbrace{DL^Tx}_{=z} = b $$

$$
\begin{cases}
Lz = b \\
z = D\underbrace{L^Tx}_{=y} \\
\end{cases} \quad\Rightarrow\quad
\begin{cases}\begin{align}
Lz = b &\to \text{Triangolo inferiore} \\
Dy = z &\to t_1 = \frac{z_i}{d_{ii}}\quad i=1,\dots,n\quad \\
L^T = y &\to \text{Triangolo superiore} \\
\end{align}\end{cases}
$$

### Matrici speciali $-$ Proprietà di Simmetria + Strettamente positiva

Se una matrice è simmetrica tutti i suoi autovalori sono reali, in più se questi autovalori sono tutti positivi allora la matrice è definita positiva.

- **Simmetria**: La complessità si riduce della metà: $\mathcal{O}(\frac{n^3}{6})$.
- **Positività**: Algoritmo + stabile di tutti (algoritmo di Cholesky).

Se $A$ è simmetrica e definita positiva, allora esiste una matrice $\mathcal{L}$ triangolare inferiore tale che:

$$ A = \mathcal{LL}^T $$

Sul collab di laboratorio della prof c'è una descrizione dell'algoritmo di Cholesky e della sua derivazione.

#### Algoritmo di Pavimentazione

$$ A = \mathcal{LL}^T \Rightarrow
\begin{pmatrix}
a_{11} & a_{21} & a_{31} \\
a_{21} & a_{22} & a_{32} \\
a_{31} & a_{32} & a_{33} \\
\end{pmatrix}
=
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
=
\begin{pmatrix}
l_{11}^2     & \dots & \dots \\
l_{21}l_{11} & \dots & \dots \\
l_{31}l_{11} & \dots & \dots \\
\end{pmatrix}
$$

- $$ a_{11} = l_{11}^2 \to l_{11} = \sqrt{a_{11}} $$
- $$ a_{21} = l_{21}l_{11} \to l_{21} = \frac{a_{21}}{l{11}} $$
- $$ a_{31} = l_{31}l_{11} \to l_{31} = \frac{a_{31}}{l{11}} $$
- $$ \dots $$

Più stabile e meno costoso computazionalmente.

### Fattorizzazione QR

Matrici ortogonali

Una matrice $Q\in\R^{n\times n}$ si dice **Ortogonale** se:

$$ Q^TQ = QQ^T = I $$

Se una matrice è ortogonale, come diretta conseguenza della definizione, è anche una matrice **non singolare** e $Q^{-1}=Q^T$.

Quindi se dovessimo risolvere un sistema:

$$
\begin{align}
Qy &= b \\
\underbrace{Q^TQ}_{I}y &= Q^Tb \\
y &= Q^Tb \\
\end{align}
$$

La fattorizzazione ha lo scopo di prendere una matrice non singolare e ricavare due matrici, una ortogonale $Q\in\R^{n\times n}$ e una matrice triangolare superiore nonsingolare $R\in\R^{n\times n}$ tali che

$$ A=QR $$

Esistono diversi algoritmi per calcolare le matrici $Q$ ed $R$. L'algoritmo che vedremo noi è il più efficiente e si chiama **algoritmo di Householder**.

### Algoritmo di Householder $-$ Calcolo di $Q$ e $R$

#### Differenza con il metodo di Gauss

- Nella **fattorizzazione di Gauss**:

    $$L_{n-1}\cdots L_2L_1A=U $$
    
    Ad ogni passo azzeriamo tutti gli elementi sotto il perno.
    Lo facciamo per tutti i passi fino ad arrivare ad una matrice triangolare superiore. Per fare questo utilizziamo matrici triangolari inferiori di Gauss.
    - Matrici L: triangolari inferiori
    - Matrice U: triangolare superiore

- Nella **trasformazione di Householder**:

    $$U_{n-1}\cdots U_2U_1A=R $$

    Si parte dalla matrice $A$. Si moltiplica la matrice di partenza per una serie di matrici $U_k$ chiamate **Trasformazioni Elementari di Householder**. Queste matrici sono ortogonali (T rovesciata).
    - Matrici U: ortogonali
    - Matrice R: triangolare superiore

    Assomiglia a quella del metodo di Gauss.

#### Dal punto di vista geometrico

$$
A = 
\begin{pmatrix}
a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \dots & a_{2n} \\
\vdots \\
a_{n1} & a_{n2} & a_{n3} & \dots & a_{nn} \\
\end{pmatrix}
$$

Con $U_1$ ortogonale, e

$$ U_1A =
\begin{pmatrix}
a_{11}^{(2)} & a_{12}^{(2)} & a_{13}^{(2)} & \dots & a_{1n}^{(2)} \\
0 & a_{22}^{(2)} & a_{23}^{(2)} & \dots & a_{2n}^{(2)} \\
\vdots \\
0 & a_{n2}^{(2)} & a_{n3}^{(2)} & \dots & a_{nn}^{(2)} \\
\end{pmatrix}
$$

Riduciamo il ragionamento sulla prima colonna.

$$
\begin{pmatrix}
a_{11} \\ a_{21} \\ \vdots \\ a_{n1}
\end{pmatrix} \qquad
U_1a_1 = \begin{pmatrix}
a_{11}^{(2)} \\ 0 \\ \vdots \\ 0
\end{pmatrix}
$$

Vogliamo effettuare una sorta di rotazione del vettore. Riducendo la dimensione dell'ambiente ad un piano. e abbiamo un vettore di due componenti $t_1,t_2$.

Vogliamo ottenere un altro vettore che abbia il primo componente diverso da zero, ed il successivo a zero (Pivot ed elementi nulli al di sotto). Questo esprime l'idea della rotazione.

Vogliamo ottenere un vettore che abbia la seconda componente del vettore rutotandolo in modo da annullare il primo componente.

$$
\begin{pmatrix}
t_1 \\ t_2
\end{pmatrix} \Rightarrow
\begin{pmatrix}
\|t_1\| \\ 0
\end{pmatrix}
$$

Rutoato in senso orario.

La rotazione del vettore ci permette di annullare tutte le componenti di un vettore tranne una. Questa stessa operazione la possiamo effettuare su molteplici dimensioni.

#### Algoritmo di Triangolarizzazione

Dato $\underbrace{a_1}_{1° colonna di A}\to U_1$ tale che:
1. $U_1$ è ortogonale
2. $U_2a_1 = \begin{pmatrix} -\|a\| \\ 0 \\ \vdots \\ 0\end{pmatrix}$

Passi:
1. $\sigma_1 = \|a_1\| \ne 0$
2. $V_1 = a_1 + \sigma_1e_1     \qquad e_1=\text{ primo vettore base canonica}$
3. $\alpha_1=\frac{1}{2}\|v_1\|_{\text{euclidea}}^2$
4. $U_1 = I - \frac{1}{\alpha_1}\underbrace{v_1v_1^T}_{\text{matrice }n\times n}$

Effettuata la rotazione del vettore.

---

# (13) Lezione 24-03-2026 | s 201.. | Varianti della fattorizzazione di Gauss per matrici speciali

### Fattorizzazione QR

Vogliamo fattorizzare la matrice $A$ nel prodotto di matrici $QR$.

- La matrice $Q$ (**Ortogonale**).
- La matrice $R$ (**Triangolare superiore**), ha gli elementi diagonali diversi da zero. A seconda di come impostiamo l'algoritmo di fattorizzazione potremo decidere il segno di questi elementi.

Abbiamo citato diversi algoritmi in grado di decomporre A nelle matrici ortogonale e triangolare superiore. Ma quello che abbiamo scelto è Housholder.

Il punto comune della fattorizzazione di Gauss e di Householder è che otteniamo una matrice triangolare superiore. La differenza tra i due metodi l'ho già spiegata.

Partendo da una matrice di forma qualsiasi dobbiamo operare sui suoi elementi per arrivare alla forma $QR$.

---

#### Procedimento fattorizzazione QR

Procediamo con una serie di trasformazioni matriciali allo scopo di ottenere alla fine dele trasformazione una matrice triangolare superiore $R$ e una matrice ortogonale $Q$. Come in Gauss vogliamo annullare tutti gli elementi sotto la diagonale principale di $A$, ma in modo diverso da Gauss.

**Passo 1**

$$ U_1A_1 =
\begin{pmatrix}
a_{11}^{(2)} & a_{12}^{(2)} & a_{13}^{(2)} & \dots & a_{1n}^{(2)} \\
0 & a_{22}^{(2)} & a_{23}^{(2)} & \dots & a_{2n}^{(2)} \\
0 & a_{32}^{(2)} & a_{33}^{(2)} & \dots & a_{3n}^{(2)} \\
\vdots & \vdots & \vdots & & \vdots \\
0 & a_{n2}^{(2)} & a_{n3}^{(2)} & \dots & a_{nn}^{(2)} \\
\end{pmatrix} = A_2
$$

dove:

1. $\sigma_1 = \|a_1\| \ne 0$
2. $V_1 = a_1 + \sigma_1e_1$
3. $\alpha_1=\frac{1}{2}\|v_1\|_{\text{euclidea}}^2$
4. $U_1 = I - \frac{1}{\alpha_1}v_1v_1^T$

**Passo 2**

$$ U_2A_2 =
\begin{pmatrix}
a_{11}^{(2)} & a_{12}^{(2)} & a_{13}^{(2)} & \dots & a_{1n}^{(2)} \\
0 & a_{22}^{(3)} & a_{23}^{(3)} & \dots & a_{2n}^{(3)} \\
0 & 0 & a_{33}^{(3)} & \dots & a_{3n}^{(3)} \\
\vdots & \vdots & \vdots & & \vdots \\
\underbrace{0}_{U_1a_1} & \underbrace{0}_{U_2a_2} & \underbrace{a_{n3}^{(3)}}_{\dots} & \dots & a_{nn}^{(3)} \\
\end{pmatrix} = A_3
$$

dove:

$$ a_2 = 
\begin{pmatrix}
a_{22}^{(2)} \\ a_{32}^{(2)} \\ \vdots \\ a_{n2}^{(2)} \\
\end{pmatrix} \in \R^{n-1}
$$

1. $\sigma_2 = \|a_2^{(2)}\| \ne 0$
2. $v_2 = a_2^{(2)} + \sigma_2e_2$
3. $\alpha_2=\frac{1}{2}\|v_2\|_{\text{euclidea}}^2$
4. $\tilde U_2 = I_{n-1} - \frac{1}{\alpha_2}v_2v_2^T$

**Passo 3**

$$
A_3 = U_2A_2 = \dots
$$

Matrici sempre più piccole. Le matrici di householder agiscono solo su sotto colonne, e non su tutte.

**Passo n-1 esimo**

$$
U_{n-1}\cdot U_1A = R
$$

Utilizzando delle matrici ortogonali $U_i$ otteniamo alla fine una matrice ortogonale $U$ con le proprietà che ne seguono. Mentre la matrice $R$ è naturalmente triangolare superiore.

#### Procedimenti algoritmico

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

**Algoritmo di ogni passo ed implementazione in laboratorio**.

---

#### Teoria e dimostrazione dei passaggi visti

La matrice ortogonale $U$ ha forma:

$$ U = I - \frac{1}{\alpha}vv^T = \frac{1}{2}\|v\|^2 \quad\to\quad \|v\|^2 = 2\alpha$$

1. **Simmetria** $\quad U = U^T$

    $$\begin{align}
    U^T &= (I - \frac{1}{\alpha}vv^T)T \\
    &= I^T - \frac{1}{\alpha}(vv^T)^T \\
    &= I - \frac{1}{\alpha}(v^T)^T(v)^T \\
    &= I - \frac{1}{\alpha}vv^T = U
    \end{align}$$

    Abbiamo riottenuto la matrice U.

2. **Ortogonalità** $\quad U^TU = I$

    $$
    \begin{align}
    &= \Big(I-\frac{1}{\alpha}vv^T\Big)^T \Big(I-\frac{1}{\alpha}vv^T\Big) \\
    &= I - \frac{1}{\alpha}vv^T - \frac{1}{\alpha}vv^T + \frac{1}{\alpha^2}vv^Tvv^T \\
    &= I - \frac{2}{\alpha}vv^T + \frac{1}{\alpha^2}v\underbrace{(v^Tv)}_{\text{scalare }\|v\|^2}v^T \\
    &= I - \frac{2}{\alpha}vv^T + \frac{1}{\alpha^2}\cdot\|v\|^2vv^T \\
    &= I - \underline{\frac{2}{\alpha}vv^T} + \underline{\frac{2\alpha}{\alpha^2}vv^T} \\
    &= I
    \end{align}$$

**Passi**

1. $ \alpha\in\R^n $
2. $ \sigma = \|a\| $
3. $ v = a + \sigma e_1 $
4. $ \alpha = \frac{1}{2} \|v\|^2 $
5. $ U = I - \frac{1}{\alpha} v v^T $

**Th.**

$$
U a =
\begin{pmatrix}
-\sigma \\ 0 \\ \vdots \\ 0
\end{pmatrix}
$$

$$\begin{align}
\alpha &= \frac{1}{2}\|v\|^2 = \frac{1}{2}vv^T \\
&= \frac{1}{2}(\alpha + \sigma e_1)^T(\alpha + \sigma e_1) \\
&= \frac{1}{2}(\alpha^T+ \sigma e_1^T)^T(\alpha + \sigma e_1) \\
&= \frac{1}{2}(\alpha^Te + \sigma\underbrace{\alpha^Te_1}_{=e_1^T\alpha} + \sigma \underbrace{e_1^T\alpha}_{=\alpha^Te_1} + \sigma^2 \underbrace{e_1^T e_1}_{= 1}  ) \\
&= \frac{1}{2}(\sigma^2 + 2\sigma e_1^T\alpha + \alpha^2)
\end{align}$$

Abbiamo trovato che:

$$\boxed{
\alpha = \frac{1}{2}\|v\|^2 = \frac{1}{2}vv^T = \sigma^2 + 2\sigma e_1^T\alpha + \alpha^2
}$$

Quindi:

$$\begin{align}
Ua &= (I - \frac{1}{\alpha}vv^T)a = a - \frac{1}{\alpha}vv^Ta \\
&= a - \frac{1}{\alpha}(a + \sigma e_1)(a+\sigma e_1)^Ta \\
&= a - \frac{1}{\alpha}(a + \sigma e_1)\underbrace{(\sigma^2 + \sigma e_1^Ta)}_{\alpha} \\
&= a - \frac{1}{\alpha}(a + \sigma e_1)\alpha \\
&= - \sigma e_1
\end{align}$$

---

#### Ortogonalità nella fattorizzazione

$$ \underbrace{U_{n-1}\cdots U_2U_1}_{\text{ortogonali}} = R $$

$$ A = U_1^TU_2^T\cdots U_{n-1}^T = R $$

#### Implementazione dell'algoritmo

Non è necessario utilizzare $n^2$ di spazio per il calcolo della matrice $U$. In realtà la matrice di householder non si vede mai in memoria del computer. Ci bassta riscrivere il prodotto in questo modo (matrix free):

$$ z = Uy = \Big( I - \frac{1}{\alpha}vv^T \Big)y = y - \frac{1}{\alpha}v(v^Ty) $$

dove:

- $\alpha = \frac{1}{2}\|v\|^2 \to\mathcal{O}(n)$
- $p = v^Ty \to\mathcal{O}(n)$
- $z = y - v(\frac{p}{\alpha}) \to\mathcal{O}(2n)$

La complessità computazionale ad ogni passo: $\mathcal{O}(4n) \approx \mathcal{O}(n)$.
Ognuna delle olonne quindi impiega un costo computazionale che si approssima ad $n$.

#### Nota sul costo computazionale

Fattorizzazione:
- Householder: $\mathcal{O}(\frac{2/3}n^3)$;
- Gauss: $\mathcal{O}(\frac{1/3}n^3)$.

In teoria la fattorizzazione di Gauss è il doppia più veloce ma ci sono alcuni casi in cui householder conviene.