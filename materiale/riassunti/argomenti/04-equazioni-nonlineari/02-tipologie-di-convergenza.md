# Studio della convergenza dei metodi iterativi

Sia $\{x_k\}_{k \in \mathbb{N}} \subset \mathbb{R}$ una successione che converge a un valore $x_*$:

$$
\lim_{k \to \infty} x_k = x_*
$$

L’obiettivo è quantificare **quanto velocemente** $x_k$ si avvicina a $x_*$. A questo scopo si introduce il concetto di **ordine di convergenza**.

Si dice che la successione converge a $x_*$ con ordine $p \ge 1$ se esiste una costante $C > 0$ tale che:

$$
|x_{k+1} - x_*| \le C\,|x_k - x_*|^p \qquad \text{per } k \text{ sufficientemente grande}
$$

Poiché la successione converge, gli errori $|x_k - x_*|$ tendono **a zero**. L’ordine $p$ descrive la **velocità** con cui ciò avviene: più $p$ è grande, più rapidamente l’errore si riduce.

Una formulazione equivalente (più precisa dal punto di vista teorico) è:

$$
\lim_{k \to \infty} \frac{|x_{k+1} - x_*|}{|x_k - x_*|^p} = C
$$

Questa espressione permette di identificare sia l’ordine di convergenza $p$ sia la costante asintotica $C$.

---

# Tipologie di convergenza

Nel caso di metodi iterativi, si distinguono alcune classi fondamentali di convergenza.

---

La **convergenza lineare** si ha per $p = 1$ con $C \in (0,1)$:

$$
\lim_{k \to \infty} \frac{|x_{k+1} - x_*|}{|x_k - x_*|} = C
$$

In questo caso l’errore viene ridotto di un fattore costante ad ogni iterazione. Il metodo di bisezione rientra in questa categoria (con fattore circa $\frac{1}{2}$), motivo per cui converge in modo affidabile ma relativamente lento.

---

La **convergenza superlineare** si ha per $p = 1$ ma con $C = 0$:

$$
\lim_{k \to \infty} \frac{|x_{k+1} - x_*|}{|x_k - x_*|} = 0
$$

Qui la riduzione dell’errore è più rapida rispetto al caso lineare, anche se non raggiunge la velocità dei metodi di ordine superiore.

---

La **convergenza quadratica** si ha per $p = 2$:

$$
\lim_{k \to \infty} \frac{|x_{k+1} - x_*|}{|x_k - x_*|^2} = C
$$

In questo caso l’errore viene approssimativamente elevato al quadrato ad ogni iterazione, producendo una riduzione estremamente rapida. Metodi con convergenza quadratica (come il metodo di Newton, che verrà studiato successivamente) risultano molto efficienti quando si è sufficientemente vicini alla soluzione.

In sintesi, l’ordine di convergenza è uno strumento fondamentale per confrontare l’efficienza dei metodi iterativi: metodi con ordine più alto richiedono, in generale, molte meno iterazioni per raggiungere una data precisione.

---