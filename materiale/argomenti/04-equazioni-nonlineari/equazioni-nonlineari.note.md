
# Metodi Non-Lineari

## Metodi per equazioni nonlineari

Sia $f : [a,b] \to \mathbb{R}$. L’obiettivo è determinare un punto $x_* \in [a,b]$ tale che $f(x_*) = 0$. Un tale punto viene detto radice (o zero) della funzione.

In questa prima fase si considera il caso di una sola equazione in una sola incognita, con l’idea di costruire metodi numerici che permettano di approssimare la soluzione quando non è possibile determinarla in forma analitica.

---

### Teorema degli zeri (o teorema di esistenza)

Si considera una funzione continua $f$ definita su un intervallo $[a,b]$. Se i valori della funzione agli estremi dell’intervallo hanno segno opposto, cioè:

$$
f(a)\cdot f(b) < 0
$$

allora esiste almeno un punto $x_* \in (a,b)$ tale che $f(x_*) = 0$.

Questo risultato fornisce una **condizione sufficiente** per garantire l’esistenza di almeno una radice nell’intervallo. Non assicura invece l’unicità, a meno che non si imponga una condizione aggiuntiva.

In particolare, se la funzione è **strettamente monotona** nell’intervallo, allora **la radice**, se esiste, **è unica**.

---

### Metodi iterativi per la ricerca degli zeri

I metodi numerici per la ricerca delle radici sono generalmente **iterativi**: a partire da un intervallo iniziale che contiene almeno una radice, si costruisce una successione di intervalli sempre più piccoli che convergono verso la soluzione.

Tra questi, si distinguono i **metodi dicotomici**, tra cui il metodo di bisezione e il metodo della regula falsi (o falsa posizione). Entrambi sfruttano il teorema degli zeri e richiedono come ipotesi iniziale un intervallo in cui la funzione cambia segno.

---

### Metodo di bisezione

Il metodo di bisezione richiede come dato iniziale un intervallo $[a_0, b_0]$ tale che $f(a_0)\cdot f(b_0) < 0$, ovvero **un intervallo che contiene almeno una radice**.

Ad ogni iterazione si considera il punto medio dell’intervallo corrente:

$$
c_k = \frac{a_k + b_k}{2}
$$

Si valuta il segno di $f(c_k)$ e si seleziona il sottointervallo in cui la funzione continua a cambiare segno. In questo modo si costruisce una successione di intervalli annidati:

$$
[a_0,b_0] \supset [a_1,b_1] \supset [a_2,b_2] \supset \cdots
$$

che continuano a contenere almeno una radice della funzione.

Se la funzione è continua, allora per ogni iterazione vale:

$$
\exists x_* \in [a_k, b_k] \quad \text{tale che} \quad f(x_*) = 0
$$

Il processo restringe progressivamente l’intervallo, e la **lunghezza dell’intervallo si dimezza ad ogni iterazione**. Dopo $k$ iterazioni, la lunghezza dell’intervallo è:

$$
b_k - a_k = \frac{b_0 - a_0}{2^k}
$$

Il punto medio $c_k$ rappresenta un’approssimazione della radice. L’errore assoluto massimo tra $c_k$ e la soluzione $x_*$ è limitato da metà della lunghezza dell’intervallo:

$$
|c_k - x_*| \le \frac{b_k - a_k}{2} = \frac{b_0 - a_0}{2^{k+1}}
$$

In molti contesti si usa una stima equivalente (a fattore costante vicino) del tipo:

$$
|c_k - x_*| \le \frac{b_0 - a_0}{2^k}
$$

---

#### Criterio di arresto

Il metodo di bisezione è uno dei pochi metodi per cui è possibile **controllare a priori la distanza dalla soluzione**. Si introduce una tolleranza $\tau > 0$ e si interrompe l’algoritmo quando l’intervallo è sufficientemente piccolo:

$$
b_k - a_k \le \tau
$$

Siccome:

$$
b_k - a_k = \frac{b_0 - a_0}{2^k}
$$

si ottiene la condizione:

$$
\frac{b_0 - a_0}{2^k} \le \tau
$$

da cui:

$$
2^k \ge \frac{b_0 - a_0}{\tau}
$$

e quindi il numero minimo di iterazioni richiesto è:

$$
k \ge \log_2\!\left(\frac{b_0 - a_0}{\tau}\right)
$$

Questo risultato evidenzia che il metodo di bisezione **converge con velocità logaritmica** rispetto alla precisione richiesta. In altre parole, per migliorare la precisione di un fattore 2 è sufficiente una sola iterazione in più.

Dopo $k$ iterazioni, il punto medio $c_k$ soddisfa una stima dell’errore del tipo:

$$
|c_k - x_*| \le \frac{b_0 - a_0}{2^k} \le \tau
$$

Quindi, una volta raggiunto tale numero di iterazioni, si ha la garanzia che la distanza tra l’approssimazione $c_k$ e la radice $x_*$ è inferiore alla tolleranza fissata, e dunque l’approssimazione è considerata accettabile.

---

#### Osservazione sul calcolo del punto medio

Per calcolare il punto medio di un intervallo $[a,b]$ si possono utilizzare due formule matematicamente equivalenti:

$$
c = \frac{a + b}{2} \qquad \text{oppure} \qquad c = a + \frac{b - a}{2}
$$

Dal punto di vista numerico, però, le due espressioni non sono equivalenti in termini di stabilità.

La formula più immediata, $c = (a + b)/2$, può risultare numericamente instabile quando $a$ e $b$ sono numeri molto grandi (in valore assoluto) o molto vicini tra loro. In questi casi, la somma $a + b$ può introdurre errori di arrotondamento significativi (overflow o perdita di cifre significative).

Per questo motivo si preferisce utilizzare la forma:

$$
c = a + \frac{b - a}{2}
$$

Questa espressione è algebraicamente equivalente, ma numericamente più stabile, perché evita di sommare direttamente due numeri potenzialmente grandi e riduce il rischio di perdita di precisione.

Va comunque osservato che anche questa seconda formula non elimina completamente gli errori di arrotondamento, ma nella pratica fornisce risultati più accurati e robusti.

---

#### Costo computazionale nei metodi per equazioni non lineari

Nello studio dei metodi numerici, l’implementazione degli algoritmi è progettata per ridurre al minimo il costo computazionale.

Una funzione non lineare $f(x)$ non viene calcolata esattamente a livello macchina, ma viene approssimata tramite algoritmi numerici che la riconducono a una sequenza di operazioni aritmetiche elementari (ad esempio somme, prodotti, divisioni). Spesso queste approssimazioni si basano su sviluppi polinomiali (Taylor) o tecniche equivalenti.

Per questo motivo, il costo computazionale complessivo di un metodo iterativo può essere modellato come:

$$
\mathcal{O}(n \cdot \text{costo}(f))
$$

dove $n$ è il numero di iterazioni e $\text{costo}(f)$ rappresenta il costo di una singola valutazione della funzione.

In questo contesto, è naturale considerare la funzione $f$ come un **“blocco” (o pacchetto) di operazioni elementari**. Invece di contare ogni singola operazione aritmetica, si conta quante volte viene valutata la funzione, poiché questo rappresenta la parte dominante del costo.

Di conseguenza, una misura pratica dell’efficienza di un metodo è **il numero di valutazioni di funzione per iterazione**. Ridurre questo numero significa rendere il metodo più efficiente, a parità di numero di iterazioni.

Nel caso del metodo di bisezione, ogni iterazione richiede una sola nuova valutazione della funzione (nel punto medio $c_k$). Le valutazioni agli estremi dell’intervallo possono infatti essere riutilizzate dalle iterazioni precedenti.

Pertanto, il costo computazionale per iterazione del metodo di bisezione è costante e pari a una valutazione di funzione, rendendolo un metodo semplice e prevedibile dal punto di vista computazionale, anche se **non tra i più veloci** in termini di convergenza.

---

### Metodo di Regula Falsi

Il metodo di regula falsi (o metodo della falsa posizione) appartiene, insieme al metodo di bisezione, alla **famiglia dei metodi dicotomici**. Anche in questo caso si parte da un intervallo iniziale $[a_0, b_0]$ tale che:

$$
f(a_0)\cdot f(b_0) < 0
$$

quindi si assume che la funzione sia continua e che esista almeno una radice nell’intervallo.

La differenza principale rispetto al metodo di bisezione riguarda la scelta del punto $c_k$. Invece di prendere il punto medio dell’intervallo, il metodo di regula falsi utilizza un’**approssimazione lineare della funzione**: si considera la retta secante che passa per i punti $(a_k, f(a_k))$ e $(b_k, f(b_k))$, e si prende come nuovo punto l’intersezione di questa retta con l’asse $x$.

La formula del punto $c_k$ è:

$$
c_k = b_k - \frac{f(b_k)}{\dfrac{f(b_k) - f(a_k)}{b_k - a_k}}
$$

che può essere riscritta in forma più compatta come:

$$
c_k = b_k - f(b_k)\,\frac{b_k - a_k}{f(b_k) - f(a_k)}
$$

Questo punto rappresenta una stima migliore della radice rispetto al punto medio, poiché tiene conto dei valori della funzione agli estremi dell’intervallo.

Una volta calcolato $c_k$, si procede in modo analogo al metodo di bisezione: si valuta $f(c_k)$ e si seleziona il sottointervallo in cui la funzione cambia segno, costruendo così una nuova coppia $(a_{k+1}, b_{k+1})$.

Il metodo genera quindi una successione di intervalli che continuano a contenere la radice, garantendo la convergenza sotto le stesse ipotesi di continuità.

Dal punto di vista implementativo, il metodo è molto simile a quello di bisezione: l’unica differenza consiste nella formula utilizzata per calcolare $c_k$. Anche in questo caso, il costo per iterazione è dominato dalla valutazione della funzione $f$, e si ha una sola nuova valutazione per iterazione.

Rispetto alla bisezione, il metodo di regula falsi può **convergere più rapidamente in molti casi**, poiché **sfrutta l’andamento della funzione**. Tuttavia, in alcune situazioni può **rallentare significativamente** (ad esempio quando uno degli estremi rimane quasi fisso), rendendo la convergenza non uniforme.

---

### Velocità di convergenza dei metodi dicotomici

Per analizzare la velocità di convergenza di un metodo iterativo, invece di osservare direttamente quanto una singola iterata $c_k$ si avvicina alla soluzione $x_*$, è utile confrontare l’**errore tra iterate successive**.

Nel caso del metodo di bisezione, sappiamo che vale la stima:

$$
|c_k - x_*| \le \frac{b_0 - a_0}{2^k}
$$

che possiamo interpretare, in modo approssimato, come:

$$
|c_k - x_*| \approx \frac{b_0 - a_0}{2^k}
$$

Considerando allora l’iterata successiva, otteniamo:

$$
|c_{k+1} - x_*| \approx \frac{b_0 - a_0}{2^{k+1}} = \frac{1}{2}\,\frac{b_0 - a_0}{2^k} \approx \frac{1}{2}|c_k - x_*|
$$

Questo mostra che, ad ogni iterazione, l’errore viene circa dimezzato. Si parla quindi di **convergenza lineare** con fattore di riduzione (*p*) pari a $\frac{1}{2}$.

Dal punto di vista pratico, questo implica che il numero di cifre corrette cresce lentamente: tipicamente si guadagna circa una cifra decimale ogni 3 o 4 iterazioni.

Di conseguenza, il metodo di bisezione è **molto robusto** — richiede ipotesi deboli (continuità e cambio di segno) e ha un costo computazionale contenuto per iterazione — ma risulta poco efficiente quando si desidera un’elevata precisione, poiché richiede un **numero elevato di iterazioni**.

---

### Studio della convergenza dei metodi iterativi

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

#### Tipologie di convergenza

Nel caso di metodi iterativi, si distinguono alcune classi fondamentali di convergenza.

La **convergenza lineare** si ha per $p = 1$ con $C \in (0,1)$:

$$
\lim_{k \to \infty} \frac{|x_{k+1} - x_*|}{|x_k - x_*|} = C
$$

In questo caso l’errore viene ridotto di un fattore costante ad ogni iterazione. Il metodo di bisezione rientra in questa categoria (con fattore circa $\frac{1}{2}$), motivo per cui converge in modo affidabile ma relativamente lento.

La **convergenza superlineare** si ha per $p = 1$ ma con $C = 0$:

$$
\lim_{k \to \infty} \frac{|x_{k+1} - x_*|}{|x_k - x_*|} = 0
$$

Qui la riduzione dell’errore è più rapida rispetto al caso lineare, anche se non raggiunge la velocità dei metodi di ordine superiore.

La **convergenza quadratica** si ha per $p = 2$:

$$
\lim_{k \to \infty} \frac{|x_{k+1} - x_*|}{|x_k - x_*|^2} = C
$$

In questo caso l’errore viene approssimativamente elevato al quadrato ad ogni iterazione, producendo una riduzione estremamente rapida. Metodi con convergenza quadratica (come il metodo di Newton, che verrà studiato successivamente) risultano molto efficienti quando si è sufficientemente vicini alla soluzione.

In sintesi, l’ordine di convergenza è uno strumento fondamentale per confrontare l’efficienza dei metodi iterativi: metodi con ordine più alto richiedono, in generale, molte meno iterazioni per raggiungere una data precisione.

---

### Metodo di Newton

Il metodo di bisezione non è facilmente estendibile al caso di sistemi di equazioni non lineari o funzioni in più variabili. Per questo motivo si introduce il **metodo di Newton**, che rappresenta uno dei metodi più importanti ed efficienti per la ricerca degli zeri.

L’idea alla base del metodo è di tipo geometrico: dato un punto iniziale $x_k$, si considera la retta tangente al grafico della funzione nel punto $(x_k, f(x_k))$ e si prende come nuova approssimazione $x_{k+1}$ l’intersezione tra questa retta e l’asse delle ascisse.

L’equazione della retta tangente nel punto $(x_k, f(x_k))$ è:

$$
y = f(x_k) + f'(x_k)(x - x_k)
$$

Per trovare l’intersezione con l’asse $x$, si impone $y = 0$:

$$
0 = f(x_k) + f'(x_k)(x - x_k)
$$

Risolvendo rispetto a $x$, si ottiene:

$$
x = x_k - \frac{f(x_k)}{f'(x_k)}
$$

Da cui deriva la formula iterativa del metodo di Newton:

$$
\boxed{
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}
}
$$

---

#### Ipotesi di applicabilità

Affinché il metodo sia ben definito, è necessario che:

$$
f'(x_k) \neq 0
$$

per ogni iterazione, altrimenti la formula non è applicabile (divisione per zero).

Inoltre, per garantire una buona convergenza, si richiede generalmente che la funzione sia sufficientemente regolare (derivabile) e che il punto iniziale $x_0$ sia scelto vicino alla radice.

L’ipotesi $f'(x) \neq 0$ in un intorno della soluzione implica che la funzione è localmente monotona, ma è importante notare che **non è necessario che sia globalmente strettamente monotona** su tutto l’intervallo.

---

#### Derivazione del metodo di Newton tramite sviluppo di Taylor

Un modo alternativo (e più analitico) per derivare il metodo di Newton consiste nell’utilizzare lo sviluppo di Taylor della funzione.

L’idea è quella di sostituire il problema originale, non lineare:

$$
f(x) = 0
$$

con una successione di problemi più semplici, ottenuti approssimando la funzione con il suo sviluppo di Taylor al primo ordine attorno a un punto $x_k$:

$$
f(x) \approx f(x_k) + f'(x_k)(x - x_k)
$$

Questa è un’approssimazione lineare della funzione, valida localmente (cioè per $x$ vicino a $x_k$).

Per trovare una nuova approssimazione della radice, si impone che questa approssimazione lineare si annulli:

$$
f(x_k) + f'(x_k)(x - x_k) = 0
$$

Risolvendo rispetto a $x$, si ottiene:

$$
x = x_k - \frac{f(x_k)}{f'(x_k)}
$$

che coincide esattamente con la formula iterativa del metodo di Newton:

$$
\boxed{
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}
}
$$

---

#### Interpretazione

Il metodo di Newton può quindi essere visto come un procedimento che, ad ogni iterazione, sostituisce la funzione con la sua approssimazione lineare (tramite Taylor) e risolve il problema approssimato.

Questo spiega perché il metodo è molto efficiente: se l’approssimazione lineare è buona (cioè se siamo sufficientemente vicini alla soluzione), allora la nuova iterata $x_{k+1}$ risulta molto più vicina alla radice rispetto a $x_k$.

---

#### Complessità computazionale del metodo di Newton

Nel metodo di Newton, il costo computazionale per singola iterazione è maggiore rispetto al metodo di bisezione. Questo perché, ad ogni passo, è necessario calcolare sia la funzione $f(x_k)$ sia la sua derivata $f'(x_k)$:

$$
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}
$$

Dal punto di vista del costo, entrambe queste quantità vengono considerate come valutazioni di funzioni non lineari. Anche se $f$ e $f'$ sono diverse, il loro costo computazionale è generalmente comparabile, poiché entrambe richiedono un certo numero di operazioni elementari (eventualmente tramite approssimazioni numeriche).

Di conseguenza, ogni iterazione del metodo di Newton richiede circa **due valutazioni di funzione**, contro una sola nel metodo di bisezione.

Tuttavia, questa maggiore complessità per iterazione è compensata dal fatto che il metodo di Newton converge molto più rapidamente. In particolare, quando le condizioni sono favorevoli, la convergenza è **quadratica**, il che significa che il numero di cifre corrette raddoppia (circa) ad ogni iterazione.

In termini complessivi, si ha quindi un compromesso:
il metodo di Newton ha iterazioni più costose, ma ne richiede molte meno rispetto ai metodi dicotomici. Per questo motivo, quando converge, risulta generalmente molto più efficiente del metodo di bisezione.

---

#### Covergenza del metodo di newton

Il metodo di Newton è molto più veloce rispetto ai metodi dicotomici: quando converge, lo fa tipicamente con **convergenza quadratica**, cioè l’errore viene (approssimativamente) elevato al quadrato ad ogni iterazione.

Tuttavia, a differenza della bisezione, il metodo **non garantisce sempre la convergenza**: una scelta non adeguata del punto iniziale o particolari caratteristiche della funzione (ad esempio derivata molto piccola o nulla) possono causare divergenza o comportamenti instabili.

---

### Dimostrazione della convergenza quadratica del metodo di Newton

Consideriamo il metodo di Newton definito da:

$$
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}
$$

Vogliamo studiarne la velocità di convergenza verso una radice $x_*$ della funzione $f$, cioè un punto tale che $f(x_*) = 0$.

---

#### Ipotesi

Si assumono le seguenti condizioni:

$$
f \in C^2([a,b]), \quad f'(x) \neq 0 \;\; \forall x \in [a,b], \quad f(a)\cdot f(b) < 0, \quad x_0 \in [a,b]
$$

Sotto queste ipotesi (e assumendo che il metodo converga), esiste una radice $x_* \in [a,b]$ tale che:

$$
\lim_{k \to \infty} x_k = x_*
$$

---

#### Obiettivo

Vogliamo dimostrare che la convergenza è **quadratica**, cioè:

$$
\lim_{k \to \infty} \frac{|x_{k+1} - x_*|}{|x_k - x_*|^2} = C \in \mathbb{R}
$$

---

#### Sviluppo di Taylor

Consideriamo lo sviluppo di Taylor della funzione $f$ centrato in $x_k$, valutato nel punto $x_*$:

$$
f(x_*) = f(x_k) + f'(x_k)(x_* - x_k) + \frac{1}{2}f''(\xi_k)(x_* - x_k)^2
$$

dove $\xi_k$ è un punto compreso tra $x_k$ e $x_*$.

Poiché $x_*$ è una radice, si ha $f(x_*) = 0$, quindi:

$$
0 = f(x_k) + f'(x_k)(x_* - x_k) + \frac{1}{2}f''(\xi_k)(x_* - x_k)^2
$$

---

#### Manipolazione dell’espressione

Isoliamo il termine $\dfrac{f(x_k)}{f'(x_k)}$:

$$
\frac{f(x_k)}{f'(x_k)} = (x_k - x_*) - \frac{1}{2}\frac{f''(\xi_k)}{f'(x_k)}(x_k - x_*)^2
$$

Sostituendo nella formula del metodo di Newton:

$$
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}
$$

si ottiene:

$$
x_{k+1} = x_k - \left[(x_k - x_*) - \frac{1}{2}\frac{f''(\xi_k)}{f'(x_k)}(x_k - x_*)^2 \right]
$$

Semplificando:

$$
x_{k+1} - x_* = \frac{1}{2}\frac{f''(\xi_k)}{f'(x_k)}(x_k - x_*)^2
$$

---

#### Conclusione

Prendendo il valore assoluto:

$$
|x_{k+1} - x_*| = \frac{1}{2}\left|\frac{f''(\xi_k)}{f'(x_k)}\right| |x_k - x_*|^2
$$

Dividendo per $|x_k - x_*|^2$:

$$
\frac{|x_{k+1} - x_*|}{|x_k - x_*|^2} = \frac{1}{2}\left|\frac{f''(\xi_k)}{f'(x_k)}\right|
$$

Poiché $\xi_k$ è compreso tra $x_k$ e $x_*$ e $x_k \to x_*$, segue che:

$$
\lim_{k \to \infty} \xi_k = x_*
$$

Usando la continuità di $f'$ e $f''$, si ottiene:

$$
\lim_{k \to \infty} \frac{|x_{k+1} - x_*|}{|x_k - x_*|^2}
= \frac{1}{2}\left|\frac{f''(x_*)}{f'(x_*)}\right| = C
$$

con $C \in \mathbb{R}$.

---

#### Interpretazione

Questo risultato dimostra che il metodo di Newton ha **convergenza quadratica**: l’errore al passo successivo è proporzionale al quadrato dell’errore corrente.

In termini pratici, quando si è sufficientemente vicini alla soluzione, il numero di cifre corrette raddoppia ad ogni iterazione, rendendo il metodo estremamente efficiente rispetto ai metodi dicotomici.

---

### Condizionamento del problema della ricerca degli zeri

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

#### Relazione tra errore e residuo

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

#### Interpretazione

Questa relazione mostra che la distanza dalla radice dipende non solo dal residuo, ma anche dal valore della derivata prima nel punto $x_*$. In particolare, compare un fattore di amplificazione:

$$
\frac{1}{|f'(x_*)|}
$$

Se $|f'(x_*)|$ è grande, allora il residuo è un buon indicatore della distanza dalla soluzione: piccoli valori di $|f(x)|$ implicano piccoli errori $|x - x_*|$.

Se invece $|f'(x_*)|$ è piccolo, allora il fattore $\frac{1}{|f'(x_*)|}$ diventa grande e può amplificare l’errore: anche un residuo molto piccolo può corrispondere a una distanza significativa dalla radice.

---

#### Problema ben condizionato e mal condizionato

Il problema della ricerca degli zeri si dice:

- **ben condizionato** se $|f'(x_*)|$ non è troppo piccolo  
- **mal condizionato** se $|f'(x_*)|$ è vicino a zero

Dal punto di vista geometrico, il problema è mal condizionato quando la funzione è **molto piatta** in prossimità della radice, cioè quando il grafico è quasi parallelo all’asse delle ascisse nel punto di intersezione.

In questo caso, piccole variazioni nei valori della funzione corrispondono a variazioni molto più grandi nella variabile $x$, rendendo difficile ottenere una buona approssimazione della radice.

---

#### Conclusione

Il residuo $|f(\tilde{x})|$ da solo non è sempre un indicatore affidabile dell’errore $|\tilde{x} - x_*|$. La qualità dell’approssimazione dipende dal condizionamento del problema, cioè dal valore della derivata prima nel punto di soluzione.

In sintesi, un residuo piccolo garantisce una buona approssimazione solo se il problema è ben condizionato.

---

### Metodo delle secanti

Il metodo delle secanti può essere visto come una variante del metodo di Newton in cui la derivata prima $f'(x_k)$ viene approssimata tramite un rapporto incrementale. In questo modo si evita il calcolo esplicito della derivata, rendendo il metodo applicabile anche quando essa non è facilmente disponibile.

La formula iterativa è:

$$
x_{k+1} = x_k - \frac{f(x_k)}{\dfrac{f(x_k) - f(x_{k-1})}{x_k - x_{k-1}}}
$$

che può essere riscritta in forma più compatta come:

$$
x_{k+1} = x_k - f(x_k)\,\frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})}
$$

---

#### Interpretazione geometrica

Il metodo si basa su un’idea geometrica simile a quella della regula falsi: invece di utilizzare la tangente (come in Newton), si considera la **retta secante** passante per i punti:

$$
(x_{k-1}, f(x_{k-1})) \quad \text{e} \quad (x_k, f(x_k))
$$

Il nuovo punto $x_{k+1}$ è l’intersezione tra questa retta e l’asse delle ascisse.

---

#### Struttura iterativa

A differenza del metodo di Newton, che utilizza una sola iterata precedente, il metodo delle secanti ha una **ricorrenza a tre termini**, poiché ogni nuovo valore dipende da:

- $x_{k+1}$ (nuova iterata)
- $x_k$ (iterata precedente)
- $x_{k-1}$ (iterata ancora precedente)

Per questo motivo, il metodo richiede due valori iniziali $x_0$ e $x_1$.

---

#### Proprietà e osservazioni

Il metodo delle secanti non richiede il calcolo della derivata, quindi può essere applicato anche a funzioni semplicemente continue. Tuttavia, è comunque necessario che il denominatore:

$$
f(x_k) - f(x_{k-1}) \neq 0
$$

per evitare problemi numerici.

Dal punto di vista della velocità di convergenza, il metodo è più rapido del metodo di bisezione ma, in generale, meno efficiente del metodo di Newton. La sua convergenza è **superlineare** (con ordine circa $p \approx 1.618$), quindi migliore della convergenza lineare ma inferiore a quella quadratica.

---

#### Conclusione

Il metodo delle secanti rappresenta un buon compromesso tra costo computazionale e velocità di convergenza: elimina la necessità della derivata mantenendo una velocità di convergenza elevata, anche se non garantisce sempre la stessa robustezza dei metodi dicotomici.

---

## Metodi per sistemi nonlineari

### Metodo di Newton (per sistemi nonlineari).
--> *Vedi file su gradienti e jacobiani*

Per estendere il metodo di Newton al caso multidimensionale, consideriamo una funzione vettoriale:

$$
F : \mathbb{R}^n \to \mathbb{R}^n
$$

e vogliamo trovare un vettore $x_* \in \mathbb{R}^n$ tale che:

$$
F(x_*) = 0
$$

---

#### Formula iterativa

Nel caso scalare, il metodo di Newton utilizza la derivata prima. Nel caso multidimensionale, questa viene sostituita dallo **Jacobiano** $J_F(x)$.

La formula del metodo diventa:

$$
d^{(k)} = - J_F(x^{(k)})^{-1} \, F(x^{(k)})
$$

$$
x^{(k+1)} = x^{(k)} + d^{(k)}
$$

Qui $x^{(k)} \in \mathbb{R}^n$ è un vettore, quindi anche:

- $F(x^{(k)}) \in \mathbb{R}^n$ è un vettore (valutazione della funzione),
- $J_F(x^{(k)}) \in \mathbb{R}^{n \times n}$ è una matrice (Jacobiano),
- $d^{(k)} \in \mathbb{R}^n$ è il vettore di aggiornamento.

---

#### Interpretazione come sistema lineare

In pratica, non si calcola esplicitamente l’inversa dello Jacobiano (operazione costosa e numericamente instabile). Si riformula invece il problema come un sistema lineare:

$$
J_F(x^{(k)}) \cdot d^{(k)} = -F(x^{(k)})
$$

In questo modo:

- $J_F(x^{(k)})$ è la matrice dei coefficienti,
- $d^{(k)}$ è il vettore delle incognite,
- $-F(x^{(k)})$ è il vettore dei termini noti.

Ad ogni iterazione si risolve quindi un sistema lineare per determinare la direzione di aggiornamento $d^{(k)}$.

---

#### Interpretazione

Il metodo può essere visto come una generalizzazione naturale del caso scalare: si sostituisce la funzione non lineare con la sua approssimazione lineare (tramite lo Jacobiano) e si risolve il problema linearizzato.

Questo rende il metodo molto potente, ma anche più costoso computazionalmente, poiché ad ogni iterazione è necessario:

- calcolare lo Jacobiano,
- risolvere un sistema lineare.

---

#### Conclusione

Il metodo di Newton multidimensionale mantiene le stesse proprietà teoriche del caso scalare: quando converge, lo fa tipicamente con **convergenza quadratica**, ma richiede buone condizioni iniziali e un Jacobiano non singolare.

È uno strumento fondamentale per la risoluzione di sistemi non lineari.

---

#### Da sistema non lineare a sistema lineare: implementazione

Il problema iniziale consiste nel risolvere un sistema non lineare:

$$
F(x) = 0, \quad x \in \mathbb{R}^n
$$

Il metodo di Newton trasforma questo problema in una successione di sistemi lineari. A partire da un’approssimazione iniziale $x^{(0)}$, ad ogni iterazione si costruisce e si risolve il sistema:

$$
J_F(x^{(k)}) \, d^{(k)} = -F(x^{(k)})
$$

ottenendo così la direzione di aggiornamento $d^{(k)}$, e si aggiorna la soluzione:

$$
x^{(k+1)} = x^{(k)} + d^{(k)}
$$

Questo processo viene ripetuto fino a soddisfare un criterio di arresto (ad esempio $\|F(x^{(k)})\|$ sufficientemente piccolo o variazione tra iterate trascurabile).

---

#### Pseudocodice del metodo di Newton multidimensionale

L’implementazione del metodo può essere descritta in forma compatta come segue:

```py
Input: funzione F, Jacobiano JF, punto iniziale x^(0), tolleranza tol
for k = 0,1,2,...
    calcola F(x^(k)) e JF(x^(k))

    risolvi il sistema lineare:
        JF(x^(k)) * d^(k) = -F(x^(k))

    aggiorna:
        x^(k+1) = x^(k) + d^(k)

    se ||F(x^(k+1))|| < tol:
        termina

    Output: approssimazione x^(k+1)
```

---

## Interpolazione

### Esempi e motivazioni dell’interpolazione

L’interpolazione nasce dall’esigenza di ricostruire informazioni intermedie a partire da dati noti. In molti contesti applicativi non ci interessa solo conoscere uno stato iniziale e uno finale, ma anche descrivere in modo continuo ciò che accade tra questi due estremi.

Un esempio tipico è quello del movimento di un braccio robotico. Date una configurazione iniziale e una finale, vogliamo determinare una sequenza di configurazioni intermedie che descrivano il movimento del braccio nel tempo. In questo modo è possibile ottenere un’animazione fluida (frame intermedi) che rappresenti il passaggio da uno stato all’altro. L’interpolazione permette quindi di costruire una traiettoria continua nello spazio delle configurazioni.

Un altro esempio importante riguarda l’elaborazione delle immagini. Supponiamo di avere una porzione di immagine rappresentata come una matrice di pixel di dimensione $n \times n$. Se vogliamo ingrandire questa immagine, possiamo costruire una nuova matrice più grande, ad esempio di dimensione $m \times m$ con $m = 2n$. Tuttavia, i nuovi pixel introdotti non hanno un valore assegnato.

Il problema diventa quindi quello di determinare i valori dei pixel mancanti in modo coerente con quelli originali. Questo viene fatto tramite tecniche di interpolazione, che stimano i valori ignoti utilizzando l’informazione disponibile nei pixel vicini.

In sintesi, l’interpolazione consente di passare da dati discreti a una rappresentazione più densa o continua, ed è fondamentale in applicazioni come animazioni, simulazioni fisiche e elaborazione di immagini.

---

## Interpolazione polinomiale

Il problema dell’interpolazione consiste nel costruire una funzione che passi esattamente per un insieme finito di punti dati.

I dati in ingresso sono coppie di valori:

$$
(x_i, y_i), \qquad i = 0, \dots, n
$$

dove gli $x_i$ rappresentano le ascisse (tipicamente distinti tra loro) e gli $y_i$ le corrispondenti ordinate.

L’obiettivo è costruire una funzione $g(x)$ tale che:

$$
g(x_i) = y_i \qquad \forall i = 0, \dots, n
$$

cioè una funzione che interpoli esattamente tutti i punti dati.

---

#### Scopo dell’interpolazione

Una volta costruita la funzione $g(x)$, possiamo usarla per stimare valori in punti non noti. Dato un punto $\tilde{x}$ (che non appartiene necessariamente all’insieme $\{x_i\}$), vogliamo determinare:

$$
g(\tilde{x}) = \tilde{y}
$$

In questo modo si ottiene una stima dell’ordinata associata a $\tilde{x}$, basata sull’informazione dei punti noti.

---

#### Idea di base

L’interpolazione consiste quindi nel passare da un insieme discreto di dati a una funzione continua che li descriva. Una volta costruita questa funzione, i valori ignoti vengono determinati semplicemente valutandola nei punti di interesse.

Tuttavia, esiste un aspetto importante: **non esiste un’unica funzione che interpola i dati**. In generale, infinite funzioni possono passare per gli stessi punti.

Per rendere il problema ben posto, è necessario restringere la classe delle funzioni tra cui cercare l’interpolante.

---

#### Scelta della classe di funzioni

Nella maggior parte dei casi si scelgono i **polinomi**, perché:

- sono semplici da gestire dal punto di vista computazionale,
- garantiscono (sotto opportune condizioni) esistenza e unicità della soluzione,
- sono facili da valutare e derivare.

Pertanto, il problema dell’interpolazione si riduce spesso alla costruzione di un polinomio $p(x)$ tale che:

$$
p(x_i) = y_i \qquad \forall i = 0, \dots, n
$$

Questo polinomio è detto **polinomio interpolante** dei dati.

---

#### Intermezzo sui polinomi

Un **polinomio** è una funzione che si scrive come combinazione di monomi, della forma:

$$
p(x) = a_0 + a_1 x + a_2 x^2 + \dots + a_n x^n, \qquad a_0, a_1, \dots, a_n \in \mathbb{R}
$$

dove i coefficienti $a_i$ sono numeri reali e il grado del polinomio è $n$ (supponendo $a_n \neq 0$).

---

#### Perché scegliere i polinomi per l’interpolazione?

I polinomi sono una scelta naturale per l’interpolazione perché possiedono una proprietà fondamentale: sono completamente determinati dai loro coefficienti. Un polinomio di grado al più $n$ è descritto da $n+1$ coefficienti:

$$
a_0, a_1, \dots, a_n
$$

Quindi esiste una corrispondenza tra:

- i $n+1$ dati $(x_i, y_i)$,
- e i $n+1$ coefficienti del polinomio interpolante.

Sotto opportune condizioni (in particolare $x_i$ tutti distinti), è possibile dimostrare che **esiste ed è unico** un polinomio di grado al più $n$ che interpola i dati:

$$
p(x_i) = y_i \qquad \forall i = 0, \dots, n
$$

Dal punto di vista computazionale, il problema dell’interpolazione si riduce quindi a determinare i coefficienti del polinomio. Il risultato del calcolo non è direttamente la funzione, ma un insieme di numeri (i coefficienti) che la identificano completamente.

È importante osservare che il numero di dati $n+1$ coincide con il numero di coefficienti del polinomio, e quindi con il grado massimo del polinomio interpolante.

In sintesi, i polinomi permettono di trasformare il problema dell’interpolazione in un problema algebrico ben posto, con soluzione unica e facilmente rappresentabile.

---

#### Interpolazione polinomiale ed esistenza/unicità

Un risultato fondamentale alla base dell’interpolazione polinomiale è il seguente: dati $n+1$ punti distinti nel piano, esiste **un unico polinomio di grado al più $n$** che passa esattamente per tutti questi punti.

È importante precisare un dettaglio: dati tre punti, esiste un’unica **parabola**, cioè un polinomio di **grado al più 2** (non di terzo grado), che li interpola. Questo risultato si generalizza: dati $n+1$ punti $(x_i, y_i)$ con $x_i$ distinti, esiste ed è unico il polinomio $p_n(x)$ di grado al più $n$ tale che:

$$
p_n(x_i) = y_i \qquad \forall i = 0, \dots, n
$$

---

#### Significato per l’interpolazione

Questo teorema è cruciale perché risolve due problemi:

- tra infinite funzioni possibili, restringiamo la ricerca ai polinomi;
- all’interno dei polinomi, otteniamo una **soluzione unica**.

Quindi il problema dell’interpolazione diventa ben posto: esiste una sola funzione interpolante (nel senso polinomiale) che soddisfa i vincoli.

---

#### Formulazione del problema

Dati i punti:

$$
(x_i, y_i), \qquad i = 0, \dots, n
$$

si vuole determinare un polinomio:

$$
p_n(x) = a_0 + a_1 x + a_2 x^2 + \dots + a_n x^n
$$

tale che valgano le condizioni di interpolazione:

$$
p_n(x_i) = y_i \qquad \forall i = 0, \dots, n
$$

L’obiettivo è quindi determinare i coefficienti:

$$
a_0, a_1, \dots, a_n
$$

---

#### Osservazione

L’interpolazione polinomiale è caratterizzata da due scelte fondamentali:

- si restringe la classe delle funzioni ai polinomi;
- si fissa il grado massimo del polinomio in base al numero di dati.

Queste due restrizioni garantiscono unicità e rendono il problema trattabile sia teoricamente che computazionalmente.

---

#### Interpretazione algebrica

Un polinomio è una combinazione lineare dei monomi:

$$
1, \; x, \; x^2, \; \dots, \; x^n
$$

Pertanto, imporre le condizioni di interpolazione equivale a costruire un sistema lineare in cui le incognite sono i coefficienti $a_0, \dots, a_n$.

Il problema dell’interpolazione polinomiale si riduce quindi alla risoluzione di un sistema lineare con $n+1$ equazioni e $n+1$ incognite, che ammette una soluzione unica (se gli $x_i$ sono distinti).

---

### Metodo dei coefficienti indeterminati

Per costruire il polinomio interpolante, partiamo dalla sua forma generale:

$$
p_n(x) = a_0 + a_1 x + a_2 x^2 + \dots + a_n x^n
$$

e imponiamo che soddisfi le **condizioni di interpolazione**:

$$
p_n(x_i) = y_i \qquad \forall i = 0, \dots, n
$$

che corrispondono a:

$$\begin{aligned}
i=0) &\quad p_n(x_0) = y_0 \;\Leftrightarrow\; a_0 + a_1x_0 + a_2x_0^2 + \dots + a_nx_0^n = y_0 \\
i=1) &\quad p_n(x_1) = y_1 \;\Leftrightarrow\; a_0 + a_1x_1 + a_2x_1^2 + \dots + a_nx_1^n = y_1 \\ 
\dots \\
i=n) &\quad p_n(x_n) = y_n \;\Leftrightarrow\; a_0 + a_1x_n + a_2x_n^2 + \dots + a_nx_n^n = y_n \\ 
\end{aligned}$$


Sostituendo ciascun punto $(x_i, y_i)$ nel polinomio, otteniamo un sistema di $n+1$ equazioni:

$$
\begin{cases}
a_0 + a_1 x_0 + a_2 x_0^2 + \dots + a_n x_0^n = y_0 \\
a_0 + a_1 x_1 + a_2 x_1^2 + \dots + a_n x_1^n = y_1 \\
\vdots \\
a_0 + a_1 x_n + a_2 x_n^2 + \dots + a_n x_n^n = y_n
\end{cases}
$$

In questo sistema:

- i valori $x_i$ e $y_i$ sono dati noti,
- le incognite sono i coefficienti $a_0, a_1, \dots, a_n$.

---

#### Forma matriciale

Il sistema può essere scritto in forma matriciale come:

$$
\boxed{
V \alpha = y
}
$$

dove:

$$
V =
\begin{pmatrix} 
1 & x_0 & x_0^2 & \dots & x_0^n \\
1 & x_1 & x_1^2 & \dots & x_1^n \\
\vdots & \vdots & \vdots & & \vdots \\
1 & x_n & x_n^2 & \dots & x_n^n
\end{pmatrix},
\quad
\alpha =
\begin{pmatrix}
a_0 \\ a_1 \\ \vdots \\ a_n
\end{pmatrix},
\quad
y =
\begin{pmatrix}
y_0 \\ y_1 \\ \vdots \\ y_n
\end{pmatrix}
$$

La matrice $V$ è detta **matrice di Vandermonde**.

---

#### Interpretazione

Il problema dell’interpolazione polinomiale si riduce quindi alla risoluzione di un sistema lineare con $n+1$ equazioni e $n+1$ incognite.

Una volta determinato il vettore dei coefficienti $\alpha$, il polinomio $p_n(x)$ è completamente noto e può essere utilizzato per valutare la funzione in qualsiasi punto.

In altre parole, “costruire la funzione” significa trovare i coefficienti reali che la identificano univocamente.

---

#### Osservazione

Il metodo dei coefficienti indeterminati è concettualmente semplice e diretto, ma presenta limiti pratici: **la matrice di Vandermonde può diventare numericamente instabile per $n$ grande**. Per questo motivo, in pratica si preferiscono altre formulazioni dell’interpolazione (come la forma di Lagrange o di Newton).

---

### Metodo di Lagrange

Un’alternativa al metodo dei coefficienti indeterminati consiste nel rappresentare il polinomio interpolante in una forma diversa, evitando di risolvere esplicitamente il sistema lineare.

L’idea è di non esprimere più il polinomio nella forma canonica:

$$
p_n(x) = a_0 + a_1 x + \dots + a_n x^n
$$

ma come combinazione lineare di una **base diversa di polinomi**, costruita direttamente a partire dai nodi di interpolazione.

---

#### Caso base: interpolazione lineare

Consideriamo due punti $(x_0, y_0)$ e $(x_1, y_1)$. Il polinomio interpolante (retta) può essere scritto come:

$$
p_1(x) = y_0 + (x - x_0)\frac{y_1 - y_0}{x_1 - x_0}
$$

Questa espressione può essere riscritta come combinazione lineare:

$$
p_1(x) = y_0 \underbrace{\frac{x - x_1}{x_0 - x_1}}_{L_0(x)} + 
          y_1 \underbrace{\frac{x - x_0}{x_1 - x_0}}_{L_1(x)}
$$

dove $L_0(x)$ e $L_1(x)$ sono polinomi di grado 1.

---

#### Generalizzazione: polinomio di grado $n$

Nel caso generale, dati $n+1$ punti $(x_i, y_i)$, il polinomio interpolante si scrive come:

$$
p_n(x) = \sum_{i=0}^{n} y_i \, L_i(x)
$$

dove i polinomi $L_i(x)$ costituiscono la **base di Lagrange** e sono definiti come:

$$
L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{x - x_j}{x_i - x_j}
$$

---

#### Proprietà fondamentale

I polinomi di Lagrange sono costruiti in modo tale da soddisfare:

$$
\begin{cases}
L_i(x_i) = 1 \\
L_i(x_j) = 0 \quad \text{per } j \neq i
\end{cases}
$$

Questa proprietà garantisce automaticamente le condizioni di interpolazione:

$$
p_n(x_i) = y_i
$$

Infatti, valutando $p_n(x)$ in $x = x_i$, tutti i termini si annullano tranne quello con indice $i$.

---

#### Interpretazione

In questa formulazione:

- i coefficienti $y_i$ sono noti (sono i dati),
- le funzioni base $L_i(x)$ dipendono solo dai nodi $x_i$ e devono essere costruite.

Il polinomio interpolante è quindi ottenuto come combinazione lineare di queste funzioni base.

---

#### Vantaggi e svantaggi

Questo metodo evita la risoluzione del sistema lineare (e quindi i problemi legati alla matrice di Vandermonde, spesso mal condizionata).

Tuttavia, il costo computazionale può diventare elevato se si calcolano direttamente i prodotti per ogni $L_i(x)$, soprattutto per $n$ grande. Per questo motivo, nella pratica è importante organizzare il calcolo in modo efficiente o utilizzare formulazioni alternative più stabili (come la forma baricentrica).

---

#### Conclusione

Il metodo di Lagrange fornisce una rappresentazione esplicita del polinomio interpolante, concettualmente semplice e teoricamente elegante, che costruisce direttamente la funzione senza passare dalla determinazione dei coefficienti nella base canonica.

---

## Approssimazione dell’interpolazione polinomiale ed errore

### Approssimazione polinomiale

Quando utilizziamo un polinomio interpolante $p(x)$ per approssimare una funzione $f(x)$, è fondamentale capire **quanto le due funzioni siano vicine**. Per farlo, introduciamo il concetto di distanza tra funzioni tramite una norma.

Assumiamo che $f : [a,b] \to \mathbb{R}$ sia continua su un intervallo chiuso e limitato. In questo contesto, possiamo definire la **norma infinito** (o norma uniforme) come:

$$
\|f\|_{\infty} = \max_{x \in [a,b]} |f(x)|
$$

Questa norma misura il valore massimo assoluto assunto dalla funzione nell’intervallo.

---

#### Distanza tra funzione e interpolante

Per confrontare la funzione originale $f$ con il polinomio interpolante $p$, consideriamo la norma della loro differenza:

$$
\|f - p\|_{\infty} = \max_{x \in [a,b]} |f(x) - p(x)|
$$

Questa quantità rappresenta **l’errore massimo** tra le due funzioni sull’intero intervallo.

Se vale:

$$
\|f - p\|_{\infty} < \varepsilon
$$

allora significa che, per ogni $x \in [a,b]$:

$$
|f(x) - p(x)| < \varepsilon
$$

cioè:

$$
f(x) - \varepsilon < p(x) < f(x) + \varepsilon
$$

---

#### Interpretazione geometrica

La norma infinito ha un significato molto intuitivo: rappresenta la **massima distanza verticale** tra i grafici di $f$ e $p$.

Dire che:

$$
\|f - p\|_{\infty} < \varepsilon
$$

significa che il grafico del polinomio $p(x)$ è sempre contenuto in una “fascia” di ampiezza $2\varepsilon$ centrata attorno al grafico di $f(x)$.

---

#### Qualità dell’approssimazione

Più il valore:

$$
\|f - p\|_{\infty}
$$

è piccolo, migliore è l’approssimazione. In altre parole, il polinomio interpolante descrive fedelmente il comportamento della funzione originale su tutto l’intervallo.

Questo concetto è fondamentale perché permette di valutare **globalmente** la bontà dell’interpolazione, e non solo nei punti in cui i due grafici coincidono (i nodi).

---

#### Osservazione

L’interpolazione garantisce che:

$$
p(x_i) = f(x_i)
$$

nei nodi, quindi l’errore è nullo in quei punti. Tuttavia, tra i nodi l’errore può crescere, ed è proprio la norma infinito che ci permette di quantificare il caso peggiore.

---

### Resto di interpolazione

Per studiare l’errore dell’interpolazione polinomiale introduciamo il **resto di interpolazione**, definito come la differenza tra la funzione originale e il polinomio interpolante:

$$
\boxed{
R_n(x) = f(x) - p_n(x)
}
$$

dove $p_n(x)$ è il polinomio interpolante di grado al più $n$, costruito a partire dai nodi $x_0, x_1, \dots, x_n$ tali che:

$$
p_n(x_i) = f(x_i) \qquad \forall i = 0, \dots, n
$$

con:

$$
x_i \in [a,b]
$$

---

#### Interpretazione

Il resto $R_n(x)$ misura, punto per punto, quanto il polinomio si discosta dalla funzione reale. Nei nodi di interpolazione vale:

$$
R_n(x_i) = 0
$$

perché il polinomio interpola esattamente la funzione in quei punti.

Tuttavia, per $x \neq x_i$, il resto può essere diverso da zero, ed è proprio questo comportamento che vogliamo analizzare.

---

#### Errore massimo

Per valutare globalmente l’errore, consideriamo la norma infinito del resto:

$$
\|R_n\|_{\infty} = \max_{x \in [a,b]} |R_n(x)| = \max_{x \in [a,b]} |f(x) - p_n(x)|
$$

Questa quantità rappresenta il **massimo errore di interpolazione** sull’intervallo.

---

#### Significato

Studiare il resto di interpolazione significa capire quanto il polinomio interpolante approssima bene la funzione reale non solo nei nodi, ma su tutto l’intervallo.

In particolare, l’obiettivo è rendere $\|R_n\|_{\infty}$ il più piccolo possibile, scegliendo opportunamente:

- il grado del polinomio,
- la posizione dei nodi $x_i$.

Questo porta naturalmente a problemi più avanzati, come la scelta ottimale dei nodi (ad esempio i nodi di Chebyshev).

---

### Dimostrazione della formula del resto di interpolazione

L’obiettivo è comprendere come si comporta l’errore di interpolazione:

$$
R_n(x) = f(x) - p_n(x)
$$

in funzione di:
- il numero di nodi $n+1$ utilizzati;
- la loro distribuzione nell’intervallo $[a,b]$.

---

#### Ipotesi

Sia $f : [a,b] \to \mathbb{R}$ tale che:

$$
f \in C^{n+1}([a,b])
$$

cioè $f$ è derivabile fino all’ordine $n+1$ con derivate continue. Siano inoltre:

$$
x_0, x_1, \dots, x_n \in [a,b]
$$

i nodi di interpolazione, e $p_n$ il polinomio di grado al più $n$ tale che:

$$
p_n(x_i) = f(x_i) \qquad \forall i = 0,\dots,n
$$

---

#### Teorema (formula del resto)

Per ogni $x \in [a,b]$ esiste un punto $\xi = \xi(x) \in [a,b]$ tale che:

$$
\boxed{
R_n(x) = \frac{(x - x_0)(x - x_1)\cdots(x - x_n)}{(n+1)!}\, f^{(n+1)}(\xi)
}
$$

---

#### Interpretazione della formula

Introduciamo il polinomio:

$$
\omega_{x_0,\dots,x_n}(x) = (x - x_0)(x - x_1)\cdots(x - x_n)
$$

che è un polinomio di grado $n+1$ con coefficiente principale pari a $1$.

Questo polinomio si annulla nei nodi:

$$
\omega_{x_0,\dots,x_n}(x_i) = 0
$$

e rappresenta la parte dell’errore che dipende **solo dalla scelta dei nodi**.

La formula del resto può quindi essere scritta come:

$$
R_n(x) = \frac{\omega_{x_0,\dots,x_n}(x)}{(n+1)!}\, f^{(n+1)}(\xi)
$$

---

#### Idea della dimostrazione

Si costruisce una funzione ausiliaria:

$$
\Omega(x,t) = R_n(t)\,\omega(x) - R_n(x)\,\omega(t)
$$

fissato $x$, si considera $\Omega(x,t)$ come funzione della variabile $t$.

Questa funzione si annulla in $n+2$ punti:
- nei nodi $t = x_i$, perché $R_n(x_i) = 0$;
- nel punto $t = x$.

Applicando ripetutamente il **teorema di Rolle**, si dimostra che esiste $\xi$ tale che:

$$
\frac{d^{n+1}}{dt^{n+1}} \Omega(x,t)\Big|_{t=\xi} = 0
$$

da cui si ricava la formula del resto.

---

#### Stima dell’errore (norma infinito)

Prendendo il valore assoluto:

$$
|R_n(x)| = \left| \frac{\omega(x)}{(n+1)!} f^{(n+1)}(\xi) \right|
$$

e facendo il massimo su $[a,b]$:

$$
\|R_n\|_{\infty} = \max_{x \in [a,b]} |R_n(x)|
\le
\frac{\max_{x \in [a,b]} |\omega(x)|}{(n+1)!}
\cdot
\max_{x \in [a,b]} |f^{(n+1)}(x)|
$$

Se definiamo:

$$
M_{n+1} = \max_{x \in [a,b]} |f^{(n+1)}(x)|
$$

e:

$$
\omega^* = \max_{x \in [a,b]} |\omega(x)|
$$

otteniamo la stima:

$$
\boxed{
\|R_n\|_{\infty} \le \frac{\omega^*}{(n+1)!} \, M_{n+1}
}
$$

---

#### Osservazioni fondamentali

L’errore dipende da due fattori distinti:

La quantità:

$$
M_{n+1}
$$

dipende solo dalla funzione $f$ e misura quanto è “irregolare” (quanto cresce la derivata di ordine alto).

La quantità:

$$
\omega^* = \max_{x \in [a,b]} |\omega(x)|
$$

dipende solo dai nodi di interpolazione.

---

#### Conseguenza importante

Non basta aumentare il numero di nodi per migliorare l’approssimazione: è fondamentale **scegliere bene i nodi**.

Infatti, per nodi equispaziati, $\omega(x)$ può diventare molto grande (fenomeno di Runge), peggiorando l’errore.

Una scelta ottimale consiste nei **nodi di Chebyshev**, che minimizzano il massimo di $|\omega(x)|$ e quindi riducono l’errore globale.

---

### Ripasso sull’interpolazione polinomiale e resto di interpolazione

Sia data una funzione

$$
f : [a,b] \to \mathbb{R}
$$

e siano fissati $n+1$ nodi distinti

$$
x_0, x_1, \dots, x_n \in [a,b].
$$

Esiste ed è unico il polinomio interpolante $p_n(x)$ di grado al più $n$ tale che

$$
p_n(x_i)=f(x_i)\qquad \forall i=0,\dots,n.
$$

Definiamo **resto di interpolazione** (o errore di interpolazione puntuale) la funzione

$$
R_n(x)=f(x)-p_n(x).
$$

Questa quantità misura, punto per punto, quanto il polinomio interpolante si discosta dalla funzione originale.

---

#### Formula del resto di interpolazione

Dal teorema dimostrato sul resto di interpolazione sappiamo che, per ogni $x\in[a,b]$, esiste un punto

$$
\xi=\xi(x)\in[a,b]
$$

tale che

$$
R_n(x)=\frac{\omega_{x_0,\dots,x_n}(x)}{(n+1)!}\,f^{(n+1)}(\xi),
$$

dove

$$
\omega_{x_0,\dots,x_n}(x)=(x-x_0)(x-x_1)\cdots(x-x_n)
$$

è il **polinomio nodale**, polinomio di grado $n+1$ che si annulla esattamente nei nodi di interpolazione.

---

#### Stima dell’errore

Supponiamo che

$$
f\in C^{n+1}([a,b]),
$$

cioè che $f$ abbia derivata $(n+1)$-esima continua nell’intervallo. Essendo continua su un compatto, tale derivata ammette massimo assoluto:

$$
M_{n+1}^f=\max_{x\in[a,b]}|f^{(n+1)}(x)|.
$$

Prendendo il valore assoluto nella formula del resto otteniamo:

$$
|R_n(x)|
=
\left|
\frac{\omega_{x_0,\dots,x_n}(x)}{(n+1)!}\,f^{(n+1)}(\xi)
\right|
$$

e quindi la stima

$$
|R_n(x)|
\le
\frac{|\omega_{x_0,\dots,x_n}(x)|}{(n+1)!}\,M_{n+1}^f.
$$

---

#### Interpretazione della stima

Questa disuguaglianza è fondamentale perché mostra che l’errore di interpolazione dipende essenzialmente da due fattori:

$$
|R_n(x)| \lesssim
\frac{M_{n+1}^f}{(n+1)!}\,|\omega_{x_0,\dots,x_n}(x)|.
$$

In molti casi pratici questa stima descrive bene anche il comportamento qualitativo dell’errore, cioè il resto si comporta **come se fosse proporzionale** al polinomio nodale $\omega$.

La costante di proporzionalità è circa

$$
\frac{M_{n+1}^f}{(n+1)!}.
$$

Questo significa che:

- se $\omega(x)$ oscilla molto, anche l’errore tenderà a oscillare molto;
- se $\omega(x)$ assume valori grandi, anche l’errore potrà diventare grande.

---

#### Collegamento con il fenomeno di Runge

Il fenomeno di Runge si manifesta quando il polinomio interpolante oscilla fortemente, specialmente vicino agli estremi dell’intervallo.

Dalla formula dell’errore si capisce che il principale responsabile di questo comportamento è proprio il polinomio nodale

$$
\omega_{x_0,\dots,x_n}(x).
$$

Infatti, scegliendo male i nodi (ad esempio nodi equispaziati), il polinomio $\omega$ può crescere molto vicino agli estremi, causando un grande errore di interpolazione.

Per ridurre questo effetto occorre scegliere i nodi in modo più opportuno, ad esempio utilizzando i **nodi di Chebyshev**, che minimizzano il massimo valore assoluto del polinomio nodale.

---

#### Conclusione

Il fenomeno di Runge è dovuto principalmente a due fattori strettamente collegati:

1. La **scelta dei nodi di interpolazione**, che influenza la forma del polinomio nodale.

2. Il comportamento del **polinomio nodale**

    $$
    \omega_{x_0,\dots,x_n}(x),
    $$

    che determina direttamente l’andamento dell’errore di interpolazione.

Per questo motivo, nell’interpolazione polinomiale non conta solo quanti punti si usano, ma soprattutto **dove vengono scelti**.

---

## Interpolazione a Tratti

### Altri metodi di interpolazione

L’interpolazione polinomiale globale presenta alcuni limiti pratici importanti.

Il primo inconveniente è che il grado del polinomio interpolante cresce con il numero dei nodi: se si vogliono interpolare molti punti, si è costretti a costruire un polinomio di grado elevato. Questo può portare sia a problemi numerici sia a oscillazioni indesiderate, come nel fenomeno di Runge.

Un secondo limite è che l’interpolazione polinomiale classica richiede di conoscere **tutti i punti fin dall’inizio**. Se nuovi dati vengono aggiunti successivamente, in generale occorre ricostruire completamente il polinomio interpolante.

---

### Idea dell'Interpolazione a Tratti

Per superare questi problemi si può rinunciare a costruire un unico polinomio globale e utilizzare invece **più polinomi locali**, ciascuno valido solo su una parte dell’intervallo.

L’idea più semplice consiste nel collegare ogni coppia di punti consecutivi con un segmento, ottenendo una funzione spezzata che interpola tutti i dati.

Questa funzione **non è un polinomio globale** su tutto l’intervallo, ma possiede una struttura polinomiale locale: se la si restringe a uno specifico sottointervallo, allora coincide con un polinomio di grado 1.

In altre parole, l’interpolazione a tratti costruisce una funzione che è:

- globalmente una funzione spezzata;
- localmente, su ciascun intervallo, un polinomio.

---

#### Vantaggio principale

Il vantaggio fondamentale è che **il numero di nodi viene disaccoppiato dal grado dei polinomi utilizzati**.

Con l’interpolazione polinomiale globale:

$$
n+1 \text{ nodi } \Rightarrow \text{ polinomio di grado } n
$$

Con l’interpolazione lineare a tratti:

$$
n+1 \text{ nodi } \Rightarrow n \text{ polinomi di grado } 1
$$

Quindi anche con moltissimi punti si continua a lavorare con polinomi semplici.

---

#### Suddivisione dell’intervallo

Supponiamo di avere nodi ordinati:

$$
x_0 < x_1 < \cdots < x_n
$$

Essi suddividono l’intervallo complessivo nei sottointervalli:

$$
I_i = [x_i, x_{i+1}], \qquad i=0,\dots,n-1
$$

Su ciascun intervallo $I_i$ costruiremo un interpolante locale.

---

#### Come si valuta l’interpolante a tratti

Per calcolare il valore dell’interpolante in un punto $x$:

Si individua anzitutto il sottointervallo $I_j$ tale che

$$
x \in [x_j, x_{j+1}]
$$

Successivamente si utilizza il polinomio locale associato a quell’intervallo, cioè la retta passante per i punti:

$$
(x_j, y_j), \qquad (x_{j+1}, y_{j+1})
$$

---

#### Formula dell’interpolante lineare locale

La retta interpolante sul sottointervallo $I_i=[x_i,x_{i+1}]$ è:

$$
p_i(x)=
y_i+
\frac{y_{i+1}-y_i}{x_{i+1}-x_i}(x-x_i)
$$

oppure, in forma equivalente:

$$
p_i(x)=
y_i\frac{x-x_{i+1}}{x_i-x_{i+1}}
+
y_{i+1}\frac{x-x_i}{x_{i+1}-x_i}
$$

Questa formula vale solo per:

$$
x\in[x_i,x_{i+1}]
$$

---

#### Osservazione finale

L’interpolazione a tratti produce quindi una funzione definita **pezzo per pezzo**, dove ogni pezzo ha una propria formula.

Questo significa che non esiste un’unica espressione valida su tutto l’intervallo, ma una famiglia di polinomi locali:

$$
p_0(x),\,p_1(x),\,\dots,\,p_{n-1}(x)
$$

ciascuno associato al proprio sottointervallo.

L’idea fondamentale è che si sacrifica la semplicità di avere un unico polinomio globale, in cambio di una maggiore stabilità numerica e di una migliore gestione di grandi quantità di dati.

---

### Interpolazione lineare a tratti: proprietà ed errore

Un importante vantaggio dell’interpolazione lineare a tratti è che **non soffre del fenomeno di Runge**.

A differenza dell’interpolazione polinomiale globale, la sua stabilità non peggiora al crescere del numero dei nodi e dipende molto meno dalla loro posizione.

Sia data una funzione

$$
f:[a,b]\to\mathbb{R}, \qquad f\in C^2([a,b])
$$

e siano fissati nodi ordinati

$$
a=x_0<x_1<\dots<x_m<x_{m+1}=b.
$$

Indichiamo con $s(x)$ l’interpolante lineare a tratti, cioè la funzione spezzata tale che

$$
s(x_i)=f(x_i)\qquad i=0,\dots,m+1.
$$

Assumiamo quindi che i dati interpolati provengano dal grafico della funzione $f$.

---

#### Resto di interpolazione lineare

Definiamo il resto (errore) dell’interpolazione lineare a tratti come

$$
R^s(x)=s(x)-f(x).
$$

Poiché $s(x)$ è definita a tratti, anche l’analisi dell’errore deve essere fatta **localmente su ciascun sottointervallo**.

Fissiamo quindi un intervallo della partizione:

$$
x\in[x_i,x_{i+1}].
$$

Su questo intervallo, $s(x)$ coincide con la retta interpolante i due punti estremi:

$$
s(x)=f(x_i)+\frac{f(x_{i+1})-f(x_i)}{x_{i+1}-x_i}(x-x_i).
$$

---

#### Formula del resto locale

Poiché su $[x_i,x_{i+1}]$ stiamo interpolando con un polinomio di grado 1, possiamo applicare la formula generale del resto di interpolazione con $n=1$.

Otteniamo quindi che esiste un punto

$$
\xi_i\in[x_i,x_{i+1}]
$$

tale che

$$
R^s(x)=s(x)-f(x)
=
\frac{(x-x_i)(x-x_{i+1})}{2}\,f''(\xi_i).
$$

Questa è la formula esatta dell’errore dell’interpolazione lineare su ciascun intervallo.

---

#### Stima dell’errore

Passando al valore assoluto:

$$
|R^s(x)|
=
\frac{|(x-x_i)(x-x_{i+1})|}{2}\,|f''(\xi_i)|.
$$

Poiché $f''$ è continua su $[a,b]$, esiste il massimo assoluto:

$$
M_2^f=\max_{x\in[a,b]}|f''(x)|.
$$

Quindi:

$$
|R^s(x)|
\le
\frac{|(x-x_i)(x-x_{i+1})|}{2}\,M_2^f.
$$

Osserviamo che per $x\in[x_i,x_{i+1}]$ vale:

$$
x-x_i\ge 0,\qquad x-x_{i+1}\le 0,
$$

perciò:

$$
|(x-x_i)(x-x_{i+1})|
=
(x-x_i)(x_{i+1}-x).
$$

Otteniamo dunque:

$$
|R^s(x)|
\le
\frac{(x-x_i)(x_{i+1}-x)}{2}\,M_2^f.
$$

---

#### Massimo del termine geometrico

Studiamo la funzione

$$
\phi(x)=(x-x_i)(x_{i+1}-x)
$$

nell’intervallo $[x_i,x_{i+1}]$.

Essa è una parabola concava con massimo nel punto medio:

$$
\tilde x=\frac{x_i+x_{i+1}}{2}.
$$

Il valore massimo vale:

$$
\phi(\tilde x)
=
\left(\frac{x_{i+1}-x_i}{2}\right)^2
=
\frac{(x_{i+1}-x_i)^2}{4}.
$$

Sostituendo nella stima precedente:

$$
|R^s(x)|
\le
\frac{1}{2}\cdot\frac{(x_{i+1}-x_i)^2}{4}\,M_2^f
=
\frac{(x_{i+1}-x_i)^2}{8}\,M_2^f.
$$

Quindi:

$$
\boxed{
|R^s(x)|
\le
\frac{(x_{i+1}-x_i)^2}{8}\,M_2^f
\qquad x\in[x_i,x_{i+1}]
}
$$

---

#### Caso di nodi equispaziati

Se i nodi sono equispaziati, cioè

$$
x_{i+1}-x_i=h
$$

per ogni $i$, allora la stima si semplifica in:

$$
\boxed{
|R^s(x)|
\le
\frac{h^2}{8}\,M_2^f
\qquad \forall x\in[a,b]
}
$$

---

#### Interpretazione della stima

Questa formula mostra che:

$$
|R^s(x)|=\mathcal O(h^2).
$$

Quindi l’errore dell’interpolazione lineare a tratti decresce quadraticamente con la distanza tra i nodi.

In particolare:

- dimezzando la distanza $h$ tra i nodi,
- l’errore si riduce di circa un fattore 4.

---

#### Perché non compare il fenomeno di Runge

A differenza dell’interpolazione polinomiale globale:

- ogni errore locale dipende solo dalla lunghezza del singolo intervallo;
- non compare alcun polinomio nodale globale che possa oscillare molto;
- l’errore è controllato uniformemente da $h^2$.

Per questo motivo l’interpolazione lineare a tratti è **stabile** e non può manifestare il fenomeno di Runge.

---

