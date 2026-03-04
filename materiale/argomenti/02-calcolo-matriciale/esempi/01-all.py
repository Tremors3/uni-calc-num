import numpy as np

# Costruzione di un array
a = np.array([1, 2., 3, 4])

# Stampa array e relativo tipo
print(a, a.dtype)

# Attributi relativi alla dimensione degli ndarray
print(
    a.ndim,             # Numero di dimensioni (1 = una dimensione)
    a.shape,            # Mostra il numero di elementi per riga
    a.size              # Numero di elementi totali dell'array
)

# La forma dell'array è espressa tramite una tupla.
# Capire come rappresentare matrici tramite questa sintassi.

# Creazione di array speciali
b = np.empty((4,), dtype = float)   # Crea un array senza assegnare nessun dato

# Genera un vettore di Interi all'interno di un certo range
c = np.arange(1, 10) 
print(c, c.dtype)

# Partizionare un intervallo (termini float)
d = np.linspace(10, 50, 11, dtype=float)
print(d, d.dtype)

# Usa Distriuzione Gaussiana Standard (Normale) per generare valori random
# Ci servirà per generare vettori con termini randomici.
e = np.random.randn(10)
print(e)

# Array slicing
print(a[0:2])

# Selezione senza slicing
# print(a[[0, 1, 4]]) # Estrazione della prima, seconda e quinta componente da un array

# Accesso mediante valori logici (bitmap)
# Il numero di bit deve essere pari al numero di elementi dell'array.
#b = a[[True, False, False]]

# Numpy prende come tipo comune dei dati di una lista quello "più generico".
# Se definisco una lista composta da interi e float, il tipo di dato comune 
#  sarà per tutti float. Lo si può notare nella stampa dell'array stesso.

# === GESTIONE DELLA MEMORIA (array) ===

# Esempio
a = np.array([1, 2, 3, 4])
b = a
print(a, b) # Dure referenze alla stess istanza
b = a.copy()
print(a)    # Referenze a due aree di memoria differenti

# Gli overload degli operatori su array creano un nuovo array.
# Non viene modificata l'istanza dell'operando lhs.
c = a + 1

# Dal punto di vista della memoria, sommare un array numpy
# con uno scalare, genera un nuovo oggetto. Condivisione di memoria.

# Lo slicing, al contrario, non genera nuova memoria.
# Condivide la memoria dell'oggetto da cui siamo partiti.
a = np.array([1,2,3,4,5])
b = a[1:3]
b[0] = 0
print(a, b)

# Questa volta invece il vettore a non viene modificato.
# La selezione di componenti mediante liste di interi crea due oggetti separati.
a = np.array([1,2,3,4,5])
b = a[[1,2]]    # Selezione tramite lista
b[0] = 0
print(a, b)

# === OPERAZIONI SU ARRAY === #

# Tra componenti di array
def sumFirstN(n: int): return (n * (n - 1)) / 2
n = 10
a = np.arange(1, n + 1)
print(a.sum(), sumFirstN(n))  # Due metodi per la somma
print(a.prod())  # Produttoria :)
print(a**2, 2**a)  # Elevamento a potenza (componente per componente)

# In generale, gli operatori aritmetici tra scalari valgono anche per i array
# interpretata componente per componente dello stesso.

# Tra array
a = np.array([1,2,3,4])
b = np.random.randn(4)
print(a + b, a * b, ...)  # Somma componente per componente (stessi indici)

# Questo vale per tutti gli operatori che abbiamo visto.
# Naturalmente il numero di elementi degli array deve essere lo stesso.

# === PRODOTTO SCALARE IN PYTHON ===
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print(
    np.dot(a, b), 
    (a * b).sum() # Prodotto scalare senza ciclo esplicito
)

# === COSTRUZIONE MATRICI ===

A = np.array([[1,2,3], [4.0,5,6], [7,8,9]])
print(A, A.dtype)   # Stampa matrice e relativo tipo
print(A.flags)      # Flag riguardo alla matrice

# Ci interessiamo alle flags:
#   C_CONTIGUOUS: bool --> Memorizzata per righe (come in C)
#   F_CONTIGUOUS: bool --> Memorizzata per colonne (come in Fortran)

# === MATRICI PARTICOLARI ===

# Matrici di tutti 1 o 0.
E = np.ones((3, 2))
Z = np.zeros((3, 2))
print(E, E.dtype)
print(Z, Z.dtype)

# Matrice Identità
I1 = np.eye(3, 3)   # Quadrata
I2 = np.eye(3, 2)   # Rettangolare
print(I1, I2)

# Otteniamo gli elementi che stanno sulla diagonale principale di una matrice
d = np.array([1,2,3,4])
D = np.diag(d)
print(d)

# caso contrario rispetto al precedente
A = np.random.randn(4, 4)
print(np.diagonal(A, 0))    # Diagonale principale
print(np.diagonal(A, -1))   # Diagonale inferore alla principale
print(np.diagonal(A,  1))   # Diagonale superiore alla principale

# Otteniamo matrice triangolare superiore/inferiore
print(
    np.triu(A),
    np.tril(A),
    sep='\n'
)

# Slicing di un array 2D
A = np.array([[1,2,3], [4,5,6]])
print(A[0,0])  # Accesso ad elemento: indice di riga; indice di colonna.
print(A[:,0])  # Otteniamo tutti gli elementi della prima colonna dell'array.
print(A[1,:])  # Otteniamo tutti gli elementi della seconda riga dell'array.

# Calcolo della trasposta di una atrice
print(A.T)

# Somma matriciale
A = np.array([[1,2,3], [4,5,6]])
B = np.array([[7,8,9], [10,11,12]])
print(A + B) # Somma componente per componente

# Prodotto per scalare
C = 2 * A
print(C) # Prodotto di ciascun elemento per 2

# Prodotto matriciale
A = np.array([[1,2,3], [4,5,6]])
B = np.array([[2,2,2], [4,5,6], [5,6,7]])
c = A @ B   # Operatore prodotto matriciale
print(C)

# Esempio calcolo prodotto scalare
A = np.array([[1,2,3], [4,5,6]])
B = np.array([[2,2,2], [4,5,6], [5,6,7]])

for i in range(2):
    for j in range(3):
        for t in range(3):
            C[i, j] += A[i, t] * B[t, j]
print(C)