# (5,6) Lezione 03-03-2026 | s 97..120 | Richiami Algebra e NumPy

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

Il prodotto matriciale naturalmente non gode della proprietà commutativa. Sempre stare attenti quando si moltiplicano due matrici per vedere se sono compatibili.

### Inversa di una matrice

Per una matrice $A$ invertibile, l'ordine di applicazione di Trasposizione e Inversione non importa. Si parla di matrici quadrate.

La non singolarità di una matrice è strettamente legata al determinante di una matrice quadrata (slide 110). Determinante è calcolabile tramite un procediento ricorsivo.

### Autovalori e Autovettori

Gli autovalori posisamo immaginarli come una sorta di carta di identità della matrice stessa. Gli autovalori sono degli scalari, mentre la matrice è un oggetto bidimensionale. In questo modo otteniamo scalri che descrivono completamente le informazioni contenute in una matrice.

Da una matrice $M^{n\times n}$ otteniamo $n$ autovalori. Dati $n$ autovalori possiamo ottenere il Raggio Spettrale che non è altro che il maggiore tra i $n$ autovalori. 

### Norme vettoriali (spazio $R^{n}$)

Spesso e volentieri è importante misurare distanze tra i dati.

Il valore assoluto misura l'entità del dato. Mediante il valore assoluto possiamo ottenere la distanza tra i dati.

Le norme sono un modo per associare ad ogni vettore o matrice un unico numero $\ge 0$, che in un qualche modo ci indica la sua grandezza. Viene naturale utilizzare la **Norma Euclidea** (**Norma 2**) come definizione di norma:

$$ \|x_2\| = \sqrt{\sum_{i=1}^n x_i^2} $$

Ma esistono infinite altre funzioni che si possono utilizzare.

### Norme matriciali (spazio $R^{n\times n}$)

Per definire una norma matriciale possiamo usare la stessa definizione che vale per le norme vettoriali. 

Considereremo formalmente le norme matriciali indotte definite a partire da una norma vettoriale. La definizione della norma teorica (slide 117) non è implementabile. Però ci dimostra che le norme indotte corrispondenti hanno una forma più semplice ed implementabile.

L'operazione di calcolo della Norma 2 di una matrice è molto dispendiosa.

$$ \|A\| = \sqrt{p(A^TA)} $$

- Trovare la matrice $A^T$;
- Moltiplicazione $A^T \cdot A$;
- Trovare il massimo autovapre $p$.

Possiamo quindi misurare una matrice e la distanza di due matrici come la norma della loro differenza.

### Compatibilità con le norme vettoriali

- $\|Ax\|_\bullet \le \|A\|_\bullet\cdot \|x\|_\bullet$: La norma applicata alla matrice è indotta da quella applicata al vettore.

### Significato norme

Abbiamo degli strumenti per poter fare delle stime quando avremo vettori e matrici da confrontare tra loro.


