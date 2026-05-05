
# (28) Lezione 05-04-2026 | s 342.. | Approssimazione di dati e funzioni: il criterio dei minimi quadrati

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

