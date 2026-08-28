# Minimi quadrati non lineari e metodo del gradiente

## Minimi quadrati non lineari

Nel criterio dei minimi quadrati si parte dall'ipotesi che i dati sperimentali siano descrivibili, almeno approssimativamente, attraverso una funzione $f$ dipendente da un insieme di parametri incogniti.

Supponiamo di avere $m$ dati sperimentali

$$
(x^{(i)},y_i),
\qquad i=1,\dots,m
$$

e una funzione modello

$$
f(\alpha_0,\dots,\alpha_{n-1};x)
$$

dipendente dai parametri $\alpha_0,\dots,\alpha_{n-1}$. L'obiettivo è trovare i valori dei parametri tali che

$$
f(\alpha_0,\dots,\alpha_{n-1};x^{(i)})\simeq y_i
$$

per tutti i dati disponibili.

Per misurare quanto il modello si discosta dai dati si considera la somma dei quadrati dei residui:

$$
\boxed{
F(\alpha_0,\dots,\alpha_{n-1})
=
\sum_{i=1}^{m}
\left(
f(\alpha_0,\dots,\alpha_{n-1};x^{(i)})-y_i
\right)^2
}
$$

Il criterio dei minimi quadrati consiste quindi nello scegliere i parametri che rendono minima questa funzione.

Se il modello è **lineare rispetto ai parametri**, il problema può essere scritto nella forma

$$
F(\alpha)=\|A\alpha-y\|_2^2
$$

e si parla di **minimi quadrati lineari**.

Se invece la funzione $f$ dipende **non linearmente dai parametri**, in generale non è possibile riscrivere il problema nella forma

$$
F(\alpha)=\|A\alpha-y\|_2^2
$$

con una matrice $A$ indipendente dai parametri. Si ottiene quindi un problema di **minimi quadrati non lineari**.

Un esempio è il modello esponenziale

$$
f(\alpha_0,\alpha_1;x)
=
\alpha_0e^{\alpha_1x}
$$

dove il parametro $\alpha_1$ compare all'interno dell'esponenziale. Non è quindi possibile raccogliere i parametri in un prodotto matrice-vettore lineare.

Il problema diventa in generale un problema di ottimizzazione non lineare:

$$
\boxed{
\min_{\alpha\in\mathbb R^n}F(\alpha)
}
$$

La funzione $F:\mathbb R^n\to\mathbb R$ viene chiamata **funzione obiettivo**.

---

## Problemi di minimo e problemi di massimo

Un problema di minimo consiste nel cercare il punto $\alpha$ in cui la funzione obiettivo assume il valore più piccolo possibile.

Un punto $\alpha^*\in\mathbb R^n$ è un **punto di minimo locale** per $F:\mathbb R^n\to\mathbb R$ se esiste $\varepsilon>0$ tale che

$$
F(\alpha^*)\leq F(\alpha)
$$

per ogni punto $\alpha$ appartenente alla palla centrata in $\alpha^*$ di raggio $\varepsilon$, cioè

$$
\boxed{
F(\alpha^*)\leq F(\alpha)
\qquad
\forall\alpha\in
\left\{
z\in\mathbb R^n:
\|z-\alpha^*\|_2\leq\varepsilon
\right\}
}
$$

In altre parole, $\alpha^*$ è un minimo locale se, considerando solamente i punti sufficientemente vicini ad $\alpha^*$, nessuno di essi produce un valore della funzione inferiore a $F(\alpha^*)$.

Se invece vale

$$
F(\alpha^*)\leq F(\alpha)
\qquad
\forall\alpha\in\mathbb R^n
$$

allora $\alpha^*$ è un **punto di minimo globale**.

Un minimo locale quindi riguarda soltanto un intorno del punto, mentre un minimo globale riguarda tutto il dominio.

Non è in generale garantito che un minimo esista, né che sia unico.

Un problema di minimo può essere trasformato in modo equivalente in un problema di massimo considerando la funzione opposta:

$$
\boxed{
\min_{\alpha\in\mathbb R^n}F(\alpha)
\quad\Longleftrightarrow\quad
\max_{\alpha\in\mathbb R^n}-F(\alpha)
}
$$

Infatti, i punti che minimizzano $F$ sono esattamente i punti che massimizzano $-F$. Il valore del massimo di $-F$ è l'opposto del valore del minimo di $F$.

---

# Condizioni di ottimalità

Per costruire algoritmi di ottimizzazione è importante capire quali proprietà deve soddisfare un punto di minimo.

## Caso di una variabile: teorema di Fermat

Consideriamo inizialmente una funzione

$$
F:\mathbb R\to\mathbb R
$$

e supponiamo che sia differenziabile.

Il **teorema di Fermat** afferma che se $\alpha^*$ è un punto di minimo locale interno al dominio, allora

$$
\boxed{
F'(\alpha^*)=0
}
$$

Questa è una **condizione necessaria** per l'ottimalità.

Di conseguenza, per cercare i possibili punti di minimo possiamo cercare le soluzioni dell'equazione

$$
F'(\alpha)=0
$$

Tuttavia, è importante capire che questa condizione non è sufficiente in generale.

Infatti, un punto in cui

$$
F'(\alpha)=0
$$

non è necessariamente un punto di minimo. Può essere, ad esempio, un punto di massimo oppure un punto stazionario che non è né massimo né minimo.

Le soluzioni dell'equazione

$$
F'(\alpha)=0
$$

sono chiamate **punti stazionari**.

Quindi:

$$
\boxed{
\text{minimo locale}
\Longrightarrow
\text{punto stazionario}
}
$$

ma, in generale,

$$
\boxed{
\text{punto stazionario}
\not\Longrightarrow
\text{minimo locale}
}
$$

Per ottenere condizioni più forti è necessario introdurre il concetto di **convessità**.

---

# Funzioni convesse

Una funzione $F:\mathbb R^n\to\mathbb R$ è detta **convessa** se, per ogni $z_1,z_2\in\mathbb R^n$ e per ogni $\lambda\in[0,1]$, vale

$$
\boxed{
F\left(\lambda z_1+(1-\lambda)z_2\right)
\leq
\lambda F(z_1)+(1-\lambda)F(z_2)
}
$$

Geometricamente, questa proprietà significa che il grafico della funzione si trova al di sotto del segmento che congiunge due suoi punti.

Nel caso particolare di una funzione di una variabile due volte continuamente derivabile,

$$
F:\mathbb R\to\mathbb R
$$

la convessità può essere verificata attraverso la derivata seconda:

$$
\boxed{
F\text{ convessa}
\quad\Longleftrightarrow\quad
F''(\alpha)\geq0
\quad\forall\alpha\in\mathbb R
}
$$

È importante osservare che la condizione corretta è $F''(\alpha)\geq0$, non necessariamente $F''(\alpha)>0$.

---

## Minimo locale e globale per funzioni convesse

La convessità rende molto più semplice il problema di ottimizzazione.

Se $F$ è convessa e $\alpha^*$ è un punto di minimo locale, allora $\alpha^*$ è automaticamente anche un punto di minimo globale.

Quindi:

$$
\boxed{
F\text{ convessa}
\quad\Longrightarrow\quad
\text{ogni minimo locale è globale}
}
$$

Inoltre, se $F$ è convessa e differenziabile, la condizione di Fermat diventa anche sufficiente:

$$
\boxed{
\alpha^*\text{ è minimo globale}
\quad\Longleftrightarrow\quad
F'(\alpha^*)=0
}
$$

Pertanto, per una funzione convessa differenziabile, i punti di minimo coincidono esattamente con i punti stazionari.

Bisogna però distinguere la convessità dall'esistenza del minimo. Una funzione può essere convessa senza possedere un punto di minimo. Ad esempio,

$$
F(\alpha)=e^\alpha
$$

è convessa, ma non raggiunge mai il proprio estremo inferiore: infatti

$$
\lim_{\alpha\to-\infty}e^\alpha=0
$$

ma $e^\alpha>0$ per ogni $\alpha\in\mathbb R$.

---

# Gradiente e teorema di Fermat in $\mathbb R^n$

Il teorema di Fermat si estende direttamente a più dimensioni.

Se $F$ ha derivate parziali continue e $\alpha^*$ è un punto di minimo locale, allora

$$
\boxed{
\nabla F(\alpha^*)=0
}
$$

Quindi tutti i punti di minimo sono soluzioni del sistema di equazioni

$$
\boxed{
\nabla F(\alpha)=0
}
$$

Anche in questo caso, però, l'implicazione inversa non vale in generale.

Le soluzioni del sistema

$$
\nabla F(\alpha)=0
$$

sono i **punti stazionari** della funzione.

Pertanto:

$$
\boxed{
\text{minimo}
\Longrightarrow
\text{punto stazionario}
}
$$

ma

$$
\boxed{
\text{punto stazionario}
\not\Longrightarrow
\text{minimo}
}
$$

Per funzioni convesse e differenziabili, invece, vale

$$
\boxed{
\nabla F(\alpha^*)=0
\quad\Longleftrightarrow\quad
\alpha^*\text{ è un punto di minimo globale}
}
$$

---

# Esempio: modello esponenziale

Consideriamo il modello non lineare

$$
f(\alpha_0,\alpha_1;x)
=
\alpha_0e^{\alpha_1x}
$$

e i dati

$$
(x_i,y_i),
\qquad i=1,\dots,m.
$$

La funzione obiettivo dei minimi quadrati è

$$
\boxed{
F(\alpha_0,\alpha_1)
=
\sum_{i=1}^{m}
\left(
\alpha_0e^{\alpha_1x_i}-y_i
\right)^2
}
$$

Vogliamo trovare i valori di $\alpha_0$ e $\alpha_1$ che minimizzano $F$.

Calcoliamo le derivate parziali.

Per $\alpha_0$ otteniamo

$$
\frac{\partial F}{\partial\alpha_0}
=
2\sum_{i=1}^{m}
\left(
\alpha_0e^{\alpha_1x_i}-y_i
\right)e^{\alpha_1x_i}
$$

mentre per $\alpha_1$:

$$
\frac{\partial F}{\partial\alpha_1}
=
2\sum_{i=1}^{m}
\left(
\alpha_0e^{\alpha_1x_i}-y_i
\right)
\alpha_0x_i e^{\alpha_1x_i}
$$

Il punto di minimo deve quindi soddisfare

$$
\nabla F(\alpha_0,\alpha_1)=0
$$

ossia il sistema

$$
\begin{cases}
\displaystyle
2\sum_{i=1}^{m}
\left(
\alpha_0e^{\alpha_1x_i}-y_i
\right)e^{\alpha_1x_i}
=0
\\[3mm]
\displaystyle
2\sum_{i=1}^{m}
\left(
\alpha_0e^{\alpha_1x_i}-y_i
\right)
\alpha_0x_i e^{\alpha_1x_i}
=0
\end{cases}
$$

Il fattore $2$ può essere eliminato, ottenendo

$$
\boxed{
\begin{cases}
\displaystyle
\sum_{i=1}^{m}
\left(
\alpha_0e^{\alpha_1x_i}-y_i
\right)e^{\alpha_1x_i}
=0
\\[3mm]
\displaystyle
\sum_{i=1}^{m}
\left(
\alpha_0e^{\alpha_1x_i}-y_i
\right)
\alpha_0x_i e^{\alpha_1x_i}
=0
\end{cases}
}
$$

Abbiamo quindi trasformato il problema di minimizzazione in un **sistema di equazioni non lineari**.

Questo è un punto fondamentale: nel caso dei minimi quadrati lineari potevamo ricondurci alla soluzione di un sistema lineare, mentre nei minimi quadrati non lineari dobbiamo generalmente risolvere un problema di ottimizzazione non lineare.

---

# Metodo del gradiente

Consideriamo il problema generale

$$
\boxed{
\min_{\alpha\in\mathbb R^n}F(\alpha)
}
$$

e supponiamo di avere un punto iniziale

$$
\alpha^{(0)}\in\mathbb R^n.
$$

Il **metodo del gradiente**, detto anche **metodo della discesa del gradiente**, costruisce una successione di punti

$$
\alpha^{(0)},\alpha^{(1)},\alpha^{(2)},\dots
$$

attraverso la formula ricorsiva

$$
\boxed{
\alpha^{(k+1)}
=
\alpha^{(k)}
-
\gamma_k\nabla F(\alpha^{(k)})
}
$$

dove

$$
\gamma_k>0
$$

è chiamato **parametro di lunghezza di passo** (*steplength*).

L'idea geometrica è semplice. Il gradiente $\nabla F(\alpha)$ indica la direzione di massima crescita della funzione. Di conseguenza, la direzione opposta

$$
-\nabla F(\alpha)
$$

è la direzione di massima discesa locale.

Il metodo parte quindi da $\alpha^{(0)}$, calcola il gradiente nel punto corrente e si sposta nella direzione opposta al gradiente:

$$
\alpha^{(k)}
\longrightarrow
\alpha^{(k+1)}
=
\alpha^{(k)}
-
\gamma_k\nabla F(\alpha^{(k)})
$$

Il parametro $\gamma_k$ determina quanto ci si sposta lungo questa direzione.

Se il passo è troppo piccolo, il metodo può procedere molto lentamente. Se il passo è troppo grande, invece, il metodo può oscillare o addirittura non convergere.

Esistono principalmente due possibilità.

Nel **metodo a passo fisso** si utilizza sempre lo stesso valore:

$$
\boxed{
\gamma_k=\gamma
\qquad\forall k
}
$$

Nel **metodo a passo variabile**, invece, il valore può cambiare a ogni iterazione:

$$
\gamma_0,\gamma_1,\gamma_2,\dots
$$

---

# Perché ci si muove nella direzione opposta al gradiente?

Per comprendere il metodo del gradiente consideriamo inizialmente il caso di una variabile.

Supponiamo di trovarci nel punto $\alpha$ e di volerci spostare di una quantità $\gamma$ nella direzione $d$.

Consideriamo quindi

$$
F(\alpha+\gamma d).
$$

Se scegliamo

$$
d=-F'(\alpha),
$$

lo spostamento avviene nella direzione opposta alla derivata.

In particolare, se $\gamma$ è sufficientemente piccolo, questo spostamento produce una diminuzione del valore della funzione:

$$
\boxed{
F(\alpha-\gamma F'(\alpha))<F(\alpha)
}
$$

purché siano soddisfatte opportune ipotesi sulla funzione e sul valore di $\gamma$.

In più dimensioni il ragionamento è identico, sostituendo la derivata con il gradiente:

$$
\boxed{
F(\alpha-\gamma\nabla F(\alpha))
<
F(\alpha)
}
$$

per un passo $\gamma$ sufficientemente piccolo.

Questa è la **proprietà di discesa** del metodo del gradiente.

---

# Gradiente Lipschitziano

Per studiare in modo rigoroso la scelta della lunghezza di passo si introduce il concetto di **Lipschitzianità del gradiente**.

Si dice che il gradiente di $F$ è Lipschitziano di costante $L>0$ se

$$
\boxed{
\|\nabla F(u)-\nabla F(v)\|_2
\leq
L\|u-v\|_2
\qquad
\forall u,v\in\mathbb R^n
}
$$

Intuitivamente, questa condizione impedisce al gradiente di cambiare troppo rapidamente.

La costante $L$ fornisce quindi una misura di quanto rapidamente può variare il gradiente della funzione.

Sotto questa ipotesi si può dimostrare la seguente disuguaglianza:

$$
F(\alpha-\gamma\nabla F(\alpha))
\leq
F(\alpha)
-
\gamma
\left(
1-\frac{L\gamma}{2}
\right)
\|\nabla F(\alpha)\|_2^2
$$

Questa relazione mostra direttamente quando il metodo produce una diminuzione della funzione.

Se

$$
1-\frac{L\gamma}{2}>0,
$$

allora

$$
\gamma<\frac{2}{L}.
$$

Pertanto, per

$$
\boxed{
0<\gamma<\frac{2}{L}
}
$$

si ottiene, quando $\nabla F(\alpha)\neq0$,

$$
\boxed{
F(\alpha-\gamma\nabla F(\alpha))
<
F(\alpha)
}
$$

Quindi, se il passo è sufficientemente piccolo, muoversi nella direzione opposta al gradiente garantisce una diminuzione della funzione obiettivo.

---

# Convergenza del metodo del gradiente

Consideriamo il metodo a passo fisso

$$
\boxed{
\alpha^{(k+1)}
=
\alpha^{(k)}
-
\gamma\nabla F(\alpha^{(k)})
}
$$

e supponiamo che:

$$
F:\mathbb R^n\to\mathbb R
$$

sia continuamente differenziabile, che possieda almeno un punto di minimo e che il gradiente sia Lipschitziano con costante $L$.

Se scegliamo

$$
\boxed{
0<\gamma<\frac{2}{L}
}
$$

allora ogni iterazione, quando il gradiente non è nullo, produce una diminuzione della funzione obiettivo.

In particolare, ogni punto di accumulazione della successione

$$
\{\alpha^{(k)}\}_{k\in\mathbb N}
$$

se esiste, è un **punto stazionario** di $F$, cioè soddisfa

$$
\boxed{
\nabla F(\alpha^*)=0
}
$$

Questa conclusione, da sola, non garantisce che il punto trovato sia un minimo: in una funzione non convessa un punto stazionario potrebbe essere anche un massimo o un altro tipo di punto critico.

Se, oltre alle ipotesi precedenti, $F$ è anche **convessa**, allora ogni punto stazionario è un punto di minimo globale.

In questo caso la successione generata dal metodo del gradiente converge a un punto di minimo:

$$
\boxed{
F\text{ convessa}
\quad\Longrightarrow\quad
\alpha^{(k)}
\to
\alpha^*
}
$$

dove $\alpha^*$ è un punto di minimo di $F$.

È quindi importante distinguere i due casi:

$$
\boxed{
\begin{array}{c}
F\text{ non convessa}\\
\Downarrow\\
\text{si converge, sotto le ipotesi, a un punto stazionario}
\end{array}
}
$$

mentre

$$
\boxed{
\begin{array}{c}
F\text{ convessa}\\
\Downarrow\\
\text{un punto stazionario è un minimo globale}
\end{array}
}
$$

---

# Criteri di arresto

Un metodo iterativo non può essere eseguito indefinitamente. È quindi necessario stabilire quando fermare le iterazioni.

Dal teorema di Fermat sappiamo che in un punto di minimo deve essere

$$
\nabla F(\alpha^*)=0.
$$

Possiamo quindi controllare quanto il gradiente dell'iterata corrente sia vicino a zero.

Un criterio di arresto naturale è

$$
\boxed{
\|\nabla F(\alpha^{(k)})\|_2\leq\tau
}
$$

dove $\tau>0$ è una tolleranza scelta dall'utente.

Questo criterio misura il **residuo della condizione necessaria di ottimalità**.

Se la norma del gradiente è molto piccola, significa che ci troviamo vicino a un punto stazionario.

Un secondo criterio può essere basato sulla variazione relativa della funzione obiettivo tra due iterazioni consecutive:

$$
\boxed{
\frac{
|F(\alpha^{(k)})-F(\alpha^{(k+1)})|
}{
|F(\alpha^{(k)})|
}
\leq\tau
}
$$

Questo criterio verifica invece se il valore della funzione obiettivo sta cambiando molto poco.

In pratica, i due criteri possono essere utilizzati contemporaneamente: il metodo viene arrestato quando il gradiente è sufficientemente piccolo e/o quando il valore della funzione obiettivo non cambia più in modo significativo.

---

# Schema concettuale

Il passaggio dai minimi quadrati lineari ai minimi quadrati non lineari può essere riassunto nel seguente modo.

Nel caso lineare il modello può essere scritto come

$$
f(\alpha;x)=A\alpha
$$

e quindi il problema è

$$
\min_\alpha\|A\alpha-y\|_2^2.
$$

Questo problema può essere risolto mediante strumenti dell'algebra lineare, come la fattorizzazione QR o la SVD.

Nel caso non lineare il modello dipende invece non linearmente dai parametri:

$$
f(\alpha;x)
$$

e il problema diventa

$$
\boxed{
\min_{\alpha\in\mathbb R^n}
F(\alpha)
}
$$

dove, nel caso dei minimi quadrati non lineari,

$$
\boxed{
F(\alpha)
=
\sum_{i=1}^{m}
\left(
f(\alpha;x_i)-y_i
\right)^2
}
$$

Non possiamo più ricondurci direttamente a un sistema lineare. Una possibile strategia consiste nel cercare i punti stazionari risolvendo

$$
\nabla F(\alpha)=0
$$

e, dal punto di vista numerico, possiamo utilizzare un metodo iterativo come il **metodo del gradiente**:

$$
\boxed{
\alpha^{(k+1)}
=
\alpha^{(k)}
-
\gamma_k\nabla F(\alpha^{(k)})
}
$$

La direzione scelta è quella dell'antigradiente perché è localmente la direzione di massima discesa, mentre la lunghezza di passo $\gamma_k$ determina quanto ci si sposta in tale direzione.

La scelta del passo è fondamentale per il comportamento del metodo. Se il gradiente è Lipschitziano con costante $L$, una scelta a passo fisso che soddisfa

$$
0<\gamma<\frac{2}{L}
$$

garantisce la proprietà di discesa della funzione obiettivo. Se inoltre $F$ è convessa, la convergenza conduce a un punto di minimo globale.
