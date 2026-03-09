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