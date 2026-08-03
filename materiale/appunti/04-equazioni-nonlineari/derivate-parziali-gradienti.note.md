
## Derivate parziali e gradiente

Quando si studiano le derivate in una variabile, si considera una funzione del tipo $f(x)$ e si analizza come cambia il valore della funzione al variare di $x$. La derivata misura quindi la **velocità di variazione della funzione rispetto a quella variabile**.

Nel caso delle funzioni di più variabili, ad esempio $f(x, y)$, la situazione si estende in modo naturale. Qui il valore della funzione dipende contemporaneamente da più grandezze.

Possiamo immaginare $f(x, y)$ come una **superficie nello spazio tridimensionale**: a ogni coppia $(x, y)$ corrisponde un valore $z = f(x, y)$, cioè un’altezza.

A questo punto è importante capire come la funzione varia al variare delle singole variabili. Se vogliamo studiare cosa succede modificando solo $x$, mantenendo $y$ costante, utilizziamo la **derivata parziale rispetto a $x$**. Analogamente, per studiare la variazione rispetto a $y$, manteniamo $x$ costante.

Le derivate parziali si indicano con:

$$
\frac{\partial f}{\partial x} \quad \text{e} \quad \frac{\partial f}{\partial y}
$$

Dal punto di vista operativo, il calcolo è molto semplice: si deriva rispetto alla variabile scelta trattando tutte le altre come costanti.

Consideriamo ad esempio la funzione:

$$
f(x, y) = x^2 + 3xy + y^2
$$

Derivando rispetto a $x$ (trattando $y$ come costante) si ottiene:

$$
\frac{\partial f}{\partial x} = 2x + 3y
$$

Derivando rispetto a $y$ (trattando $x$ come costante) si ottiene:

$$
\frac{\partial f}{\partial y} = 3x + 2y
$$

Dal punto di vista intuitivo, $\frac{\partial f}{\partial x}$ rappresenta quanto cambia la funzione se ci muoviamo lungo la direzione orizzontale (asse $x$), mentre $\frac{\partial f}{\partial y}$ descrive la variazione lungo la direzione verticale (asse $y$). In altre parole, le derivate parziali **descrivono il comportamento della funzione lungo direzioni specifiche**.

Tuttavia, spesso non è sufficiente studiare una direzione alla volta. Se vogliamo capire in quale direzione la funzione cresce più velocemente, dobbiamo considerare tutte le direzioni contemporaneamente. Questo porta alla definizione di **gradiente**.

Il gradiente di una funzione è un vettore colonna che raccoglie tutte le derivate parziali:

$$
\nabla f(x, y) = \begin{pmatrix}
    \frac{\partial f}{\partial x} \\
    \frac{\partial f}{\partial y}
\end{pmatrix}
$$

Nel caso dell’esempio precedente, il gradiente è:

$$
\nabla f(x, y) = (2x + 3y,\; 3x + 2y)
$$

Il significato geometrico del gradiente è fondamentale. Se immaginiamo la funzione come una superficie, il gradiente in un punto indica **la direzione in cui la funzione cresce più rapidamente partendo da quel punto**. Inoltre, la lunghezza del vettore gradiente indica quanto rapidamente avviene questa crescita.

Possiamo visualizzare questo concetto pensando a una collina: la funzione rappresenta l’altezza del terreno, e il gradiente indica la direzione in cui la salita è più ripida. Se invece ci si muove nella direzione opposta al gradiente, si scende nel modo più rapido possibile.

Questo concetto è estremamente importante nel calcolo numerico. Molti algoritmi di ottimizzazione si basano proprio sull’uso del gradiente. Ad esempio, nel metodo del **gradient descent**, si parte da un punto iniziale e si aggiorna iterativamente la soluzione muovendosi nella direzione opposta al gradiente:

$$
x_{k+1} = x_k - \alpha \nabla f(x_k)
$$

dove $\alpha$ è un parametro che controlla la dimensione del passo.

In sintesi, le derivate parziali permettono di studiare come una funzione varia lungo singole direzioni, mentre il gradiente combina queste informazioni per descrivere il comportamento complessivo della funzione e individuare la direzione di variazione più significativa. Questi strumenti sono alla base di molti metodi numerici utilizzati per risolvere problemi di ottimizzazione e analisi di funzioni multivariate.

---

## Appunti presi a lezione: derivate parziali, gradiente e Jacobiano

Consideriamo una funzione scalare di due variabili:

$$
\begin{aligned}
f: \mathbb{R}^2 &\to \mathbb{R} \\
(x_1, x_2) &\mapsto f(x_1, x_2)
\end{aligned}
$$

Le **derivate parziali** misurano la variazione della funzione rispetto a una variabile, mantenendo fissa l’altra. Sono definite come:

$$
\frac{\partial f}{\partial x_1}(x_1, x_2) = \lim_{h \to 0} \frac{f(x_1 + h, x_2) - f(x_1, x_2)}{h}
$$

$$
\frac{\partial f}{\partial x_2}(x_1, x_2) = \lim_{h \to 0} \frac{f(x_1, x_2 + h) - f(x_1, x_2)}{h}
$$

Queste quantità rappresentano le pendenze della funzione nelle direzioni degli assi coordinati.

---

### Gradiente

Il **gradiente** di $f$ è il vettore che raccoglie tutte le derivate parziali ed è definito come:

$$
\nabla f(x_1, x_2) =
\begin{pmatrix}
\frac{\partial f}{\partial x_1}(x_1, x_2) \\
\frac{\partial f}{\partial x_2}(x_1, x_2)
\end{pmatrix}
\in \mathbb{R}^2
$$

Il gradiente generalizza il concetto di derivata prima alle funzioni di più variabili: indica la direzione di massima crescita della funzione e la sua intensità.

---

### Funzioni vettoriali

Per trattare sistemi di equazioni non lineari, è necessario considerare funzioni vettoriali del tipo:

$$
\begin{aligned}
F: \mathbb{R}^2 &\to \mathbb{R}^2 \\
(x_1, x_2) &\mapsto
\begin{pmatrix}
f_1(x_1, x_2) \\
f_2(x_1, x_2)
\end{pmatrix}
\end{aligned}
$$

In questo caso, ogni componente $f_i$ è una funzione scalare:

$$
f_1, f_2 : \mathbb{R}^2 \to \mathbb{R}
$$

e ciascuna di esse ha il proprio gradiente:

$$
\nabla f_1(x_1, x_2), \quad \nabla f_2(x_1, x_2) \in \mathbb{R}^2
$$

---

### Jacobiano

Per generalizzare il concetto di derivata alle funzioni vettoriali, si introduce lo **Jacobiano**, che è una matrice contenente tutte le derivate parziali delle componenti di $F$.

Nel caso $F : \mathbb{R}^2 \to \mathbb{R}^2$, lo Jacobiano è:

$$
J_F(x_1, x_2) =
\begin{pmatrix}
\frac{\partial f_1}{\partial x_1}(x_1, x_2) & \frac{\partial f_1}{\partial x_2}(x_1, x_2) \\
\frac{\partial f_2}{\partial x_1}(x_1, x_2) & \frac{\partial f_2}{\partial x_2}(x_1, x_2)
\end{pmatrix}
\in \mathbb{R}^{2 \times 2}
$$

Equivalentemente, lo Jacobiano può essere visto come la matrice che ha per righe i gradienti trasposti delle singole componenti:

$$
J_F(x_1, x_2) =
\begin{pmatrix}
\nabla f_1(x_1, x_2)^T \\
\nabla f_2(x_1, x_2)^T
\end{pmatrix}
$$

---

### Interpretazione

Lo Jacobiano rappresenta la migliore approssimazione lineare della funzione vettoriale $F$ in un punto, ed è l’analogo multidimensionale della derivata prima nel caso scalare.

Questo concetto è fondamentale per estendere metodi come quello di Newton al caso di sistemi non lineari.