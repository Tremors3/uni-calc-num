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
$$ 1 + \frac{1}{2^{k}} = 1 \quad k \ge 53 $$
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

$$ fl(\alpha) = \alpha(1 + \varepsilon), \quad |\varepsilon| \le u $$

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

## Proprietà algebriche e aritmetica floating point

Nell’aritmetica reale valgono proprietà fondamentali come l’associatività della somma, la distributività del prodotto rispetto alla somma e la legge di annullamento del prodotto. Tuttavia, quando si lavora in aritmetica floating point, queste proprietà non sono più garantite. Il motivo è che ogni operazione di macchina introduce un errore di arrotondamento, e questi errori dipendono dall’ordine con cui le operazioni vengono eseguite.

È essenziale comprendere che il calcolatore non lavora sui numeri reali, ma sulle loro approssimazioni finite. Ogni volta che si esegue un’operazione, il risultato viene nuovamente arrotondato al numero rappresentabile più vicino. Questo fa sì che il risultato finale di un’espressione dipenda dall’algoritmo utilizzato per calcolarla.

### Non validità della proprietà associativa della somma

In matematica vale sempre:

$$ (x + y) + z = x + (y + z) $$

In aritmetica floating point, invece, può accadere che:

$$ fl(fl(x + y) + z) = fl(x + fl(y + z)) $$

Il problema nasce dal fatto che, prima ancora di eseguire la somma, la macchina deve **riallineare gli esponenti**. Se i numeri hanno ordini di grandezza diversi, il numero con esponente più piccolo viene shiftato verso destra, e può **subire troncamento**.

Di conseguenza, se in un caso si sommano prima due numeri piccoli e poi il risultato viene sommato a uno grande, l’errore può essere diverso rispetto al caso in cui si somma prima un numero grande con uno piccolo. Anche se sulla carta i due **algoritmi sono equivalenti**, in macchina producono **risultati differenti**.

Questo mostra che l’associatività della somma non è valida nell’aritmetica finita.

### Non validità della proprietà distributiva

In matematica vale la proprietà distributiva:

$$ x(y + z) = xy + xz $$

In aritmetica floating point, invece, può verificarsi che:

$$ fl(x + z) \ne fl(fl(x \cdot y) + fl(x \cdot z)) $$

Anche qui il problema è legato agli arrotondamenti intermedi. Nel primo caso si effettua prima la somma $y + z$, con il relativo errore, e poi si moltiplica il risultato per $x$. Nel secondo caso si eseguono prima due prodotti separati, ciascuno con il proprio errore di arrotondamento, e poi si sommano i risultati, introducendo un ulteriore errore.

Le due sequenze di operazioni, pur essendo **matematicamente equivalenti**, generano **catene di errori diverse**. Il risultato finale può quindi differire in modo anche significativo, soprattutto se i numeri coinvolti hanno ordini di grandezza molto diversi.

### Legge di annullamento del prodotto

Un altro fenomeno tipico dell’aritmetica floating point riguarda la moltiplicazione di numeri molto piccoli. Supponiamo di avere due numeri $x$ e $y$, entrambi compresi tra 0 e 1 e ancora rappresentabili in macchina. Il loro prodotto può essere **così piccolo da non essere più rappresentabile** nel formato scelto.

In questo caso si verifica un **underflow** e può accadere che:

$$ fl(x \cdot y) = 0 \space\text{ anche se }\space x,y \ne 0 $$

Questo contraddice la legge matematica secondo cui il prodotto di due numeri non nulli non può essere nullo. In aritmetica finita, invece, il risultato può “collassare” a zero perché esce dall’intervallo dei numeri rappresentabili.

### Conseguenze per gli algoritmi numerici

Questi esempi mostrano un fatto fondamentale:

1. Nell’aritmetica del calcolatore non valgono molte delle proprietà algebriche usuali. **L’aritmetica finita introduce errori a ogni operazione**, e tali **errori si propagano** lungo la sequenza di calcoli.

2. Il risultato di un’espressione, intesa come successione di operazioni aritmetiche, dipende quindi dall’**algoritmo utilizzato per calcolarla**. Due algoritmi matematicamente equivalenti possono produrre risultati diversi in macchina, perché **generano e propagano errori in modo differente**.

Per questo motivo, nel Calcolo Numerico non ci si limita a verificare che un algoritmo sia corretto dal punto di vista matematico, ma si analizza anche la sua stabilità numerica.

- L’**obiettivo** è scegliere formulazioni che riducano al minimo l’amplificazione degli errori e che forniscano risultati il più possibile accurati all’interno dell’aritmetica finita del calcolatore.

- **Trade-off** tra efficienza in termini di risorse (temporali, spaziali) e **stabilità** (*correttezza, accuratezza, consistenza*) dei risultati.

## Relazione tra errore relativo e precisione di macchina

Quando eseguiamo un’operazione in aritmetica floating point, il risultato memorizzato non coincide esattamente con il valore reale dell’operazione, ma con la sua approssimazione rappresentabile. Tuttavia, l’errore relativo che si commette è sempre limitato superiormente dalla **precisione di macchina**.

Se indichiamo con $fl(x \bullet y)$ il risultato di macchina dell’operazione reale $x \bullet y$, vale:

$$ \frac{|fl(x \bullet y ) - (x \bullet y)|}{|x \bullet y|} \le k\beta^{1-t} $$

dove:
- $\beta$ è la base (per IEEE 754, $\beta = 2$)
- $t$ è il numero di cifre della mantissa
- $k$ dipende dal tipo di approssimazione

Nel caso di **troncamento**, l’errore massimo può arrivare fino all’intera distanza tra due numeri consecutivi, quindi:

$$ k = 1 $$

Nel caso di arrotondamento al più vicino (quello usato in IEEE 754), l’errore massimo è metà di tale distanza, quindi:

$$ k = \frac{1}{2} $$

### Definizione di precisione di macchina

In genere si incorpora il fattore $k$ direttamente nella definizione di precisione di macchina $u$, scrivendo:

$$ fl(z) = z(1 + \varepsilon), \quad |\varepsilon| \le u $$

dove

$$ u = \begin{cases}
    \beta^{1-t} & (\text{troncamento})\\
    \frac{1}{2}\beta^{1-t} & (\text{arrotondamento al più vicino})
\end{cases}$$

Poiché nei calcolatori la base è $\beta = 2$, arrotondando al più vicino, l’errore massimo possibile è metà di quella distanza:

$$ u = \frac{1}{2}\beta^{1-t} = \beta^{-t} $$

Qui $t$ è il numero di bit significativi effettivi della mantissa, cioè includendo il bit nascosto: in singola precisione $t = 24$, in doppia precisione $t = 53$.

### Osservazione importante

Il fatto che **l’errore relativo sia limitato dalla precisione di macchina** vale per qualsiasi numero reale rappresentabile e, in particolare, per i risultati delle singole operazioni di macchina.

Ogni operazione introduce un errore relativo al più dell’ordine di $u$. Tuttavia, quando si eseguono **molte operazioni in sequenza**, questi piccoli errori possono **propagarsi o amplificarsi**, ed è per questo che l’analisi degli algoritmi numerici non si limita al singolo passo, ma considera l’intero processo di calcolo.

## Analisi degli errori: peso e propagazione

Quando si lavora in aritmetica floating point, ogni numero **memorizzato dal calcolatore** contiene già un **piccolo errore relativo** dovuto alla rappresentazione. Possiamo scrivere ogni variabile come

$$ fl(s) = s(1 + \varepsilon), \quad |\varepsilon| \le u $$

dove $u$ è la precisione di macchina. Questo errore iniziale si chiama **errore sugli input**.

Supponiamo di voler calcolare $\alpha = x + y + z$ e consideriamo l’algoritmo che somma prima $x + y$ e poi aggiunge $z$:

$$ \alpha^* = fl\big(fl(fl(x) + fl(y)) + fl(z)\big) $$

Analizzando passo passo:

1. Gli input sono già approssimati:

    - $fl(x) = x(1 + \varepsilon_x), \text{ con } |\varepsilon_x| \le u$
    - $fl(y) = y(1 + \varepsilon_y), \text{ con } |\varepsilon_y| \le u$
    - $fl(z) = z(1 + \varepsilon_z), \text{ con } |\varepsilon_z| \le u$

2. La prima somma introduce un nuovo errore $\varepsilon_1$ dovuto all’operazione stessa:

    $$\begin{aligned}
        fl(fl(x) + fl(y)) 
        &= (fl(x) + fl(y))(1 + \varepsilon_1), && |\varepsilon_1| \le u \\
        &= \big(x(1+\varepsilon_x) + y(1+\varepsilon_y)\big)(1 + \varepsilon_1) \\
        &= x + y + x\varepsilon_x + y\varepsilon_y + x\varepsilon_1 + y\varepsilon_1 
        + \textcolor{lightgreen}{x\varepsilon_x \varepsilon_1 + y\varepsilon_y \varepsilon_1} \\
        &\simeq x + y + x\varepsilon_x + y\varepsilon_y + (x+y)\varepsilon_1
    \end{aligned}$$

    > Stiamo applicando un'**approssimazione lineare**. Il termine completo sarebbe
    >
    > $$ x\varepsilon_x\varepsilon_1 + y\varepsilon_y\varepsilon_1$$
    >
    > cioè il prodotto tra l’errore sugli input e l’errore dell’operazione.
    >
    > Questi termini sono **di secondo ordine**, cioè dell’ordine $u^2$, molto piccoli rispetto agli altri termini ($u$ è la precisione di macchina, tipicamente $2^{-24}$ o $2^{-53}$).
    >
    > In analisi dell’errore numerico, si **trascurano i termini di secondo ordine**, perché non contribuiscono significativamente alla stima dell’errore relativo complessivo. Questo semplifica il raccolimento e permette di scrivere i termini come una somma pesata lineare degli errori.

3. Aggiungendo $fl(z)$ e arrotondando di nuovo si introduce un secondo errore $\varepsilon_2$:

    $$ \alpha^* \simeq x + y + z + x\varepsilon_x + y\varepsilon_y + z\varepsilon_z + (x+y)\varepsilon_1 + (x+y+z)\varepsilon_2 $$

### Somma pesata degli errori

Normalizzando per $x + y + z$, l’errore relativo totale diventa:

$$
E_r \simeq 
\underbrace{\frac{x}{x+y+z}\varepsilon_x + \frac{y}{x+y+z}\varepsilon_y + \frac{z}{x+y+z}\varepsilon_z}_{\text{errore sugli input}}
+
\underbrace{\frac{x+y}{x+y+z}\varepsilon_1 + \varepsilon_2}_{\text{errore dell’algoritmo}}
$$

In questa formula:

- La prima parte rappresenta l’errore dovuto alla **rappresentazione dei dati**, cioè il fatto che i numeri iniziali non sono esatti.

- La parte in giallo rappresenta l’errore dovuto alle **operazioni**, cioè all’algoritmo utilizzato e al troncamento/arrottondamento in ciascun passo.

Osservazioni chiave:

1. L’errore sugli input viene **pesato** rispetto al contributo di ciascun numero nella somma totale: numeri più grandi trasmettono un errore maggiore.

2. L’errore dell’algoritmo cresce con la somma dei numeri coinvolti nell’operazione: più grande è la quantità che stiamo arrotondando, maggiore sarà l’errore assoluto introdotto.

3. Questo modello mostra come gli errori **si propagano e si combinano** lungo la sequenza di operazioni. La scelta dell’algoritmo e l’ordine delle operazioni influenzano direttamente il risultato finale.

> **Nota**: in una macchina ideale con aritmetica infinita, non ci sarebbe errore introdotto dalle operazioni; l’unica fonte di errore sarebbe quella dei dati rappresentati in floating point.

## Somma generica pesata degli errori

Supponiamo di voler calcolare:

$$ \alpha = x_1 + x_2 + \cdots + x_n $$

e che l'algoritmo sommi i numeri **uno alla volta** seguendo l'ordine $\big(\big(\big(x_1 + x_2\big) + x_3\big) + \cdots + x_n\big)$.

### 1) Errori sugli input

Ogni numero ha un valore relativo iniziale $\varepsilon_i$:

$$ fl(x_i) = x_i(1 + \varepsilon_i), \quad |\varepsilon_i| \le u $$

Quando normalizziamo rispetto alla somma totale $\sum_{i=1}^{n} x_i$, il contributo di ciascun errore sugli input è **pesato**:

$$ \text{Errore sugli input} = \sum_{i = 1}^{n} \frac{x_i}{\sum_{j = 1}^{n} x_j}\varepsilon_i $$

### 2) Errori introdotti dalle operazioni

Ogni somma parziale introduce un nuovo errore di arrotondamento $\varepsilon_k$ (errore dell’algoritmo) che viene **pesato dalla somma dei termini già sommati**:

$$ \text{Errore delle operazioni} = \sum_{k = 1}^{n - 1} \frac{\sum_{i = 1}^{k} x_i}{\sum_{i = 1}^{n} x_i}\varepsilon_k + \varepsilon_n $$

- Qui $\varepsilon_1$ è l'errore della prima somma $x_1 + x_2$, $\epsilon_2$ della seconda somma $(x_1 + x_2) + x_3$, e così via fino a $\varepsilon_{n-1}$.
- L’ultimo termine non introduce un nuovo peso perché dopo l’ultima somma si prende l’errore $\varepsilon_{n-1}$ della somma finale.

### 3) Formula generale

Combinando i due contributi otteniamo l’errore relativo totale:

$$
E_r \simeq 
\underbrace{\sum_{i=1}^n \frac{x_i}{\sum_{j=1}^n x_j} \varepsilon_i}_{\text{errore sugli input}}
+
\underbrace{\sum_{k=1}^{n-1} \frac{\sum_{i=1}^k x_i}{\sum_{i=1}^n x_i} \varepsilon_k}_{\text{errore dell'algoritmo}}
$$

Dove:

- $x_i$ = i-esimo numero da sommare
- $\varepsilon_i$ = errore relativo sugli input
- $\varepsilon_k$ = errore introdotto dalla k-esima operazione di somma

## Consigli pratici nella somma di numeri floating point

Quando si sommano numeri di magnitudine diversa, l’ordine di somma influisce sull’errore relativo:

- Conviene sommare **prima i numeri più piccoli**, così da ridurre l’errore di incolonnamento.
- In generale, sommare numeri con **esponenti simili** minimizza la perdita di informazioni.
- Una volta sommati i piccoli numeri, il risultato parzialmente sommato (più grande) può essere sommato ai numeri più grandi successivi, riducendo l’accumulo di errore.

La **propagazione dell’errore dipende sia dal condizionamento del problema sia dall’algoritmo scelto**, confermando l’importanza di considerare entrambe le caratteristiche per ottenere risultati affidabili (Vedi esempio slide 81-86).

## Stabilità e condizionamento

In Calcolo Numerico è fondamentale distinguere **stabilità e condizionamento**, perché indicano due cose diverse: come reagisce l’algoritmo agli errori e quanto è sensibile il problema stesso agli errori nei dati.

**Stabilità** riguarda l’algoritmo. Un algoritmo è stabile se gli errori introdotti durante i calcoli (ad esempio arrotondamenti e troncamenti) non si amplificano in modo eccessivo lungo la sequenza di operazioni. In altre parole, una piccola perturbazione in corso d’opera non provoca un grande scostamento nel risultato finale.

**Condizionamento**, invece, è una proprietà intrinseca del problema matematico. Un problema si dice ben condizionato se piccole perturbazioni dei dati portano a piccole variazioni nella soluzione. Viceversa, un problema è mal condizionato se anche piccole perturbazioni nei dati possono generare grandi variazioni nella soluzione.

- Il condizionamento **non dipende dall’algoritmo**: è una caratteristica della funzione che lega i dati alla soluzione del problema.
- È fortemente legato ai dati specifici del problema.

**Esempio pratico** (slide 79): Supponiamo di risolvere un problema con dati che contengono un errore relativo dell’ordine di $10^{-6}$. Se la soluzione ottenuta presenta un errore relativo dell’ordine di $10^{-3}$, il problema è **mal condizionato**, perché l’errore sulla soluzione è mille volte maggiore dell’errore sui dati.

## Come affrontare un problema numerico

1. Prima di tutto, occorre verificare che la soluzione esista e sia unica.
2. Successivamente, si valuta il condizionamento: se il problema è mal condizionato, anche algoritmi stabili produrranno inevitabilmente risultati con un certo grado di imprecisione, perché la sensibilità del problema amplifica gli errori sui dati.

