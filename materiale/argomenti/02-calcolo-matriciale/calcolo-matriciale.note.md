
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







## Introduzione a NumPy: vettori e matrici

**NumPy** è una delle librerie fondamentali di Python per il **calcolo numerico**. Fornisce strutture dati efficienti per lavorare con vettori e matrici, chiamate **ndarray (N-dimensional array)**.

```py
import numpy as np
```

### Creazione di array

La struttura dati principale di NumPy è **l’array multidimensionale (`ndarray`)**.

Un array può essere creato direttamente da una lista Python.

```py
a = np.array([1, 2., 3, 4])
```

Possiamo stampare l’array e il tipo dei suoi elementi:

```
print(a, a.dtype)
```

#### Tipo degli elementi (`dtype`)

NumPy richiede che **tutti gli elementi dell’array abbiano lo stesso tipo**. Se nella lista sono presenti tipi diversi, NumPy sceglie **il tipo più generale**.

Esempio:

```py
np.array([1, 2., 3])
```

In questo caso:

- `1` e `3` sono interi
- `2.` è float

Il tipo più generale è **float**, quindi **tutti gli elementi diventano float**.

### Attributi relativi alla dimensione degli array

Ogni array NumPy possiede alcune proprietà fondamentali.

```py
print(
    a.ndim,
    a.shape,
    a.size
)
```

- `ndim`: Numero di dimensioni dell’array.

    Esempio:
    - vettore $\to$ `ndim = 1`
    - matrice $\to$ `ndim = 2`

- `shape`: Descrive la **forma dell’array**, cioè il numero di elementi per dimensione. È rappresentata tramite **una tupla**.

    Esempi:
    - (4,)  $\to$ `vettore di 4 elementi`
    - (3,4) $\to$ `matrice 3 × 4`

- `size` Numero totale di elementi contenuti nell’array.

    Esempio:
    - (3,4) $\to$ `size = 12`

### Creazione di array particolari

NumPy offre molte funzioni per creare array rapidamente.

#### Array non inizializzato

```py
b = np.empty((4,), dtype=float)
```

Crea un array di 4 elementi **senza inizializzare i valori**. Gli elementi conterranno **valori casuali già presenti in memoria**. Serve quando si vuole **allocare memoria rapidamente** e riempirla dopo.

#### Generazione di sequenze di interi

```py
c = np.arange(1, 10)
```

Funziona come `range()` ma produce un array NumPy.

Output:

```
[1 2 3 4 5 6 7 8 9]
```

#### Partizionare un intervallo

```py
d = np.linspace(10, 50, 11, dtype=float)
```

Genera **11 valori equispaziati** tra 10 e 50.

È molto usato in:

- analisi numerica
- grafici
- simulazioni

#### Generazione di numeri casuali

e = np.random.randn(10)

Genera **10 numeri casuali** con **distribuzione normale standard (gaussiana)**:

- media = 0
- varianza = 1

Questa funzione è molto utile per:

- simulazioni
- test numerici
- generazione di dati casuali

### Accesso agli elementi e slicing

Gli array NumPy supportano lo slicing, simile alle liste Python.

```py
print(a[0:2])
```

Restituisce gli elementi con indice:

```
0 e 1
```

#### Selezione tramite lista di indici

È possibile selezionare elementi specifici tramite una lista di indici.

```py
a[[0, 1, 4]]
```

Questo estrae:
- primo elemento
- secondo elemento
- quinto elemento

#### Selezione tramite maschera logica

Si può usare un array booleano.

```py
a[[True, False, False]]
```

La lunghezza della maschera deve essere **uguale al numero di elementi dell’array**.

### Gestione della memoria negli array

Capire come NumPy gestisce la memoria è fondamentale per evitare errori.

#### Riferimenti alla stessa memoria

```py
a = np.array([1,2,3,4])
b = a
```

In questo caso:

- `a` e `b` puntano allo **stesso oggetto**

Modificare uno modifica anche l’altro.

#### Copia esplicita

```py
b = a.copy()
```

Ora:

- `a` e `b` sono **indipendenti**
- hanno **due aree di memoria diverse**

### Operazioni sugli array e memoria

Gli operatori matematici su array **creano nuovi array**.

```py
c = a + 1
```

Questo **non modifica** `a`, ma crea un nuovo array.

### Slicing e condivisione della memoria

Lo slicing **non crea una copia**, ma una **vista (view)**.

Esempio:

```py
a = np.array([1,2,3,4,5])
b = a[1:3]

b[0] = 0
```

Risultato:

```
a = [1 0 3 4 5]
b = [0 3]
```

Questo accade perché `b` condivide la memoria di `a`.

#### Selezione tramite lista

Diversamente dallo slicing:

```
b = a[[1,2]]
```

qui viene creata **una copia indipendente**.

Modificare `b` **non modifica** `a`.

### Operazioni tra array

NumPy permette di eseguire operazioni **senza cicli espliciti**.

Le operazioni sono **element-wise** (componente per componente).

#### Somma e prodotto

```py
a = np.arange(1, n+1)

print(a.sum())
print(a.prod())
```

- `sum()` $\to$ somma degli elementi

- `prod()` $\to$ prodotto degli elementi

#### Potenze

```py
a**2
2**a
```

Le operazioni sono **elemento per elemento**.

#### Operazioni tra due array

```py
a = np.array([1,2,3,4])
b = np.random.randn(4)

print(a + b)
print(a * b)
```

Gli array devono avere **stessa dimensione**.

### Prodotto scalare tra vettori

Il **prodotto scalare** può essere calcolato in due modi.

```py
np.dot(a,b)
```

oppure

```py
(a * b).sum()
```

Entrambi restituiscono:

$$ a_1b_1 + a_2b_2 + \dots + a_nb_n $$

### Costruzione di matrici

Le matrici sono semplicemente **array bidimensionali**.

```py
A = np.array([
    [1,2,3],
    [4.0,5,6],
    [7,8,9]
])
```

Anche qui il tipo degli elementi è uniforme.

#### Flags della matrice

```py
print(A.flags)
```

Tra le informazioni più importanti troviamo:

- `C_CONTIGUOUS`: La matrice è memorizzata **per righe** (come nel linguaggio C).

- `F_CONTIGUOUS`: La matrice è memorizzata **per colonne** (come in Fortran).

### Matrici particolari

NumPy permette di generare rapidamente matrici comuni.

#### Matrice di uno

```py
E = np.ones((3,2))
```

#### Matrice di zeri

```py
Z = np.zeros((3,2))
```

#### Matrice identità

```py
I = np.eye(3)
```

Produce

```
1 0 0
0 1 0
0 0 1
```

Può anche essere **rettangolare**:

```py
np.eye(3,2)
```

### Diagonali delle matrici

Creare una matrice diagonale

```py
d = np.array([1,2,3,4])
D = np.diag(d)
```

Produce:

```
1 0 0 0
0 2 0 0
0 0 3 0
0 0 0 4
```

#### Estrarre diagonali

```py
np.diagonal(A, 0)
```

- `0` $\to$ diagonale principale

- `1` $\to$ diagonale sopra la principale

- `-1` $\to$ diagonale sotto la principale

### Matrici triangolari

Si possono estrarre le parti triangolari.

```py
np.triu(A)
```

- triangolare superiore

```
a b c
0 e f
0 0 i
```

```py
np.tril(A)
```

- triangolare inferiore

```
a 0 0
d e 0
g h i
```

### Slicing di matrici

L’accesso agli elementi usa **due indici**:

```py
A[riga, colonna]
```

Esempi:

```py
A[0,0]
```

- elemento in alto a sinistra

#### Colonna

```py
A[:,0]
```

":" significa **tutte le righe**

#### Riga

```py
A[1,:]
```

":" significa **tutte le colonne**

### Trasposta di una matrice

La trasposta scambia righe e colonne.

```py
A.T
```

$$ \text{Se } A \text{ è } m \times n \text{ allora } A^T \text{ é } n \times m $$

### Operazioni tra matrici

#### Somma

```py
A + B
```

Somma **elemento per elemento**.

Le matrici devono avere **stessa dimensione**.

#### Prodotto per scalare

```py
C = 2 * A
```

Moltiplica **ogni elemento della matrice** per lo scalare.

#### Prodotto matriciale

Il prodotto matriciale si esegue con:

```py
C = A @ B
```

Oppure:

```py
np.matmul(A,B)
```

Condizione di compatibilità:

```
A = m×n
B = n×p
```

Risultato:

```
C = m×p
```

### Implementazione manuale del prodotto matriciale

Il prodotto matriciale deriva dalla formula:
​
$$ C_{ij} = \sum_{i=1}^n A_{it}B_{tj} $$

Esempio con cicli:

```py
A = np.array([ [1,2,3], [4,5,6] ])
B = np.array([ [2,2,2], [4,5,6], [5,6,7] ])
C = np.zeros((A.shape[0], B.shape[1]))  # Inizializzazione a zero

for i in range(A.shape[0]):         # righe di A
    for j in range(B.shape[1]):     # colonne di B
        for t in range(A.shape[1]): # colonne di A / righe di B
            C[i, j] += A[i, t] * B[t, j]
```

I tre cicli rappresentano:

- `i` $\to$ riga di A
- `j` $\to$ colonna di B
- `t` $\to$ indice della somma

NumPy esegue questa operazione **in modo estremamente più efficiente** usando l’operatore `@`.
