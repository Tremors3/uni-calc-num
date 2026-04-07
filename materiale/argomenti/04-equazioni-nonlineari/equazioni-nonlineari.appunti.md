
# (17) Lezione 01-04-2026 | s 247.. | Metodi per la soluzione di equazioni nonlineari

### Introduzione ai metodi per equazioni nonlineari

Sia $\mathcal{f} : [a,b] \to\R$, l'obiettivo è trovare $x_*\in[a,b]$ tale che $\mathcal{f}(x_*) = 0$. Questi punti vengono chiamati anche radici di una funzione o zeri di una funzione.

Una semplificazione che inizialmente facciamo è che consideriamo una sola espressione con una sola incognita.

#### Teorema del valor medio

Si applica a funzioni continue (ipotesi minima che faremo), definita in un intervallo. Se il segno che la funzione assume agli esptremi dell'intervallo è discorde, allora il teorema ci garantisce che esiste almeno un punto nell'intervallo in cui la funzione si annulla. Si tratta di una condizione sufficiente.

Se la funzione è **strettamente monotona allora la radice sarà unica**.

#### Quattro metodi che studieremo

Due tipologie di metodi differenti:

- Metodi dicotomici

    1) Metodo di bisezione
    2) Metodo di regula fasi

- ...

Si tratta sempre di metodi iterativi.

---

### Metodo di Bisezione

Richiede come punto di partenza del metodo l'intervallo in cui cercare una radice. L'input del metodo sono l'estremo dx e sx.

Assumiamo che la funzione a cui vogliamo applicare il metodo soddisfi il teorema del valor medio.

Procedimento:

1) L'algoritmo individua ad ogni iterazione il punto medio $c_i$ nel sotto intervallo considerato.

2) In quale dei due sottointervalli considerati è ancora vero il teorema del valor medio? Considero il sotto intervallo in cui è valida. Itero il procedimento logaritmicamente; andando a prendere un intervallo sempre più piccolo.

3) Notiamo che ci stringiamo sempre di più verso una delle radici della funzione.

Quando c'è più di una radice non possiamo sapere verso quale radice ci stiamo dirigendo.

#### Fattore di interruzione del metodo

E' linico metodo che ci permette di controllare la distanza dalla soluzione reale. Fattore di Tolleranza. Ogni volta che facciamo un passo sul metodo di bisezione stiamo dimezzando l'intervallo fino a che non è abbastanza piccolo (sotto la tolleranza). La radice si troverà sicuramente in quell'intervallo.

Abbiamo che:

$$
\{[a_k,b_k]\}_{k=1}^\infin
$$

$$
{c_k}_{k=1}^\infin \qquad c_k = \frac{a_k + b_k}{2}
$$

Per le proprietà del metodo, esiste sicuramente una radice

$$ \exists x_* \text{radice} : x_* \in{a_k,b_k} $$

Ora, qual'è la distanza massima tra $c_k$ e la soluzione dell'intervallo $x_*$?

$$
|c_k - x_*| \le \frac{a_k + b_k}{2} = \frac{b - a}{2^k}
$$

Per il metodo di bisezione siamo in grado di stabilire quale sarà il numero totale di iterazioni da effettuare.

$$
\frac{b - a}{2^k} \le \tau
$$

$$
2^k \ge \frac{b - a}{\tau} \\
k \ge \log_2(\frac{b - a}{\tau})
$$

---
