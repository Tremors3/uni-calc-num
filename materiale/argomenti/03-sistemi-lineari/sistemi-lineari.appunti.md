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

Supponiamo che l'errore si trovi tutto nel termine noto. In realtà un'analisi simile la può fare anche quando gli errori li abbiamo sugli elementi della matrice. Quindi abbiamo errori sui termini noti e sulla matrice (slide 132). C'è sempre di mezzo l'indice di condizionamento.A−1b

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

# (9) Lezione 11-03-2026 | s 140.. | Sistemi Lineari Generici

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

#### In generale

Ad un generico passo $k$. Abbiamo in ingresso la matrice $A_k$ (dai passi precedenti) e dobbiamo produrre la matrice $A_{k+1}$. Prendo gli elementi che stavano nella vecchia matrice, meno i moltiplicatori di quella riga li moltiplicati per gli elementi che stavano sulla stessa riga e colonna del moltiplicatore.

Iteriamo l'algoritmo $n-1$ volte. Alla fine ritrovaremo la matrice trasformata nella forma triangolare superiore.

#### Studio dell'algoritmo

Le formule di aggiornamento sono l'algoritmo di Gauss. Prenderequeste formule ed implementarle per i vari indici.

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