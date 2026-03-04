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

# === GESTIONE DELLA MEMORIA (array) ===

# Esempio
a = np.array([1, 2, 3, 4])
b = a
print(a, b) # Dure referenze alla stess istanza
b = a.copy()
print(a)    # Referenze a due aree di memoria differenti

# Gli overload degli operatori su array creano un nuovo array.
# Non modificano l'istanza dell'operando lhs.
c = a + 1

