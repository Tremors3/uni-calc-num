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

# (9) Lezione 11-03-2026 | s 139.. | Sistemi Lineari Generici



---