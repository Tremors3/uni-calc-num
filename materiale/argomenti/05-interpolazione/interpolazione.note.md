
# Interpolazione

### Esempi e motivazioni dell’interpolazione

L’interpolazione nasce dall’esigenza di ricostruire informazioni intermedie a partire da dati noti. In molti contesti applicativi non ci interessa solo conoscere uno stato iniziale e uno finale, ma anche descrivere in modo continuo ciò che accade tra questi due estremi.

Un esempio tipico è quello del movimento di un braccio robotico. Date una configurazione iniziale e una finale, vogliamo determinare una sequenza di configurazioni intermedie che descrivano il movimento del braccio nel tempo. In questo modo è possibile ottenere un’animazione fluida (frame intermedi) che rappresenti il passaggio da uno stato all’altro. L’interpolazione permette quindi di costruire una traiettoria continua nello spazio delle configurazioni.

Un altro esempio importante riguarda l’elaborazione delle immagini. Supponiamo di avere una porzione di immagine rappresentata come una matrice di pixel di dimensione $n \times n$. Se vogliamo ingrandire questa immagine, possiamo costruire una nuova matrice più grande, ad esempio di dimensione $m \times m$ con $m = 2n$. Tuttavia, i nuovi pixel introdotti non hanno un valore assegnato.

Il problema diventa quindi quello di determinare i valori dei pixel mancanti in modo coerente con quelli originali. Questo viene fatto tramite tecniche di interpolazione, che stimano i valori ignoti utilizzando l’informazione disponibile nei pixel vicini.

In sintesi, l’interpolazione consente di passare da dati discreti a una rappresentazione più densa o continua, ed è fondamentale in applicazioni come animazioni, simulazioni fisiche e elaborazione di immagini.

---

## Interpolazione polinomiale

Il problema dell’interpolazione consiste nel costruire una funzione che passi esattamente per un insieme finito di punti dati.

I dati in ingresso sono coppie di valori:

$$
(x_i, y_i), \qquad i = 0, \dots, n
$$

dove gli $x_i$ rappresentano le ascisse (tipicamente distinti tra loro) e gli $y_i$ le corrispondenti ordinate.

L’obiettivo è costruire una funzione $g(x)$ tale che:

$$
g(x_i) = y_i \qquad \forall i = 0, \dots, n
$$

cioè una funzione che interpoli esattamente tutti i punti dati.

---

#### Scopo dell’interpolazione

Una volta costruita la funzione $g(x)$, possiamo usarla per stimare valori in punti non noti. Dato un punto $\tilde{x}$ (che non appartiene necessariamente all’insieme $\{x_i\}$), vogliamo determinare:

$$
g(\tilde{x}) = \tilde{y}
$$

In questo modo si ottiene una stima dell’ordinata associata a $\tilde{x}$, basata sull’informazione dei punti noti.

---

#### Idea di base

L’interpolazione consiste quindi nel passare da un insieme discreto di dati a una funzione continua che li descriva. Una volta costruita questa funzione, i valori ignoti vengono determinati semplicemente valutandola nei punti di interesse.

Tuttavia, esiste un aspetto importante: **non esiste un’unica funzione che interpola i dati**. In generale, infinite funzioni possono passare per gli stessi punti.

Per rendere il problema ben posto, è necessario restringere la classe delle funzioni tra cui cercare l’interpolante.

---

#### Scelta della classe di funzioni

Nella maggior parte dei casi si scelgono i **polinomi**, perché:

- sono semplici da gestire dal punto di vista computazionale,
- garantiscono (sotto opportune condizioni) esistenza e unicità della soluzione,
- sono facili da valutare e derivare.

Pertanto, il problema dell’interpolazione si riduce spesso alla costruzione di un polinomio $p(x)$ tale che:

$$
p(x_i) = y_i \qquad \forall i = 0, \dots, n
$$

Questo polinomio è detto **polinomio interpolante** dei dati.

---

#### Intermezzo sui polinomi

Un **polinomio** è una funzione che si scrive come combinazione di monomi, della forma:

$$
p(x) = a_0 + a_1 x + a_2 x^2 + \dots + a_n x^n, \qquad a_0, a_1, \dots, a_n \in \mathbb{R}
$$

dove i coefficienti $a_i$ sono numeri reali e il grado del polinomio è $n$ (supponendo $a_n \neq 0$).

---

#### Perché scegliere i polinomi per l’interpolazione?

I polinomi sono una scelta naturale per l’interpolazione perché possiedono una proprietà fondamentale: sono completamente determinati dai loro coefficienti. Un polinomio di grado al più $n$ è descritto da $n+1$ coefficienti:

$$
a_0, a_1, \dots, a_n
$$

Quindi esiste una corrispondenza tra:

- i $n+1$ dati $(x_i, y_i)$,
- e i $n+1$ coefficienti del polinomio interpolante.

Sotto opportune condizioni (in particolare $x_i$ tutti distinti), è possibile dimostrare che **esiste ed è unico** un polinomio di grado al più $n$ che interpola i dati:

$$
p(x_i) = y_i \qquad \forall i = 0, \dots, n
$$

Dal punto di vista computazionale, il problema dell’interpolazione si riduce quindi a determinare i coefficienti del polinomio. Il risultato del calcolo non è direttamente la funzione, ma un insieme di numeri (i coefficienti) che la identificano completamente.

È importante osservare che il numero di dati $n+1$ coincide con il numero di coefficienti del polinomio, e quindi con il grado massimo del polinomio interpolante.

In sintesi, i polinomi permettono di trasformare il problema dell’interpolazione in un problema algebrico ben posto, con soluzione unica e facilmente rappresentabile.

---

#### Interpolazione polinomiale ed esistenza/unicità

Un risultato fondamentale alla base dell’interpolazione polinomiale è il seguente: dati $n+1$ punti distinti nel piano, esiste **un unico polinomio di grado al più $n$** che passa esattamente per tutti questi punti.

È importante precisare un dettaglio: dati tre punti, esiste un’unica **parabola**, cioè un polinomio di **grado al più 2** (non di terzo grado), che li interpola. Questo risultato si generalizza: dati $n+1$ punti $(x_i, y_i)$ con $x_i$ distinti, esiste ed è unico il polinomio $p_n(x)$ di grado al più $n$ tale che:

$$
p_n(x_i) = y_i \qquad \forall i = 0, \dots, n
$$

---

#### Significato per l’interpolazione

Questo teorema è cruciale perché risolve due problemi:

- tra infinite funzioni possibili, restringiamo la ricerca ai polinomi;
- all’interno dei polinomi, otteniamo una **soluzione unica**.

Quindi il problema dell’interpolazione diventa ben posto: esiste una sola funzione interpolante (nel senso polinomiale) che soddisfa i vincoli.

---

#### Formulazione del problema

Dati i punti:

$$
(x_i, y_i), \qquad i = 0, \dots, n
$$

si vuole determinare un polinomio:

$$
p_n(x) = a_0 + a_1 x + a_2 x^2 + \dots + a_n x^n
$$

tale che valgano le condizioni di interpolazione:

$$
p_n(x_i) = y_i \qquad \forall i = 0, \dots, n
$$

L’obiettivo è quindi determinare i coefficienti:

$$
a_0, a_1, \dots, a_n
$$

---

#### Osservazione

L’interpolazione polinomiale è caratterizzata da due scelte fondamentali:

- si restringe la classe delle funzioni ai polinomi;
- si fissa il grado massimo del polinomio in base al numero di dati.

Queste due restrizioni garantiscono unicità e rendono il problema trattabile sia teoricamente che computazionalmente.

---

#### Interpretazione algebrica

Un polinomio è una combinazione lineare dei monomi:

$$
1, \; x, \; x^2, \; \dots, \; x^n
$$

Pertanto, imporre le condizioni di interpolazione equivale a costruire un sistema lineare in cui le incognite sono i coefficienti $a_0, \dots, a_n$.

Il problema dell’interpolazione polinomiale si riduce quindi alla risoluzione di un sistema lineare con $n+1$ equazioni e $n+1$ incognite, che ammette una soluzione unica (se gli $x_i$ sono distinti).

---

### Metodo dei coefficienti indeterminati

Per costruire il polinomio interpolante, partiamo dalla sua forma generale:

$$
p_n(x) = a_0 + a_1 x + a_2 x^2 + \dots + a_n x^n
$$

e imponiamo che soddisfi le **condizioni di interpolazione**:

$$
p_n(x_i) = y_i \qquad \forall i = 0, \dots, n
$$

che corrispondono a:

$$\begin{aligned}
i=0) &\quad p_n(x_0) = y_0 \;\Leftrightarrow\; a_0 + a_1x_0 + a_2x_0^2 + \dots + a_nx_0^n = y_0 \\
i=1) &\quad p_n(x_1) = y_1 \;\Leftrightarrow\; a_0 + a_1x_1 + a_2x_1^2 + \dots + a_nx_1^n = y_1 \\ 
\dots \\
i=n) &\quad p_n(x_n) = y_n \;\Leftrightarrow\; a_0 + a_1x_n + a_2x_n^2 + \dots + a_nx_n^n = y_n \\ 
\end{aligned}$$


Sostituendo ciascun punto $(x_i, y_i)$ nel polinomio, otteniamo un sistema di $n+1$ equazioni:

$$
\begin{cases}
a_0 + a_1 x_0 + a_2 x_0^2 + \dots + a_n x_0^n = y_0 \\
a_0 + a_1 x_1 + a_2 x_1^2 + \dots + a_n x_1^n = y_1 \\
\vdots \\
a_0 + a_1 x_n + a_2 x_n^2 + \dots + a_n x_n^n = y_n
\end{cases}
$$

In questo sistema:

- i valori $x_i$ e $y_i$ sono dati noti,
- le incognite sono i coefficienti $a_0, a_1, \dots, a_n$.

---

#### Forma matriciale

Il sistema può essere scritto in forma matriciale come:

$$
\boxed{
V \alpha = y
}
$$

dove:

$$
V =
\begin{pmatrix} 
1 & x_0 & x_0^2 & \dots & x_0^n \\
1 & x_1 & x_1^2 & \dots & x_1^n \\
\vdots & \vdots & \vdots & & \vdots \\
1 & x_n & x_n^2 & \dots & x_n^n
\end{pmatrix},
\quad
\alpha =
\begin{pmatrix}
a_0 \\ a_1 \\ \vdots \\ a_n
\end{pmatrix},
\quad
y =
\begin{pmatrix}
y_0 \\ y_1 \\ \vdots \\ y_n
\end{pmatrix}
$$

La matrice $V$ è detta **matrice di Vandermonde**.

---

#### Interpretazione

Il problema dell’interpolazione polinomiale si riduce quindi alla risoluzione di un sistema lineare con $n+1$ equazioni e $n+1$ incognite.

Una volta determinato il vettore dei coefficienti $\alpha$, il polinomio $p_n(x)$ è completamente noto e può essere utilizzato per valutare la funzione in qualsiasi punto.

In altre parole, “costruire la funzione” significa trovare i coefficienti reali che la identificano univocamente.

---

#### Osservazione

Il metodo dei coefficienti indeterminati è concettualmente semplice e diretto, ma presenta limiti pratici: **la matrice di Vandermonde può diventare numericamente instabile per $n$ grande**. Per questo motivo, in pratica si preferiscono altre formulazioni dell’interpolazione (come la forma di Lagrange o di Newton).

---

### Metodo di Lagrange

Un’alternativa al metodo dei coefficienti indeterminati consiste nel rappresentare il polinomio interpolante in una forma diversa, evitando di risolvere esplicitamente il sistema lineare.

L’idea è di non esprimere più il polinomio nella forma canonica:

$$
p_n(x) = a_0 + a_1 x + \dots + a_n x^n
$$

ma come combinazione lineare di una **base diversa di polinomi**, costruita direttamente a partire dai nodi di interpolazione.

---

#### Caso base: interpolazione lineare

Consideriamo due punti $(x_0, y_0)$ e $(x_1, y_1)$. Il polinomio interpolante (retta) può essere scritto come:

$$
p_1(x) = y_0 + (x - x_0)\frac{y_1 - y_0}{x_1 - x_0}
$$

Questa espressione può essere riscritta come combinazione lineare:

$$
p_1(x) = y_0 \underbrace{\frac{x - x_1}{x_0 - x_1}}_{L_0(x)} + 
          y_1 \underbrace{\frac{x - x_0}{x_1 - x_0}}_{L_1(x)}
$$

dove $L_0(x)$ e $L_1(x)$ sono polinomi di grado 1.

---

#### Generalizzazione: polinomio di grado $n$

Nel caso generale, dati $n+1$ punti $(x_i, y_i)$, il polinomio interpolante si scrive come:

$$
p_n(x) = \sum_{i=0}^{n} y_i \, L_i(x)
$$

dove i polinomi $L_i(x)$ costituiscono la **base di Lagrange** e sono definiti come:

$$
L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{x - x_j}{x_i - x_j}
$$

---

#### Proprietà fondamentale

I polinomi di Lagrange sono costruiti in modo tale da soddisfare:

$$
\begin{cases}
L_i(x_i) = 1 \\
L_i(x_j) = 0 \quad \text{per } j \neq i
\end{cases}
$$

Questa proprietà garantisce automaticamente le condizioni di interpolazione:

$$
p_n(x_i) = y_i
$$

Infatti, valutando $p_n(x)$ in $x = x_i$, tutti i termini si annullano tranne quello con indice $i$.

---

#### Interpretazione

In questa formulazione:

- i coefficienti $y_i$ sono noti (sono i dati),
- le funzioni base $L_i(x)$ dipendono solo dai nodi $x_i$ e devono essere costruite.

Il polinomio interpolante è quindi ottenuto come combinazione lineare di queste funzioni base.

---

#### Vantaggi e svantaggi

Questo metodo evita la risoluzione del sistema lineare (e quindi i problemi legati alla matrice di Vandermonde, spesso mal condizionata).

Tuttavia, il costo computazionale può diventare elevato se si calcolano direttamente i prodotti per ogni $L_i(x)$, soprattutto per $n$ grande. Per questo motivo, nella pratica è importante organizzare il calcolo in modo efficiente o utilizzare formulazioni alternative più stabili (come la forma baricentrica).

---

#### Conclusione

Il metodo di Lagrange fornisce una rappresentazione esplicita del polinomio interpolante, concettualmente semplice e teoricamente elegante, che costruisce direttamente la funzione senza passare dalla determinazione dei coefficienti nella base canonica.

---

## Approssimazione dell’interpolazione polinomiale ed errore

### Approssimazione polinomiale

Quando utilizziamo un polinomio interpolante $p(x)$ per approssimare una funzione $f(x)$, è fondamentale capire **quanto le due funzioni siano vicine**. Per farlo, introduciamo il concetto di distanza tra funzioni tramite una norma.

Assumiamo che $f : [a,b] \to \mathbb{R}$ sia continua su un intervallo chiuso e limitato. In questo contesto, possiamo definire la **norma infinito** (o norma uniforme) come:

$$
\|f\|_{\infty} = \max_{x \in [a,b]} |f(x)|
$$

Questa norma misura il valore massimo assoluto assunto dalla funzione nell’intervallo.

---

#### Distanza tra funzione e interpolante

Per confrontare la funzione originale $f$ con il polinomio interpolante $p$, consideriamo la norma della loro differenza:

$$
\|f - p\|_{\infty} = \max_{x \in [a,b]} |f(x) - p(x)|
$$

Questa quantità rappresenta **l’errore massimo** tra le due funzioni sull’intero intervallo.

Se vale:

$$
\|f - p\|_{\infty} < \varepsilon
$$

allora significa che, per ogni $x \in [a,b]$:

$$
|f(x) - p(x)| < \varepsilon
$$

cioè:

$$
f(x) - \varepsilon < p(x) < f(x) + \varepsilon
$$

---

#### Interpretazione geometrica

La norma infinito ha un significato molto intuitivo: rappresenta la **massima distanza verticale** tra i grafici di $f$ e $p$.

Dire che:

$$
\|f - p\|_{\infty} < \varepsilon
$$

significa che il grafico del polinomio $p(x)$ è sempre contenuto in una “fascia” di ampiezza $2\varepsilon$ centrata attorno al grafico di $f(x)$.

---

#### Qualità dell’approssimazione

Più il valore:

$$
\|f - p\|_{\infty}
$$

è piccolo, migliore è l’approssimazione. In altre parole, il polinomio interpolante descrive fedelmente il comportamento della funzione originale su tutto l’intervallo.

Questo concetto è fondamentale perché permette di valutare **globalmente** la bontà dell’interpolazione, e non solo nei punti in cui i due grafici coincidono (i nodi).

---

#### Osservazione

L’interpolazione garantisce che:

$$
p(x_i) = f(x_i)
$$

nei nodi, quindi l’errore è nullo in quei punti. Tuttavia, tra i nodi l’errore può crescere, ed è proprio la norma infinito che ci permette di quantificare il caso peggiore.

---

### Resto di interpolazione

Per studiare l’errore dell’interpolazione polinomiale introduciamo il **resto di interpolazione**, definito come la differenza tra la funzione originale e il polinomio interpolante:

$$
\boxed{
R_n(x) = f(x) - p_n(x)
}
$$

dove $p_n(x)$ è il polinomio interpolante di grado al più $n$, costruito a partire dai nodi $x_0, x_1, \dots, x_n$ tali che:

$$
p_n(x_i) = f(x_i) \qquad \forall i = 0, \dots, n
$$

con:

$$
x_i \in [a,b]
$$

---

#### Interpretazione

Il resto $R_n(x)$ misura, punto per punto, quanto il polinomio si discosta dalla funzione reale. Nei nodi di interpolazione vale:

$$
R_n(x_i) = 0
$$

perché il polinomio interpola esattamente la funzione in quei punti.

Tuttavia, per $x \neq x_i$, il resto può essere diverso da zero, ed è proprio questo comportamento che vogliamo analizzare.

---

#### Errore massimo

Per valutare globalmente l’errore, consideriamo la norma infinito del resto:

$$
\|R_n\|_{\infty} = \max_{x \in [a,b]} |R_n(x)| = \max_{x \in [a,b]} |f(x) - p_n(x)|
$$

Questa quantità rappresenta il **massimo errore di interpolazione** sull’intervallo.

---

#### Significato

Studiare il resto di interpolazione significa capire quanto il polinomio interpolante approssima bene la funzione reale non solo nei nodi, ma su tutto l’intervallo.

In particolare, l’obiettivo è rendere $\|R_n\|_{\infty}$ il più piccolo possibile, scegliendo opportunamente:

- il grado del polinomio,
- la posizione dei nodi $x_i$.

Questo porta naturalmente a problemi più avanzati, come la scelta ottimale dei nodi (ad esempio i nodi di Chebyshev).

---

### Dimostrazione della formula del resto di interpolazione

L’obiettivo è comprendere come si comporta l’errore di interpolazione:

$$
R_n(x) = f(x) - p_n(x)
$$

in funzione di:
- il numero di nodi $n+1$ utilizzati;
- la loro distribuzione nell’intervallo $[a,b]$.

---

#### Ipotesi

Sia $f : [a,b] \to \mathbb{R}$ tale che:

$$
f \in C^{n+1}([a,b])
$$

cioè $f$ è derivabile fino all’ordine $n+1$ con derivate continue. Siano inoltre:

$$
x_0, x_1, \dots, x_n \in [a,b]
$$

i nodi di interpolazione, e $p_n$ il polinomio di grado al più $n$ tale che:

$$
p_n(x_i) = f(x_i) \qquad \forall i = 0,\dots,n
$$

---

#### Teorema (formula del resto)

Per ogni $x \in [a,b]$ esiste un punto $\xi = \xi(x) \in [a,b]$ tale che:

$$
\boxed{
R_n(x) = \frac{(x - x_0)(x - x_1)\cdots(x - x_n)}{(n+1)!}\, f^{(n+1)}(\xi)
}
$$

---

#### Interpretazione della formula

Introduciamo il polinomio:

$$
\omega_{x_0,\dots,x_n}(x) = (x - x_0)(x - x_1)\cdots(x - x_n)
$$

che è un polinomio di grado $n+1$ con coefficiente principale pari a $1$.

Questo polinomio si annulla nei nodi:

$$
\omega_{x_0,\dots,x_n}(x_i) = 0
$$

e rappresenta la parte dell’errore che dipende **solo dalla scelta dei nodi**.

La formula del resto può quindi essere scritta come:

$$
R_n(x) = \frac{\omega_{x_0,\dots,x_n}(x)}{(n+1)!}\, f^{(n+1)}(\xi)
$$

---

#### Idea della dimostrazione

Si costruisce una funzione ausiliaria:

$$
\Omega(x,t) = R_n(t)\,\omega(x) - R_n(x)\,\omega(t)
$$

fissato $x$, si considera $\Omega(x,t)$ come funzione della variabile $t$.

Questa funzione si annulla in $n+2$ punti:
- nei nodi $t = x_i$, perché $R_n(x_i) = 0$;
- nel punto $t = x$.

Applicando ripetutamente il **teorema di Rolle**, si dimostra che esiste $\xi$ tale che:

$$
\frac{d^{n+1}}{dt^{n+1}} \Omega(x,t)\Big|_{t=\xi} = 0
$$

da cui si ricava la formula del resto.

---

#### Stima dell’errore (norma infinito)

Prendendo il valore assoluto:

$$
|R_n(x)| = \left| \frac{\omega(x)}{(n+1)!} f^{(n+1)}(\xi) \right|
$$

e facendo il massimo su $[a,b]$:

$$
\|R_n\|_{\infty} = \max_{x \in [a,b]} |R_n(x)|
\le
\frac{\max_{x \in [a,b]} |\omega(x)|}{(n+1)!}
\cdot
\max_{x \in [a,b]} |f^{(n+1)}(x)|
$$

Se definiamo:

$$
M_{n+1} = \max_{x \in [a,b]} |f^{(n+1)}(x)|
$$

e:

$$
\omega^* = \max_{x \in [a,b]} |\omega(x)|
$$

otteniamo la stima:

$$
\boxed{
\|R_n\|_{\infty} \le \frac{\omega^*}{(n+1)!} \, M_{n+1}
}
$$

---

#### Osservazioni fondamentali

L’errore dipende da due fattori distinti:

La quantità:

$$
M_{n+1}
$$

dipende solo dalla funzione $f$ e misura quanto è “irregolare” (quanto cresce la derivata di ordine alto).

La quantità:

$$
\omega^* = \max_{x \in [a,b]} |\omega(x)|
$$

dipende solo dai nodi di interpolazione.

---

#### Conseguenza importante

Non basta aumentare il numero di nodi per migliorare l’approssimazione: è fondamentale **scegliere bene i nodi**.

Infatti, per nodi equispaziati, $\omega(x)$ può diventare molto grande (fenomeno di Runge), peggiorando l’errore.

Una scelta ottimale consiste nei **nodi di Chebyshev**, che minimizzano il massimo di $|\omega(x)|$ e quindi riducono l’errore globale.

---

### Ripasso sull’interpolazione polinomiale e resto di interpolazione

Sia data una funzione

$$
f : [a,b] \to \mathbb{R}
$$

e siano fissati $n+1$ nodi distinti

$$
x_0, x_1, \dots, x_n \in [a,b].
$$

Esiste ed è unico il polinomio interpolante $p_n(x)$ di grado al più $n$ tale che

$$
p_n(x_i)=f(x_i)\qquad \forall i=0,\dots,n.
$$

Definiamo **resto di interpolazione** (o errore di interpolazione puntuale) la funzione

$$
R_n(x)=f(x)-p_n(x).
$$

Questa quantità misura, punto per punto, quanto il polinomio interpolante si discosta dalla funzione originale.

---

#### Formula del resto di interpolazione

Dal teorema dimostrato sul resto di interpolazione sappiamo che, per ogni $x\in[a,b]$, esiste un punto

$$
\xi=\xi(x)\in[a,b]
$$

tale che

$$
R_n(x)=\frac{\omega_{x_0,\dots,x_n}(x)}{(n+1)!}\,f^{(n+1)}(\xi),
$$

dove

$$
\omega_{x_0,\dots,x_n}(x)=(x-x_0)(x-x_1)\cdots(x-x_n)
$$

è il **polinomio nodale**, polinomio di grado $n+1$ che si annulla esattamente nei nodi di interpolazione.

---

#### Stima dell’errore

Supponiamo che

$$
f\in C^{n+1}([a,b]),
$$

cioè che $f$ abbia derivata $(n+1)$-esima continua nell’intervallo. Essendo continua su un compatto, tale derivata ammette massimo assoluto:

$$
M_{n+1}^f=\max_{x\in[a,b]}|f^{(n+1)}(x)|.
$$

Prendendo il valore assoluto nella formula del resto otteniamo:

$$
|R_n(x)|
=
\left|
\frac{\omega_{x_0,\dots,x_n}(x)}{(n+1)!}\,f^{(n+1)}(\xi)
\right|
$$

e quindi la stima

$$
|R_n(x)|
\le
\frac{|\omega_{x_0,\dots,x_n}(x)|}{(n+1)!}\,M_{n+1}^f.
$$

---

#### Interpretazione della stima

Questa disuguaglianza è fondamentale perché mostra che l’errore di interpolazione dipende essenzialmente da due fattori:

$$
|R_n(x)| \lesssim
\frac{M_{n+1}^f}{(n+1)!}\,|\omega_{x_0,\dots,x_n}(x)|.
$$

In molti casi pratici questa stima descrive bene anche il comportamento qualitativo dell’errore, cioè il resto si comporta **come se fosse proporzionale** al polinomio nodale $\omega$.

La costante di proporzionalità è circa

$$
\frac{M_{n+1}^f}{(n+1)!}.
$$

Questo significa che:

- se $\omega(x)$ oscilla molto, anche l’errore tenderà a oscillare molto;
- se $\omega(x)$ assume valori grandi, anche l’errore potrà diventare grande.

---

#### Collegamento con il fenomeno di Runge

Il fenomeno di Runge si manifesta quando il polinomio interpolante oscilla fortemente, specialmente vicino agli estremi dell’intervallo.

Dalla formula dell’errore si capisce che il principale responsabile di questo comportamento è proprio il polinomio nodale

$$
\omega_{x_0,\dots,x_n}(x).
$$

Infatti, scegliendo male i nodi (ad esempio nodi equispaziati), il polinomio $\omega$ può crescere molto vicino agli estremi, causando un grande errore di interpolazione.

Per ridurre questo effetto occorre scegliere i nodi in modo più opportuno, ad esempio utilizzando i **nodi di Chebyshev**, che minimizzano il massimo valore assoluto del polinomio nodale.

---

#### Conclusione

Il fenomeno di Runge è dovuto principalmente a due fattori strettamente collegati:

1. La **scelta dei nodi di interpolazione**, che influenza la forma del polinomio nodale.

2. Il comportamento del **polinomio nodale**

    $$
    \omega_{x_0,\dots,x_n}(x),
    $$

    che determina direttamente l’andamento dell’errore di interpolazione.

Per questo motivo, nell’interpolazione polinomiale non conta solo quanti punti si usano, ma soprattutto **dove vengono scelti**.

---

## Interpolazione a Tratti

### Altri metodi di interpolazione

L’interpolazione polinomiale globale presenta alcuni limiti pratici importanti.

Il primo inconveniente è che il grado del polinomio interpolante cresce con il numero dei nodi: se si vogliono interpolare molti punti, si è costretti a costruire un polinomio di grado elevato. Questo può portare sia a problemi numerici sia a oscillazioni indesiderate, come nel fenomeno di Runge.

Un secondo limite è che l’interpolazione polinomiale classica richiede di conoscere **tutti i punti fin dall’inizio**. Se nuovi dati vengono aggiunti successivamente, in generale occorre ricostruire completamente il polinomio interpolante.

---

### Idea dell'Interpolazione a Tratti

Per superare questi problemi si può rinunciare a costruire un unico polinomio globale e utilizzare invece **più polinomi locali**, ciascuno valido solo su una parte dell’intervallo.

L’idea più semplice consiste nel collegare ogni coppia di punti consecutivi con un segmento, ottenendo una funzione spezzata che interpola tutti i dati.

Questa funzione **non è un polinomio globale** su tutto l’intervallo, ma possiede una struttura polinomiale locale: se la si restringe a uno specifico sottointervallo, allora coincide con un polinomio di grado 1.

In altre parole, l’interpolazione a tratti costruisce una funzione che è:

- globalmente una funzione spezzata;
- localmente, su ciascun intervallo, un polinomio.

---

#### Vantaggio principale

Il vantaggio fondamentale è che **il numero di nodi viene disaccoppiato dal grado dei polinomi utilizzati**.

Con l’interpolazione polinomiale globale:

$$
n+1 \text{ nodi } \Rightarrow \text{ polinomio di grado } n
$$

Con l’interpolazione lineare a tratti:

$$
n+1 \text{ nodi } \Rightarrow n \text{ polinomi di grado } 1
$$

Quindi anche con moltissimi punti si continua a lavorare con polinomi semplici.

---

#### Suddivisione dell’intervallo

Supponiamo di avere nodi ordinati:

$$
x_0 < x_1 < \cdots < x_n
$$

Essi suddividono l’intervallo complessivo nei sottointervalli:

$$
I_i = [x_i, x_{i+1}], \qquad i=0,\dots,n-1
$$

Su ciascun intervallo $I_i$ costruiremo un interpolante locale.

---

#### Come si valuta l’interpolante a tratti

Per calcolare il valore dell’interpolante in un punto $x$:

Si individua anzitutto il sottointervallo $I_j$ tale che

$$
x \in [x_j, x_{j+1}]
$$

Successivamente si utilizza il polinomio locale associato a quell’intervallo, cioè la retta passante per i punti:

$$
(x_j, y_j), \qquad (x_{j+1}, y_{j+1})
$$

---

#### Formula dell’interpolante lineare locale

La retta interpolante sul sottointervallo $I_i=[x_i,x_{i+1}]$ è:

$$
p_i(x)=
y_i+
\frac{y_{i+1}-y_i}{x_{i+1}-x_i}(x-x_i)
$$

oppure, in forma equivalente:

$$
p_i(x)=
y_i\frac{x-x_{i+1}}{x_i-x_{i+1}}
+
y_{i+1}\frac{x-x_i}{x_{i+1}-x_i}
$$

Questa formula vale solo per:

$$
x\in[x_i,x_{i+1}]
$$

---

#### Osservazione finale

L’interpolazione a tratti produce quindi una funzione definita **pezzo per pezzo**, dove ogni pezzo ha una propria formula.

Questo significa che non esiste un’unica espressione valida su tutto l’intervallo, ma una famiglia di polinomi locali:

$$
p_0(x),\,p_1(x),\,\dots,\,p_{n-1}(x)
$$

ciascuno associato al proprio sottointervallo.

L’idea fondamentale è che si sacrifica la semplicità di avere un unico polinomio globale, in cambio di una maggiore stabilità numerica e di una migliore gestione di grandi quantità di dati.

---

### Interpolazione lineare a tratti: proprietà ed errore

Un importante vantaggio dell’interpolazione lineare a tratti è che **non soffre del fenomeno di Runge**.

A differenza dell’interpolazione polinomiale globale, la sua stabilità non peggiora al crescere del numero dei nodi e dipende molto meno dalla loro posizione.

Sia data una funzione

$$
f:[a,b]\to\mathbb{R}, \qquad f\in C^2([a,b])
$$

e siano fissati nodi ordinati

$$
a=x_0<x_1<\dots<x_m<x_{m+1}=b.
$$

Indichiamo con $s(x)$ l’interpolante lineare a tratti, cioè la funzione spezzata tale che

$$
s(x_i)=f(x_i)\qquad i=0,\dots,m+1.
$$

Assumiamo quindi che i dati interpolati provengano dal grafico della funzione $f$.

---

#### Resto di interpolazione lineare

Definiamo il resto (errore) dell’interpolazione lineare a tratti come

$$
R^s(x)=s(x)-f(x).
$$

Poiché $s(x)$ è definita a tratti, anche l’analisi dell’errore deve essere fatta **localmente su ciascun sottointervallo**.

Fissiamo quindi un intervallo della partizione:

$$
x\in[x_i,x_{i+1}].
$$

Su questo intervallo, $s(x)$ coincide con la retta interpolante i due punti estremi:

$$
s(x)=f(x_i)+\frac{f(x_{i+1})-f(x_i)}{x_{i+1}-x_i}(x-x_i).
$$

---

#### Formula del resto locale

Poiché su $[x_i,x_{i+1}]$ stiamo interpolando con un polinomio di grado 1, possiamo applicare la formula generale del resto di interpolazione con $n=1$.

Otteniamo quindi che esiste un punto

$$
\xi_i\in[x_i,x_{i+1}]
$$

tale che

$$
R^s(x)=s(x)-f(x)
=
\frac{(x-x_i)(x-x_{i+1})}{2}\,f''(\xi_i).
$$

Questa è la formula esatta dell’errore dell’interpolazione lineare su ciascun intervallo.

---

#### Stima dell’errore

Passando al valore assoluto:

$$
|R^s(x)|
=
\frac{|(x-x_i)(x-x_{i+1})|}{2}\,|f''(\xi_i)|.
$$

Poiché $f''$ è continua su $[a,b]$, esiste il massimo assoluto:

$$
M_2^f=\max_{x\in[a,b]}|f''(x)|.
$$

Quindi:

$$
|R^s(x)|
\le
\frac{|(x-x_i)(x-x_{i+1})|}{2}\,M_2^f.
$$

Osserviamo che per $x\in[x_i,x_{i+1}]$ vale:

$$
x-x_i\ge 0,\qquad x-x_{i+1}\le 0,
$$

perciò:

$$
|(x-x_i)(x-x_{i+1})|
=
(x-x_i)(x_{i+1}-x).
$$

Otteniamo dunque:

$$
|R^s(x)|
\le
\frac{(x-x_i)(x_{i+1}-x)}{2}\,M_2^f.
$$

---

#### Massimo del termine geometrico

Studiamo la funzione

$$
\phi(x)=(x-x_i)(x_{i+1}-x)
$$

nell’intervallo $[x_i,x_{i+1}]$.

Essa è una parabola concava con massimo nel punto medio:

$$
\tilde x=\frac{x_i+x_{i+1}}{2}.
$$

Il valore massimo vale:

$$
\phi(\tilde x)
=
\left(\frac{x_{i+1}-x_i}{2}\right)^2
=
\frac{(x_{i+1}-x_i)^2}{4}.
$$

Sostituendo nella stima precedente:

$$
|R^s(x)|
\le
\frac{1}{2}\cdot\frac{(x_{i+1}-x_i)^2}{4}\,M_2^f
=
\frac{(x_{i+1}-x_i)^2}{8}\,M_2^f.
$$

Quindi:

$$
\boxed{
|R^s(x)|
\le
\frac{(x_{i+1}-x_i)^2}{8}\,M_2^f
\qquad x\in[x_i,x_{i+1}]
}
$$

---

#### Caso di nodi equispaziati

Se i nodi sono equispaziati, cioè

$$
x_{i+1}-x_i=h
$$

per ogni $i$, allora la stima si semplifica in:

$$
\boxed{
|R^s(x)|
\le
\frac{h^2}{8}\,M_2^f
\qquad \forall x\in[a,b]
}
$$

---

#### Interpretazione della stima

Questa formula mostra che:

$$
|R^s(x)|=\mathcal O(h^2).
$$

Quindi l’errore dell’interpolazione lineare a tratti decresce quadraticamente con la distanza tra i nodi.

In particolare:

- dimezzando la distanza $h$ tra i nodi,
- l’errore si riduce di circa un fattore 4.

---

#### Perché non compare il fenomeno di Runge

A differenza dell’interpolazione polinomiale globale:

- ogni errore locale dipende solo dalla lunghezza del singolo intervallo;
- non compare alcun polinomio nodale globale che possa oscillare molto;
- l’errore è controllato uniformemente da $h^2$.

Per questo motivo l’interpolazione lineare a tratti è **stabile** e non può manifestare il fenomeno di Runge.

---

### Ripasso $-$ Resto dell’interpolazione lineare a tratti

Consideriamo una partizione dell’intervallo $[a,b]$ data dai nodi

$$
a=x_0<x_1<\dots<x_{m+1}=b
$$

e definiamo i sottointervalli

$$
I_i=[x_i,x_{i+1}], \qquad i=0,\dots,m.
$$

Supponiamo di conoscere i valori della funzione

$$
y_i=f(x_i), \qquad i=0,\dots,m+1
$$

con

$$
f:[a,b]\to\mathbb R, \qquad f\in C^2([a,b]).
$$

L’interpolante lineare a tratti è la funzione $s(x)$ definita, su ciascun sottointervallo $I_i$, come la retta passante per i punti consecutivi $(x_i,y_i)$ e $(x_{i+1},y_{i+1})$:

$$
s(x)=y_i+\frac{y_{i+1}-y_i}{x_{i+1}-x_i}(x-x_i),
\qquad x\in I_i.
$$

Questa funzione è continua su tutto $[a,b]$, ma è soltanto **lineare a tratti**: su ogni sottointervallo è un polinomio di grado 1, mentre globalmente non è un unico polinomio.

---

#### Formula del resto locale

Per studiare quanto bene $s(x)$ approssima $f(x)$, fissiamo un intervallo $I_i=[x_i,x_{i+1}]$ e consideriamo l’errore

$$
R^s(x)=f(x)-s(x), \qquad x\in[x_i,x_{i+1}].
$$

Applicando la formula del resto dell’interpolazione polinomiale al caso di interpolazione su **due nodi** ($x_i$ e $x_{i+1}$), otteniamo:

$$
R^s(x)=\frac{(x-x_i)(x-x_{i+1})}{2}\,f''(\xi_i),
\qquad \xi_i\in[x_i,x_{i+1}].
$$

Questa formula mostra che l’errore locale dipende:

$$
\text{dalla curvatura di }f \quad (\text{tramite }f'')
$$

e

$$
\text{dalla posizione di }x\text{ nel sottointervallo}.
$$

---

#### Maggiorazione dell’errore

Passando al valore assoluto:

$$
|f(x)-s(x)|
=
\left|
\frac{(x-x_i)(x-x_{i+1})}{2}f''(\xi_i)
\right|.
$$

Poiché $f\in C^2([a,b])$, la derivata seconda è continua e quindi limitata. Possiamo definire

$$
M_2^f=\max_{x\in[a,b]}|f''(x)|.
$$

Da cui segue:

$$
|f(x)-s(x)|
\le
\frac{|(x-x_i)(x-x_{i+1})|}{2}M_2^f.
$$

---

#### Massimo del termine geometrico

Per $x\in[x_i,x_{i+1}]$, il prodotto

$$
(x-x_i)(x_{i+1}-x)
$$

è una parabola concava che assume massimo nel punto medio del sottointervallo:

$$
x=\frac{x_i+x_{i+1}}{2}.
$$

Il valore massimo è

$$
\max_{x\in[x_i,x_{i+1}]}
(x-x_i)(x_{i+1}-x)
=
\frac{(x_{i+1}-x_i)^2}{4}.
$$

Sostituendo nella stima precedente otteniamo:

$$
|f(x)-s(x)|
\le
\frac{(x_{i+1}-x_i)^2}{8}M_2^f,
\qquad x\in[x_i,x_{i+1}].
$$

---

#### Stima globale sull’intervallo

Definiamo

$$
h=\max_{i=0,\dots,m}(x_{i+1}-x_i),
$$

cioè la lunghezza massima dei sottointervalli della partizione.

Allora per ogni $x\in[a,b]$ vale la stima globale:

$$
|f(x)-s(x)|
\le
\frac{h^2}{8}M_2^f.
$$

Questa è la stima fondamentale dell’errore per l’interpolazione lineare a tratti.

---

#### Caso di nodi equispaziati

Se i nodi sono scelti uniformemente in $[a,b]$, allora

$$
x_i=a+i\,h,
\qquad i=0,\dots,m+1,
$$

con passo costante

$$
h=\frac{b-a}{m+1}.
$$

La stima dell’errore diventa:

$$
|f(x)-s(x)|
\le
\frac{(b-a)^2}{(m+1)^2}\frac{M_2^f}{8},
\qquad \forall x\in[a,b].
$$

Facendo tendere il numero dei sottointervalli (e quindi il numero di nodi) all’infinito:

$$
m\to+\infty
\quad\Rightarrow\quad
h\to0
\quad\Rightarrow\quad
|f(x)-s(x)|\to0.
$$

Quindi:

$$
s(x)\to f(x)
\quad\text{uniformemente su }[a,b].
$$

---

#### Considerazioni finali

L’interpolazione lineare a tratti **non soffre del fenomeno di Runge**, perché l’errore dipende solo dalla dimensione locale degli intervalli e non da oscillazioni globali di un polinomio di alto grado.

Inoltre:

$$
\text{più piccoli sono i sottointervalli} \;\Rightarrow\; \text{più accurata è l’approssimazione.}
$$

Il limite principale è che la funzione interpolante $s(x)$, pur essendo continua, **non è derivabile nei nodi** $x_i$: in ciascun nodo esistono in generale derivata destra e derivata sinistra diverse.

Di conseguenza:

$$
s\in C^0([a,b]),
\qquad
s\notin C^1([a,b]).
$$

Questo motiva l’introduzione di interpolanti più regolari, come le **spline cubiche**, che mantengono la struttura a tratti ma migliorano la regolarità.

---

## Interpolazione con Funzioni Spline

Per superare i limiti dell’interpolazione lineare a tratti (continua ma non derivabile nei nodi) si introducono le **funzioni spline**, che permettono di costruire interpolanti a tratti più regolari.

Sia data una partizione dell’intervallo $[a,b]$:

$$
a=x_0<x_1<\dots<x_{m+1}=b
$$

e fissato un grado $n$.

Una **spline di grado $n$** relativa a questa partizione è una funzione $s:[a,b]\to\mathbb R$ tale che, su ciascun sottointervallo

$$
I_i=[x_i,x_{i+1}], \qquad i=0,\dots,m,
$$

la restrizione di $s$ a $I_i$ sia un polinomio di grado al più $n$:

$$
s|_{I_i}=s_i.
$$

Quindi una spline è una funzione **polinomiale a tratti**, composta da $m+1$ polinomi distinti:

$$
s_0,\dots,s_m.
$$

---

### Condizioni di regolarità

Affinché il polinomio a tratti sia una vera spline, non basta che sia definito a pezzi: i vari polinomi devono raccordarsi in modo regolare nei nodi interni.

Si richiede infatti che

$$
s\in C^{\,n-1}([a,b]),
$$

cioè che la funzione abbia derivate continue fino all’ordine $n-1$ su tutto l’intervallo.

Questo significa che, per ogni nodo interno $x_{i+1}$, devono coincidere i valori delle derivate dei due polinomi adiacenti:

$$
\begin{cases}
s_i(x_{i+1})=s_{i+1}(x_{i+1})\\
s_i'(x_{i+1})=s_{i+1}'(x_{i+1})\\
s_i''(x_{i+1})=s_{i+1}''(x_{i+1})\\
\vdots\\
s_i^{(n-1)}(x_{i+1})=s_{i+1}^{(n-1)}(x_{i+1})
\end{cases}
\qquad i=0,\dots,m-1
$$

Queste condizioni garantiscono che la spline sia liscia nei punti di raccordo.

---

### Interpretazione geometrica

Un generico polinomio a tratti può presentare “spigoli” nei nodi, cioè punti in cui la derivata cambia bruscamente.

Le spline costituiscono il sottoinsieme dei polinomi a tratti che **raccordano correttamente i vari pezzi**, imponendo continuità non solo della funzione, ma anche delle sue derivate.

In altre parole:

$$
\text{Spline} = \text{Polinomio a tratti + Regolarità nei raccordi}
$$

---

### Caso importante: spline cubiche

Il caso più utilizzato in pratica è quello delle **spline cubiche**, cioè spline di grado 3.

In questo caso ogni tratto è un polinomio cubico:

$$
s_i(x)=a_{0i}+a_{1i}x+a_{2i}x^2+a_{3i}x^3
$$

e si richiede:

$$
s\in C^2([a,b]).
$$

Quindi nei nodi interni devono essere continue:

- la funzione,
- la derivata prima,
- la derivata seconda.

Le spline cubiche rappresentano un ottimo compromesso tra:

- semplicità computazionale,
- regolarità,
- accuratezza dell’approssimazione.

---

### Numero di parametri di una spline

Ogni polinomio $s_i$ di grado $n$ dipende da $n+1$ coefficienti:

$$
s_i(x)=a_{0i}+a_{1i}x+\dots+a_{ni}x^n.
$$

Poiché ci sono $m+1$ intervalli, il numero totale iniziale di coefficienti è:

$$
(n+1)(m+1).
$$

---

#### Vincoli di raccordo

Nei $m$ nodi interni bisogna imporre la continuità delle derivate fino all’ordine $n-1$.

Per ogni nodo interno ci sono quindi $n$ condizioni:

$$
\text{continuità di }s,s',\dots,s^{(n-1)}.
$$

Essendo i nodi interni esattamente $m$, il numero totale di vincoli di raccordo è:

$$
nm.
$$

Pertanto i gradi di libertà residui diventano:

$$
(n+1)(m+1)-nm=n+m+1.
$$

---

#### Condizioni di interpolazione

Se vogliamo che la spline interpoli i dati

$$
(x_i,y_i), \qquad i=0,\dots,m+1,
$$

dobbiamo imporre:

$$
s(x_i)=y_i
\qquad \forall i=0,\dots,m+1.
$$

Queste sono $m+2$ condizioni aggiuntive.

Sottraendole ai gradi di libertà residui otteniamo:

$$
n+m+1-(m+2)=n-1.
$$

---

#### Conseguenza fondamentale

Dopo aver imposto:

- regolarità nei nodi,
- interpolazione dei dati,

rimangono ancora

$$
n-1
$$

gradi di libertà da fissare.

Questo significa che:

> **Le sole condizioni di interpolazione e regolarità non bastano a determinare univocamente una spline di grado $n$.**

Servono quindi **ulteriori condizioni al bordo**.

---

### Caso delle spline cubiche

Per spline cubiche ($n=3$) rimangono:

$$
n-1=2
$$

gradi di libertà.

Occorrono quindi **due condizioni aggiuntive**, tipicamente imposte agli estremi $a$ e $b$.

Le più comuni sono:

- **Spline naturale**

$$
s''(a)=0,\qquad s''(b)=0
$$

- **Spline completa (clamped)**

$$
s'(a)=f'(a),\qquad s'(b)=f'(b)
$$

- **Spline periodica**, se il problema ha struttura ciclica.

---

### Idea chiave da ricordare

L’interpolazione spline mantiene i vantaggi dell’interpolazione a tratti:

- evita polinomi globali di alto grado,
- non soffre del fenomeno di Runge,

ma produce anche una funzione molto più regolare della semplice spezzata.

In particolare:

$$
\text{Spline cubica} =
\text{Interpolante a tratti regolare, stabile e molto usato in pratica.}
$$

---

#### Ripasso: Interpolazione con Funzioni Spline

Siano dati i punti di interpolazione

$$
(x_i,y_i), \qquad i=0,\dots,m+1,
$$

con nodi ordinati

$$
x_0<x_1<\dots<x_{m+1}.
$$

Fissato un grado $n\ge 1$, vogliamo costruire una funzione spline $s(x)$ di grado $n$ relativa alla partizione individuata dai nodi, tale che

$$
s(x_i)=y_i,
\qquad i=0,\dots,m+1.
$$

L’obiettivo è quindi determinare una funzione polinomiale a tratti che interpoli tutti i dati assegnati e che sia sufficientemente regolare nei punti di raccordo.

---

#### Ripasso: Caso delle spline cubiche

Il caso più importante in applicazioni numeriche è quello delle **spline cubiche**, cioè spline di grado

$$
n=3.
$$

In questo caso la spline cercata è una funzione $s(x)$ tale che, per ogni sottointervallo

$$
I_i=[x_i,x_{i+1}], \qquad i=0,\dots,m,
$$

la restrizione

$$
s_i=s|_{I_i}
$$

sia un polinomio di grado al più 3.

Quindi ogni tratto ha la forma:

$$
s_i(x)=a_i+b_i x+c_i x^2+d_i x^3.
$$

---

### Condizioni che deve soddisfare una spline cubica

La spline cubica deve rispettare simultaneamente tre famiglie di condizioni.

1. Anzitutto, su ogni intervallo deve essere un polinomio cubico:

$$
s_i\in\mathbb P_3,
\qquad i=0,\dots,m.
$$

2. Inoltre deve essere regolare nei nodi interni, cioè appartenere a $C^2([a,b])$.
    Questo significa che nei punti di raccordo devono coincidere valore, derivata prima e derivata seconda dei polinomi adiacenti:

    $$
    \begin{cases}
    s_i(x_{i+1})=s_{i+1}(x_{i+1})\\
    s_i'(x_{i+1})=s_{i+1}'(x_{i+1})\\
    s_i''(x_{i+1})=s_{i+1}''(x_{i+1})
    \end{cases}
    \qquad i=0,\dots,m-1.
    $$

3. Infine deve interpolare i dati assegnati:

    $$
    s(x_i)=y_i,
    \qquad i=0,\dots,m+1.
    $$

---

#### Gradi di libertà residui

Anche imponendo tutte le condizioni precedenti, una spline cubica **non è ancora univocamente determinata**.

Infatti, dal conteggio dei gradi di libertà, rimangono ancora:

$$
3-1=2
$$

parametri liberi.

Questo significa che:

> le condizioni di interpolazione e di raccordo non bastano da sole a determinare un’unica spline cubica.

Sono necessarie **due condizioni aggiuntive al bordo** per chiudere il problema.

---

#### Condizioni al bordo

Le due condizioni mancanti vengono generalmente imposte agli estremi dell’intervallo e determinano il tipo di spline cubica utilizzata.

Una scelta molto comune è la **spline naturale**, definita imponendo:

$$
s''(x_0)=0,
\qquad
s''(x_{m+1})=0.
$$

Questa scelta forza la spline ad avere curvatura nulla agli estremi.

Altre possibilità sono:

$$
s'(x_0)=\alpha,\qquad s'(x_{m+1})=\beta
$$

(spline completa o clamped),

oppure condizioni periodiche se il problema lo richiede.

---

#### Risoluzione pratica

Tutte le condizioni viste:

- interpolazione,
- continuità di $s$,
- continuità di $s'$,
- continuità di $s''$,
- condizioni al bordo,

si traducono in un **sistema lineare quadrato** nelle incognite che descrivono i coefficienti dei polinomi cubici.

Risolvendo tale sistema si ottiene in modo univoco la spline cubica interpolante.

---

### Costruzione della spline cubica interpolante

Per costruire una spline cubica interpolante si rappresenta ciascun tratto della spline su ogni intervallo $[x_i,x_{i+1}]$ mediante un polinomio cubico espresso in forma locale rispetto al nodo sinistro dell’intervallo:

$$
s_i(x)=\alpha_i+\beta_i(x-x_i)+\gamma_i(x-x_i)^2+\delta_i(x-x_i)^3,
\qquad i=0,\dots,m
$$

Questa rappresentazione è preferibile rispetto alla forma canonica del polinomio perché semplifica notevolmente i calcoli delle derivate e l’imposizione delle condizioni di raccordo tra intervalli consecutivi. Ogni tratto della spline dipende quindi da quattro coefficienti incogniti:

$$
\alpha_i,\beta_i,\gamma_i,\delta_i
\qquad i=0,\dots,m
$$

L’obiettivo è determinare tali coefficienti imponendo le condizioni di interpolazione e di regolarità della spline.

#### 1. Determinazione del coefficiente $\alpha_i$

Poiché la spline deve interpolare i dati assegnati, si richiede che:

$$
s_i(x_i)=y_i
$$

Sostituendo $x=x_i$ nella forma locale del polinomio si ottiene immediatamente:

$$
\alpha_i=y_i
$$

Questo significa che il termine costante di ciascun tratto coincide con l’ordinata del nodo iniziale dell’intervallo.

#### 2. Derivate della spline locale

Per imporre le condizioni di raccordo servono anche derivata prima e seconda di ciascun tratto:

$$
s_i'(x)=\beta_i+2\gamma_i(x-x_i)+3\delta_i(x-x_i)^2
$$

$$
s_i''(x)=2\gamma_i+6\delta_i(x-x_i)
$$

Introduciamo inoltre la quantità:

$$
h_i=x_{i+1}-x_i
$$

che rappresenta la lunghezza dell’intervallo $[x_i,x_{i+1}]$.

#### 3. Condizioni di interpolazione e raccordo

Imponendo che il tratto $s_i$ interpoli anche l’estremo destro dell’intervallo si ottiene:

$$
s_i(x_{i+1})=y_{i+1}
$$

ossia

$$
y_i+\beta_i h_i+\gamma_i h_i^2+\delta_i h_i^3=y_{i+1}
$$

Inoltre, per garantire continuità di derivata prima e seconda nei nodi interni, si richiede:

$$
s_i'(x_{i+1})=s_{i+1}'(x_{i+1})
$$

$$
s_i''(x_{i+1})=s_{i+1}''(x_{i+1})
$$

che diventano rispettivamente:

$$
\beta_i+2\gamma_i h_i+3\delta_i h_i^2=\beta_{i+1}
$$

$$
2\gamma_i+6\delta_i h_i=2\gamma_{i+1}
$$

Pertanto, per ogni intervallo si ottiene il sistema di relazioni:

$$
\begin{cases}
y_i+\beta_i h_i+\gamma_i h_i^2+\delta_i h_i^3=y_{i+1}\\[4pt]
\beta_i+2\gamma_i h_i+3\delta_i h_i^2=\beta_{i+1}\\[4pt]
2\gamma_i+6\delta_i h_i=2\gamma_{i+1}
\end{cases}
$$

Queste equazioni legano tra loro i coefficienti dei polinomi dei vari intervalli.

#### 4. Sistema lineare risultante

Le relazioni precedenti permettono, dopo opportune sostituzioni algebriche, di ridurre il problema alla risoluzione di un sistema lineare nelle incognite residue (tipicamente nei coefficienti legati alle derivate seconde nei nodi). Tale sistema ha struttura particolare — spesso tridiagonale — e può essere risolto efficientemente con algoritmi numerici dedicati.

#### 5. Necessità di condizioni aggiuntive

Le condizioni viste finora non sono ancora sufficienti per determinare univocamente la spline cubica: rimangono infatti **due gradi di libertà**. Per eliminare questa indeterminazione è necessario imporre due condizioni supplementari ai bordi dell’intervallo.

A seconda della scelta di queste condizioni si ottengono diverse tipologie di spline cubiche:

1. **Spline cubica naturale**, in cui si impone:

    $$
    s''(x_0)=0,\qquad s''(x_{m+1})=0
    $$

    ossia curvatura nulla agli estremi.

2. **Spline cubica periodica**, utilizzata quando i dati rappresentano fenomeni ciclici, imponendo continuità periodica delle derivate agli estremi.

3. **Spline cubica not-a-knot**, spesso adottata nelle librerie numeriche standard, che impone una condizione di regolarità aggiuntiva sui primi e ultimi intervalli trattandoli come se il primo e l’ultimo nodo interno non fossero veri punti di raccordo.

---

#### Osservazione finale

Le spline cubiche rappresentano uno degli strumenti più usati nell’interpolazione numerica perché combinano:

$$
\text{accuratezza locale}
\quad+\quad
\text{regolarità globale}
\quad+\quad
\text{stabilità numerica}.
$$

Rispetto all’interpolazione polinomiale globale:

- evitano il fenomeno di Runge,
- non richiedono polinomi di grado elevato,
- producono funzioni lisce e derivabili fino al secondo ordine.

---







### Teorema delle spline cubiche a curvatura minima

Una proprietà fondamentale delle spline cubiche interpolanti è che possono essere interpretate come le curve **più “dolci” possibile** tra tutte quelle che interpolano gli stessi dati.  

In termini geometrici, ciò significa che la spline cubica tende a evitare oscillazioni inutili e realizza la curva con **curvatura complessiva minima**.

Più precisamente, tra tutte le funzioni

$$
f\in C^2([a,b])
$$

che interpolano i punti assegnati

$$
(x_i,y_i),\qquad i=0,\dots,m+1
$$

e che soddisfano le stesse condizioni al bordo della spline (naturale, vincolata oppure periodica), la spline cubica interpolante $s(x)$ è quella che minimizza il funzionale

$$
\int_a^b (s''(x))^2\,dx
$$

nel senso che vale:

$$
\boxed{
\int_a^b (s''(x))^2\,dx \le \int_a^b (f''(x))^2\,dx
}
$$

per ogni altra funzione interpolante ammessa $f$, con uguaglianza **solo** nel caso in cui

$$
f=s
$$

Questo risultato giustifica formalmente l’idea intuitiva secondo cui la spline cubica sia la curva interpolante “più regolare” o “meno piegata” possibile.

---

### Teorema sull’errore di interpolazione delle spline cubiche

Siano assegnati i dati

$$
(x_i,y_i),\qquad i=0,\dots,m+1
$$

con

$$
y_i=f(x_i)
$$

dove

$$
f:[a,b]\to\mathbb R,\qquad f\in C^2([a,b])
$$

e sia $s(x)$ la spline cubica interpolante associata a tali dati.

Indichiamo con

$$
h=\max_{i=0,\dots,m}(x_{i+1}-x_i)
$$

la massima ampiezza degli intervalli della partizione.

Allora vale la seguente stima dell’errore:

$$
\boxed{
|f(x)-s(x)|\le
h^{3/2}
\left(
\int_a^b (f''(x))^2\,dx
\right)^{1/2}
\qquad \forall x\in[a,b]
}
$$

Questa disuguaglianza mostra che l’errore di interpolazione dipende da due fattori:

1. Il primo è la **regolarità/curvatura della funzione originale**, misurata tramite l’integrale della derivata seconda al quadrato:

    $$
    \int_a^b (f''(x))^2\,dx
    $$

    che può essere visto come una costante dipendente dalla funzione da approssimare.

2. Il secondo è la **densità dei nodi**, rappresentata da $h$: più i nodi sono vicini, più piccolo sarà l’errore.

    In particolare, se si aumentano i punti di interpolazione mantenendoli nell’intervallo fissato $[a,b]$, allora:

    $$
    m\to+\infty
    \qquad\Longrightarrow\qquad
    h\to0
    $$

    e quindi:

    $$
    |f(x)-s(x)|\to0
    $$

    cioè la spline converge uniformemente alla funzione.

---

#### Approssimazione della derivata

Un risultato ancora più forte è che anche la derivata prima della spline approssima la derivata della funzione originale:

$$
\boxed{
|f'(x)-s'(x)|\le
h^{1/2}
\left(
\int_a^b (f''(x))^2\,dx
\right)^{1/2}
\qquad \forall x\in[a,b]
}
$$

Questo significa che, aumentando il numero dei nodi, non solo la spline approssima sempre meglio la funzione, ma riesce anche a riprodurne sempre meglio la **pendenza locale**.

In altre parole, con abbastanza punti la spline cubica non solo “passa vicino” al grafico della funzione, ma ne segue bene anche l’andamento delle tangenti.

---

#### Osservazione conclusiva

Questo comportamento rende le spline cubiche particolarmente potenti rispetto agli altri metodi di interpolazione visti finora.  
Infatti:

- l’interpolazione polinomiale globale può soffrire del fenomeno di Runge;
- l’interpolazione lineare a tratti non è derivabile nei nodi;
- la spline cubica invece fornisce una funzione regolare, stabile e con ottime proprietà di approssimazione sia sulla funzione sia sulla sua derivata.

Per questo motivo le spline cubiche rappresentano uno degli strumenti più importanti e utilizzati nell’interpolazione numerica.

---