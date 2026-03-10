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
