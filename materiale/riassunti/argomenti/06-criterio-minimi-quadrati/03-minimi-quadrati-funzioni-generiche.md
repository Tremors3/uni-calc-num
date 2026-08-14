
# Minimi Quadrati con Funzioni Generiche

Non sempre i dati sperimentali sono ben approssimati da un polinomio. Alcuni fenomeni presentano periodicità, oscillazioni o altre strutture che possono essere descritte meglio utilizzando funzioni diverse dalle potenze di $x$.

Ad esempio, per fenomeni periodici si possono utilizzare seno e coseno.

Consideriamo il modello

$$
f(x;a_0,a_1,a_2,a_3)
=
a_0+a_1x+a_2\sin(2\pi x)+a_3\cos(2\pi x)
$$

Il modello non è polinomiale, ma è comunque **lineare rispetto ai parametri**

$$
a_0,a_1,a_2,a_3
$$

Possiamo infatti scriverlo come

$$
f(x)
=
a_0\phi_0(x)
+a_1\phi_1(x)
+a_2\phi_2(x)
+a_3\phi_3(x)
$$

con

$$
\phi_0(x)=1
$$

$$
\phi_1(x)=x
$$

$$
\phi_2(x)=\sin(2\pi x)
$$

$$
\phi_3(x)=\cos(2\pi x)
$$

Il problema rientra quindi nel caso generale dei minimi quadrati lineari.

Dato un insieme di dati $(x_i,y_i)$, si costruisce la matrice

$$
A=
\begin{pmatrix}
\phi_0(x_0) & \phi_1(x_0) & \dots & \phi_{n-1}(x_0)\\
\phi_0(x_1) & \phi_1(x_1) & \dots & \phi_{n-1}(x_1)\\
\vdots & \vdots & & \vdots\\
\phi_0(x_m) & \phi_1(x_m) & \dots & \phi_{n-1}(x_m)
\end{pmatrix}
$$

e il vettore

$$
\alpha=
\begin{pmatrix}
a_0\\
a_1\\
\vdots\\
a_{n-1}
\end{pmatrix}
$$

Il problema diventa ancora

$$
\boxed{
\min_\alpha\|A\alpha-y\|_2^2
}
$$

La differenza rispetto al caso polinomiale è che $A$ non è necessariamente una matrice di Vandermonde. Le sue colonne sono ottenute valutando le funzioni di base $\phi_i$ nei punti $x_j$.

Dal punto di vista implementativo, la matrice di regressione viene quindi costruita fornendo i dati $x_i$ e le funzioni di base scelte. Ogni funzione genera una colonna della matrice.

## Rango della matrice di regressione

Nel caso generale non è garantito automaticamente che le colonne di $A$ siano linearmente indipendenti.

Può infatti accadere che due o più funzioni della base siano linearmente dipendenti, oppure quasi dipendenti, quando vengono valutate sui dati considerati.

La condizione di rango pieno sulle colonne è

$$
\boxed{
\operatorname{rank}(A)=n
}
$$

dove $n$ è il numero di colonne.

Nel caso tipico

$$
A\in\mathbb R^{m\times n},
\qquad m>n
$$

le righe non possono essere tutte linearmente indipendenti, mentre ciò che interessa per l’unicità dei parametri sono le **colonne**.

Le colonne rappresentano infatti le funzioni di base utilizzate per costruire il modello.

Quando le colonne sono linearmente indipendenti, il problema dei minimi quadrati ha una soluzione unica. Quando invece il rango è inferiore a $n$, possono esistere infinite soluzioni minimizzanti.

Per problemi generali o quando il rango è incerto, la **decomposizione ai valori singolari (SVD)** è particolarmente utile perché permette di gestire anche matrici rettangolari e di rango non pieno.

---