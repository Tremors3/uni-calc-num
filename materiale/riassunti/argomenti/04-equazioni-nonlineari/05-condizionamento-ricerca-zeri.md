
# Condizionamento del problema della ricerca degli zeri

Nel contesto dei metodi numerici per la ricerca degli zeri, una questione fondamentale è capire quanto il **residuo** $|f(\tilde{x})|$ fornisca informazione sulla distanza dalla soluzione esatta $x_*$.

In pratica, dato un punto $\tilde{x}$ (ad esempio una iterata del metodo) tale che:

$$
|f(\tilde{x})| \le \delta
$$

con $\delta$ tolleranza fissata, ci si chiede se questo implichi che $\tilde{x}$ sia effettivamente vicino alla radice $x_*$, cioè:

$$
|f(\tilde{x})| \le \delta \quad \Rightarrow \quad \tilde{x} \approx x_*
$$

La risposta, in generale, è **no**: questa implicazione dipende dal comportamento della funzione $f$ in prossimità della radice.

---

### ▸ Relazione tra errore e residuo

Per chiarire questo aspetto, consideriamo la definizione di derivata:

$$
f'(x_*) = \lim_{x \to x_*} \frac{f(x) - f(x_*)}{x - x_*}
$$

Poiché $f(x_*) = 0$, per $x$ sufficientemente vicino a $x_*$ possiamo approssimare:

$$
f'(x_*) \approx \frac{f(x)}{x - x_*}
$$

Da cui si ottiene:

$$
x - x_* \approx \frac{f(x)}{f'(x_*)}
$$

Passando ai valori assoluti:

$$
|x - x_*| \approx \frac{|f(x)|}{|f'(x_*)|}
$$

Se $|f(x)| \le \delta$, allora:

$$
|x - x_*| \lesssim \frac{\delta}{|f'(x_*)|}
$$

---

### ▸ Interpretazione

Questa relazione mostra che la distanza dalla radice dipende non solo dal residuo, ma anche dal valore della derivata prima nel punto $x_*$. In particolare, compare un fattore di amplificazione:

$$
\frac{1}{|f'(x_*)|}
$$

Se $|f'(x_*)|$ è grande, allora il residuo è un buon indicatore della distanza dalla soluzione: piccoli valori di $|f(x)|$ implicano piccoli errori $|x - x_*|$.

Se invece $|f'(x_*)|$ è piccolo, allora il fattore $\frac{1}{|f'(x_*)|}$ diventa grande e può amplificare l’errore: anche un residuo molto piccolo può corrispondere a una distanza significativa dalla radice.

---

### ▸ Problema ben condizionato e mal condizionato

Il problema della ricerca degli zeri si dice:

- **ben condizionato** se $|f'(x_*)|$ non è troppo piccolo  
- **mal condizionato** se $|f'(x_*)|$ è vicino a zero

Dal punto di vista geometrico, il problema è mal condizionato quando la funzione è **molto piatta** in prossimità della radice, cioè quando il grafico è quasi parallelo all’asse delle ascisse nel punto di intersezione.

In questo caso, piccole variazioni nei valori della funzione corrispondono a variazioni molto più grandi nella variabile $x$, rendendo difficile ottenere una buona approssimazione della radice.

---

### ▸ Conclusione

Il residuo $|f(\tilde{x})|$ da solo non è sempre un indicatore affidabile dell’errore $|\tilde{x} - x_*|$. La qualità dell’approssimazione dipende dal condizionamento del problema, cioè dal valore della derivata prima nel punto di soluzione.

In sintesi, un residuo piccolo garantisce una buona approssimazione solo se il problema è ben condizionato.

---