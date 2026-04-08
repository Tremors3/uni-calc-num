
# (17) Lezione 01-04-2026 | s 247..252 | Metodi per la soluzione di equazioni nonlineari

### Introduzione ai metodi per equazioni nonlineari

Sia $\mathcal{f} : [a,b] \to\R$, l'obiettivo è trovare $x_*\in[a,b]$ tale che $\mathcal{f}(x_*) = 0$. Questi punti vengono chiamati anche radici di una funzione o zeri di una funzione.

Una semplificazione che inizialmente facciamo è che consideriamo una sola espressione con una sola incognita.

#### Teorema del valor medio

Si applica a funzioni continue (ipotesi minima che faremo), definita in un intervallo. Se il segno che la funzione assume agli esptremi dell'intervallo è discorde, allora il teorema ci garantisce che esiste almeno un punto nell'intervallo in cui la funzione si annulla. Si tratta di una condizione sufficiente.

Se la funzione è **strettamente monotona allora la radice sarà unica**.

#### Quattro metodi che studieremo

Due tipologie di metodi differenti:

- Metodi dicotomici

    1) Metodo di bisezione
    2) Metodo di regula fasi

- ...

Si tratta sempre di metodi iterativi.

---

### Metodo di Bisezione

Richiede come punto di partenza del metodo l'intervallo in cui cercare una radice. L'input del metodo sono l'estremo dx e sx.

Assumiamo che la funzione a cui vogliamo applicare il metodo soddisfi il teorema del valor medio.

Procedimento:

1) L'algoritmo individua ad ogni iterazione il punto medio $c_i$ nel sotto intervallo considerato.

2) In quale dei due sottointervalli considerati è ancora vero il teorema del valor medio? Considero il sotto intervallo in cui è valida. Itero il procedimento logaritmicamente; andando a prendere un intervallo sempre più piccolo.

3) Notiamo che ci stringiamo sempre di più verso una delle radici della funzione.

Quando c'è più di una radice non possiamo sapere verso quale radice ci stiamo dirigendo.

#### Fattore di interruzione del metodo

E' linico metodo che ci permette di controllare la distanza dalla soluzione reale. Fattore di Tolleranza. Ogni volta che facciamo un passo sul metodo di bisezione stiamo dimezzando l'intervallo fino a che non è abbastanza piccolo (sotto la tolleranza). La radice si troverà sicuramente in quell'intervallo.

Abbiamo che:

$$
\{[a_k,b_k]\}_{k=1}^\infin
$$

$$
{c_k}_{k=1}^\infin \qquad c_k = \frac{a_k + b_k}{2}
$$

Per le proprietà del metodo, esiste sicuramente una radice

$$ \exists x_* \text{radice} : x_* \in{a_k,b_k} $$

Ora, qual'è la distanza massima tra $c_k$ e la soluzione dell'intervallo $x_*$?

$$
|c_k - x_*| \le \frac{a_k + b_k}{2} = \frac{b - a}{2^k}
$$

Per il metodo di bisezione siamo in grado di stabilire quale sarà il numero totale di iterazioni da effettuare.

$$
\frac{b - a}{2^k} \le \tau
$$

$$
2^k \ge \frac{b - a}{\tau} \\
k \ge \log_2(\frac{b - a}{\tau})
$$

---

# (18) Lezione 08-04-2026 | s 253.. | Ripasso; Implementazione metodo di Bisezione; Metodo di Newton

### Metodo di Bisezione

#### Ripasso del metodo

- La soluzione non può essere più lontana dal punto medio non può essere più grande della metà dell'ampiezza dell'intervallo k-esimo.

---

#### Nota sul numero di iterazioni

Il numero minimo di iterazioni richiesto è:

$$
k \ge \log_2\!\left(\frac{b_0 - a_0}{\tau}\right)
$$

Questo mostra che il metodo converge con velocità logaritmica rispetto alla precisione richiesta. L'ultimo punto medio che calcoliamo sarà $\le\tau$. Fatte quelle iterazioni li sappiamo che la distanza tra la soluzione ed il punto medio è tollerabile.

---

#### Osservazione sul calcolo del punto medio

Le formule a disposizione per calcolare il punto medio sono:

$$
\frac{a+b}{2} \qquad\qquad a+\frac{b-a}{2}
$$

Qua**le delle due formule è conveniente utilizzare?** La formula più intuitiva è la prima: $(a + b) / 2$, che però risulta essere instabile. Infatti la somma tra $a$ e $b$ può comportare un troncamento importante al risultato. Per questo motivo scegliamo di utilizzare la seconda forma, equivalente e più stabile.

**Nota**: anche la seconda forma può portare al troncamento del risultato ma generalmente permette di ottenere una stima migliore (maggiore stabilità). Esempio a slide 258.

---

#### Implementazione (slide 259)

Pensata per ridurre al minimo necessario il costo computazionale.

Un'operazione non lineare (come ad esempio una funzione come sin/cos/...) viene tradotta in un polinomio che approssima il risultato reale della funzione.

Così facendo riusciamo ad ottenere una stima del costo computazionale del metodo. Infatti sarà la funzione scelta che comprenderà la maggior parte del costo computazionale. Dobbiamo considerare la funzione $f()$ come una sequenza di passi elementari che hanno un certo costo.

$$
\mathcal{O}(n \cdot \text{costo computazionale di }f)
$$

Dunque per aumentare l'efficienza del metodo dobbiamo cercare di chiamare il minor numero di volte possibile la funzione interessata.

---

### Metodo di Regula Falsi

Ha proprietà simili al metodo di bisezione. I metodi di bisezione e regula falsi si dicono **metodi dicotomici**.

Il metodo di regula falsi, invece del punto medio dell'intervallo, prende il punto di intersezione dell'asse delle ascisse con il segmento che parte dal punto della funzione sull'asse ordinata di a con quello di b. La relativa formula è:

$$
c = b - \frac{f(b)}{\frac{f(b)-f(a)}{b-a}}
$$

L'implementazione è identica a quella del metodo di bisezione ma sostituendo la formula per il calcolo del punto medio con questa.

---

#### Velocità di convergenza dei metodi dicotomici visti

Invece di analizzare la velocità di convergenza di un metodo cercando di studiare quanto una iterata k-esima si avvicina velocemente alla soluzione:

Confrontiamo la **distanza dalla soluzione di due iterate successive**.
Iterando il procedimento all'infinito otteniamo una successione di punti medi.

$$
|c_k - x_*| \le \frac{b - a}{2^k} \qquad\Rightarrow\qquad |c_k - x_*| \approx \frac{b - a}{2^k}
$$

Possiamo interpretare questa disequazione come una approssimazione dei due valori. Assumendo questo allora possiamo calcolare la distanza dell'iterata successiva come:

$$
|c_{k+1} - x_*| \approx \frac{b - a}{2^{k+1}} \approx \frac{1}{2}|c_k - x_*|
$$

La distanza dell'iterata $k+1$ esima è circa **la metà rispetto all'iterata precedente**.

Aggiungiamo una cifra decinale ogni 3 o 4 iterate. Se vogliamo allora un numero ingente di cifre decimali dovremmo iterare molto tempo.

Il metodo di bisezione richiede poco sia in termini di ipotesi iniziali, sia in termini di complessità. Ma se vogliamo un risultato preciso, dovremo fare molte iterazioni.

#### Studio convergenza dei metodi iterativi con ordine di convergenza p

Supponiamo di avere una successione di valori reali:

$$
{\{x_m\}}_{k\in\N} \in \R, \qquad \exists\; x_* : \lim_{n\to\infin} x_k = x_*
$$

La successione ha ordine di convergenza $p$ se

$$
|x_{k+1} - x_*| \le C{|x_k - x_*|}^p \qquad\forall\; k \;\textit{"abbastanza grande"}
$$

Le distanze in valore assoluto vanno tutte a zero per via della convergenza. Più p diventa grande più la parte destra della disequazione si riduce (equivale a dire che la distanza si riduce).

$$
\Leftrightarrow\qquad \lim_{k\to\infin} \frac{x_{k+1}-x_*}{{x_k-x_*}^p} = C
$$

In generale, per un metodo iterativo convergente, possiamo applicare il teorema.

#### Alcune tipologie di convergenza p

- Convergenza Lineare $p = 1, C \in (0,1)$

    $$
    \lim_{k\to\infin} \frac{x_{k+1}-x_*}{{x_k-x_*}^p} = C
    $$

    Il **metodo di bisezione ha convergenza lineare**.

---

### Metodo di Newton (delle Tangenti)

Il metodo di bisezione non può essere applicato a delle funzioni in più incognite ed in più equazioni (sistemi). Viene in soccorso il metodo di Newton.

Dato un punto, il nuovo punto è l'intersezione tra l'asse delle ascisse e la retta tangente di coordinate $x_k, f(x_k)$ nell'intervallo $[a, b]$.

Possiamo ottenere la formula dal ragionamento geometrico. Dobbiamo ricordare la formula della tangente del grafico della funzione $f$ nel suo punto di coordinate $x_k, f(x_k)$.

$$\begin{cases}
y &= 0 \\
y &= f(x_k) + f'(x_k)(x-x_k)
\end{cases} \quad\Rightarrow\quad x = x_k - \frac{f(x_k)}{f'(x_k)}
$$

Quindi abbiamo:

$$
0 = f(x_k) + f'(x_k)(x-x_k)
$$

Assumento che $f'(x_K)\ne 0$:

$$
0 = \frac{f(x_k)}{f'(x_k)} + x - x_k \quad\to\quad x = \boxed{x_k - \frac{f(x_k)}{f'(x_k)} = x_{k+1}}
$$

Perchè tutto funzioni necessitiamo che la derivata prima della funzione non si annulli mai in nessuno dei punti in cui capitiamo. Questa è un'ulteriore ipotesi che facciamo.

$$ f'(x_k) \ne 0 $$

Possiamo rivedere questo assunto come avere una: **Funzione derivabile** e **Strettamente monotona**.

---

#### Riconduciamoci alla formula del metodo di Newton tramite approssimazione Taylor

Sostituisce il problema difficile (non lineare) $f(x)=0$ (che non ha una soluzione diretta) con una successione di problemi più semplici: sostituendo alla funzione il suo sviluppo di taylor troncato al primo ordine:

$$
f(x) \approx f(x_0) + f'(x_0)(x-x_0)
$$

e quindi otteniamo l'approssimazione lineare:

$$
f(x_0) + f'(x_0)(x-x_0) = 0 \quad\Rightarrow\quad \boxed{x = x_0 - \frac{f(x_0)}{f'(x_0)}}
$$

che è la formula del metodo di newton.

---

#### Complessità computazionale

Qui il costo raddoppia, rispetto al metodo di bisezione. Il costo computazionale lo calcoliamo considerando il numero di funzioni da calcolare ad ogni passo. Nel caso del metodo di Newton ne abbiamo due, una al numeratore ed una al denominatore. E' vero che le due funzioni sono diverse ma si tratta comunque di due funzioni nonlineari e allora le consideriamo insieme (equiparabili).

Il metodo di Newton effettua un numero molto minore di iterazioni rispetto al metodo di bisezione. Quindi il costo delle singole iterazioni viene bilanciato dal numero di iterazioni.

---

#### Velocità di convergenza

Se il metodo di newton per una funzione converge, allora lo fa in modo quadratico.

---
