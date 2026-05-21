
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

> **Nota**: Possiamo utilizzare la QR solamente se siamo sicuri che le colonne della matrice A siano linearmente indipendenti.

Le colonne \[righe\] di una matrice sono linearmente indipendenti se nessuna di esse può essere espressa come combinazione lineare delle altre. Operativamente, le colonne \[righe\] sono linearmente indipendenti se il rango della matrice è uguale al numero di colonne \[righe\], ovvero se riducendo la matrice a scala (con l'algoritmo di Gauss), non si ottengono colonne \[righe\] nulle.

Se la matrice ha più righe che colonne, le righe sono necessariamente linearmente dipendenti.

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
\vdots & & & \vdots & \vdots & & \vdots \\  
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
\sigma_1\gamma_1 \\ \sigma_2\gamma_2 \\ \vdots \\ \sigma_k\gamma_k \\ 0 \\ \vdots \\ 0
\end{pmatrix}
-
\begin{pmatrix}
z_1 \\ z_2 \\ \vdots \\ z_k \\ z_{k+1} \\ \vdots \\ z_m
\end{pmatrix}
=
\begin{pmatrix}
\sigma_1\gamma_1-z_1 \\ \sigma_2\gamma_2-z_2 \\ \vdots \\ \sigma_k\gamma_k-z_k \\ -z_{k+1} \\ \vdots \\ -z_{m}
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

# (32) Lezione 13-05-2026 | s .. | Continuo SVD $-$ Decomposizione ai Valori Singolari

### Ripasso lezione precedente

Data la fattorizzazione:

$$
A = U\Sigma V^T
$$

Abbiamo trovato la soluzione di minima norma:

$$
\min_{d\in\R^n}\|A = U\Sigma V^T\|^2
$$

Per fare ciò abbiamo calcolato:

$$
\boxed{1}\;
z = U^Ty
,\qquad
\boxed{2}\;
\begin{pmatrix}
\frac{z_1}{\sigma_1} \\ \frac{z_2}{\sigma_2} \\ \vdots \\ \frac{z_k}{\sigma_k} \\ 0 \\ \vdots \\ 0
\end{pmatrix}
,\qquad
\boxed{3}\;
\alpha=V\gamma
$$

### Risoluzione con matrice pseudo inversa

Questi tre passaggi possiamo esprimerli tramite un singolo prodotto matrice vettore:

$$
\underbrace{
\begin{pmatrix}
\frac1{\sigma_1} &0  & 0 & 0 \\
0 & \ddots & 0 & 0 \\
0 & 0 & \frac1{\sigma_k} & 0 \\
0 & \ldots & \ldots & 0  \\
\vdots & & &\vdots \\
0 & \ldots & \ldots & 0  \\
\end{pmatrix}
}_{\Sigma}
\begin{pmatrix}
z_1 \\ z_2 \\ \vdots \\ z_k \\ z_{k+1} \\ \vdots \\ z_m
\end{pmatrix}
=
\begin{pmatrix}
\frac{z_1}{\sigma_1} \\ \frac{z_2}{\sigma_2} \\ \vdots \\ \frac{z_k}{\sigma_k} \\ 0 \\ \vdots \\ 0
\end{pmatrix}
= \gamma
$$

Stessa struttura della matrice già vista prima ma in questo caso i valori singolari sono invertiti.

> **Attenzione**. Si tratta di un modo formale che ci permette di esprimere il prodotto dell'algoritmo nel suo secondo passo. MA NON E' COSI' CHE SI FA: questo metodo è instabile. Perchè può dare luogo a problemi di stabilità (troncamento): data dall'inversione dei valori singolari e la successiva moltiplicazione con le $z_i$.

Sappiamo che:

$$
\alpha = V\gamma = V\Sigma^\dagger z = \underbrace{V\Sigma^\dagger U^T}_{A^\dagger}y
$$

$A^\dagger$ viene chiamata la **matrice pseudo inversa** di $A$.
- L'inversa di una matrice quadrata e non signolare è un caso particolare della pseudo inversa.
- La pseudo inversa però la si può definire per matrici non quadrate e che non hanno rango pieno.

Ma questa non è la strata dumericamente corretta da seguire per avere la massima stabilità possibile.

---

## Minimi Quadrati - Altro utilizzo per l'SVD - Compressione di matrici

Noi sappiamo che data una matrice $A$ sappiamo scriverla come

$$
A = U\Sigma V^T
$$

Per interpretare in un modo utile la formula introduciamo una notazione per indicare le colonne di $U$ e righe di $V$:

- $u_i\in\R^m=i$-esima colonna di $U\;i=1,\ldots,m$
- $v_i\in\R^n=i$-esima riga di $V\;i=1,\ldots,n$

Scriviamo A come la concatenazione delle colonne

$$\begin{aligned}
A = U\Sigma V^T &= (u_1\;u_2\;\ldots\;u_k\;u_{k+1}\;\ldots\;u_m)
\underbrace{
\begin{pmatrix}
\sigma_1 &0  & 0 & 0 \\
0 & \ddots & 0 & 0 \\
0 & 0 & \sigma_k & 0 \\
\vdots & & &\vdots \\
0 & \ldots & \ldots & 0  \\
\end{pmatrix}
\begin{pmatrix}
v_1^T \\ v_2^T \\ \vdots \\ v_{k}^T \\ v_{k+1}^T \\ \vdots \\ v_n^T
\end{pmatrix}
}_{m\times n\;\cdot\; n\times n \qquad\textit{calcoliamo per primo}}
\\&=
(u_1\;u_2\;\ldots\;u_k\;u_{k+1}\;\ldots\;u_m)
\begin{pmatrix}
\sigma_1v_1^T \\ \sigma_2v_2^T \\ \vdots \\ \sigma_kv_{k}^T \\ 0 \\ \vdots \\ 0
\end{pmatrix}
\\\textit{colonne}\times\textit{righe} &=
\sigma_1u_1v_1^T + \sigma_2u_2v_2^T + \ldots + \sigma_ku_kv_k^T
\end{aligned}$$

- Abbiamo scritto la matrice V come la concatenazione delle sue colonne

    $$
    V = (v_1\;\ldots\;v_n)
    $$

    Le v sono vettori colonne. Se vogliamo metterli su una riga dobbiamo trasporli.

Possiamo quindi riscrivere la matrice $A$ come:

$$
\boxed{A = \sigma_1u_1v_1^T + \sigma_2u_2v_2^T + \ldots + \sigma_ku_kv_k^T}
$$

Cioè una somma pesata di $k$ termini ciascuno dei quali che dipendono dalle colonne corrispondenti di $U$ e $V$. Somma pesata di $k$ matrici, ciascuna con le stesse dimensioni di $A$, pesate per i valori singolari.

Inoltre abbiamo le $u_i\cdot v_i^T\in\R^{m\times n}$.

E' quindi sufficiete calcolare solamente le prime $k$ colonne della matrice $U$ e le prime $k$ righe della matrice $V$. Questo comporta un aumento dell'efficienza. Si evita di calcolare una parte dell'output completo. (Opzione `np.svd(..., full_matrices=False)`)

### Compressione di una matrice

> **Oss**. I valori singolari (pesi dell'espressione di $A$) sono ordinati in modo decrescente
>
> $$\sigma_1 \ge \sigma_2 \ge \ldots \ge \sigma_k$$
>
> L'idea legata alla **compressione** è questa: 
> costruire un'approssimazione di $A$ costruita a partire dalla somma pesata che abbiamo trovato ma che prende dentro meno termini:
>
> $$ \bar A = \sigma_1u_1v_1^T + \sigma_2u_2v_2^T + \ldots + \sigma_{\bar k}u_{\bar k}v_{\bar{k}}^T \qquad\bar k < k $$
>
> Una matrice richiede solitamente $m\times n$ valori floating-point.
> Apportando l'approssimazione avremo invece il seguente numero di locazioni di memoria:
>
> $$ \bar{k}\cdot(m+n+1) $$
>
> Di solito questo numero è ovviamente molto più piccolo di $m\times n$

### Implementazione dell'SVD con la compressione

Vista durante il laboratorio (**laboratorio 10a**).

---

La norma 2 di una matrice è la radice del massimo degli autovalori di $A^TA$:

$$
\|A\|_2 = \sqrt{\underbrace{\max_{1,\ldots,m}\lambda_i(A^TA)}_{\sigma_1^2}}
$$

Possiamo riformulare questa norma in modo da utilizzare i **valori singolari**. Abbiamo che $\sigma_1$^2 è il più grande dei valori singolari al cubo e corrisponde al massimo degli autovalori. 

$$
\|A\|_2 = \sigma_1
$$

Proprietà di invarianza rispetto alla norma:

$$
U: \qquad \|AU\|_2 = \|A\|_2 \\
V: \qquad \|VA\|_2 = \|A\|
$$

La norma di Frobenius è la radice della somma degli elementi al quadrato della matrice:

$$
\|A\|_F = \sqrt{\sum_{i,\;j} a_{ij}^2}
$$

Quindi può valere ad esempio:

$$
\|Ax\|_2 = \|A\|_F\cdot\|x\|_2
$$

La norma di Frobenius può essere mescolata con la Euclidea ed anchessa è invariante per prodotti con matrici ortogonali.

Abbiamo che

$$\begin{aligned}
\|A - \bar A\| &= \|U\Sigma V^T - U\bar\Sigma V^T\| \\
&= \|U(\Sigma-\bar\Sigma)V^T\| \\
&= \|\Sigma-\bar\Sigma\|
\end{aligned}$$

Quella intera ha anche i valori singolari oltre a $\bar k$, mentre la seconda ha al loro posto degli zeri.

Una misura di distanza tra le due matrici è ad esempio

$$\begin{aligned}
\|A - \bar A\|_F &= \|U\Sigma V^T - U\bar\Sigma V^T\| \\
&= \|U(\Sigma-\bar\Sigma)V^T\|_F \\
&= \|\Sigma-\bar\Sigma\|_F \\
&= \max{\sigma_{k+1},\ldots,\sigma_k} = \sigma_{k+1}
\end{aligned}$$

---

# (33) Lezione 18-05-2026 | s 365.. | Regressione lineare in più dimensioni (sempre SVD)

## Regressione Lineare in Più Dimensioni

Altro proble risolvibile tramite l'algoritmo dell'SVD

Caso più semplice di un problema molto più generale che è quello tipico del Machine Learning e dell'apprendimento.

Problema di regressione lineare, che però rispetto ai casi precedenti lo spazio dei dati non è più piano ma in più dimensioni.

**DATI**:
Abbiamo sembre un vettore di coppie, ma le coppie non contengono più uno scalare (coordinata x o y) ma un vettore con p componenti (da qui l'aumento di dimensioni).

$$
\{(x^{(i)}, y_i)\} \qquad\text{con } x^{(i)}\in\R^p, y_i\in\R
$$

- Il primo vettore $x^{(i)}$ della coppia è un vettore le cui componenti sono dette FEATURES.

- $y_i$ invece viene chiamta risposta del campione.

Esista una funzione $f$ dipendente da un certo numero di parametri $\alpha_0,\dots,\alpha_n$. Funzione della variabile $x$ ha valori in $\R$ tale che.

Quello che troviamo dev'essere la variabile di rispostta $y_i$. Si assume che esista un legame tra i dati e questa $y_i$; e che questo legame dipenda da un certo numero di parametri.

$$
f : \R^p\to\R, \quad f(\alpha_0,\ldots,\alpha_n;x)
$$

vogliamo trovare $\alpha_0,\ldots,\alpha_n$ tali che la funzione ci porti ad un valore che si avvicina ad $y_i$:

$$
f(\alpha_0,\ldots,\alpha_n;x) \approxeq y_i
$$

Questi valori devono essere IMPARATI dai dati (learning). Il problema che uno ha di fronte davanti ad un dataset di questo tipo è, una volta che abbiamo fissato il modello, dobbiamo trovare la configurazione dei parametri ottimale in modo che la funzione $f$ spieghi bene il set di dati.

Esprimento il problema con i Minimi Quadrati abbiamo:

$$
\min_{\alpha\R^{n+1}} \sum_{i=1}^n\left(f(\alpha_0,\ldots,\alpha_n;x^{(i)})-y_i\right)^2
$$

### 1. Modello Lineare

Si tratta di una generalizzazione di quello che abbiamo visto precedentemente.

$$
f(\alpha_0,\ldots,\alpha_n;x^{(i)}) = \alpha_0 + \alpha_1x + \alpha_2x^2 + \ldots + \alpha_nx^n
$$

Non è altro che una somma pesata delle varia features. Quando scegliamo un modello di questo tip ostiamo assumento che la variabile di risposta sia in qualche modo legata ad una combinazione lineare (somma pesata) di tutte le features.

Si definisce quindi la matrice di regressione $A$ (come matrice di Householder) ed il vettor edelle risposte.

$$
A = \begin{pmatrix}
1 & x_1^{(1)} & x_2^{(1)} & \ldots & x_n^{(1)} \\
1 & x_1^{(2)} & x_2^{(2)} & \ldots & x_n^{(2)} \\
\vdots & \vdots & \vdots & & \vdots \\
1 & x_1^{(m)} & x_2^{(m)} & \ldots & x_n^{(m)} \\
\end{pmatrix} \quad y = \begin{pmatrix}
y_1 \\ y_2 \\ \vdots \\ y_n
\end{pmatrix}
$$

Dove abbiamo per esempio nella seconda colonna:

$$
\begin{matrix}
x_1^{(1)} & \text{Prima feature, primo campione} \\
x_1^{(2)} & \text{Prima feature, secondo campione} \\
\vdots \\
\end{matrix}
$$

Il criterio dei minimi quadrati si formula nel modo seguente:

$$
\min_{\alpha\in\R^{n+1}} \|A\alpha - y\|^2
$$

Risolvibile come abbiamo visto.

#### Esempio in laboratorio

Esempio di dataset ed applicazione del modello nel caso lineare (**laboratorio 11a**).

#### Features e Pesi

Abbiamo visto due casi d'esempio:
1. Il primo in cui si avevano poche features ma dataset grande;
2. Il secondo con un numero ingente di features ma un dataset ristretto.

Nel secondo caso potrebbero esserci alcune features che sono meno influenti rispetto ad altre features.

Questo lo capiano perchè il dato che stiamo cercando sono proprio i pesi che moltiplicano le features.

Quindi se abbiamo un $\alpha_i$ grande la feature importerà molto, mentre se è piccolo allora la feature forse ha meno importanza rispetto alla risposta ($y_i$).

Ci si rende conto quali sono le features più rilevanti per la risposta. Non tutte solitamente sono importanti per la risposta.

#### Perchè vogliamo la funzione f con gli alpha giusti?

Perchè ho bisogno di fare una previsione. Per esempio voglio sapere qual'è il prezzo più giusto per vendere un'immobile. Con un modello costruito bene ho una funzione con i parametri giusti che mi darà il prezzo migliore per vendere l'immobile.

#### 

Suddivisione del dataset per fare training:
- $50-70\%$ dei campione per il training set
- $30-50\%$ dei campioni per il testing set

---