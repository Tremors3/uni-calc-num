
## Metodi risolutivi per sistemi lineari generici

### 1) Calcolo esplicito dell'inversa della matrice

Dato il sistema lineare $Ax=b$ con $A\in\R^{n\times n}$ invertibile, dal punto di vista teorico la soluzione può essere scritta come

$$ x=A^{-1}b. $$

Questo suggerisce un possibile metodo risolutivo: calcolare prima l'inversa della matrice $A$ e poi moltiplicarla per il vettore dei termini noti $b$.

Tuttavia questo approccio **non viene utilizzato nel calcolo numerico**. Il calcolo esplicito dell'inversa è infatti **computazionalmente costoso e può introdurre problemi di stabilità numerica**, soprattutto quando la matrice contiene coefficienti molto grandi o i termini noti sono molto piccoli.

Per questo motivo, nella pratica si preferiscono **metodi più efficienti e stabili** che permettono di risolvere direttamente il sistema $Ax=b$ senza calcolare l'inversa della matrice.

---

### 2) Metodo di Cramer

Il **metodo di Cramer** è un procedimento teorico per risolvere un sistema lineare $Ax=b$ basato sul **calcolo dei determinanti**. La soluzione si ottiene calcolando $n+1$ determinanti di matrici di ordine $n$: uno per la matrice $A$ e $n$ determinanti ottenuti sostituendo, una alla volta, le colonne di $A$ con il vettore $b$.

Tuttavia il calcolo di un determinante con l’algoritmo diretto ha costo dell’ordine di $n!$, che cresce molto rapidamente con la dimensione della matrice. Di conseguenza il metodo di Cramer risulta **computazionalmente troppo costoso** e non è utilizzato nella pratica per risolvere sistemi lineari di grandi dimensioni.

---

### 3) Metodo di Gauss

Il **metodo di Gauss** (o **eliminazione gaussiana**) è uno degli algoritmi fondamentali per risolvere sistemi lineari della forma

$$ Ax=b $$

dove $A\in\R^{n\times n}$ è la matrice dei coefficienti, $x\in\R^n$ il vettore delle incognite e $b\in\R^n$ il vettore dei termini noti.

L’idea principale dell’algoritmo è **trasformare il sistema originale in uno equivalente ma più semplice da risolvere**.

In particolare, attraverso *opportune combinazioni lineari* delle righe della matrice $A$, il metodo trasforma la matrice dei coefficienti in una matrice triangolare, per la quale la soluzione del sistema diventa immediata tramite gli algoritmi di sostituzione.