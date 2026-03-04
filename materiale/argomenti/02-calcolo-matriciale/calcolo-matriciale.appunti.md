# (5) Lezione 03-03-2026 | s 97.. | Richiami Algebra e NumPy

## Nozioni calcolo matriciale

Lavoreremo con matrici i cui elementi sono numeri reali (Matrici Reali).

Quando la prof scrive un vettore nello spazio $\R^m$ intende un vettore colonna $\R^{m\times1}$. Mentre per il vettore riga $\R^{1\times m}$.

**Nota Indicizzazione**: la formulazione matematica più comune prevede di numerare le righe e le colonne di una matrice partendo da 1. NumPy sceglie di partire da indice 0. 

## Operazioni su Vettori

Dato $v \in \R^n$ abbiamo che:

$$v = \begin{pmatrix}
    v_1 \\ \vdots \\ v_n
\end{pmatrix}$$

E data una $\lambda \in \R$ abbiamo che 

$$\lambda\cdot v = \begin{pmatrix}
    \lambda v_1 \\ \vdots \\ \lambda v_n
\end{pmatrix}$$

E la somma tra vettori $v,w \in R^n$ abbiamo:

$$ v + w = \begin{pmatrix}
    v_1 + w_1 \\ \vdots \\ v_n + w_n
\end{pmatrix}$$

Definizione di prodotto scalare tra due vettori $v, w \in \R^n$:

$$ \sum_{i=1}^n v_iw_i = v_1w_1 + v_2w_2 + \dots + v_nw_n $$

Quando confronteremo algoritmi tra loro non ci baseremo solamente sulla velocità di esecuzione. Ma anche sulla **Complessità Computazionale** dell'algoritmo. Le due misure saranno comunque *proporzionali*.

Nel caso del prodotto scalare effettuiamo $\mathbf{n}$ **prodotti fp** e $\mathbf{n-1}$ **somme fp**. Cioè qualcosa che è nell'ordine di $O(n)$ somme e $O(n)$ prodotti.

Per non fissarci sun un certo tipo di architettura utilizzeremo la Complessità Computazionale come misura per indicare l'efficienza di un algoritmo.

## Note sul calcolo matriciale

Conoscere la struttura di una matrice consente di **rappresentarla in modo più efficiente** in memoria. Ad esempio una matrice diagonale può essere rappresentata come un vettore. Per una matrice triangolare ci basta tenere traccia degli elementi che stanno sopra/sotto la diagonale principale.

### Prodotto matriciale 

Avendo $A \in \R^{m\times n}$ e un vettore colonna $x \in \R^{n\times 1}$ l'operatore di **prodotto matriciale** è definito come: $A \;@\; x$.

Il prodotto matriciale è composto da molti prodotti scalari. Ognuno degli elementi della matrice prodotto è il risultato di un prodotto scalare. 