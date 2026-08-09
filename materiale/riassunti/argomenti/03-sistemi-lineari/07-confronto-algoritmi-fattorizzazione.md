## Confronto degli algoritmi di fattorizzazione

| Metodo | Ipotesi | Complessità | Stabilità |
|---|---|---:|---|
| Gauss con pivoting parziale | $A$ nonsingolare | $\mathcal{O}\left(\frac{n^3}{3}\right)$ | **Debole** |
| **$LDL^T$** | $A$ simmetrica, minori principali $\neq 0$ | $\mathcal{O}\left(\frac{n^3}{6}\right)$ | **Debole** |
| Cholesky ($LL^T$) | $A$ simmetrica definita positiva | $\mathcal{O}\left(\frac{n^3}{6}\right)$ | **Forte** |
| QR | Colonne di $A$ linearmente indipendenti | $\mathcal{O}\left(\frac{2n^3}{3}\right)$ | **Debole** |

## Stabilità delle fattorizzazioni

La stabilità delle fattorizzazioni si studia individuando dei **limiti superiori per gli elementi dei fattori** prodotti dall'algoritmo.

Si parla di **stabilità forte** quando tali limiti superiori **non dipendono dalla dimensione $n$ della matrice**. In questo caso, la crescita degli elementi dei fattori è controllata indipendentemente dalla dimensione del problema.

Si parla invece di **stabilità debole** quando i limiti superiori **dipendono dalla dimensione $n$ della matrice**. All'aumentare della dimensione del problema, quindi, i limiti sugli elementi dei fattori possono crescere.

In sintesi:

$$
\boxed{
\begin{aligned}
\text{Stabilità forte} &\quad\Longrightarrow\quad
\text{limiti indipendenti da } n\\[2mm]
\text{Stabilità debole} &\quad\Longrightarrow\quad
\text{limiti dipendenti da } n
\end{aligned}
}
$$

---