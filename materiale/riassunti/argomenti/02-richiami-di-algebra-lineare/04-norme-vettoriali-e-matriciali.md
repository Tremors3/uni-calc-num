
## Norme nel Calcolo Numerico

### ▸ Norme vettoriali

Spesso è necessario **misurare la grandezza di un vettore** o la **distanza tra due vettori**.

Le **norme** sono funzioni che associano ad ogni vettore un numero reale non negativo che rappresenta la sua “dimensione”.

Una norma è quindi una funzione

$$ \|\cdot\|:\R^n\to\R_{\ge 0} $$

Una delle norme più naturali è la **norma euclidea**, detta anche **norma 2**, definita come

$$ \|x\|_2 = \sqrt{\sum_{i=1}^n x^2_i } $$

Questa norma corrisponde **alla lunghezza del vettore nello spazio euclideo**.

In realtà esistono **molte norme possibili**, ognuna con proprietà diverse utili in vari contesti dell’analisi numerica.

| Norma | Formula | Significato | Note |
|:------|:--------|:------------|:-----|
| **Norma $\infty$** | $\|x\|_\infty=\max\limits_{i=1,...,n} \|x_i\|$ | Massimo valore assoluto tra le componenti del vettore. | Misura la componente di modulo maggiore. |
| **Norma 1** | $\|x\|_1=\sum_{i=1}^{n}\|x_i\|$ | Somma dei valori assoluti delle componenti. | È detta anche **norma Manhattan** o **taxicab**. |
| **Norma 2 (Euclidea)** | $$\|x\|_2=\sqrt{\sum_{i=1}^{n}x_i^2}$$ | Lunghezza (modulo) del vettore nello spazio euclideo. | È la norma più utilizzata; vale $$\|x\|_2=\sqrt{x^Tx}$$. |

---

### ▸ Norme matriciali

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

| Norma | Formula | Significato | Note |
|:------|:--------|:------------|:-----|
| **Norma $\infty$** | $\|A\|_\infty=\max\limits_{i=1,\ldots,n}\sum_{j=1}^{n}\|a_{ij}\|$ | Massima somma dei valori assoluti degli elementi di una riga. | È detta anche **norma per righe**. |
| **Norma 1** | $\|A\|_1=\max\limits_{j=1,\ldots,n}\sum_{i=1}^{n}\|a_{ij}\|$ | Massima somma dei valori assoluti degli elementi di una colonna. | È detta anche **norma per colonne**. |
| **Norma 2** (o **norma spettrale**) | $\|A\|_2=\sqrt{\rho(A^TA)}$ | Radice del massimo autovalore di $A^TA$. | Equivale al massimo valore singolare di A: $\|A\|_2=\sigma_{\max}(A)$ |

---

## Norme e Distanza tra matrici

Le **norme** esprimono il concetto di misura e svolgono per vettori e matrici lo stesso ruolo che il **valore assoluto** svolge per gli scalari.

Una norma permette di associare ad un vettore o ad una matrice un numero reale non negativo che ne rappresenta la "dimensione" o l'ampiezza.

Date due quantità dello stesso tipo, ad esempio due vettori

$$
x,y\in\mathbb{R}^n,
$$

la norma permette di definire una **distanza** tra essi:

$$
d(x,y)=\|x-y\|.
$$

Il valore ottenuto rappresenta quanto i due vettori sono lontani tra loro.

---

### ▸ Errore assoluto ed errore relativo

Nell'analisi numerica le norme vengono utilizzate principalmente per misurare gli errori tra una soluzione esatta e una soluzione approssimata.

Se $x$ è la soluzione esatta e $\tilde{x}$ una sua approssimazione, l'**errore assoluto** è definito come

$$
\|x-\tilde{x}\|.
$$

Questo valore misura la distanza assoluta tra la soluzione reale e quella calcolata.

Per confrontare l'errore rispetto alla grandezza della soluzione si utilizza invece l'**errore relativo**:

$$
\frac{\|x-\tilde{x}\|}{\|x\|}.
$$

L'errore relativo fornisce una misura normalizzata dell'errore e permette di confrontare risultati con scale diverse.

Le stesse considerazioni valgono anche nel caso delle matrici. Date due matrici $A$ e $B$, la loro distanza può essere definita come

$$
d(A,B)=\|A-B\|.
$$

Analogamente, l'errore assoluto tra una matrice esatta e una approssimata è

$$
\|A-\tilde{A}\|,
$$

mentre l'errore relativo è

$$
\frac{\|A-\tilde{A}\|}{\|A\|}.
$$

---

## Importanza delle norme nell'analisi numerica

Le norme sono strumenti fondamentali nell'analisi numerica perché permettono di:

- misurare la **dimensione** di vettori e matrici;
- definire **distanze** tra dati numerici;
- valutare **errori** assoluti e relativi;
- analizzare la **stabilità** e la precisione degli algoritmi.

Grazie alle norme è quindi possibile confrontare risultati numerici e determinare quanto una soluzione approssimata sia vicina alla soluzione esatta.
