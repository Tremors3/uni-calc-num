
# Compressione di matrici tramite SVD

Una delle applicazioni più importanti della SVD è la **compressione di matrici**.

Consideriamo

$$
A=U\Sigma V^T
$$

e indichiamo con

$$
u_i
$$

la $i$-esima colonna di $U$ e con

$$
v_i
$$

la $i$-esima colonna di $V$.

Possiamo scrivere

$$
U=(u_1\;u_2\;\dots\;u_m)
$$

e

$$
V=(v_1\;v_2\;\dots\;v_n)
$$

Da questa rappresentazione segue

$$
\boxed{
A
=
\sigma_1u_1v_1^T
+
\sigma_2u_2v_2^T
+
\dots
+
\sigma_ku_kv_k^T
}
$$

Ogni termine

$$
\sigma_i u_iv_i^T
$$

è una matrice di rango 1.

La matrice $A$ può quindi essere vista come una somma di matrici di rango 1, ciascuna pesata dal corrispondente valore singolare.

Poiché

$$
\sigma_1\ge\sigma_2\ge\dots\ge\sigma_k>0
$$

i primi termini sono quelli associati ai valori singolari più grandi e, in generale, rappresentano le componenti più importanti della matrice.

## Compressione tramite troncamento

Possiamo approssimare $A$ utilizzando soltanto i primi $\bar k$ termini, con

$$
\bar k<k
$$

ottenendo

$$
\boxed{
\bar A
=
\sum_{i=1}^{\bar k}
\sigma_i u_iv_i^T
}
$$

ossia

$$
\bar A
=
\sigma_1u_1v_1^T
+\dots+
\sigma_{\bar k}u_{\bar k}v_{\bar k}^T
$$

La matrice originale richiede la memorizzazione di

$$
mn
$$

numeri.

Per memorizzare l’approssimazione tramite SVD troncata sono invece sufficienti:

- i $\bar k$ valori singolari;
- le $\bar k$ colonne di $U$;
- le $\bar k$ colonne di $V$.

Il numero complessivo di valori da memorizzare è quindi

$$
\boxed{
\bar k(m+n+1)
}
$$

Se $\bar k\ll k$, il risparmio di memoria può essere molto significativo.

Questa proprietà rende la SVD utile, ad esempio, per la compressione di immagini, segnali e dati numerici.

---