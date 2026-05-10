
# (28) Lezione 05-05-2026 | s 342.. | Approssimazione di dati e funzioni: il criterio dei minimi quadrati

### Svantaggio dell'approssimazione di dati mediante interpolazione

Ogni qualvolt che misuriamo qualcosa, la misurazione non verrà mai perfetta; conterrà sicuramente un qualche errore. L'interpolazione tradizionale ci porterebbe ad avere funzioni che seguono l'andamento generale della funzione originale ma reso inattendibile dal rumore. La prof ci ha mostrato un esempio in cui una relazione lineare come la legge di Ohm $V = iR$ con resistenza tenuta costante in realtà la misurazione oscillerà e non sarà una retta dato il rumore. L'interpolazione che abbiamo studiato segue l'errore fornendoci una funnzione che oscilla.

## Criterio dei Minimi Quadrati (Idea della Regressione)

Per impostare il problema di regressione, oltre ai dati, dobbiamo scegliere qual'è secondo noi il modello ideale che li rappresenta bene. Per quanto riguarda l'intelligenza artificiale il modello non lo si conosce e si va di forza bruta.

### Caso semplice: Retta di Regressione

Sappiamo che questi dati a meno dell'errore dovrebbero allinearsi per una retta:

$$
y = a_0 + a_1x
$$

si vuole determinare quella che 'spiega' meglio i dati.

$$
(x_i,y_i),\;i=1,\dots,m
$$

Spiegare bene i dati potremmo riesprimerlo come: "Trovare la retta che passa più vicino ai dati che abbiamo".

Misuriamo la distanza di una retta da un'insieme di dati significa minimizzare

$$
Q(a_0,a_1) = \sum_{i=0}^m (a_0+a_1x_i - y_i)^2
$$

> **Spiegazione**. Si misurano le distanze verticali tra la retta $a_0+a_1x$ e ciascuno dei punti. Si cerca di minimizzare la somma di queste distanze (sulle ordinate).
> 
> Le chiamiamo distanze ma non sono distanze euclidee tra i punti e la retta.


1. Consideriamo la distanza tra retta e la corrispondente y

    $$(a_0+a_1x_i - y_i)$$

2. Eleviamo al quadrato in modo da togliere la questione del segno

    $$(a_0+a_1x_i - y_i)^2$$

3. Sommiamo tutte le "distanze" in modo da ottenere un valore che esprime l'errore totale.

    $$
    Q(a_0,a_1) = \sum_{i=0}^m (a_0+a_1x_i - y_i)^2
    $$

Ottenimo questa distanza quadratica cumulativa che corrisponde alla "distanza" dei due coefficienti dalla retta.

Questo criterio definisce la miglior scelta cioè la retta che rende minima questa distanza quadratica cumulativa. E' la retta identificata dal coefficiente angolare e di altezza che minimizza la distanza.

### Caso semplice: Qual'è il problema?

Dobbiamo trovare qual'è la coppia $a_0,a_1$ che identificano la retta che minimizza la distanza quadratica cumulativa.

Vedremo di esprimere il problema in termini di vettori, matrici ed incognite. Troveremo un algoritmo generale che si può applicare anche a funzioni polinomiali di un grado più alto.

---

# (29) Lezione 06-05-2026 | s 342.. | Criterio dei Minimi Quadrati

Fino ad ora abbiamo considerato il caso lineare. Come facciamo a risolvere il problema e trovare le giuste $a_0,a_0$?

### Obiettivo: Trovare la retta

**DATI**: $(x_i),y_i,\;i=1,\dots,n$

**MODELLO**: $f(x,a_0,a_1) = a_0 + a_1x$

Ci serve quindi almeno una qualche informazione riguardo al tipo di funzione che può spiegare bene i dati. Per ora assumiamo che questa funzione sia una retta.

Il modello che noi scegliamo per approssimare i dati debba dipendere da un numero finito di parametri (le $a$). Va calcolata la retta e quindi i parametri $a_0,a_1$ che minimizzano la funzione:

$$
Q(a_0,a_1) = \sum_{i=0}^m (a_0+a_1x_i - y_i)^2
$$

### Come facciamo? 

Un primo passaggio utile consiste nel riformare la funzione della distanza quadratica cumulativa. Abbiamo quindi:

$$\begin{aligned}
Q(a_0,a_1) &= \sum_{i=0}^m (a_0+a_1x_i - y_i)^2 \\
&= \begin{pmatrix}
a_0+a_1x_0 \\
a_0+a_1x_1 \\
\vdots \\
a_0+a_1x_m \\
\end{pmatrix} - \begin{pmatrix}
y_1\\
y_2 \\
\vdots \\
y_m \\
\end{pmatrix} 
\end{aligned}$$


Se $v\in\R^n$ allora $\|v\|_2^2 = \sqrt{v_1^2+v_2^2+\dots+v_n^2}$. Cioè la norma 2 al quadrato di un vettore non è altro che la somma dei quadrati delle sue componenti.

Quindi analogamente possiamo porre:

$$\begin{aligned}
\Big\|\begin{pmatrix}
a_0+a_1x_0 \\
a_0+a_1x_1 \\
\vdots \\
a_0+a_1x_m \\
\end{pmatrix} - \underbrace{\begin{pmatrix}
y_1\\
y_2 \\
\vdots \\
y_m \\
\end{pmatrix}}_{y}\Big\|^2
&=
\underbrace{\begin{pmatrix}
1 & x_1 \\
2 & x_2 \\
\vdots & \vdots \\
m & x_m \\
\end{pmatrix}}_{A\in\R^{m\times 2}} \cdot \underbrace{\begin{pmatrix} a_0 \\ a_1 \end{pmatrix}}_{\alpha\in\R^2}
- \underbrace{y}_{\R^m}\Big\|^2 
=
\|A\alpha-y\|^2
\end{aligned}$$

Notiamo che la prima matrice corrisponde alle prime due colonne della **matrice di Vandermonde**. La troviamo all'interno di un sistema nella forma $A\alpha - y$ sotto la norma elevata al quadrato.

### Caso di una parabola

Possiamo estendere il procedimento per una funzione che segue l'andamento di una parabola:

**INPUT**: $(x_i,y_i), i=1,\dots,m$
$f(x;a_0,a_1,a_2) = a_0 + a_1x_1 + a_2x_2^2$

Anche nel caso di una parabola il ragionamento rimane lo stesso. Andiamo a confrontare **in verticare l'ordinata dei dati** e il **valore che il modello assume sulla stessa scissa**.

Avremo quindi la seguente funzione $Q$, dipendente dai tre parametri:

$$\begin{aligned}

Q(a_0,a_1,a_2) &= \sum_{i=0}^m (a_0+a_1x_i+a_2x_2^2 - y_i)^2 \\
&= \Big\|\begin{pmatrix}
a_0+a_1x_0+a_2x_1^2 \\
a_0+a_1x_1+a_2x_2^2 \\
\vdots \\
a_0+a_1x_m+a_2x_m^2 \\
\end{pmatrix} - \begin{pmatrix}
y_1\\
y_2 \\
\vdots \\
y_m \\
\end{pmatrix}\Big\|^2 \\
&= 
\underbrace{\begin{pmatrix}
1 & x_1 & x_1 \\
2 & x_2 & x_2 \\
\vdots & \vdots & \vdots \\
m & x_m & x_m \\
\end{pmatrix}}_{A\in\R^{m\times 3}} \cdot \underbrace{\begin{pmatrix} a_0 \\ a_1 \\ a_2 \end{pmatrix}}_{\alpha\in\R^3}
- \underbrace{y}_{\R^m}\Big\|^2 
=
\|A\alpha-y\|^2
\end{aligned}$$

### Caso di un polinomio di grado $n$-esimo

Possiamo rieffettuare la stessa procedura per un polinomio di qualsiasi grado $n$:

$$\begin{aligned}

Q(a_0,a_1,a_2) &= \sum_{i=0}^m (a_0+a_1x_i+a_2x_2^2+\dots+a_{n-1}x_i^{n-1} - y_i)^2 \\
&= \Big\|\begin{pmatrix}
a_0+\dots +a_{n-1}x_1^{n-1} \\
a_0+\dots +a_{n-1}x_2^{n-1} \\
\vdots \\
a_0+\dots +a_{n-1}x_m^{n-1} \\
\end{pmatrix} - \begin{pmatrix}
y_1\\
y_2 \\
\vdots \\
y_m \\
\end{pmatrix}\Big\|^2 \\
&= 
\underbrace{\begin{pmatrix}
1 & x_1 & \dots & x_1^{n-1} \\
2 & x_2 & \dots & x_2^{n-1} \\
\vdots & \vdots & & \vdots \\
m & x_m & \dots & x_m^{n-1} \\
\end{pmatrix}}_{A\in\R^{m\times n-1}} \cdot \underbrace{\begin{pmatrix} a_0 \\ a_1 \\ \vdots \\ a_{n-1} \end{pmatrix}}_{\alpha\in\R^{n-1}}
- \underbrace{y}_{\R^m}\Big\|^2 
=
\|A\alpha-y\|^2

\end{aligned}$$

### Caso Generale Lineare

Come somma pesata di funzioni fissate:

$$
f(x,a_0,\dots,a_{m-1}) = a_0\phi_0(x)+a_1\phi_1(x)+\dots+a_{n-1}\phi_{n-1}(x)
$$

Dove le $\{\phi_i\}$ sono una qualsiasi funzione tra ad esempio sin,cos,log,exp...; Quello che rimane lineare nel modello è la dipendenza rispetto ai parametri.

$$
\phi_i(x) = x^i
$$

Quello che dovrò minimizzare sarà quindi:

$$\begin{aligned}

Q(a_0,\dots,a_{n-1}) &= \sum_{i=0}^m (a_0\phi_0(x)+\dots+a_{n-1}\phi_{n-1}(x) - y_i)^2 \\
&= \Big\|\begin{pmatrix}
\phi_0(x_1) & \phi_1(x_1) & \dots & \phi_{n-1}(x_1) \\
\vdots & \vdots & & \vdots \\
\phi_0(x_m) & \phi_1(x_m) & \dots & \phi_{n-1}(x_m)
\end{pmatrix}
\cdot
\begin{pmatrix} a_0 \\ a_1 \\ \vdots \\ a_{n-1} \end{pmatrix}
-
\begin{pmatrix} y_1 \\ \vdots \\ y_m \end{pmatrix}\Big\|^2 \\
&= \boxed{\|A\alpha - y\|^2}
\end{aligned}$$

Ci siamo ricondotti anche in questo caso alla stessa forma.

#### Non applicabilità del metodo per alcune funzioni

Riusciamo ad estrarre la matrice di Regressione perchè in un qualche modo i parametri sono separati. La matrice deve dipendere solo dai dati ed il vettore solo dai parametri. Ma non è sempre così.

Quando i parametri si mescolano all'interno di una funzione nonlineare:

$$
f_i(x) = a_0\cdot e^{a_1x_i}
$$

non possiamo applicare il metodo del caso generale lineare e non possiamo ricavare la matrice di Regressione.

### Obiettivo

**TROVA**

Vogliamo trovare il vettore

$$
\alpha = \begin{pmatrix} a_0 \\ \vdots \\ a_{m-1} \end{pmatrix}\in\R^n
$$

che minimizza

$$
Q(\alpha) = \|A\alpha-y\|^2
$$

dove

$$
A\in\R^{m\times n}, \qquad y\in\R^n
$$

**Hp**. $n\ge n$; le colonne di $A$ sono linearmente indipendenti.

Ipotesi **non degenere** sicuramente soddisfatta nel caso polinomiale di qualsiasi grado dove $n-1\le m$ numero dei punti.

Le colonne della matrice di regressione $A$ potrebbero diventare linearmente Dipendenti se cambiamo la funzione di base.

Ci ricordiamo di un teorema che afferma che la matrice $A$ può essere espressa tramite fattorizzazione $QR$ (anche se la matrice non è quadrata):

$$
\underbrace{A}_{n\times n} = \underbrace{Q}_{m\times m}
\cdot
\underbrace{\begin{pmatrix} R \\ O \end{pmatrix}}_{n}

\begin{matrix} \}\;\qquad n \\ \}\; m-n \end{matrix}
$$

1. **Prima proprietà** 

    Abbiamo

    $z\in\R^m$
    
    $Q\in\R^{m\times n}$ ortogonale

    Calcoliamo

    $$
    \boxed{\|Qz\|^2 = (Qz)^T(Qz) = z^TQ^TQz = z^Tz = \|z\|^2}
    $$
    
    Calcolare la norma di un vettore moltiplicato per una matrice ordogonale, equivale a calcolare la norma di un vettore. Questo è sempre vero per qualsiasi vettore.

2. **Seconda proprietà**

    Abbiamo

    $y_1\in\R^{n_1} \qquad y_2\in\R^{n_2} \qquad y=\begin{pmatrix}y_1 \\ y_2\end{pmatrix}\in\R^{n_1+n_2}$

    Calcoliamo

    $$
    \boxed{\|y\|^2 = \|y_1\|^2 + \|y_2\|^2}
    $$

Usiamo queste due proprietà sulla norma euclidea per risolvere il nostro problema.

### Risoluzione del problema

$$\begin{aligned}
\|A\alpha - y\|^2 &= \|Q\begin{pmatrix}R\\O\end{pmatrix}\alpha-y\|^2 \\
&= \|Q^T\Big(Q\begin{pmatrix}R\\O\end{pmatrix}\alpha-y\Big)\|^2 \\
&= \|\begin{pmatrix}R\\O\end{pmatrix}\alpha-\underbrace{Q^Ty}_{\tilde y}\|^2 \\
\text{1° propprietà}\to&= \|\begin{pmatrix}R\alpha\\O\end{pmatrix} - \begin{pmatrix}\tilde y_1 \\\tilde y_2\end{pmatrix}\|^2 \\
&= \| \begin{pmatrix}R\alpha-\tilde y_1 \\ -\tilde y_2\end{pmatrix} \|^2 \\
\text{2° propprietà}\to&= \boxed{\|R\alpha-\tilde y_1\|^2 + \|-\tilde y_2\|^2} \\
\end{aligned}$$

Come possiamo minimizzare questa quantità? Osserviamo che entrambe le norme sono $\ge0$. Il problema è che non possiamo farci nulla direttamente con la formula, perchè le $\tilde y_i$ dipendeno dai dati.

Notiamo però che: per minimizzare l'unica possibilità di azione l'abbiamo sul primo terminte. Dato che la componente è $\ge0$ allora minimizzarlo significa renderlo vicino proprio a $0$.

Cioè facendo in modo che la componente si annulli:

$$
\boxed{\alpha : R\alpha = \tilde y_1}
$$

L'alpha che minimizza la funzione $Q$ è la stessa $\alpha$ che soddisfa questa uguaglianza.

I passaggi che abbiamo fatto sono proprio quelli che sono implementati nell'algoritmo.

Ci troviamo quindi a dover risolvere questo sistema lineare la cui soluzione esiste ed è unica. Il sistema è triangolare dato che $R$ è la funzione triangolare superiore. Si risolve semplicemente applicando metodo della sostituzione all'indietro.

---

### Casi che vedremo

Casi che vedremo per i problemi di regressione
- Caso generale lineare caso rango piento
- Caso generale lineare caso degenere (non rango piento)
- Ulteriori caso in cui non si ha una somma pesata di funzioni.

---

# (30) Lezione 11-05-2026 | s 342.. | Criterio dei Minimi Quadrati
