# Numeri di Macchina

## Introduzione ad Alcune Problematiche

### (1) Esempio ciclo "infinito"

La prof fornito il seguente esempio di algoritmo scritto in Python:

```py
u = 1
i = 0
while u + 1 > 1:
    u /= 2
    i += 1
print(u, i)
```

In matematica reale il ciclo sarebbe infinito, perchè per ogni numreo positivo $u > 0$, vale sempre:

$$ 1 + u > 1 $$

Quindi la condizione del `while` sarebbe sempre vera.

In Python però i `float` non sono numeri reali infiniti: sono rappresentati nel formati **IEEE 754 double precision**, cioè con **64 bit**.

- 1 bit di segno
- 11 bit di esponente
- 52 bit di mantissa (+ 1 bit implicito)

Questo indica che esiste una **precisione finita**. Intorno al numero 1, la distanza tra due numeri rappresentabili consecutivi è:

$$ 2^{-52} $$

Quando `u` diventa più piccolo di questa quantità, l'operazione `1 + u` non riesce più a distinguere il risultato da 1, perchè `u` è sotto la soglia di precisione della mantissa.

Quindi accade che:
$$ 1 + \frac{1}{2^{k}} = 1 \hspace{25px} k \ge 53 $$
e la condizione `u + 1 > 1` diventa `1 > 1` che è falsa.

Il numero di iterazioni è 53 perchè sto dividendo per 2 partendo da 1:

$$ u = 2^{-i} $$

La prima potenza di due che non modifica più l'1 nella somma è $2^{-53}$. Dopo 53 divisioni `u` è troppo piccolo per influenzare il risultato.

### (2) Esempio ciclo infinito

La prof fornito il seguente esempio di algoritmo scritto in Python:

```py
a = 1000
while a != 0:
    a -= 0.001
print(a)
```

Matematicamente il ciclo dovrebbe terminare in un numero finito di iterazioni. Infatti:

$$ 1000 = 10^6 \cdot 10^{-3} $$

Quindi dopo $1.000.000$ sottrazioni di $0,001$ il valore dovrebbe diventare esattamente 0.

Il problema nasce dal fatto che in Python i `float` sono rappresentati in formati **IEEE 754 double precision**. Quindi il numero $0,001 = 10^{-3}$ non è rappresentabile esattamente in base 2. In memoria viene salvato come un numero **approssimato**. 

Qindi ciò che realmente avviene è del tipo:

$$ a = 1000 - 0,001 $$

dove $0,001$ è una piccola approssimazione di $0,001$. Ad ogni iterazione si **sottrae un valore leggermente impreciso**; e l'errore totale di approssimazione **si accumula**.

Dopo moltissime iterazioni quasi sicuramente **NON otterremo esattamente 0**, arrivando ad un `a` negativo e proseguendo con le iterazioni.

### (3) Esempio divisione ed esponente

La prof fornito il seguente esempio di algoritmo scritto in Python:

```py
print(
    (33 / 5) ** 2,
    (33 ** 2) / (5 ** 2)
)
>> 43.559999999999995 43.56
```

Matematicamente le due espressioni sono equivalenti:
$$ \left( \frac{33}{5} \right)^2 = \frac{33^2}{5^2} $$
e dovrebbero risultare entrambe **43.56**.

Il problema nasce dal fatto che in Python i `float` sono rappresentati in formati **IEEE 754 double precision**.

Nel primo caso, $(33/5)^2$ abbiamo che:
1. `33 / 5` produce **6.6**, ma 6.6 non è rappresentabile esattamente in binario. Viene salvato come qualcosa tipo:
    $$ 6.5999999999999996\dots $$
2. Poi eleviamo al quadrato quel numero **già approssiamato**. L'errore iniziale viene quindi **amplificato dal quadrato**, e otteniamo:
    $$ 43.559999999999995 $$

Nel secondo caso, $(33^2) / (5^2)$ abbiamo che:
1. `33 ** 2 = 1089` $\to$ intero esatto;
2. `5 ** 2 = 25` $\to$ intero esatto;
3. Solo alla fine facciamo `1089 / 25`.

Il risultato matematico è 43.56, che in binario **non è rappresentabile esattamente**, ma l'approssimazione prodotta dal sistema **è così vicina** che Python lo stampa come 43.56 (La conversione in stringa lo arrotonda meglio).

> **NOTA**: In aritmetica floating point vale:
> $$ (a \div b)^2 \ne a^2 \div b^2 $$
> non per motivi matematici, ma per **propagazione diversa degli errori di arrotondmento**.

---

## Esempio Conversione (Base decimale $\Rightarrow$ Forma scientifica)

1. **Numero dato**: $-123,987$
2. **Scomposizione in potenze di 10**:
    $$-\;(1\cdot 10^2 + 2\cdot 10^1 + 3\cdot 10^0 + 9\cdot 10^{-1} + 8\cdot 10^{-2} + 7\cdot 10^{-3})$$
3. Per ottenere la **forma Scientifica** si scrive il numero come:
    $$\pm m \cdot 10^e$$
    con mantissa normalizzata. Nel nostro caso, con mantissa compresa tra 0 e 1:
    $$ -0,123987 \cdot 10^3 $$
4. **Otteniamo qundi**:
    $$ -123,987 = (-1) \cdot 0,123987 \cdot 10^3 $$
    Dove:
    - **Segno** = Negativo
    - **Esponente** = $3$
    - **Mantissa** = $0,123987$

## Rappresentazione IEEE 754 dei Numeri Reali

La rappresentazione dei numeri reali nei calcolatori segue lo standard **IEEE 754**, che definisce come memorizzare i numeri in virgola mobile. L’idea alla base è la stessa della notazione scientifica, ma in base 2 invece che in base 10. Un numero viene quindi scritto nella forma normalizzata

$$ \pm (1.a_2\dots a_t)_\beta \cdot \beta^r $$

dove il segno è separato, la parte frazionaria costituisce la mantissa e $r$ è l’esponente.

In IEEE 754 un numero è suddiviso in tre parti: un bit di segno, un campo per l’esponente e un campo per la mantissa (o frazione). Il valore rappresentato è

$$ (-1)^S \cdot 1.F \cdot 2^{(E - bias)} $$

dove $S$ è il bit di segno, $F$ è la frazione memorizzata e il $bias$ è una costante che serve per interpretare correttamente l’esponente.

I formati standard fissano il numero totale di bit utilizzati. In **precisione singola (32 bit)** si hanno 1 bit di segno, 8 bit di esponente e 23 bit di mantissa. In **precisione doppia (64 bit)** si hanno 1 bit di segno, 11 bit di esponente e 52 bit di mantissa. Anche se in singola precisione la mantissa occupa 23 bit, la precisione effettiva è di 24 bit: nei numeri normalizzati il primo bit della mantissa è sempre 1, quindi non viene memorizzato (è il cosiddetto "bit nascosto"). Questo permette di aumentare la precisione senza occupare spazio aggiuntivo.

L’esponente può essere sia positivo sia negativo. Per evitare di dedicare un bit al suo segno, si utilizza una rappresentazione con bias: invece di memorizzare direttamente l’esponente reale $r$, si memorizza $r + bias$. Nel formato a 32 bit il bias vale **127**, mentre in quello a 64 bit vale **1023**. Quando il numero viene utilizzato nelle operazioni aritmetiche, l’hardware sottrae automaticamente il bias per ricostruire l’esponente corretto.

Il bias non serve solo a rappresentare esponenti negativi senza un bit di segno separato. Ha anche un ruolo pratico nelle operazioni di macchina. Poiché gli esponenti sono memorizzati come numeri non negativi (grazie al bias), il confronto tra due esponenti per stabilire quale sia maggiore è più semplice dal punto di vista hardware. Questo facilita proprio l’operazione di riallineamento necessaria per somme e sottrazioni.

Lo **zero** non può essere rappresentato in forma normalizzata, perché non esiste un primo 1 significativo. Per questo IEEE 754 prevede una configurazione speciale: esponente e mantissa tutti a zero. Esistono sia $+0$ sia $-0$, distinti solo dal bit di segno.

Un aspetto fondamentale per il Calcolo Numerico è che n**on tutti i numeri reali sono rappresentabili esattamente**. Se, dopo la conversione in binario e la normalizzazione, la mantissa richiede più bit di quelli disponibili, i bit in eccesso devono essere eliminati. Questo comporta una **perdita di informazione** e introduce un **errore di rappresentazione**. In teoria si potrebbe semplicemente troncare (**Troncamento**) i bit in eccesso, ma lo standard IEEE 754 prevede modalità di arrotondamento (la più comune è l’**Arrotondamento** al più vicino), che riducono l’errore medio.

Di conseguenza, l’insieme dei numeri rappresentabili in macchina è finito e discreto, mentre l’insieme dei numeri reali è infinito e continuo. Ogni operazione aritmetica può introdurre piccoli errori di arrotondamento, che **nel tempo possono accumularsi o propagarsi**. Proprio da queste considerazioni nasce l’importanza, nel Calcolo Numerico, dello studio degli errori e della stabilità degli algoritmi.

---

## Errori di Approssimazione

Quando lavoriamo con numeri reali al calcolatore dobbiamo sempre ricordare che il numero memorizzato non è, in generale, il numero reale "vero", ma una sua approssimazione. Indichiamo con $\alpha$ il numero reale esatto e con $\alpha^*$ oppure $fl(\alpha)$ la sua rappresentazione in macchina (floating point).

La differenza tra questi due valori introduce un errore, che può essere misurato in modi diversi.

### Errore Assoluto

L’**errore assoluto** misura la distanza effettiva tra il numero reale e la sua approssimazione:

$$ E_a = |\alpha - \alpha^*| $$

È semplicemente la differenza in valore assoluto. Ci dice “di quanto sbagliamo”, ma non ci dice se l’errore è grande o piccolo rispetto al numero di partenza.

Ad esempio, un errore assoluto pari a 0.1 può essere:
- enorme se il numero vale $0.2$
- trascurabile se il numero vale $10.000$

Per questo motivo l’errore assoluto, da solo, non è sufficiente per confrontare l’accuratezza su numeri di grandezza diversa.

### Errore relativo

Per valutare l’errore in modo proporzionale alla grandezza del numero, si introduce l’**errore relativo**:

$$ E_r = \frac{E_a}{|\alpha|} = \frac{|\alpha - \alpha^*|}{|\alpha|} $$

L’errore relativo normalizza l’errore assoluto rispetto al valore reale. In questo modo possiamo capire se l’errore è grande o piccolo in termini percentuali.

È importante osservare che:

- non ha senso confrontare errori assoluti di numeri molto diversi tra loro;
- per confrontare l’accuratezza si usa l’errore relativo.

Inoltre, l’errore relativo fornisce un’indicazione su quante cifre significative sono corrette. Se l’errore relativo è dell’ordine di $10^{-k}$, significa che circa $k$ cifre decimali sono affidabili.

#### Esempio

Supponiamo di avere il numero reale:

$$ \alpha = {(1.001)}_2 \cdot 2^1 = {(2.25)}_{10} $$

e che, a causa della limitazione della mantissa, venga rappresentato in macchina come:

$$ fl(\alpha) = {(1.00)}_2 \cdot 2^1 = {(2)}_{10} $$

Si è perso l’ultimo bit significativo.

L’errore assoluto vale:

$$ E_a = |2 - 2.25| = 0.25 $$

L’errore relativo è:

$$ E_r = \frac{0.25}{2.25} \simeq 0.111\dots $$

cioè un errore dell’$11$%. Questo mostra chiaramente come la perdita di un solo bit possa generare un errore non trascurabile.

### Teorema dell’errore di rappresentazione

Un risultato fondamentale del Calcolo Numerico stabilisce un limite superiore all’errore relativo dovuto alla rappresentazione in macchina. Viene infatti:

$$ \frac{|fl(\alpha) - \alpha|}{|\alpha|} \le \beta^{1 - t} $$

dove:

- $\beta$ è la base (per IEEE 754, $\beta = 2$)
- $t$ è il numero di cifre della mantissa (in singola precisione si considerano 24 cifre effettive grazie al bit nascosto)

In forma equivalente si può scrivere:

$$ fl(\alpha) = \alpha(1 + \epsilon), \hspace{12px} |\epsilon| \le u $$

dove $u = \beta^{1 - t}$ è detta **precisione di macchina** (o machine epsilon, in senso teorico).

### Precisione di macchina

La precisione di macchina rappresenta il **massimo errore relativo** che si può commettere nella rappresentazione di un numero reale nel formato scelto.

In altre parole:

- è la distanza relativa massima tra un numero reale e la "crocetta" più vicina rappresentabile in macchina
- è il limite superiore dell’errore di rappresentazione

Per IEEE 754:

- in singola precisione (32 bit), $ u \approx 2^{-23} $
- in doppia precisione (64 bit), $ u \approx 2^{-52} $

Questo valore è estremamente piccolo in doppia precisione, motivo per cui i calcoli scientifici usano quasi sempre i 64 bit.

### Rappresentazione dei float in Python

In Python, i numeri `float` sono rappresentati in **doppia precisione (64 bit)** secondo lo standard IEEE 754. Possiamo ottenere informazioni sul formato usando:

```py
import sys
sys.float_info
```

Questa struttura contiene:

- la precisione di macchina (`epsilon`),
- il massimo e minimo numero rappresentabile,
- il numero di cifre significative,
- informazioni sull’esponente.

Ad esempio, `sys.float_info.epsilon` restituisce la differenza tra 1 e il più piccolo numero maggiore di 1 rappresentabile in macchina. Questo valore è collegato alla precisione di macchina studiata teoricamente.

---

## Operazioni con i numeri floating point

Quando si eseguono operazioni tra numeri floating point, il calcolatore non lavora direttamente sui valori reali, ma sulle loro rappresentazioni finite in formato IEEE 754. Questo comporta passaggi interni che possono introdurre ulteriori errori rispetto al solo errore di rappresentazione.

### Somma tra due numeri

Consideriamo ad esempio la somma tra due numeri in virgola mobile con esponenti diversi. Prima di poterli sommare, la macchina deve esprimerli con lo stesso esponente. Per farlo, confronta gli esponenti e riallinea le mantisse. In particolare, l’esponente più piccolo viene portato al valore di quello più grande, e questo comporta uno shift verso destra della mantissa del numero con esponente minore.

Questo passaggio è inevitabile: per sommare due numeri in notazione scientifica (anche in base 10) è necessario che abbiano la stessa potenza. Tuttavia, lo shift verso destra può far “uscire” dei bit significativi dalla mantissa. Se questi bit superano la lunghezza disponibile, vengono persi, generando un errore per troncamento o arrotondamento.

La macchina sceglie sempre di portare l’esponente più piccolo a quello più grande e non il contrario. Se si facesse l’operazione inversa, si dovrebbe shiftare verso destra la mantissa del numero più grande, causando una perdita di informazione molto più grave. In questo modo si minimizza l’errore complessivo.

### Errore di incolonnamento

Un caso particolarmente delicato si verifica quando si somma (o sottrae) un numero molto grande con uno molto piccolo. Dopo il riallineamento degli esponenti, la mantissa del numero piccolo può essere shiftata così tanto verso destra da diventare irrilevante rispetto alla precisione disponibile.

In situazioni estreme può accadere che:

$$ x + y = x \text{ anche se } y \ne 0 $$

Questo fenomeno è noto come errore di incolonnamento. Il numero piccolo viene completamente “assorbito” dal numero grande perché, dopo l’allineamento, le sue cifre significative cadono oltre la precisione della macchina.

Una condizione tipica in cui questo accade è quando il numero più piccolo ha modulo dell’ordine di:

$$ |y| \le \frac{u}{\beta}|x| $$

dove $u$ è la precisione di macchina e $\beta$ è la base (per IEEE 754, $\beta = 2$). In particolare, se il numero piccolo è inferiore alla precisione di macchina rispetto al numero grande, l’operazione di somma non modifica il risultato rappresentato: il numero grande rimane invariato.

Questo effetto è strettamente legato alla distribuzione non uniforme dei numeri rappresentabili: più ci si allontana dallo zero, maggiore è la distanza tra due numeri consecutivi rappresentabili. Di conseguenza, numeri molto piccoli rispetto a un numero grande possono risultare “invisibili” alla macchina.

### Non validità della proprietà associativa

...

---
