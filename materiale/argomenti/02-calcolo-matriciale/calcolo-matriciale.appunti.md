# (5) Lezione 03-03-2026 | s 97.. | Richiami Algebra e NumPy

## Nozioni calcolo matriciale

Lavoreremo con matrici i cui elementi sono numeri reali (Matrici Reali).

Quando la prof scrive un vettore nello spazio $\R^m$ intende un vettore colonna $\R^{m\times1}$. Mentre per il vettore riga $\R^{1\times m}$.

Il pacchetto che utilizzeremo per rappresentare array è `NumPy`. La prof ha aggiunto su moodle un link al colab notebook dove troveremo il materiale ed esempi trattati a lezione.

**Nota Indicizzazione**: la formulazione matematica più comune prevede di numerare le righe e le colonne di una matrice partendo da 1. NumPy sceglie di partire da indice 0. 

## Array e NumPy

Numpy prende come tipo comune dei dati di una lista quello "più generico". Se definisco una lista composta da interi e float, il tipo di dato comune sarà per tutti float. Lo si può notare nella stampa dell'array stesso.

