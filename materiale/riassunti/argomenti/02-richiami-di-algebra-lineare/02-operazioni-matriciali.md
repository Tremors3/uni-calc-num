
# Calcolo Matriciale

## Tabella riassuntiva delle operazioni matriciali

| Operazione | Condizione | Risultato | Formula | Complessità | Proprietà principali |
|:-----------|:-----------|:----------|:--------|:-----------:|:---------------------|
| **Somma matriciale** | $A,B\in\mathbb{R}^{m\times n}$ | $C\in\mathbb{R}^{m\times n}$ | $c_{ij}=a_{ij}+b_{ij}$ | $\mathcal{O}(mn)$ | Commutativa, associativa, elemento neutro: $A+0=A$ |
| **Moltiplicazione per scalare** | $A\in\mathbb{R}^{m\times n},\ \lambda\in\mathbb{R}$ | $\lambda A\in\mathbb{R}^{m\times n}$ | $c_{ij}=\lambda a_{ij}$ | $\mathcal{O}(mn)$ | Distributiva: $\lambda(A+B)=\lambda A+\lambda B$; $(\lambda+\mu)A=\lambda A+\mu A$; $(\lambda\mu)A=\lambda(\mu A)$ |
| **Prodotto matrice-matrice** | $A\in\mathbb{R}^{m\times n},\ B\in\mathbb{R}^{n\times p}$ | $C=AB\in\mathbb{R}^{m\times p}$ | $c_{ij}=\displaystyle\sum_{k=1}^{n}a_{ik}b_{kj}$ | $\mathcal{O}(mnp)$<br>Quadrate: $\mathcal{O}(n^3)$ | Associativa; distributiva; **non commutativa**; $AI_n=I_mA=A$; $(AB)^T=B^TA^T$ |
| **Prodotto matrice-vettore** | $A\in\mathbb{R}^{m\times n},\ x\in\mathbb{R}^{n}$ | $y=Ax\in\mathbb{R}^{m}$ | $y_i=\displaystyle\sum_{k=1}^{n}a_{ik}x_k$ | $\mathcal{O}(mn)$<br>Quadrate: $\mathcal{O}(n^2)$ | Caso particolare del prodotto matriciale; rappresenta una trasformazione lineare |
| **Prodotto scalare** | $u,v\in\mathbb{R}^{n}$ | $s\in\mathbb{R}$ | $u^Tv=\displaystyle\sum_{k=1}^{n}u_kv_k$ | $\mathcal{O}(n)$ | Commutativo: $u^Tv=v^Tu$; distributivo; $u^Tu=\|u\|_2^2\ge0$ |

---

## Operazioni tra matrici, vettori e scalari

### ▸ **Somma tra matrici**

La **somma matriciale** è definita solamente tra due matrici aventi la **stessa dimensione**. Se

$$
A,B\in\mathbb{R}^{m\times n},
$$

allora la loro somma è una matrice

$$
C=A+B\in\mathbb{R}^{m\times n},
$$

i cui elementi si ottengono sommando gli elementi corrispondenti delle due matrici:

$$
c_{ij}=a_{ij}+b_{ij},
\qquad
i=1,\ldots,m, \;
j=1,\ldots,n.
$$

La somma matriciale viene quindi eseguita **elemento per elemento** e produce una matrice della stessa dimensione delle matrici di partenza.

Dal punto di vista computazionale, essendo necessario effettuare una somma per ciascuno degli (mn) elementi della matrice, la complessità è

$$
\mathcal{O}(mn).
$$

> #### **Proprietà**
> 
> La somma matriciale soddisfa le proprietà fondamentali dell'algebra lineare:
> 
> * **Commutativa**
> 
>     $$
>     A+B=B+A.
>     $$
> 
> * **Associativa**
> 
>     $$
>     (A+B)+C=A+(B+C).
>     $$
> 
> * **Elemento neutro**
> 
>     Esiste la matrice nulla (0) tale che
> 
>     $$
>     A+0=A.
>     $$

---

### ▸ **Moltiplicazione di una matrice per uno scalare**

Data una matrice e uno scalare

$$
A\in\mathbb{R}^{m\times n},
\qquad
\lambda\in\mathbb{R}
$$

la moltiplicazione per scalare consiste nel moltiplicare ogni elemento della matrice per il numero reale ($\lambda$).

Si ottiene così una nuova matrice i cui elementi sono

$$
C=\lambda A\in\mathbb{R}^{m\times n},
\qquad
c_{ij}=\lambda a_{ij}.
$$

La dimensione della matrice rimane invariata.

Poiché occorre effettuare un prodotto per ciascun elemento, la complessità computazionale è

$$
\mathcal{O}(mn).
$$

> #### **Proprietà**
> 
> La moltiplicazione per scalare soddisfa le seguenti proprietà:
> 
> $$
> \lambda(A+B)=\lambda A+\lambda B,
> $$
> 
> $$
> (\lambda+\mu)A=\lambda A+\mu A,
> $$
> 
> $$
> (\lambda\mu)A=\lambda(\mu A),
> $$
> 
> $$
> 1\cdot A=A,
> $$
> 
> $$
> 0\cdot A=0.
> $$

---

### ▸ **Prodotto tra matrici**

Il **prodotto matriciale** è definito solamente quando il numero di colonne della prima matrice coincide con il numero di righe della seconda.

Se

$$
A\in\mathbb{R}^{m\times n},
\qquad
B\in\mathbb{R}^{n\times p},
$$

allora

$$
C=AB\in\mathbb{R}^{m\times p}.
$$

L'elemento ($c_{ij}$) della matrice prodotto si ottiene calcolando il prodotto scalare tra la riga (i)-esima della matrice (A) e la colonna (j)-esima della matrice (B):

$$
c_{ij}=\sum_{k=1}^{n}a_{ik}b_{kj}.
$$

Per questo motivo il prodotto matriciale è anche noto come **prodotto righe-colonne**.

Ogni elemento della matrice risultante richiede (n) prodotti e (n-1) somme. Poiché gli elementi della matrice risultante sono (mp), la complessità computazionale è

$$
\mathcal{O}(mnp).
$$

Nel caso particolare di matrici quadrate, $m=n=p,$ la complessità diventa

$$
\mathcal{O}(n^3).
$$

> #### **Proprietà**
> 
> Il prodotto matriciale gode della proprietà associativa:
> 
> $$
> (AB)C=A(BC).
> $$
> 
> È inoltre distributivo rispetto alla somma:
> 
> $$
> A(B+C)=AB+AC,
> $$
> 
> $$
> (A+B)C=AC+BC.
> $$
> 
> In generale **non vale la proprietà commutativa**, cioè
> 
> $$
> AB\neq BA.
> $$
> 
> In molti casi uno dei due prodotti può addirittura non essere definito.
> 
> L'elemento neutro del prodotto è la matrice identità:
> 
> $$
> AI_n=A,
> $$
> 
> $$
> I_mA=A.
> $$
> 
> La trasposta del prodotto soddisfa inoltre la relazione
> 
> $$
> (AB)^T=B^TA^T.
> $$
> 
> Si osservi che l'ordine delle matrici si **inverte**.

---

### ▸ **Prodotto matrice-vettore**

Il prodotto matrice-vettore rappresenta un caso particolare del prodotto matriciale.

Data una matrice e un vettore colonna

$$
A\in\mathbb{R}^{m\times n},
\qquad
x\in\mathbb{R}^{n}
$$

si ottiene un nuovo vettore

$$
y=Ax\in\mathbb{R}^{m}.
$$

Ogni componente del vettore risultante si calcola eseguendo il prodotto scalare tra una riga della matrice e il vettore:

$$
y_i=\sum_{k=1}^{n}a_{ik}x_k,
\qquad
i=1,\ldots,m.
$$

Dal punto di vista geometrico, una matrice può quindi essere interpretata come una trasformazione lineare che trasforma un vettore in un altro vettore.

La complessità computazionale è

$$
\mathcal{O}(mn),
$$

che diventa

$$
\mathcal{O}(n^2)
$$

nel caso di matrici quadrate.

---

### ▸ **Prodotto scalare tra vettori**

Il **prodotto scalare** è un'operazione definita tra due vettori appartenenti allo stesso spazio vettoriale.

Se

$$
u,v\in\mathbb{R}^{n},
$$

il loro prodotto scalare è il numero reale

$$
s=u^Tv=\sum_{k=1}^{n}u_kv_k.
$$

Il risultato del prodotto scalare è quindi **uno scalare** e non un vettore.

Il prodotto scalare è utilizzato frequentemente nel calcolo matriciale perché costituisce il mattoncino fondamentale del prodotto matrice-matrice e del prodotto matrice-vettore.

La complessità computazionale è

$$
\mathcal{O}(n).
$$

> #### Proprietà
> 
> Il prodotto scalare soddisfa le proprietà
> 
> $$
> u^Tv=v^Tu,
> $$
> 
> $$
> u^T(v+w)=u^Tv+u^Tw,
> $$
> 
> $$
> (\lambda u)^Tv=\lambda(u^Tv),
> $$
> 
> e inoltre
> 
> $$
> u^Tu=|u|_2^2\ge0,
> $$
> 
> con uguaglianza se e solo se
> 
> $$
> u=0.
> $$
