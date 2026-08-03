import numpy as np

print("\n==============================")
print("NUMPY DEMO")
print("==============================")

# --------------------------------------------------
# CREAZIONE ARRAY
# --------------------------------------------------

print("\n--- Creazione array ---")

a = np.array([1, 2., 3, 4])
print("Array a:", a)
print("dtype:", a.dtype)

print("\nAttributi:")
print("ndim:", a.ndim)
print("shape:", a.shape)
print("size:", a.size)


# --------------------------------------------------
# ARRAY SPECIALI
# --------------------------------------------------

print("\n--- Creazione array speciali ---")

b = np.empty((4,), dtype=float)
print("Array non inizializzato (empty):", b)

c = np.arange(1, 10)
print("arange(1,10):", c)

d = np.linspace(10, 50, 11, dtype=float)
print("linspace(10,50,11):", d)

e = np.random.randn(10)
print("random gaussian vector:", e)


# --------------------------------------------------
# SLICING E SELEZIONE
# --------------------------------------------------

print("\n--- Slicing e selezione ---")

a = np.array([1,2,3,4,5])

print("Array:", a)
print("a[0:2]:", a[0:2])

print("Selezione con lista indici a[[0,2,4]]:", a[[0,2,4]])

mask = np.array([True, False, True, False, True])
print("Selezione con maschera:", a[mask])


# --------------------------------------------------
# GESTIONE MEMORIA
# --------------------------------------------------

print("\n--- Gestione memoria ---")

a = np.array([1,2,3,4])
b = a

print("a:", a)
print("b:", b)

b[0] = 99

print("Dopo modifica b:")
print("a:", a)
print("b:", b)

print("\nCopia esplicita")

a = np.array([1,2,3,4])
b = a.copy()

b[0] = 99

print("a:", a)
print("b:", b)


# --------------------------------------------------
# SLICING E CONDIVISIONE MEMORIA
# --------------------------------------------------

print("\n--- Slicing con condivisione memoria ---")

a = np.array([1,2,3,4,5])
b = a[1:3]

print("a:", a)
print("b:", b)

b[0] = 0

print("Dopo modifica b:")
print("a:", a)
print("b:", b)

print("\nSelezione con lista (crea copia)")

a = np.array([1,2,3,4,5])
b = a[[1,2]]

b[0] = 0

print("a:", a)
print("b:", b)


# --------------------------------------------------
# OPERAZIONI SU ARRAY
# --------------------------------------------------

print("\n--- Operazioni su array ---")

n = 10
a = np.arange(1, n+1)

print("a:", a)
print("Somma:", a.sum())
print("Prodotto:", a.prod())

print("a^2:", a**2)
print("2^a:", 2**a)


# --------------------------------------------------
# OPERAZIONI TRA ARRAY
# --------------------------------------------------

print("\n--- Operazioni tra array ---")

a = np.array([1,2,3,4])
b = np.random.randn(4)

print("a:", a)
print("b:", b)

print("a + b:", a + b)
print("a * b:", a * b)


# --------------------------------------------------
# PRODOTTO SCALARE
# --------------------------------------------------

print("\n--- Prodotto scalare ---")

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

print("a:", a)
print("b:", b)

print("np.dot(a,b):", np.dot(a,b))
print("(a*b).sum():", (a*b).sum())


# --------------------------------------------------
# MATRICI
# --------------------------------------------------

print("\n--- Creazione matrice ---")

A = np.array([
    [1,2,3],
    [4.0,5,6],
    [7,8,9]
])

print("Matrice A:")
print(A)

print("dtype:", A.dtype)
print("flags:", A.flags)


# --------------------------------------------------
# MATRICI PARTICOLARI
# --------------------------------------------------

print("\n--- Matrici particolari ---")

E = np.ones((3,2))
Z = np.zeros((3,2))

print("Ones:")
print(E)

print("Zeros:")
print(Z)

I = np.eye(3)
print("Identità:")
print(I)


# --------------------------------------------------
# DIAGONALI
# --------------------------------------------------

print("\n--- Diagonali ---")

d = np.array([1,2,3,4])
D = np.diag(d)

print("Vettore:", d)
print("Matrice diagonale:")
print(D)

A = np.random.randn(4,4)

print("Matrice casuale:")
print(A)

print("Diagonale principale:", np.diagonal(A,0))
print("Diagonale superiore:", np.diagonal(A,1))
print("Diagonale inferiore:", np.diagonal(A,-1))


# --------------------------------------------------
# MATRICI TRIANGOLARI
# --------------------------------------------------

print("\n--- Matrici triangolari ---")

print("Triangolare superiore:")
print(np.triu(A))

print("Triangolare inferiore:")
print(np.tril(A))


# --------------------------------------------------
# SLICING MATRICE
# --------------------------------------------------

print("\n--- Slicing matrice ---")

A = np.array([
    [1,2,3],
    [4,5,6]
])

print("A:")
print(A)

print("Elemento A[0,0]:", A[0,0])
print("Prima colonna:", A[:,0])
print("Seconda riga:", A[1,:])


# --------------------------------------------------
# TRASPOSTA
# --------------------------------------------------

print("\n--- Trasposta ---")

print("A:")
print(A)

print("A.T:")
print(A.T)


# --------------------------------------------------
# OPERAZIONI TRA MATRICI
# --------------------------------------------------

print("\n--- Operazioni tra matrici ---")

A = np.array([
    [1,2,3],
    [4,5,6]
])

B = np.array([
    [7,8,9],
    [10,11,12]
])

print("A:")
print(A)

print("B:")
print(B)

print("A + B:")
print(A + B)

print("2*A:")
print(2*A)


# --------------------------------------------------
# PRODOTTO MATRICIALE
# --------------------------------------------------

print("\n--- Prodotto matriciale ---")

A = np.array([
    [1,2,3],
    [4,5,6]
])

B = np.array([
    [2,2,2],
    [4,5,6],
    [5,6,7]
])

C = A @ B

print("A:")
print(A)

print("B:")
print(B)

print("A @ B:")
print(C)


# --------------------------------------------------
# PRODOTTO MATRICIALE MANUALE
# --------------------------------------------------

print("\n--- Prodotto matriciale manuale ---")

C_manual = np.zeros((A.shape[0], B.shape[1]))

for i in range(A.shape[0]):
    for j in range(B.shape[1]):
        for t in range(A.shape[1]):
            C_manual[i, j] += A[i, t] * B[t, j]

print("Risultato manuale:")
print(C_manual)

print("Uguale a NumPy?", np.allclose(C, C_manual))


print("\n==============================")
print("FINE DEMO")
print("==============================")