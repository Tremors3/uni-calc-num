
$$
\newcommand{\tcr}[1]{\textcolor{red}{#1}}
\newcommand{\tcy}[1]{\textcolor{yellow}{#1}}
\newcommand{\tclg}[1]{\textcolor{lightgreen}{#1}}
\newcommand{\tclb}[1]{\textcolor{lightblue}{#1}}
$$

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

# (18) Lezione 08-04-2026 | s 253..268 | Ripasso; Implementazione metodo di Bisezione; Metodo di Newton

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

#### Nota sul costo computazionale (slide 259)

L'implementazione è pensata per ridurre al minimo necessario il costo computazionale.

Un'operazione non lineare (come ad esempio una funzione come sin/cos/...) può essere tradotta in un polinomio che approssima il risultato reale della funzione.

Così facendo riusciamo ad ottenere una stima del costo computazionale del metodo. Infatti sarà la funzione scelta che comprenderà la maggior parte del costo computazionale. Dobbiamo considerare la funzione $f()$ come una sequenza di passi elementari che hanno un certo costo.

$$
\mathcal{O}(n \cdot \text{costo computazionale di }f)
$$

Dunque per aumentare l'efficienza del metodo dobbiamo cercare di chiamare il minor numero di volte possibile la funzione interessata.

---

### Metodo di Regula Falsi

Ha proprietà simili al metodo di bisezione. I metodi di bisezione e regula falsi si dicono **metodi dicotomici**.

Il metodo di regula falsi, invece del punto medio dell'intervallo, definisce $c_k$ come il punto di intersezione tra l'asse delle ascisse e la retta che passa per i punti del piano $(a_k, f(a_k)),\;(b_k,f(b_k)) $. La relativa formula è:

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

Aggiungiamo una cifra decimale ogni 3 o 4 iterate. Se vogliamo allora un numero ingente di cifre decimali dovremmo iterare molto tempo.

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

- Convergenza quadratica $p=2$

    $$
    \lim_{k\to\infin} \frac{|x_{k+1}-x_*|}{|{x_k-x_*}|^2} = C
    $$

- Convergenza lineare $p = 1, C \in (0,1)$

    $$
    \lim_{k\to\infin} \frac{|x_{k+1}-x_*|}{|{x_k-x_*}|} = C
    $$

    Il metodo di bisezione fa parte di questa categoria.

- Convergenza superlineare $p = 1, C = 0$

    $$
    \lim_{k\to\infin} \frac{|x_{k+1}-x_*|}{|{x_k-x_*}|} = 0
    $$

---

### Metodo di Newton (delle Tangenti)

Il metodo di bisezione non può essere applicato a delle funzioni in più incognite ed in più equazioni (sistemi). Viene in soccorso il metodo di Newton.

Dato un punto, il nuovo punto è l'intersezione tra l'asse delle ascisse e la retta tangente di coordinate $(x_k, f(x_k))$ nell'intervallo $[a, b]$.

Possiamo ottenere la formula dal ragionamento geometrico. Dobbiamo ricordare la formula della tangente del grafico della funzione $f$ nel suo punto di coordinate $(x_k, f(x_k))$.

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

# (19) Lezione 13-04-2026 | s 268..273 | Continuo metodo di Newton

### Metodo di Newton

#### Risultato analisi di convergenza del metodo

Slide 269. Il metodo converge se applicato ad un'intervallo in cui è rispettata una delle quattro regole spiegate sulle slides. In generale serve che la funzione, nell'intervallo scelto, debbe essere localmente monotona e deve contenere una radice. Oltre a rispettare le assunzioni già viste (es. $f'(x) \ne 0$). Vedi slides per chiarimento.

#### Dimostrazione convergenza quadratica Newton

**Hp.** $f \in C^2([a,b]), \quad f'(x) \ne 0 \; \forall x\in[a,b], f(a)\cdot f(b) < 0, x_0 \in [a,b]$

$$\begin{aligned}
x_{k+1} &= x_k - \frac{f(x_k)}{f'(x_k)} \\
&\Rightarrow \nexists x_*\in[a,b] : f'(x_*) = 0, \quad \lim_{k\to\infin} x_k = x_*
\end{aligned}$$

$$

$$

**Th.** Vogliamo far vedere che:

$$
\lim_{k\to\infin} \frac{|x_{k+1} - x_*|}{|x_k - x_*|^2} = C \in\R
$$

Dimostrabile con il teorema e sviluppi di Taylor. Sviluppo di taylor centrato in $x_*$:

$$
f(x) = f(x_k) + f'(x_k)(x - x_k) + \frac{1}{2}f''(\xi_k)(x-x_k)^2
$$

Sappiamo che il valore $\xi_k \in [x,x_k]$. In particolare utilizziamo questa formula ponendo $x = x_*$:

$$
\underbrace{f(x)}_{0} = f(x_k) + \underbrace{f'(x_k)}_{\ne 0}(x_* - x_k) + \frac{1}{2}f''(\xi_k)(x_*-x_k)^2
$$

Quindi ora $\xi_k \in [x_*,x_k]$. Cominciamo ad osservare che il punto $x_*$ non è un punto qualsiasi dell'intervallo ma una radice. Quindi $x_* = 0$:

$$
0 = \underbrace{\frac{f(x_k)}{f'(x_k)} - x_k}_{- x_{*}} + x_* + \frac{1}{2}\frac{f''(\xi_k)}{f'(x_k)}(x_k - x_*)^2
$$

quindi:

$$
0 = x_* - x_k  + \frac{1}{2}\frac{f''(\xi_k)}{f'(x_k)}(x_k - x_*)^2
$$

dividiamo tutto per il quadrato:

$$
0 = \frac{x_* - x_k}{(x_k - x_*)^2} + \frac{1}{2}\frac{f''(\xi_k)}{f'(x_k)}
$$

Siamo praticamente arrivati. Adesso ricaviamo il primo quoziente:

$$
\frac{x_* - x_k}{(x_k - x_*)^2} = + \frac{1}{2}\frac{f''(\xi_k)}{f'(x_k)}
$$

Passiamo poi al valore assoluto ad entrambi i lati dell'uguaglianza:

$$
\frac{|x_* - x_k|}{|x_k - x_*|^2} = + \frac{1}{2}\frac{|f''(\xi_k)|}{|f'(x_k)|}
$$

Passiamo al limite ad entrambi i lati:

$$
\lim_{k\to\infin} \frac{|x_* - x_k|}{|x_k - x_*|^2} =  \lim_{k\to\infin} \frac{1}{2}\frac{|f''(\xi_k)|}{|f'(x_k)|}
$$

Dato che $x_* < \xi_k < x_k$ e abbiamo che $x_k \to x_*$ allora abbiamo che

$$
\lim_{k\to\infin} \xi_k = x_*
$$

Allora:

$$
\lim_{k\to\infin} \frac{|x_* - x_k|}{|x_k - x_*|^2} =
\lim_{k\to\infin} \frac{1}{2}\frac{|f''(\xi_k)|}{|f'(x_k)|}
= \underbrace{\boxed{\frac{1}{2}\frac{|f''(\xi_k)|}{|f'(x_k)|}}}_{C} \in\R
$$

In laboratorio abbiamo notato che Newton batte i metodi dicotomici in termini di velocità di convergenza. Con questa dimostrazione siamo arrivati alla conclusione che Newton converge quadraticamente. Rispetto ai metodi dicotomici che convergono linearmente.

#### Condizionamento problemi della ricerca degli zeri

Quanto il residuo riesce a darci informazione riguardo alla lontananza dalla soluzione.

Se riusciamo a trovare un punto $\tilde x$ (una delle $x_k$ calcolate) come approssimazione se il valore della funzione in quel punto sta sotto una certa tolleranza $\delta$.

$$
|f(\tilde x)| \le \delta \qquad(\text{tol = 1e-4})
$$

Vogliamo trovare un valore per cui:

$$
f(x_*) = 0 \qquad \tilde x \approx x_*
$$

Ma non è possibile trovare $x_*$, dobiamo accontentarci di un valore di $x$ che per la funzione ci da qualcosa di piccolo ma non proprio 0. Una approssimazione.

La domanda è:

$$
|f(\tilde x)| \le \delta \quad\xRightarrow{?}\quad x \approx x_*
$$

Questa condizione garantisce effettivamente che ci troviamo vicino ad una radice? Dipende se alcune condizioni sulla funzione $f$ sono rispettate.

$$
f'(x_*) = \lim_{x\to x_*} \frac{f(x) - f(x_*)}{x - x_*}
$$

Supponiamo che per tutte le $x$ "vicine" a $x_*$, possiamo approssimare la derivata prima col rapporto incrementale:

$$
f'(x_*) \approx \frac{f(x) - f(x_*)}{x - x_*} \qquad x \text{ "vicine" a } x_*
$$

L'idea è quella di moltiplicare e dividere entrambi i lati dell'uguaglianza per $f'(x_*),\; (x - x_*)$:

$$
x - x_* \approx \frac{f(x) - \overbrace{f(x_*)}^{0}}{f'(x_*)}
= \frac{f(x)}{f'(x_*)}
$$

Questa circa uguaglianza mette in relazione la distanza di un punto dalla radice, con il rapporto tra il valore della funzione in quel punto diviso il valore della derivata prima di $f$ in $x_*$.

$$
|x - x_*| \approx \frac{|f(x)|}{|f'(x_*)|} \le \frac{\delta}{|f'(x_*)|} = \Big(\tcy{\frac{1}{|f'(x_*)|}}\Big) \cdot \delta
$$

Quel punto $x$ quanto è vicino ad $x_*$? Circa come il valore della funzione in $\tilde x$ diviso la derivata prima di $f$ in $x_*$.

Non è vero quindi in generale che se il valore della funzione è piccolo la distanza della radice sia altrattanto piccola. Perchè del fattore di amplificazione presente al denominatore.

$$
\frac{1}{|f'(x_*)|}
$$

Quando il residuo è piccolo non è detto che la distanza sia altrettanto piccola.

**Visione Grafica slide 251 del mal condizionamento.**

Il problema è mal condizionato quando $|f'(x_*)|$ **è piccolo** perchè fattore di aplificazione che sta al denominatore. Quando il valore della derivata prima di $f$ in $x_*$ è piccola? **Quando la funzione è molto piatta (quasi parallela all'asse delle ascisse)** nel punto dell'intersezione con l'asse; ma non completamente altrimenti la derivata prima avrebbe valore zero.

Più la funzione è "appiattita" nel punto dell'intersezione con l'asse delle ascisse. Più il valore della derivata sarà grande ed il problema mal condizionato.

---

### Metodo delle Secanti

Variante del metodo di Newton. Invece della derivata prima utilizziamo il rapporto incrementale.

$$
x_{k+1} = x_l - \frac{f(x_k)}{\frac{f(x_k) - f(x_{k-1})}{x_k - x_{k-1}}}
$$

Ha una formula di ricorrenza a tre termini:
- Iterata nuova
- Iterata precedente
- Iterata ancora precedente

Il nuovo punto è l'intersezione tra l'asse delle ascisse e la retta per i punti di coordinate $(x_{k-1}, f(x_{k-1}), (x_k, f(x_k)))$.

- Può essere applicabile a funzioni anche solo continue dato che nella formula non compare la derivata prima al denominatore.
- La sua velocità è sublineare.

---

### Estensione ai sistemi di equazioni nonlineari (Newton e Secanti)

Esteso al caso in cui abbiamo sistemi di equazioni non lineari in altrettante incognite (prenderemo tante incognite quante saranno le equazioni non lineari).

#### Derivate parziali

Quando uno ha una funzione in $n$ variabili. Es $n = 2$:

$$
f(x_1, x_2) = x_1^2 + x_2
$$

$$
\frac{\partial}{\partial x_1}f(x_1, x_2) = \text{Derivata parziale f rispetto ad } x_1 = 2x
$$

Calcolare la derivata rispetto solamente alla variabile $x_1$. Consideriamo la variabile $x_2$ come una costante, che non da constributo.

$$
\frac{\partial}{\partial x_2}f(x_1, x_2) = 1
$$

Relativo gradiente:

$$
\nabla f(x_1, x_2) = \begin{pmatrix}
\frac{\partial}{\partial x_1}f(x_1, x_2), &
\frac{\partial}{\partial x_2}f(x_1, x_2)
\end{pmatrix}
$$

Dobbiamo trovare il vettore $(x_1, \dots, x_n)$ tale che ciascuna funzione ad $n$ variabili si annulli (all'interno del vettore di funzioni).

---

# (20) Lezione 15-04-2026 | s 274.. | Estensione ai sistemi di equazioni nonlineari

Ripasso derivate parziali, gradienti, jacobiani:

$$\begin{aligned}
f:\R^2&\to\R \\
(x_1, x_2) &\to f(x_1, x_2)
\end{aligned}$$

$$
\frac{\partial f}{\partial x_1}(x_1, x_2) \lim_{h\to\infin}\frac{f(x_1 + h, x_2) - f(x_1, x_2)}{h}
$$

$$
\frac{\partial f}{\partial x_1}(x_1, x_2) \lim_{h\to\infin}\frac{f(x_1, x_2 + h) - f(x_1, x_2)}{h}
$$

Ed il rispettivo gradiente, come vettore colonna:

$$
\nabla f(x_1, x_2) = \begin{pmatrix}
\frac{\partial f}{\partial x_1}(x_1, x_2) \\
\frac{\partial f}{\partial x_2}(x_1, x_2)
\end{pmatrix}\in\R^2
$$

Aumentando la dimensione dello spazio, del dominio della funzione, possiamo parlare di gradiente di $f$. In questo primo passaggio abiamo aumentato lo spazio che contiene il dominio della funzione.

Ci serve considerare delle funzioni che sono definite come: 

$$\begin{aligned}
F:\R^2&\to\R^2 \\
(x_1, x_2)&\to\begin{pmatrix}f_1(x_1,x_2) \\ f_2(x_1,x_2)\end{pmatrix}
\end{aligned}$$

In questo caso avremo bisogno di due funzioni che definiscono le singole componenti del vettore immagine:

$$\begin{aligned}
f_1:\R^2\to\R &\quad\Rightarrow\quad \nabla f_1(x_1, x_2) \in\R^2\\
f_2:\R^2\to\R &\quad\Rightarrow\quad \nabla f_2(x_1, x_2) \in\R^2
\end{aligned}$$

Ciascuna di queste due funzioni avrà un graduente. Stiamo cercando un equivalente della derivata prima anche per funzioni che vanno da $\R^2\to\R^2$.

La definizoine di dello Jacoiano è una matrice che dipende da n variabili. In questo caso con due variabili:

$$\begin{aligned}
JF(x_1,x_2) &= \begin{pmatrix}\nabla f_1(x_1, x_2)^T \\ \nabla f_1(x_1, x_2)^T\end{pmatrix} \in\R^{2\times 2} \\
&=\begin{pmatrix}\frac{\partial f_1}{\partial x_1}f(x_1, x_2) & \frac{\partial f_1}{\partial x_2}f(x_1, x_2) \\ \frac{\partial f_2}{\partial x_1}f(x_1, x_2) & \frac{\partial f_2}{\partial x_2}f(x_1, x_2) \end{pmatrix}
\end{aligned}$$

---

### Esercizio suo gradienti in laboratorio

In laboratorio, abbiamo definito il campo F:

$$F(x) = \begin{pmatrix} 
L_1 \cos(x_1) + L_2 \cos(x_1 + x_2) - P_1 \\
L_1 \sin(x_1) + L_2 \sin(x_1 + x_2) - P_2
\end{pmatrix}$$

Proviamo a calcolare lo Jacobiano di questo vettore.

Gradiente della prima funzione:

$$\begin{aligned}
\frac{\partial f_1}{\partial x_1}(x_1, x_2) &= L_1\sin(x_1) - L_2\sin(x_1 + x_2) \\
\frac{\partial f_1}{\partial x_2}(x_1, x_2) &= - L_2\sin(x_1 + x_2)
\end{aligned}$$

Gradiente della seconda funzione:

$$\begin{aligned}
\frac{\partial f_2}{\partial x_1}(x_1, x_2) &= L_1\cos(x_1) - L_2\cos(x_1 + x_2) \\
\frac{\partial f_2}{\partial x_2}(x_1, x_2) &= - L_2\cos(x_1 + x_2)
\end{aligned}$$

Vogliamo trovare la coppia $x_1,x_2$ che ci consenta di annullare queste quantità.

---

Formula del metodo di newton aggiornata per funzionare su più dimensioni:

$$
d_k = -\frac{f(x_k)}{f'(x_k)} = - \underbrace{(f'(x_k))^{-1}}_{JF(x_k)^{-1}} \cdot \underbrace{f(x_k)}_{F(x^{(k)})}
$$

Riformuliamo la formula come:

$$\begin{aligned}
d^{(k)} &= - JF(x^{(k)})^{-1} \cdot F(x^{(k)}) \\
x^{(k+1)} &= x^{(k)} + d^{(k)}
\end{aligned}$$

Quando ho l'iterato k-esimo, è in realtà un vettore con n componenti.
Quindi $F(x^{(k)})$ si può calcolare ed è semplicemente un vettore di numeri. Mentre $JF(x^{(k)})$ è una matrice di numeri che posso calcolare.

Scritto in questo modo, il vettore $d^{(k)}$, è il vettore che risolve il sistema:

$$
JF(x^{(k)})\cdot d^{(k)} = - F(x^{(k)})
$$

E' la soluzione di un sistema lineare che ha come:
- $JF(x^{(k)})$: matrice dei coefficienti;
- $d^{(k)}$: vettore delle incognite;
- $F(x^{(k)})$: vettore dei termini noti.

---

#### Da sistema nonlineare a sistema lineare

Il sistema da cui siamo partiti $F(x) = 0$ è nonlineare.

Dato $x^{(0)}\in\R^2$:
$$ \text{for } k=0,1,\dots \\
\qquad JF(x^{k}), F(x^{k}) \\
\qquad\qquad\qquad\qquad d^{(k)} = - JF(x^{(k)})^{-1} \cdot F(x^{(k)}) \\
\qquad\qquad x^{(k+1)} = x^{(k)} + d^{(k)}
$$

Come visto. Ad ogni passo del metodo di Newton è richiesta la risoluzione di un sistema lineare.

---

#### Implemetazione del metodo di Newton per i sistemi di equazioni nonlineari

In laboratorio.

---

# (21) Lezione 20-04-2026 | s .. | Interpolazione

