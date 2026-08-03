
## Richiami di Algebra Lineare

Questa lezione introduce alcuni richiami di **algebra lineare** che saranno utilizzati nel corso di Calcolo Numerico. In particolare si lavorerà con **vettori e matrici a coefficienti reali**, cioè oggetti appartenenti agli spazi:

$$ \R^n \quad e \quad \R^{m\times n} $$

Nel contesto matematico del corso, quando si parla di **vettore nello spazio** $\R^m$ si intende implicitamente un **vettore colonna**, cioè un oggetto di dimensione:

$$ \R^{m\times 1} $$

mentre un **vettore riga** appartiene allo spazio

$$ \R^{1\times m} $$

È importante ricordare anche una differenza pratica tra matematica e programmazione. Nella notazione matematica classica gli indici di righe e colonne **partono da 1**, mentre nelle librerie di programmazione come **NumPy** gli indici **partono da 0**.

---

### Operazioni sui vettori

Consideriamo un vettore

$$ v \in \R^n $$

che può essere scritto nella forma

$$v = \begin{pmatrix}
    v_1 \\ \vdots \\ v_n
\end{pmatrix}$$

---

### Moltiplicazione per scalare

Dato uno scalare $\lambda \in \R$, la moltiplicazione scalare tra $\lambda$ e il vettore $v$ consiste nel moltiplicare **ogni componente del vettore per lo scalare**:

$$\lambda v = \begin{pmatrix}
    \lambda v_1 \\ \vdots \\ \lambda v_n
\end{pmatrix}$$

Questa operazione è definita **componente per componente**.

---

### Somma tra avettori

Se $v,w \in \R^n$, la loro somma è definita come

$$ v + w = \begin{pmatrix}
    v_1 + w_1 \\ \vdots \\ v_n + w_n
\end{pmatrix}$$

Anche questa operazione avviene **elemento per elemento**.

Per poter sommare due vettori è necessario che essi abbiano **la stessa dimensione**.

---

### Prodotto scalare

Il **prodotto scalare** tra due vettori $v,w\in\R^n$ è definito come

$$ \sum_{i=1}^n v_iw_i $$

cioè

$$ v_1w_1 + v_2w_2 + \dots + v_nw_n $$

Dal punto di vista computazionale il prodotto scalare richiede:

- $n$ **moltiplicazioni floating point**
- $n-1$ **somme floating point**

La complessità computazionale dell’operazione è quindi **lineare**, cioè

$$ O(n) $$

---

### Complessità computazionale

Nel confronto tra algoritmi non ci si basa soltanto sul **tempo di esecuzione**, perché questo dipende fortemente dall’architettura hardware e dall’implementazione.

Per questo motivo si utilizza la **complessità computazionale**, che misura il numero di operazioni necessarie in funzione della dimensione del problema.

Tempo di esecuzione e complessità sono comunque **proporzionali**, ma la complessità fornisce una misura **indipendente dalla macchina** su cui l’algoritmo viene eseguito.

---

### Struttura delle matrici e rappresentazione in memoria

Conoscere la **struttura di una matrice** può permettere di rappresentarla in memoria in modo molto più efficiente.

Ad esempio:

- una **matrice diagonale** può essere rappresentata semplicemente tramite il vettore contenente i suoi elementi diagonali;

- una **matrice triangolare** può essere memorizzata salvando soltanto gli elementi sopra o sotto la diagonale principale.

Questo tipo di rappresentazione riduce lo **spazio di memoria** necessario e spesso rende anche più efficienti le operazioni numeriche.

---

### Prodotto matriciale

Siano

$$ A\in\R^{m\times n} \quad\text{e}\quad x\in\R^{n\times 1} $$

Il **prodotto matriciale** tra $A$ e $x$ è definito come

$$ Ax $$

il risultato è un vettore appartenente allo spazio

$$ \R^{m\times 1} $$

Ogni elemento del vettore risultante è ottenuto come **prodotto scalare tra una riga della matrice e il vettore**.

In generale, il prodotto matriciale tra due matrici

$$ A\in\R^{m\times n}, \quad B\in\R^{n\times p} $$

produce una matrice

$$ C \in \R^{m\times p} $$

È importante ricordare che il prodotto matriciale **non è commutativo**, cioè in generale

$$ AB \ne BA $$

Prima di moltiplicare due matrici è quindi sempre necessario verificare che **le dimensioni siano compatibili**.

---

### Inversa di una matrice

Una matrice quadrata $A\in\R^{n\times n}$ si dice **invertibile** se esiste una matrice $A^{-1}$ tale che

$$ AA^{-1} = A^{-1}A = I $$

dove $I$ è la matrice identità.

Una proprietà importante è che per una matrice invertibile vale

$$ {(A^T)}^{-1} = {(A^{-1})}^T $$

Questo significa che **trasposizione e inversione possono essere applicate in qualsiasi ordine**.

La possibilità di invertire una matrice è strettamente legata al **determinante**. Una matrice quadrata è invertibile **se e solo se il suo determinante è diverso da zero**.

Il determinante può essere calcolato tramite procedure ricorsive, anche se in pratica si utilizzano algoritmi numericamente più efficienti.

---

### Autovalori e autovettori

Gli **autovalori** e gli **autovettori** sono proprietà fondamentali di una matrice quadrata.

Dato

$$ M\in\R^{n\times n} $$

un numero $\lambda$ è un **autovalore** se esiste un vettore non nullo $x$ tale che

$$ Mx = \lambda x $$

Gli autovalori possono essere interpretati come una sorta di **"carta di identità" della matrice**, perché descrivono proprietà strutturali profonde dell’operatore lineare rappresentato dalla matrice.

Da una matrice $n\times n$ si ottengono $n$ **autovalori** (contati con molteplicità).

Tra questi è particolarmente importante il **raggio spettrale**, definito come

$$ \rho(A) = \max_i |\lambda_i| $$

Il raggio spettrale è il **modulo massimo tra gli autovalori** della matrice.

---

### Norme vettoriali

Spesso è necessario **misurare la grandezza di un vettore** o la **distanza tra due vettori**.

Le **norme** sono funzioni che associano ad ogni vettore un numero reale non negativo che rappresenta la sua “dimensione”.

Una norma è quindi una funzione

$$ \|\cdot\|:\R^n\to\R_{\ge 0} $$

Una delle norme più naturali è la **norma euclidea**, detta anche **norma 2**, definita come

$$ \|x\|_2 = \sqrt{\sum_{i=1}^n x^2_i } $$

Questa norma corrisponde **alla lunghezza del vettore nello spazio euclideo**.

In realtà esistono **molte norme possibili**, ognuna con proprietà diverse utili in vari contesti dell’analisi numerica.

---

### Norme matriciali

Il concetto di norma può essere esteso anche alle matrici.

Una **norma matriciale** associa ad ogni matrice un numero non negativo che ne rappresenta la “dimensione”.

Nel corso verranno considerate principalmente le **norme matriciali indotte**, cioè norme derivate da una norma vettoriale.

La definizione teorica della norma indotta è

$$ \|A\| = \max_{x\ne 0} \frac{\|Ax\|}{\|x\|} $$

Questa definizione non è direttamente implementabile, ma permette di dimostrare forme equivalenti più semplici da calcolare.

Ad esempio la **norma 2 di una matrice** può essere espressa tramite gli autovalori della matrice $A^TA$:

$$ \|A\|_2 = \sqrt{\rho(A^TA)} $$

Il calcolo di questa norma è però **computazionalmente costoso**, perché richiede:

- prima il calcolo della trasposta $A^T$,
- poi la moltiplicazione $A^TA$,
- infine il calcolo dell’autovalore massimo.

---

### Distanza tra matrici

La norma permette anche di definire una **distanza tra matrici**.

Date due matrici $A$ e $B$, la loro distanza può essere definita come

$$ \|A - B\| $$

Questo concetto è molto importante nell’analisi numerica perché consente di **misurare l’errore tra una soluzione esatta e una approssimata**.

---

### Significato delle norme nell’analisi numerica

Le norme sono strumenti fondamentali nell’analisi numerica perché permettono di:

- misurare la **dimensione di vettori e matrici**
- definire **distanze tra dati numerici**
- stimare **errori e stabilità degli algoritmi**

Grazie alle norme è possibile confrontare risultati numerici e stabilire **quanto un’approssimazione sia vicina alla soluzione esatta**.
