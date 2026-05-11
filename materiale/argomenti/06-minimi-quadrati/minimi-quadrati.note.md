# Criterio dei Minimi Quadrati

### Limiti dell’interpolazione in presenza di dati rumorosi

L’interpolazione classica assume implicitamente che i dati assegnati siano **esatti**, cioè privi di errore. Nella pratica, però, i dati sperimentali ottenuti da misurazioni contengono quasi sempre rumore, errori strumentali o perturbazioni casuali.

Se si applica un metodo di interpolazione a questi dati, la funzione interpolante viene forzata a passare **esattamente per ogni punto misurato**, compresi quelli alterati dal rumore. Di conseguenza l’interpolante tende a seguire anche le oscillazioni spurie dei dati, producendo una funzione che può risultare poco fedele al fenomeno reale sottostante.

Ad esempio, se un fenomeno fisico dovrebbe teoricamente seguire una legge lineare come la legge di Ohm

$$
V=iR
$$

(con resistenza $R$ costante), le misurazioni reali di tensione e corrente non cadranno perfettamente su una retta, ma saranno disperse attorno ad essa a causa degli errori sperimentali. Interpolare tali dati significherebbe costruire una funzione che segue anche il rumore, anziché il comportamento fisico reale.

Per questo motivo, quando i dati sono affetti da errore, spesso non interessa interpolare esattamente, ma piuttosto **approssimare nel miglior modo possibile l’andamento generale dei dati**.

---

## Minimi Quadrati

L’idea alla base della regressione è scegliere una funzione appartenente a una certa famiglia di modelli e determinare quella che meglio approssima i dati osservati.

Diversamente dall’interpolazione, qui **non imponiamo** che la funzione passi per tutti i punti, ma cerchiamo quella che complessivamente si discosta il meno possibile dai dati.

Per fare questo bisogna innanzitutto scegliere un **modello matematico** ritenuto adatto a descrivere il fenomeno. Nel caso più semplice si suppone che i dati siano ben rappresentabili mediante una retta.

---

### Retta di regressione

Dato un insieme di punti sperimentali

$$
(x_i,y_i),\qquad i=1,\dots,m
$$

si cerca la retta

$$
y=a_0+a_1x
$$

che meglio approssima tali dati.

L’idea intuitiva è trovare la retta che “passa il più vicino possibile” ai punti sperimentali.

---

### Funzione obiettivo dei minimi quadrati

Per misurare quanto bene una retta approssima i dati si considerano gli **scarti verticali** tra i valori osservati $y_i$ e i valori predetti dalla retta nei corrispondenti punti $x_i$:

$$
a_0+a_1x_i-y_i
$$

Questi scarti prendono il nome di **residui**.

Poiché alcuni residui possono essere positivi e altri negativi, non è sensato sommarli direttamente (si compenserebbero tra loro). Per evitare questo problema si elevano al quadrato e si considera la somma totale:

$$
\boxed{
Q(a_0,a_1)=\sum_{i=1}^{m}(a_0+a_1x_i-y_i)^2
}
$$

Questa quantità misura l’errore quadratico complessivo commesso dalla retta rispetto ai dati.

La **retta di regressione ai minimi quadrati** è definita come quella per cui la funzione $Q(a_0,a_1)$ assume valore minimo.

---

### Interpretazione geometrica del criterio

Il metodo dei minimi quadrati cerca quindi i coefficienti $a_0$ e $a_1$ tali che la somma dei quadrati delle distanze verticali tra i punti e la retta sia minima.

È importante osservare che:

- queste non sono distanze euclidee punto-retta;
- si considerano solo gli scarti lungo l’asse verticale;
- ciò equivale ad assumere che l’errore di misura sia principalmente sulla variabile $y$.

---

### Problema matematico da risolvere

Il problema diventa quindi:

$$
\text{trovare }(a_0,a_1)\text{ tali che }Q(a_0,a_1)\text{ sia minimo}
$$

ossia determinare i coefficienti della retta che minimizzano la funzione quadratica:

$$
Q(a_0,a_1)=\sum_{i=1}^{m}(a_0+a_1x_i-y_i)^2
$$

Poiché $Q$ dipende da due variabili, il problema si traduce in un problema di **minimizzazione in più variabili**.

---

### Verso la formulazione matriciale

Per risolvere il problema in modo sistematico, soprattutto quando il modello contiene più parametri (ad esempio regressione polinomiale di grado superiore), conviene riscrivere tutto in forma matriciale.

Questo permetterà di ottenere una formulazione generale del metodo dei minimi quadrati applicabile non solo alle rette, ma a qualunque modello lineare nei parametri.

---

## Minimi Quadrati - Risoluzione del problema

### 1° $-$ Caso della retta

Possiamo riscrivere la funzione $Q$ in forma vettoriale.

Consideriamo il vettore:

$$
\begin{pmatrix}
a_0+a_1x_0 \\
a_0+a_1x_1 \\
\vdots \\
a_0+a_1x_m
\end{pmatrix}
-
\begin{pmatrix}
y_0\\
y_1\\
\vdots\\
y_m
\end{pmatrix}
$$

Il primo vettore contiene i valori assunti dalla retta nei punti $x_i$, mentre il secondo contiene i dati osservati.

Ricordiamo che, per un vettore:

$$
v=(v_1,\dots,v_n)
$$

la norma euclidea è:

$$
\|v\|_2=\sqrt{v_1^2+\dots+v_n^2}
$$

e quindi:

$$
\|v\|_2^2=v_1^2+\dots+v_n^2
$$

cioè la somma dei quadrati delle componenti.

Di conseguenza possiamo scrivere:

$$
Q(a_0,a_1)=
\left\|
\begin{pmatrix}
a_0+a_1x_0 \\
a_0+a_1x_1 \\
\vdots \\
a_0+a_1x_m
\end{pmatrix}
-
\begin{pmatrix}
y_0\\
y_1\\
\vdots\\
y_m
\end{pmatrix}
\right\|_2^2
$$

---

#### Forma matriciale

Il vettore dei valori della retta può essere scritto come prodotto matrice-vettore:

$$
\begin{pmatrix}
1 & x_0 \\
1 & x_1 \\
\vdots & \vdots \\
1 & x_m
\end{pmatrix}
\begin{pmatrix}
a_0\\
a_1
\end{pmatrix}
$$

Definiamo quindi:

$$
A=
\begin{pmatrix}
1 & x_0 \\
1 & x_1 \\
\vdots & \vdots \\
1 & x_m
\end{pmatrix}
\in\mathbb R^{(m+1)\times 2}
$$

$$
\alpha=
\begin{pmatrix}
a_0\\
a_1
\end{pmatrix}
\in\mathbb R^2
$$

$$
y=
\begin{pmatrix}
y_0\\
y_1\\
\vdots\\
y_m
\end{pmatrix}
\in\mathbb R^{m+1}
$$

In questo modo:

$$
Q(a_0,a_1)=\|A\alpha-y\|_2^2
$$

Questa è la forma fondamentale del problema ai minimi quadrati.

La matrice $A$ coincide con le prime due colonne della matrice di Vandermonde.

---

### 2° $-$ Caso della parabola

Possiamo estendere lo stesso ragionamento ad un modello quadratico:

$$
f(x)=a_0+a_1x+a_2x^2
$$

In questo caso vogliamo trovare i coefficienti:

$$
a_0,a_1,a_2
$$

che minimizzano:

$$
Q(a_0,a_1,a_2)=
\sum_{i=0}^m
(a_0+a_1x_i+a_2x_i^2-y_i)^2
$$

Anche qui possiamo scrivere il problema in forma matriciale.

La matrice diventa:

$$
A=
\begin{pmatrix}
1 & x_0 & x_0^2 \\
1 & x_1 & x_1^2 \\
\vdots & \vdots & \vdots \\
1 & x_m & x_m^2
\end{pmatrix}
$$

mentre il vettore dei coefficienti è:

$$
\alpha=
\begin{pmatrix}
a_0\\
a_1\\
a_2
\end{pmatrix}
$$

Quindi:

$$
Q(a_0,a_1,a_2)=\|A\alpha-y\|_2^2
$$

---

### 3° $-$ Caso generale: polinomio di grado $n$

Per un polinomio di grado $n$:

$$
p_n(x)=a_0+a_1x+a_2x^2+\dots+a_nx^n
$$

la funzione da minimizzare diventa:

$$
Q(a_0,\dots,a_n)
=
\sum_{i=0}^m
(a_0+a_1x_i+\dots+a_nx_i^n-y_i)^2
$$

La matrice associata è:

$$
A=
\begin{pmatrix}
1 & x_0 & x_0^2 & \dots & x_0^n \\
1 & x_1 & x_1^2 & \dots & x_1^n \\
\vdots & \vdots & \vdots & & \vdots \\
1 & x_m & x_m^2 & \dots & x_m^n
\end{pmatrix}
$$

che è ancora una matrice di Vandermonde.

Il problema rimane:

$$
Q=\|A\alpha-y\|_2^2
$$

dove:

$$
\alpha=
\begin{pmatrix}
a_0\\
a_1\\
\vdots\\
a_n
\end{pmatrix}
$$

---

### 4° $-$ Caso generale lineare

Il metodo non vale solo per i polinomi.

Possiamo scegliere un modello costruito come combinazione lineare di funzioni fissate:

$$
f(x)=a_0\phi_0(x)+a_1\phi_1(x)+\dots+a_{n-1}\phi_{n-1}(x)
$$

dove:

$$
\phi_0,\phi_1,\dots,\phi_{n-1}
$$

sono funzioni assegnate, ad esempio:

$$
\sin(x),\cos(x),e^x,\log(x),x^2,\dots
$$

Il modello è detto **lineare** perché i coefficienti:

$$
a_0,\dots,a_{n-1}
$$

compaiono linearmente, anche se le funzioni $\phi_i$ non sono lineari.

La quantità da minimizzare è:

$$
Q(a_0,\dots,a_{n-1})
=
\sum_{i=0}^m
\left(
a_0\phi_0(x_i)+\dots+a_{n-1}\phi_{n-1}(x_i)-y_i
\right)^2
$$

Definiamo allora:

$$
A=
\begin{pmatrix}
\phi_0(x_0) & \phi_1(x_0) & \dots & \phi_{n-1}(x_0) \\
\phi_0(x_1) & \phi_1(x_1) & \dots & \phi_{n-1}(x_1) \\
\vdots & \vdots & & \vdots \\
\phi_0(x_m) & \phi_1(x_m) & \dots & \phi_{n-1}(x_m)
\end{pmatrix}
$$

e:

$$
\alpha=
\begin{pmatrix}
a_0\\
a_1\\
\vdots\\
a_{n-1}
\end{pmatrix}
$$

In questo modo il problema assume ancora la forma compatta:

$$
\boxed{
Q=\|A\alpha-y\|_2^2
}
$$

Questa formulazione è fondamentale perché permette di trattare molti problemi diversi con un unico approccio matematico e numerico.

---

## Minimi Quadrati e fattorizzazione QR

### Modelli lineari e non lineari nei parametri

Nel metodo dei minimi quadrati abbiamo visto che il problema può essere scritto nella forma:

$$
Q(\alpha)=\|A\alpha-y\|^2
$$

Questo è possibile quando il modello dipende **linearmente** dai parametri da determinare.

Ad esempio, nel caso:

$$
f(x)=a_0+a_1x+a_2x^2
$$

oppure più in generale:

$$
f(x)=a_0\phi_0(x)+a_1\phi_1(x)+\dots+a_{n-1}\phi_{n-1}(x)
$$

i parametri:

$$
a_0,a_1,\dots,a_{n-1}
$$

compaiono separatamente e linearmente. In questo modo possiamo raccogliere tutti i coefficienti nella matrice di regressione:

$$
A
$$

che dipende soltanto dai dati e dalle funzioni base $\phi_i$.

---

### Quando il metodo non è direttamente applicabile

Esistono però modelli in cui i parametri compaiono in modo non lineare.

Ad esempio:

$$
f(x)=a_0e^{a_1x}
$$

In questo caso il parametro:

$$
a_1
$$

si trova dentro l’esponenziale e non può essere separato linearmente.

Di conseguenza non è possibile costruire una matrice $A$ tale che:

$$
f(x)=A\alpha
$$

e quindi il problema non può essere ricondotto direttamente alla forma:

$$
Q(\alpha)=\|A\alpha-y\|^2
$$

Il metodo dei minimi quadrati lineari non è quindi applicabile direttamente.  
Per questi casi servono tecniche di regressione non lineare.

---

### Obiettivo del problema ai minimi quadrati

Consideriamo quindi il caso lineare.

Vogliamo trovare il vettore dei parametri:

$$
\alpha=
\begin{pmatrix}
a_0\\
\vdots\\
a_{n-1}
\end{pmatrix}
\in\mathbb R^n
$$

che minimizza la funzione:

$$
Q(\alpha)=\|A\alpha-y\|^2
$$

dove:

$$
A\in\mathbb R^{m\times n},
\qquad
y\in\mathbb R^m
$$

Generalmente si assume:

$$
m\ge n
$$

cioè il numero di dati è maggiore o uguale al numero dei parametri da determinare.

Inoltre si suppone che le colonne di $A$ siano linearmente indipendenti. Questa è una condizione fondamentale perché garantisce che il problema abbia una soluzione unica.

Nel caso polinomiale questa ipotesi è soddisfatta quando i punti $x_i$ sono distinti.

---

### Fattorizzazione QR

Per risolvere il problema si utilizza la fattorizzazione QR della matrice $A$.

Ricordiamo il teorema:

$$
A=Q
\begin{pmatrix}
R\\
0
\end{pmatrix}
$$

dove:

- $Q\in\mathbb R^{m\times m}$ è una matrice ortogonale;
- $R\in\mathbb R^{n\times n}$ è triangolare superiore;
- il blocco $0$ contiene solo zeri.

La matrice ortogonale soddisfa:

$$
Q^TQ=I
$$

Questa proprietà sarà fondamentale nella minimizzazione.

---

### Proprietà della norma euclidea

#### 1° Prima proprietà

Sia:

$$
z\in\mathbb R^m
$$

e sia $Q$ una matrice ortogonale.

Allora:

$$
\|Qz\|^2
=
(Qz)^T(Qz)
=
z^TQ^TQz
=
z^Tz
=
\|z\|^2
$$

Quindi una matrice ortogonale non modifica la norma euclidea di un vettore.

In altre parole:

$$
\boxed{\|Qz\|=\|z\|}
$$

---

#### 2° Seconda proprietà

Supponiamo di avere:

$$
y=
\begin{pmatrix}
y_1\\
y_2
\end{pmatrix}
\in\mathbb R^{n_1+n_2}
$$

Allora:

$$
\|y\|^2
=
\|y_1\|^2+\|y_2\|^2
$$

La norma quadratica totale è quindi la somma delle norme quadratiche delle componenti.

---

### Applicazione al problema dei minimi quadrati

Partiamo da:

$$
\|A\alpha-y\|^2
$$

e sostituiamo la fattorizzazione QR:

$$
A=
Q
\begin{pmatrix}
R\\
0
\end{pmatrix}
$$

Otteniamo:

$$
\|A\alpha-y\|^2
=
\left\|
Q
\begin{pmatrix}
R\\
0
\end{pmatrix}
\alpha
-y
\right\|^2
$$

Moltiplichiamo ora per $Q^T$ all’interno della norma. Poiché $Q$ è ortogonale, la norma non cambia:

$$
=
\left\|
Q^T
\left(
Q
\begin{pmatrix}
R\\
0
\end{pmatrix}
\alpha
-y
\right)
\right\|^2
$$

Semplificando:

$$
=
\left\|
\begin{pmatrix}
R\\
0
\end{pmatrix}
\alpha
-Q^Ty
\right\|^2
$$

Definiamo:

$$
\tilde y = Q^Ty
$$

e separiamo il vettore in due blocchi:

$$
\tilde y=
\begin{pmatrix}
\tilde y_1\\
\tilde y_2
\end{pmatrix}
$$

Otteniamo quindi:

$$
=
\left\|
\begin{pmatrix}
R\alpha\\
0
\end{pmatrix}
-
\begin{pmatrix}
\tilde y_1\\
\tilde y_2
\end{pmatrix}
\right\|^2
$$

cioè:

$$
=
\left\|
\begin{pmatrix}
R\alpha-\tilde y_1\\
-\tilde y_2
\end{pmatrix}
\right\|^2
$$

Applicando la seconda proprietà della norma:

$$
\boxed{
\|A\alpha-y\|^2
=
\|R\alpha-\tilde y_1\|^2
+
\|\tilde y_2\|^2
}
$$

---

### Come si minimizza la funzione

Osserviamo ora una cosa fondamentale.

Il termine:

$$
\|\tilde y_2\|^2
$$

dipende soltanto dai dati e non dai parametri $\alpha$.

Quindi l’unica parte che possiamo modificare è:

$$
\|R\alpha-\tilde y_1\|^2
$$

Poiché una norma quadratica è sempre non negativa:

$$
\|R\alpha-\tilde y_1\|^2\ge0
$$

il valore minimo possibile si ottiene imponendo:

$$
R\alpha-\tilde y_1=0
$$

cioè:

$$
\boxed{
R\alpha=\tilde y_1
}
$$

Abbiamo quindi trasformato il problema di minimizzazione in un sistema lineare.

---

### Sistema finale da risolvere

La matrice:

$$
R
$$

è triangolare superiore.

Di conseguenza il sistema:

$$
R\alpha=\tilde y_1
$$

si risolve facilmente tramite **sostituzione all’indietro**.

Questo è esattamente il principio matematico utilizzato dagli algoritmi numerici basati sulla fattorizzazione QR per risolvere i problemi ai minimi quadrati.

---

## Minimi Quadrati con Funzioni Generiche

Non sempre i dati sperimentali possono essere approssimati bene tramite polinomi. In molti problemi reali il fenomeno osservato presenta comportamenti particolari, ad esempio **periodicità, oscillazioni o andamenti non riconducibili ad una semplice curva polinomiale**.

Un esempio tipico è dato dalle rilevazioni periodiche nel tempo, come:
- temperatura media annuale;
- concentrazione di $CO_2$ nell'atmosfera;
- segnali fisici periodici;
- onde sonore.

In questi casi utilizzare soltanto potenze di $x$ può produrre modelli poco accurati oppure numericamente instabili. Per descrivere correttamente il fenomeno conviene quindi introdurre altre funzioni di base, ad esempio seno e coseno.

Consideriamo il modello:

$$
f(x;a_0,a_1,a_2,a_3)
=
a_0 + a_1x + a_2\sin(2\pi x) + a_3\cos(2\pi x)
$$

Osserviamo che:
- il modello non è polinomiale;
- tuttavia rimane lineare rispetto ai parametri
  $a_0,a_1,a_2,a_3$.

Questa è la proprietà fondamentale che permette di applicare ancora il criterio dei minimi quadrati.

Infatti il modello può essere riscritto come combinazione lineare di funzioni assegnate:

$$
f(x)
=
a_0\phi_0(x)
+
a_1\phi_1(x)
+
a_2\phi_2(x)
+
a_3\phi_3(x)
$$

dove:

$$
\phi_0(x)=1,
\qquad
\phi_1(x)=x,
\qquad
\phi_2(x)=\sin(2\pi x),
\qquad
\phi_3(x)=\cos(2\pi x)
$$

Questo rientra nel cosiddetto **caso lineare generale** del metodo dei minimi quadrati.

Dato un insieme di dati:

$$
(x_i,y_i),
\qquad i=1,\dots,m
$$

si vuole trovare il vettore dei parametri

$$
\alpha =
\begin{pmatrix}
a_0\\
a_1\\
a_2\\
a_3
\end{pmatrix}
$$

che minimizza la distanza quadratica cumulativa:

$$
Q(a_0,\dots,a_{n-1})
=
\sum_{i=1}^{m}
\left(
a_0\phi_0(x_i)
+
\dots
+
a_{n-1}\phi_{n-1}(x_i)
-
y_i
\right)^2
$$

### Differenza matrice $A$ rispetto al caso polinomiale

Anche in questo caso il problema può essere scritto in forma matriciale:

$$
Q(\alpha)=\|A\alpha-y\|^2
$$

dove:
- $A$ è la matrice di regressione;
- $\alpha$ contiene i parametri incogniti;
- $y$ contiene i dati osservati.

La matrice $A$ non è più una matrice di Vandermonde classica, perché le colonne non contengono potenze di $x$, ma i valori delle funzioni base valutate nei punti dati:

$$
A =
\begin{pmatrix}
\phi_0(x_1) & \phi_1(x_1) & \dots & \phi_{n-1}(x_1)\\
\phi_0(x_2) & \phi_1(x_2) & \dots & \phi_{n-1}(x_2)\\
\vdots & \vdots & & \vdots\\
\phi_0(x_m) & \phi_1(x_m) & \dots & \phi_{n-1}(x_m)
\end{pmatrix}
$$

Dal punto di vista implementativo, invece di costruire la matrice usando i monomi:

$$
1,x,x^2,\dots
$$

si costruiscono le colonne applicando direttamente le funzioni della base ai dati $x_i$.

Quindi la funzione che costruisce la matrice di regressione riceve:
- il vettore delle ascisse $x$;
- una lista di funzioni base $\phi_i$.

Il numero di colonne della matrice coincide con il numero di funzioni scelte.

### Rango massimo non garantito

A differenza del caso polinomiale, però, **non è più garantito automaticamente che la matrice abbia rango massimo**. Alcune funzioni della base potrebbero infatti risultare linearmente dipendenti sui dati considerati.

Per questo motivo, in applicazioni generali, invece della fattorizzazione QR si preferisce spesso utilizzare la **decomposizione ai valori singolari (SVD)**.

La SVD è più stabile numericamente e permette di gestire anche casi in cui:
- la matrice è quasi singolare;
- le colonne sono quasi dipendenti;
- il problema è mal condizionato.

Per questo motivo la SVD rappresenta uno degli strumenti più importanti nell'approssimazione numerica e nell'analisi dei dati.

---