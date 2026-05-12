
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

# (29) Lezione 06-05-2026 | s .. | Criterio dei Minimi Quadrati

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
- Caso generale lineare caso rango pieno
- Caso generale lineare caso degenere (non rango pieno)
- Ulteriori casi in cui non si ha una somma pesata di funzioni.

---

# (30) Lezione 11-05-2026 | s .. | Minimi Quadrati con Funzioni Generiche

Abbiamo sperimentato con l'algoritmo dei minimi quadrati (**Laboratorio 09a**).

---

Ci sono alcuni dataframe che non sono approssimabili utilizzando la classica interpolazione o riduzione con polinomi.

Per esempio funzioni che mostrano una certa periodicità (esempio rilevazioni annuali della CO_2 nell'atmosfera). Per questo motivo introduciamo le funzioni sin e cos.

$$
f(x,a_0,a_1,a_2,a_3) = a_0 + a_1x + a_2\sin(2\pi x) + a_3\cos(2\pi x)
$$

Questo è un esempio del **caso lineare generale** del criterio dei minimi quadrati:

$$\begin{aligned}
\phi_0(x) = 1 \qquad\phi_2(x) = \sin(2\pi x) \\
\phi_1(x) = x \qquad \phi_3(x) = \cos(2\pi x)
\end{aligned}$$

Anche in questo caso, applicando gli stessi passaggi applicati per il caso dei polinomi, ci riconduciamo alla forma:

$$
Q(a_0,\ldots,a_{n-1}) = \|A\alpha -y\|^2
$$

Proviamo a pensare come riscrivere la funzione che crea la matrice di Vandermonde nel caso non abbiamo monomi ma funzioni. I parametri di ingresso rimangono 2: la x e una lista che fa riferimento alle funzioni della base che vogliamo applicare. La lunghezza della matrice sarà quindi determinata dal numero di funzioni.

Non è più detto che la matrice sia a rango pieno. Non sappiamo quali sono i valori effettivi delle x fin da subito dato che le calcoliamo con le 4 funzioni.

Invece della fattorizzazione QR ma la Decomposizione ai Valori Singoli (SVD).

---

# (31) Lezione 12-05-2026 | s .. | Continuo Criterio dei Minimi Quadrati

> Nota: Possiamo utilizzare la QR solamente se siamo sicuri che le colonne della matrice A siano linearmente indipendenti.

## La decomposizione ai valori singolari (SVD)

SI applica a matrici rettangolari di dimensione $m\times n$ di qualsiasi rango. Ovviamente il rango $k$.

Sia $A\in\R^{m\times n}$ una matrice di rango $k$. Allora $A$ si può fattorizzare nella forma

$$
A = U\Sigma V^T
$$

Dove:
- $U\in\R^{m\times m},V\in\R^{n\times n}$ sono matrici ortogonali
- $\Sigma\in\R^{m\times n}$ è una matrice rettangolar ediagonale nella forma

$$
\Sigma = \begin{pmatrix}
\sigma_1 & & & & 0 & \ldots & 0 \\
& \sigma_2 & & & 0 & \ldots & 0 \\
& & \ddots   & & 0 & \ldots & 0 \\
& & & \sigma_n & 0 & \ldots & 0 \\
0 & \ldots & \ldots & 0 & 0 & \ldots & 0 \\
\vdots  &  & & & & & \\  
0 & \ldots & \ldots & 0 & 0 & \ldots & 0 \\  

\end{pmatrix}
$$

dove gli elementi non nulli si collocano sulla diagonale principale.

I valori $\sigma_i$ sono detti i **valori singolari** di $A$. Assumiamo di numerarli dal più grande al più piccolo

$$
\sigma_1 \ge \sigma_2 \ge \ldots \ge \sigma_n
$$

In particolare si ha che $\sigma_i^2$ sono gli autovalori di $A^TA$, mentre le colonne di $U$ e $V$ sono gli autovettori di $AA^T$ e di $A^TA$.

- $A^TA$: ha rango $k$ $\to$ abbiamo $n-k$ autovalori nulli e i rimanenti positivi. La loro radice ci da esattamente i **valori singolari**.

### Dimostrazione e ottenimento della Soluzione

La decomposizione SVD è molto generale e ha molti algoritmi e implementazioni specifiche. Questi algoritmi sono molto costosi.

- Riserviamo la decomposizione SVD solamente quando non si hanno informazioni sul rango della matrice (se non si è sicuri che la matrice abbia rango pieno).

Vogliamo utilizzare questa fattorizzazione al posto della $QR$ per risolvere lo stesso problema

$$
\|A\alpha - y\|^2
$$

Che possiamo riscrivere quindi come:

$$\begin{aligned}
\|A\alpha - y\|^2
&=
\|U\Sigma V^T\alpha - y\|^2 \\
\textit{Applico proprietà norma euclidea} &=
\|U^T(U\Sigma V^T\alpha - y)\|^2 \\
&=
\|\Sigma \underbrace{V^T\alpha}_{\gamma} - \underbrace{U^Ty}_{z}\| \\
&=
\|\Sigma\gamma - z\|^2
\end{aligned}$$

- Possiamo calcolare $z=U^Ty$ direttamente dai dati.
- Con $\gamma$ abbiamo effettuato un cambio di variabile. Il vettore $\gamma$ è quindi dipendente da $\alpha$. Il notro obiettivo è quindi calcolare il vettore $\gamma$.

Ora riscriviamo il nuovo sistema come:

$$\begin{aligned}
\|\Sigma\gamma - z\|^2
&=
\begin{pmatrix}
\sigma_1 &0  & 0 & 0 \\
0 & \ddots & 0 & 0 \\
0 & 0 & \sigma_k & 0 \\
\vdots & & &\vdots \\
0 & \ldots & \ldots & 0  \\
\end{pmatrix}
\begin{pmatrix}
\gamma_1 \\ \gamma_2 \\ \vdots \\ \gamma_k \\ \gamma_{k+1} \\ \vdots \\ \gamma_n
\end{pmatrix}
-
\begin{pmatrix}
z_1 \\ z_2 \\ \vdots \\ z_k \\ z_{k+1} \\ \vdots \\ z_m
\end{pmatrix} \\
&= 
\begin{pmatrix}
\sigma_1\gamma_1 \\ \sigma_2\gamma_2 \\ \vdots \\ \sigma_k\gamma_k \\ -z_{k+1} \\ \vdots \\ -z_{m}
\end{pmatrix}
-
\begin{pmatrix}
z_1 \\ z_2 \\ \vdots \\ z_k \\ z_{k+1} \\ \vdots \\ z_n
\end{pmatrix}
=
\begin{pmatrix}
\sigma_1\gamma_1-z_1 \\ \sigma_2\gamma_2-z_2 \\ \vdots \\ \sigma_k\gamma_k-z_k \\ 0 \\ \vdots \\ 0
\end{pmatrix} \\
&=
\left\|
\begin{pmatrix}
\sigma_1\gamma_1-z_1 \\ \vdots \\ \sigma_k\gamma_k-z_k
\end{pmatrix}
\right\|^2
+
\left\|
\begin{pmatrix}
-z_{k+1} \\ \vdots \\ -z_m
\end{pmatrix}
\right\|^2
\end{aligned}$$

- Il vettore $z$ dipende esclusivamente dai dati noti.
- La matrice di regressione si calcola a partire delle funzioni note $\phi$ e dalle $x$, quindi anche $A$ dipende esclusivamente da dati noti.

L'unico caso in cui la norma del vettore ha valore minimo è se quel vettore ha tutte componenti nulle.

Dobbiamo quindi trovare $\gamma$ in modo che i valori del vettore siano minimi:

$$
\gamma_i : \sigma_i\gamma_i = z_i \xrightarrow{quindi} \boxed{\gamma_i = \frac{z_i}{\sigma_i}}
$$

Quando il vettore $\gamma$ ha le sue prime $k$ componenti che seguono quella frazione. Ma questa frazione ci definisce solamente le prime $k$ componenti del vettore. Le altre $n-k$ che fine fanno?

Si scopre essere completamente trasparenti. Lo si nota nei passaggi fatti prima. Si vede come vengono annullati dagli zeri presenti nella matrice rettangolare diagonale in cui si trovano le $\sigma_i$ sulla diagonale principale. Le abbiamo perse a fare quel prodotto matrice vettore $\gamma$.

Abbiamo quindi infinite soluzioni del problema:

$$
\begin{pmatrix}
\frac{z_1}{\sigma_1} \\ \frac{z_2}{\sigma_2} \\ \vdots \\ \frac{z_k}{\sigma_k} \\ \gamma_{k+1} \\ \vdots \\ \gamma_n
\end{pmatrix}
\;:\;
\gamma_{k+1},\ldots,\gamma_n\in\R
$$

Sono tutti quanti vettori che minimizzano la funzione di distanza quadratica.

### Individuazione di una soluzione (minima norma)

1. Sintetizzando tutti i passaggi fatti fino ad ora possiamo applicare i passaggi visti in precedenza.

2. Voglio quindi crearmi un vettore le cui prime $k$ componenti rispettano la forma $\frac{z_i}{\sigma_i}$;

3. Seleziono altri valori "a caso" per i successivi $n-k$ valori.

4. Ottengo:

    $$ V^T\alpha = \gamma \Rightarrow \boxed{\alpha = V\gamma} $$


In realtà non scelgo le $n-k$ componenti a caso. Scelgo le n-k componenti libere tutte uguali a zero:

$$
\begin{pmatrix}
\frac{z_1}{\sigma_1} \\ \frac{z_2}{\sigma_2} \\ \vdots \\ \frac{z_k}{\sigma_k} \\ 0 \\ \vdots \\ 0
\end{pmatrix}
\;:\;
\gamma_{k+1},\ldots,\gamma_n=0
$$

Viene chiamata soluzione con norma minima. Mettere a zero le componenti libere porta ad avere la norma più piccola.

Nota: Le norme euclidee sono invarianti dal prodotto di una matrice ortogonale. Quindi il rango di $\alpha$ è uguale al rango di $\gamma$.

### Algoritmo ed implementazione

Implementazione dell'algoritmo vista in laboratorio (**laboratorio 09b**).

---

# (32) Lezione 13-05-2026 | s .. | 



---