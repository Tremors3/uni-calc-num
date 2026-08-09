
# Metodi iterativi per sistemi lineari

L’idea dei metodi iterativi è costruire una **successione di vettori** che approssima progressivamente la soluzione del sistema lineare. Invece di ottenere la soluzione con un numero finito di operazioni (come nei metodi diretti), si genera una sequenza che, al crescere delle iterazioni, **converge** alla soluzione esatta.

In pratica si parte da una stima iniziale $x^{(0)}$ e si costruiscono i successivi $x^{(1)}, x^{(2)}, \dots$ con una **regola ricorsiva**. Il risultato finale non è mai esatto in senso teorico, ma **un’approssimazione** controllata tramite una tolleranza.

## Successioni e Teoria sulla Convergenza 

### ▸ Richiamo: convergenza di una successione

Sia una successione scalare:

$$
\{a_k\}_{k \in \mathbb{N}} \subset \mathbb{R}
$$

Diciamo che converge ad $a^* \in \mathbb{R}$ se:

$$
\lim_{k \to \infty} a_k = a^*
\quad \Leftrightarrow \quad
\forall \varepsilon > 0 \;\; \exists N_\varepsilon \;:\; |a_k - a^*| \le \varepsilon \;\; \forall k \ge N_\varepsilon
$$

Questo significa che i termini della successione diventano **arbitrariamente vicini** al valore limite.

### ▸ Successioni di vettori

Nel caso dei sistemi lineari lavoriamo con vettori:

$$
\{x^{(k)}\}_{k \in \mathbb{N}} \subset \mathbb{R}^n
$$

dove ogni elemento della successione è un vettore:

$$
x^{(k)} =
\begin{pmatrix}
x_1^{(k)} \\
\vdots \\
x_n^{(k)}
\end{pmatrix}
$$

La convergenza è definita tramite una norma:

$$
\lim_{k \to \infty} x^{(k)} = x^*
\quad \Leftrightarrow \quad
\forall \varepsilon > 0 \;\; \exists N_\varepsilon \;:\; \|x^{(k)} - x^*\| \le \varepsilon \;\; \forall k \ge N_\varepsilon
$$

### ▸ Interpretazioni equivalenti

La definizione di convergenza può essere espressa in modi equivalenti:

$$
\lim_{k \to \infty} x^{(k)} = x^*
\;\;\Leftrightarrow\;\;
\lim_{k \to \infty} \|x^{(k)} - x^*\| = 0
$$

oppure, componente per componente:

$$
\lim_{k \to \infty} x_i^{(k)} = x_i^*
\quad \forall i = 1,\dots,n
$$

Quindi la distanza tra il vettore iterato e la soluzione tende a zero.

### ▸ Osservazione pratica

Nei metodi iterativi non si arriva mai al limite infinito: si arresta l’algoritmo quando

$$
\|x^{(k)} - x^{(k-1)}\| \le \varepsilon
\quad \text{oppure} \quad
\|Ax^{(k)} - b\| \le \varepsilon
$$

dove $\varepsilon$ è una **tolleranza scelta**. Questo rappresenta un compromesso tra accuratezza e costo computazionale.

## Risoluzione di sistemi lineari con metodi iterativi

I metodi iterativi si basano sull’idea di costruire una successione di vettori che, iterazione dopo iterazione, si avvicina alla soluzione del sistema lineare.

A differenza dei metodi diretti (come Gauss), non producono la soluzione esatta in un numero finito di passi, ma una successione che converge alla soluzione.

Consideriamo il sistema:

$$
Ax = b, \qquad x^* \text{ soluzione tale che } Ax^* = b
$$

Un metodo iterativo parte da una stima iniziale:

$$
x^{(0)} \in \mathbb{R}^n
$$

e genera una successione tramite una formula ricorsiva del tipo:

$$
x^{(k+1)} = G x^{(k)} + c, \qquad k = 0,1,2,\dots
$$

dove $G \in \mathbb{R}^{n \times n}$ e $c \in \mathbb{R}^n$ dipendono dal metodo scelto (ad esempio Jacobi, Gauss-Seidel, ecc.).

L’idea è semplice: ad ogni passo si aggiorna la soluzione precedente applicando una trasformazione lineare e aggiungendo un termine noto. Dal punto di vista implementativo questo è molto efficiente, perché basta sovrascrivere il vettore corrente senza memorizzare tutta la successione.

### ▸ Convergenza del metodo

Affinché il metodo sia utile, la successione deve convergere alla soluzione esatta:

$$
\lim_{k \to \infty} x^{(k)} = x^*
$$

Sostituendo nella formula iterativa, la soluzione deve soddisfare:

$$
x^* = G x^* + c
$$

cioè è un punto fisso della trasformazione iterativa.

Un aspetto fondamentale è che vogliamo la convergenza **per ogni scelta del dato iniziale**:

$$
\forall x^{(0)} \in \mathbb{R}^n
$$

Questo impone condizioni sulla matrice $G$ (in particolare sul suo raggio spettrale, che deve essere minore di 1, anche se questo verrà formalizzato più avanti).

### ▸ Scelta del punto iniziale

La scelta di $x^{(0)}$ può influenzare la velocità di convergenza. In pratica:

- se non si hanno informazioni, si usa spesso $x^{(0)} = 0$ oppure un vettore di tutti 1;
- se si ha una stima iniziale migliore, il metodo converge più rapidamente.

In ogni caso, un buon metodo iterativo deve convergere indipendentemente dalla scelta iniziale, anche se con velocità diverse.

### ▸ Ottenimento di un metodo iterativo

Partiamo dal sistema lineare:

$$
Ax^* = b
$$

che possiamo riscrivere in forma equivalente come:

$$
0 = b - Ax^*
$$

L’idea è trasformare questa equazione in una forma adatta a generare una successione iterativa. Per farlo, introduciamo una matrice $M \in \mathbb{R}^{n \times n}$ **nonsingolare**, scelta opportunamente. Aggiungiamo $Mx^*$ a entrambi i membri:

$$
Mx^* = Mx^* + b - Ax^*
$$

Ora moltiplichiamo per $M^{-1}$:

$$
x^* = x^* + M^{-1}b - M^{-1}Ax^*
$$

Riorganizzando i termini e raccogliendo rispetto a $x^*$ otteniamo:

$$
x^* = (I - M^{-1}A)x^* + M^{-1}b
$$

A questo punto possiamo identificare:

$$
\boxed{G = I - M^{-1}A}, \qquad \boxed{c = M^{-1}b}
$$

e quindi scrivere:

$$
\boxed{x^* = G x^* + c}
$$

Questa è esattamente la forma dei metodi iterativi vista in precedenza. La matrice $G$ prende il nome di **matrice di iterazione**, mentre $c$ è il termine noto del metodo.

È importante capire che questa non è una nuova equazione, ma solo una **riformulazione equivalente** del problema originale. Il vantaggio è che ora possiamo definire una successione:

$$
x^{(k+1)} = G x^{(k)} + c
$$

che, sotto opportune condizioni, converge proprio a $x^*$.

### ▸ Ruolo della matrice $M$

La scelta di $M$ è cruciale: determina sia la forma del metodo iterativo (Jacobi, Gauss-Seidel, ecc.), sia le proprietà di convergenza. In generale, $M$ deve essere:

- **facile da invertire** (o da usare per risolvere sistemi);
- scelta in modo da rendere il metodo **convergente**.

### Aspetti fondamentali da verificare

Quando si costruisce un metodo iterativo, ci sono due problemi principali da affrontare.

1) L’**analisi di convergenza** serve a garantire che la successione $x^{(k)}$ converga a $x^*$ per ogni scelta iniziale. Questo dipende dalla matrice $G$ (in particolare dal fatto che le sue potenze tendano a zero).

2) I **criteri di arresto** sono invece legati all’implementazione pratica. Poiché non possiamo iterare all’infinito, dobbiamo fermarci quando la soluzione approssimata è sufficientemente accurata. Tipicamente si usa una tolleranza $\varepsilon$ e si arresta il metodo quando:

    $$
    \|x^{(k+1)} - x^{(k)}\| \le \varepsilon
    \quad \text{oppure} \quad
    \|b - Ax^{(k)}\| \le \varepsilon
    $$

    cioè quando la variazione tra iterazioni (o il residuo) è abbastanza piccola.

## Studio della convergenza

Per analizzare la convergenza, introduciamo l’**errore al passo $k$**:

$$
e^{(k)} = x^{(k)} - x^*
$$

Sostituendo nella formula iterativa:

$$
\begin{aligned}
e^{(k)} 
&= x^{(k)} - x^* \\
&= (G x^{(k-1)} + c) - (G x^* + c) \\
&= G(x^{(k-1)} - x^*) \\
&= G e^{(k-1)}
\end{aligned}
$$

Iterando il ragionamento:

$$
e^{(k)} = G^k e^{(0)}, \qquad \text{con } e^{(0)} = x^{(0)} - x^*
$$

Questa relazione è fondamentale: **l’errore dipende dalle potenze della matrice $\mathbf G$**.

---

### Condizione di convergenza

Il metodo converge se:

$$
\lim_{k \to \infty} e^{(k)} = 0
\quad \Leftrightarrow \quad
\lim_{k \to \infty} G^k = 0
$$

In norma:

$$
\|e^{(k)}\| = \|G^k e^{(0)}\| \le \|G^k\| \cdot \|e^{(0)}\|
$$

Quindi è sufficiente che:

$$
\lim_{k \to \infty} \|G^k\| = 0
$$

Utilizzando la proprietà sub-moltiplicativa della norma:

$$
\|G^k\| \le \|G\|^k
$$

si ottiene una **condizione sufficiente di convergenza**:

$$
\boxed{\|G\| < 1}
$$

Infatti, se $\|G\| < 1$, allora:

$$
\lim_{k \to \infty} \|G\|^k = 0
\quad \Rightarrow \quad
\lim_{k \to \infty} e^{(k)} = 0
$$

---

#### Interpretazione

Se $\|G\| < 1$, ogni iterazione “riduce” l’errore: la matrice $G$ agisce come una contrazione. Questo garantisce che la successione $x^{(k)}$ converga a $x^*$ **per qualunque scelta di $x^{(0)}$**.

In pratica:

$$
\boxed{
\|G\| < 1 \;\Longrightarrow\; x^{(k)} \to x^* \quad \forall x^{(0)}
}
$$

Questa è una condizione sufficiente (non sempre necessaria), ma molto importante per progettare metodi iterativi convergenti.

---

### Convergenza tramite raggio spettrale

Un altro modo (più preciso) per studiare la convergenza dei metodi iterativi utilizza gli **autovalori** della matrice di iterazione $G$.

Il **raggio spettrale** di $G$ è definito come:

$$
\rho(G) = \max_i |\lambda_i|
$$

dove $\lambda_i$ sono gli autovalori di $G$. Questo numero riassume il comportamento asintotico delle potenze della matrice.

Il risultato fondamentale è:

$$
\boxed{
\text{Il metodo iterativo converge} \;\Longleftrightarrow\; \rho(G) < 1
}
$$

Questa è una **condizione necessaria e sufficiente**, a differenza di $\|G\| < 1$ che è solo sufficiente.

---

#### Collegamento con l’errore

Ripartendo dalla relazione:

$$
e^{(k)} = G^k e^{(0)}
$$

si ottiene:

$$
\|e^{(k)}\| \le \|G^k\| \cdot \|e^{(0)}\|
\le \|G\|^k \cdot \|e^{(0)}\|
$$

Queste disuguaglianze permettono di stimare la velocità di convergenza, anche se non sono esatte.

---

#### Velocità di convergenza

In pratica, il comportamento dell’errore è ben descritto da:

$$
\|e^{(k)}\| \approx \|G\|^k \cdot \|e^{(0)}\|
$$

Ancora più precisamente, usando il raggio spettrale:

$$
\boxed{
\|e^{(k)}\| \approx \rho(G)^k \cdot \|e^{(0)}\|
}
$$

Questo significa che:

- se $\rho(G)$ è molto minore di 1 → convergenza **rapida**;
- se $\rho(G)$ è vicino a 1 → convergenza **lenta**;
- se $\rho(G) \ge 1$ → il metodo **non converge**.

#### Osservazione importante

Le stime con la norma sono utili per garantire la convergenza, ma il raggio spettrale descrive meglio il comportamento reale dell’errore. Per questo motivo è lo strumento teorico più importante nello studio dei metodi iterativi.

---

## Dal metodo all’algoritmo: criterio d’arresto

I metodi iterativi generano, in teoria, una successione infinita di vettori $\{x^{(k)}\}$. In pratica però dobbiamo fermarci dopo un numero finito di iterazioni, trasformando quindi il metodo in un **algoritmo**.

L’idea ideale sarebbe fermarsi quando:

$$
\|x^{(k)} - x^*\| \le \varepsilon
$$

dove $\varepsilon$ è una tolleranza prefissata. Tuttavia questo criterio **non è utilizzabile direttamente**, perché la soluzione esatta $x^*$ è sconosciuta.

---

### Criterio pratico: differenza tra iterate

Per questo motivo si utilizza un criterio basato sulla distanza tra due iterate successive:

$$
\frac{\|x^{(k+1)} - x^{(k)}\|}{\|x^{(k+1)}\|} < \varepsilon
$$

L’idea è che, se il metodo converge, le iterate diventano sempre più simili tra loro. Quando la differenza è molto piccola, significa che ci stiamo avvicinando al punto fisso (cioè alla soluzione).

---

#### Interpretazione teorica

Partiamo dalla differenza tra due iterate:

$$
x^{(k+1)} - x^{(k)} = Gx^{(k)} + c - x^{(k)}
$$

Usando il fatto che $x^* = Gx^* + c$, otteniamo:

$$
\begin{aligned}
x^{(k+1)} - x^{(k)} 
&= Gx^{(k)} + x^* - Gx^* - x^{(k)} \\
&= G(x^{(k)} - x^*) - (x^{(k)} - x^*) \\
&= (G - I)(x^{(k)} - x^*)
\end{aligned}
$$

cioè:

$$
\boxed{
x^{(k+1)} - x^{(k)} = (G - I)(x^{(k)} - x^*)
}
$$

Questa relazione collega direttamente:

- la differenza tra iterate successive  
- l’errore rispetto alla soluzione

---

#### Stima dell’errore

Se $(G - I)$ è invertibile (cosa vera se $\rho(G) < 1$), possiamo scrivere:

$$
x^{(k)} - x^* = (G - I)^{-1}(x^{(k+1)} - x^{(k)})
$$

e quindi, passando alle norme:

$$
\|x^{(k)} - x^*\| \le \|(G - I)^{-1}\| \cdot \|x^{(k+1)} - x^{(k)}\|
$$

Questo giustifica il criterio pratico: la differenza tra iterate è una **stima dell’errore**.

In pratica non conosciamo il fattore $\|(G - I)^{-1}\|$, ma se non è troppo grande possiamo assumere:

$$
\|x^{(k)} - x^*\| \approx \|x^{(k+1)} - x^{(k)}\|
$$

---

#### Schema algoritmico

Un possibile algoritmo è:

```py
Input: x_corr, A, b, G, c, tolleranza t

for k = 0,1,...
    x_next = G x_corr + c

    if ||x_next - x_corr|| / ||x_next|| < t
        return x_next
    else
        x_corr = x_next
end
```

---

#### Osservazione finale

Questo criterio di arresto è molto usato perché semplice ed economico. Tuttavia è solo una stima indiretta dell’errore, quindi in alcuni casi può essere troppo ottimista o troppo conservativo.

---

### Altro criterio d’arresto: il residuo

Un secondo criterio di arresto molto usato nei metodi iterativi si basa sul **residuo** del sistema lineare.

Per il sistema:

$$
Ax = b
$$

la soluzione esatta $x^*$ soddisfa:

$$
Ax^* = b \;\;\Longleftrightarrow\;\; b - Ax^* = 0
$$

Questo suggerisce di definire, per un’iterata qualsiasi $x^{(k)}$, il **vettore residuo**:

$$
r^{(k)} = b - Ax^{(k)}
$$

Il residuo misura quanto l’iterata corrente soddisfa il sistema. Se:

$$
r^{(k)} = 0
$$

allora abbiamo trovato esattamente la soluzione. In pratica questo non accade, ma possiamo fermarci quando:

$$
\|r^{(k)}\| \le \varepsilon
$$

cioè quando il residuo è sufficientemente piccolo.

---

#### Interpretazione

Il residuo fornisce una misura indiretta dell’errore: se $x^{(k)}$ è vicino a $x^*$, allora anche $Ax^{(k)}$ sarà vicino a $b$, quindi il residuo sarà piccolo.

Come per il criterio basato sulle iterate successive, anche il residuo è una **stima pratica** della distanza dalla soluzione.

---

#### Residuo e condizionamento

La relazione tra residuo ed errore è influenzata dal **condizionamento del problema**. In generale si ha una stima del tipo:

$$
\frac{\|x^{(k)} - x^*\|}{\|x^*\|} \le \kappa(A)\,\frac{\|r^{(k)}\|}{\|b\|}
$$

dove $\kappa(A)$ è l’indice di condizionamento della matrice $A$.

Questo significa che, se il problema è mal condizionato, anche un residuo piccolo può corrispondere a un errore relativamente grande. Per questo motivo il criterio sul residuo va interpretato con attenzione.

---

#### Uso combinato dei criteri

Nella pratica si utilizzano spesso entrambi i criteri:

- differenza tra iterate successive  
- norma del residuo  

Ad esempio:

$$
\frac{\|x^{(k+1)} - x^{(k)}\|}{\|x^{(k+1)}\|} < \varepsilon
\quad \text{e} \quad
\frac{\|r^{(k)}\|}{\|b\|} < \varepsilon
$$

Questo permette di controllare sia la stabilizzazione delle iterate sia la qualità della soluzione rispetto al sistema originale.

---

#### Terzo criterio: numero massimo di iterazioni

Per sicurezza si impone anche un numero massimo di iterazioni $N_{\max}$, utile per evitare loop infiniti in caso di mancata convergenza:

```py
for k = 0,1,...,N_max
    r = b - A x_corr
    x_next = G x_corr + c

    if criterio_iterate AND criterio_residuo
        return x_next
    else
        x_corr = x_next

if k == N_max
    warning: metodo non convergente o tolleranza non raggiunta
```

Questo criterio non riguarda la matematica della convergenza, ma è una misura di **sicurezza implementativa**.

---

#### Osservazione finale

I criteri d’arresto assumono implicitamente che il metodo sia convergente: solo in quel caso le iterate si stabilizzano e il residuo tende a zero. Se il metodo non converge, nessun criterio d’arresto sarà soddisfatto (a meno del limite sulle iterazioni).

---

### Complessità computazionale

A differenza dei metodi diretti, nei metodi iterativi non è possibile conoscere **a priori** il numero esatto di operazioni necessarie, perché il numero di iterazioni dipende dal criterio di arresto (tolleranza, residuo, numero massimo di iterazioni).  

Per questo motivo, la complessità si valuta considerando il **costo di una singola iterazione**.

Ad ogni passo dell’algoritmo si esegue principalmente un prodotto matrice-vettore:
$$
x^{(k+1)} = Gx^{(k)} + c
$$

Il costo di un prodotto matrice-vettore, per una matrice densa $A \in \mathbb{R}^{n \times n}$, è:
$$
\mathcal{O}(n^2)
$$

Se il metodo richiede $m$ iterazioni, il costo complessivo diventa:
$$
\mathcal{O}(m \cdot n^2)
$$

Nel caso peggiore, se $m \approx n$, si ottiene:
$$
\mathcal{O}(n^3)
$$
che è confrontabile con i metodi diretti.

Tuttavia, questa stima è spesso pessimistica. Infatti:

- se la matrice è **sparsa**, il prodotto matrice-vettore può costare molto meno di $\mathcal{O}(n^2)$;
- non è necessario memorizzare tutta la matrice, ma solo gli elementi non nulli;
- è possibile implementare operatori “matrix-free”, cioè funzioni che calcolano $Ax$ senza costruire esplicitamente $A$.

Per problemi di grandi dimensioni (ad esempio in ambito scientifico o di immagini), i metodi iterativi risultano quindi **molto più efficienti in memoria** e spesso anche più veloci.

Inoltre, quando non è richiesta una soluzione esatta ma solo una buona approssimazione, i metodi iterativi diventano particolarmente vantaggiosi.

---

#### Scelta della matrice di iterazione

La forma generale di un metodo iterativo è:
$$
x^{(k+1)} = Gx^{(k)} + c
$$

dove:
$$
G = I - M^{-1}A, \qquad c = M^{-1}b
$$

La scelta della matrice $M$ è cruciale, perché determina sia la **convergenza** che il **costo computazionale** del metodo.

Per capire meglio, consideriamo un caso limite:

Se scegliamo:
$$
M = A
$$

allora:
$$
G = I - M^{-1}A = I - A^{-1}A = 0
$$
$$
c = M^{-1}b = A^{-1}b
$$

Il metodo diventa:
$$
x^{(1)} = Gx^{(0)} + c = A^{-1}b = x^*
$$

cioè la soluzione esatta viene ottenuta **in una sola iterazione**.

Questo è però solo un risultato teorico: calcolare $A^{-1}$ è costoso e numericamente instabile, quindi non è una scelta praticabile. Di fatto, equivale a risolvere il sistema con un metodo diretto.

---

Nella pratica, la matrice $M$ viene scelta in modo che:

- sia **facile da invertire** (ad esempio diagonale o triangolare);
- sia una buona **approssimazione di $A$**, così da garantire la convergenza.

L’idea fondamentale è quindi trovare un compromesso:

- $M$ deve essere semplice → costo basso per iterazione  
- $M$ deve essere “vicina” ad $A$ → convergenza veloce  

Questa filosofia porta ai metodi classici come **Jacobi**, **Gauss-Seidel** e varianti più avanzate.

---

### Decomposizione della matrice

I metodi iterativi classici si basano sull’idea di riscrivere la matrice del sistema nella forma:

$$
A = M - N
$$

Questa decomposizione permette di ricondurre il sistema $Ax = b$ alla forma iterativa:

$$
x^{(k+1)} = M^{-1}N x^{(k)} + M^{-1}b
$$

dove la matrice di iterazione è:
$$
G = M^{-1}N, \qquad c = M^{-1}b
$$

---

Per costruire $M$ e $N$, si parte da una decomposizione naturale della matrice $A$ come somma di tre componenti. Formalmente:

$$
A = D - E - F
$$

dove:

- $D$ contiene gli **elementi diagonali** di $A$  
- $E$ contiene gli **elementi sotto la diagonale** (con *segno cambiato*)  
- $F$ contiene gli **elementi sopra la diagonale** (anch’essi con *segno cambiato*)  

Questa scelta dei segni è utile perché semplifica le formule dei metodi iterativi.


$$A = \begin{pmatrix}
\color{red}{a_{11}}&\color{green}{a_{12}}&\color{green}{a_{13}} &\color{green}{a_{14}} &\color{green}{\cdots}  &\color{green}{\cdots}   &\color{green}{a_{1n}}  \\
{\color{blue}{a_{21}}}&\color{red}{a_{22}}&\color{green}{a_{23}} &\color{green}{a_{24}} &\color{green}{\cdots} &\color{green}{\cdots} &\color{green}{a_{2n}}   \\
\color{blue}{a_{31}}&\color{blue}{a_{32}} &\color{red}{a_{33}}&\color{green}{a_{34}} & & & \color{green}{a_{3n}}   \\
 \color{blue}{\cdots} & \color{blue}{\cdots}&   &\color{red}{\ddots}&\color{green}{\cdots}& \color{green}{\cdots}& \\
\color{blue}{a_{i1}}& \color{blue}{\cdots}& &\color{blue}{a_{ii-1}}&\color{red}{a_{ii}}&\color{green}{a_{ii+1}} &\color{green}{a_{in}} \\
 \color{blue}{\cdots} &\color{blue}{\cdots} &\color{blue}{\cdots}      && &\color{red}{\ddots}  \\
\color{blue}{a_{n-11}}  &\color{blue}{\cdots} &\color{blue}{\cdots}&\color{blue}{\cdots} & \color{blue}{{a_{n-1n-2}}}&\color{red}{a_{n-1n-1}}&\color{green}{a_{n-1n}}\\
\color{blue}{a_{n1}}  & \color{blue}{\cdots}&  \color{blue}{\cdots}&\color{blue}{\cdots} &\color{blue}{\cdots} &\color{blue}{ {a_{nn-1}}}    &\color{red}{a_{nn}}
\end{pmatrix}
$$

$$E = \begin{pmatrix}
0&0&0 &0 &{\cdots}  &0  &0 \\
-{\color{blue}{a_{21}}}&0&0 &0 &{\cdots} &{\cdots} &0  \\
-\color{blue}{a_{31}}&-\color{blue}{a_{32}} &0&0& & & 0   \\
 -\color{blue}{\cdots} & -\color{blue}{\cdots}&   &0&{\cdots}& 0& \\
-\color{blue}{a_{i1}}& \color{blue}{\cdots}& &-\color{blue}{a_{ii-1}}&0&0 &0\\
 \color{blue}{\cdots} &\color{blue}{\cdots} &\color{blue}{\cdots}      && &0  \\
-\color{blue}{a_{n-11}}  &\color{blue}{\cdots} &\color{blue}{\cdots}&\color{blue}{\cdots} & -\color{blue}{{a_{n-1n-2}}}&0&0\\
-\color{blue}{a_{n1}}  & \color{blue}{\cdots}&  \color{blue}{\cdots}&\color{blue}{\cdots} &\color{blue}{\cdots} &-\color{blue}{ {a_{nn-1}}}    &0
\end{pmatrix}$$
$$F=\begin{pmatrix}
0&-\color{green}{a_{12}}&\color{green}{a_{13}} &-\color{green}{a_{14}} &\color{green}{\cdots}  &\color{green}{\cdots}   &-\color{green}{a_{1n}}  \\
0&0&-\color{green}{a_{23}} &-\color{green}{a_{24}} &\color{green}{\cdots} &\color{green}{\cdots} &-\color{green}{a_{2n}}   \\
0&0&0&-\color{green}{a_{34}} & & & -\color{green}{a_{3n}}   \\
 0& 0&   & {\ddots}&\color{green}{\cdots}& \color{green}{\cdots}& \\
0& {\cdots}& &0&0&-\color{green}{a_{ii+1}} &-\color{green}{a_{in}} \\
 {\cdots} &{\cdots} &{\cdots}      && &{\ddots}  \\
0  &0 &0&{\cdots} & 0&0&-\color{green}{a_{n-1n}}\\
0 & 0&  {\cdots}&{\cdots} &{\cdots} &0    &0
\end{pmatrix}$$


$$D = \begin{pmatrix}
\color{red}{a_{11}}&0&0 &0 & {\cdots}  & {\cdots}   &0\\
0&\color{red}{a_{22}}&0 & 0& {\cdots} & {\cdots} &0 \\
0&0 &\color{red}{a_{33}}&0 & & & 0   \\
  {\cdots} &  {\cdots}&   &\color{red}{\ddots}& {\cdots}&  {\cdots}& \\
0&  {\cdots}& &0&\color{red}{a_{ii}}&0 &0\\
  {\cdots} & {\cdots} & {\cdots}      && &\color{red}{\ddots}  \\
0 & {\cdots} & {\cdots}& {\cdots} & 0&\color{red}{a_{n-1n-1}}&0\\
0 &  {\cdots}&   {\cdots}& {\cdots} & {\cdots} &0    &\color{red}{a_{nn}}
\end{pmatrix} $$

---

A partire da questa decomposizione a tre termini, si costruisce una decomposizione a due termini $A = M - N$, scegliendo opportunamente $M$ (facile da invertire) e $N$.

Le due scelte fondamentali portano ai metodi classici:

---

**Metodo di Jacobi**

Si sceglie come matrice del metodo solo la diagonale:

$$
A = \underbrace{D}_{M} - \underbrace{(E + F)}_{N}
$$

Il metodo iterativo diventa:

$$
x^{(k+1)} = D^{-1}(E + F)x^{(k)} + D^{-1}b
$$

In questo caso ogni componente di $x^{(k+1)}$ dipende **solo dai valori della iterazione precedente**, quindi il metodo è completamente disaccoppiato.

---

**Metodo di Gauss-Seidel**

Si include anche la parte inferiore nella matrice del metodo:

$$
A = \underbrace{(D - E)}_{M} - \underbrace{F}_{N}
$$

Il metodo iterativo diventa:

$$
x^{(k+1)} = (D - E)^{-1}F x^{(k)} + (D - E)^{-1}b
$$

Qui la matrice $M$ è triangolare inferiore, quindi il sistema si risolve con **sostituzione in avanti**.  

A differenza di Jacobi, ogni componente di $x^{(k+1)}$ utilizza **anche i valori appena aggiornati**, rendendo il metodo generalmente più veloce nella convergenza.

---

### Adattamento del metodo iterativo alla decomposizione

Partiamo dalla forma generale dei metodi iterativi:

$$
x^{(k+1)} = Gx^{(k)} + c
$$

Se utilizziamo una decomposizione della matrice:

$$
A = M - N
$$

la matrice di iterazione diventa:

$$
\begin{aligned}
G &= I - M^{-1}A \\
  &= I - M^{-1}(M - N) \\
  &= I - M^{-1}M + M^{-1}N \\
  &= M^{-1}N
\end{aligned}
$$

Di conseguenza, il metodo iterativo si può riscrivere come:

$$
x^{(k+1)} = M^{-1}N x^{(k)} + M^{-1}b
$$

Dal punto di vista computazionale, è importante osservare che **non conviene mai calcolare esplicitamente l’inversa** $M^{-1}$.  

È molto più efficiente riscrivere il metodo nella forma equivalente:

$$
\boxed{M x^{(k+1)} = N x^{(k)} + b}
$$

In questo modo, ad ogni iterazione si risolve un sistema lineare con matrice $M$, che è scelto apposta per essere semplice (diagonale o triangolare).

---

#### Specializzazione dei metodi

A partire dalla decomposizione $A = D - E - F$, otteniamo i metodi classici.

---

**Metodo di Jacobi**

Si sceglie:
$$
A = D - (E + F)
$$

Il metodo diventa:

$$
x^{(k+1)} = D^{-1}(E + F)x^{(k)} + D^{-1}b
$$

oppure, in forma più operativa:

$$
D x^{(k+1)} = (E + F)x^{(k)} + b
$$

cioè:

$$
x^{(k+1)} = D^{-1}\big((E + F)x^{(k)} + b\big)
$$

La matrice di iterazione è:
$$
G_J = D^{-1}(E + F)
$$

Condizione di convergenza:
$$
\rho(G_J) < 1 \quad \Leftarrow \quad \|G_J\| < 1
$$

---

**Metodo di Gauss-Seidel**

Si sceglie:
$$
A = (D - E) - F
$$

Il metodo diventa:

$$
x^{(k+1)} = (D - E)^{-1}F x^{(k)} + (D - E)^{-1}b
$$

oppure:

$$
(D - E)x^{(k+1)} = F x^{(k)} + b
$$

La matrice di iterazione è:
$$
G_{GS} = (D - E)^{-1}F
$$

Condizione di convergenza:
$$
\rho(G_{GS}) < 1 \quad \Leftarrow \quad \|G_{GS}\| < 1
$$

---

#### Convergenza: matrici a diagonale dominante

Una classe importante di matrici per cui i metodi iterativi convergono è quella delle **matrici a diagonale dominante**.

Una matrice $A$ è diagonalmente dominante se, per ogni riga:

$$
|a_{ii}| \ge \sum_{j \ne i} |a_{ij}|
$$

Se la disuguaglianza è stretta per almeno una riga (o per tutte, nella forma più forte), si parla di **dominanza diagonale stretta**.

Questa proprietà è molto utile perché:

- garantisce la convergenza del metodo di **Gauss-Seidel**;
- garantisce anche la convergenza di **Jacobi** (anche se la dimostrazione è più tecnica).

In pratica, se gli elementi diagonali “dominano” gli altri, il metodo tende a stabilizzarsi.

---

#### Velocità di convergenza

La velocità di convergenza dipende dal **raggio spettrale** della matrice di iterazione:

$$
\rho(G)
$$

Più $\rho(G)$ è piccolo, più il metodo converge velocemente.

In generale:

- Jacobi è più semplice ma **più lento**;
- Gauss-Seidel sfrutta i valori aggiornati e quindi è **più veloce nella pratica**.

---

#### Forma per componenti (Gauss-Seidel)

Scriviamo il sistema:

$$
Ax = b
$$

in forma esplicita:

$$
\begin{cases}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n = b_2 \\
\vdots \\
a_{n1}x_1 + a_{n2}x_2 + \dots + a_{nn}x_n = b_n
\end{cases}
$$

Nel metodo di Gauss-Seidel, ogni componente viene aggiornata usando **i valori più recenti disponibili**:

$$
x_i^{(k+1)} =
\frac{1}{a_{ii}}
\left(
b_i
- \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)}
- \sum_{j=i+1}^{n} a_{ij} x_j^{(k)}
\right)
$$

Qui si vede chiaramente la differenza con Jacobi:

- per $j < i$ uso i valori **già aggiornati** ($k+1$),
- per $j > i$ uso i valori **della vecchia iterazione** ($k$).

Questo “riutilizzo immediato” dell’informazione è ciò che rende Gauss-Seidel più efficiente nella pratica.

---

In sintesi, i metodi iterativi basati su decomposizione trasformano il problema in una sequenza di sistemi semplici, sfruttando strutture (diagonali o triangolari) che rendono il calcolo efficiente sia in termini di tempo che di memoria.