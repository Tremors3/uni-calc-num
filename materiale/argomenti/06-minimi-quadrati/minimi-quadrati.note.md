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