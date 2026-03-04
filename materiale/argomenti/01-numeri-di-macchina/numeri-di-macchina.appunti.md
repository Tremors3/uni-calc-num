# (1) Lezione 23-02-2026 | s 1..28 | Intro al corso

- Introduzione al corso.

# (2) Lezione 24-02-2026 | s 29..49 | Rappresentazione numeri reali virgola fissa.

- Lezione saltata causa esame.

# (3) Lezione 25-02-2026 | s 49..68 | Rappresentazione numeri floating point virgola mobile.

$$ F(2,3, -2,1) = \{ \pm 1.a_2a_3 \cdot 2^r, a_2,a_3 \in \{0,1\}, r \in {-2,-1,0,1} \} $$

## Rappresentazione IEEE 754 $\mid$ Numeri Reali

**Slide 47**. Per rappresentare lo zero il formato IEEE 754 prevede un'altra configurazione specifica. Formato dei numeri generici per mantissa (lunga t) e esponente (r):

$$ \pm (1.a_2\dots a_t)_\beta \cdot \beta^r $$

Sulle slide abbiamo visto la suddivisione dei bit per il formato IEEE 754, in forma 32 bit e 64 bit.

**Slide 49**. I formati standard fissano anche il numero di bit totali che ogni singolo numero reale occupa in un calcolatore. Precisione singola 32 bit, e doppia a 64 bit. Questa rappresentazione coincide con quella scientifica per i numeri reali.

In riferimento alla precisione semplice, anche se la mantissa occupa 23 bit, in realtà la precisione è a 24 bit. Il motivo è semplice, il primo bit si sà essere sempre uno $\Rightarrow$ lo si omette.

Perchè all'esponente viene **aggiunto un bias**? Sappiamo che gli esponenti possono essere positivi o negativi. Per rappresentare il segno si somma all'esponente un bias (127 per precisione singola). La alu lo interpreterà correttamente.

Visto esempio traduzione numero reale decimale in IEEE 754 (32 bit).
>
Il calcolatore tronca i bit che superano il numero di bit rappresentati dal formato scelto. Se ho un numero decimale la cui mantissa si rappresenta con 30 bit, i 7 bit meno significativi vengono troncati e persi. **Si verifica una potenziale perdita di informazione**. Solitamente si applica il troncamento dei bit che superano il limite rappresentabile. Ma teoricamente si potrebbero anche approssimare.

### Errori di Approssimazione

- **Errore assoluto**: distanza effettiva tra i due numeri in valore assoluto. Quanto il valore reale dista da quello con errore.

    $$ E_a = |\alpha - \alpha^*| $$

- **Errore relativo**: errore assoluto normalizzato per il numero reale stesso. In questo modo si riesce a capire se l'errore è **grande o piccolo a seconda del valore reale originale**.

    $$ E_r = \frac{E_a}{|\alpha|} $$

    Non possiamo confrontare gli $E_a$ di valori reali differenti. Se vogliamo confrontare gli errori dobbiamo naturalmente usare $E_r$.

    L'errore relativo ci indica anche a **quale cifra decimale** del numero reale occorre l'errore (perdita di informazione). Ci dice qual'è la cifra che "salta".

    Esempio: Dobbiamo calcolare l'errore assoluto $E_a$ e relativo $E_r$ tra il numero reale $\alpha$ e il numero in EEE 754 (32bit) $fl(\alpha)$.

    $$ \alpha = 1.00\textcolor{red}{1} \cdot 2^1 = (2.25)_{10} $$
    
    diventa:

    $$ fl(\alpha) = 1.00 \cdot 2^1 = (2)_{10} $$

    Calcoliamo l'errore relativo:

    $$ \frac{|fl(\alpha) - \alpha|}{|\alpha|} = \frac{0.25}{2.25}$$

- **Teorema dell'errore di rappresentazione  dei numeri reali**:

    $$ \frac{|fl(\alpha) - \alpha|}{|\alpha|} \le \beta^{1-t} $$

    Dove: $fl(\alpha)$: numero reale in formato IEEE 754. Alternativamente:

    $$ fl(\alpha) = a(1 + \epsilon), \hspace{20px} |\epsilon| \le u =  \beta^{1-t} $$

    Dove $u$ è detta precisione di macchina. $\beta$ è la base scelta. $t$ è il numero di cifre disponibili (23 per IEEE 754 32 bit). Definizione:

    >La precisione di macchina rappresenta il **massimo errore relativo** che noi commettiamo quando lavoriamo in un certo formato.
    >- In altre parole: la *distanza massima* tra "due crocette" (slide 51).
    >- Sappiamo che non può essere più grande della precisione di macchina.

- **Informazioni sulla rappresentazione dei float in python**:

    ```py
    import sys
    sys.float_info
    ```

    Mostra alcune informazioni riguardo ai numeri floating point 64 bit in python. Come per esempio la precisione di macchina $\epsilon$, il numero massimo e minimo rappresentabili, come dell'esponente.

## Operazioni con i numeri floating point

### Operazioni con i numeri floating point

- **Esempio somma numeri fp con esponenti differenti** (Slide 64). Il calcolatore per operare su due numeri floating point deve riallineare gli esponenti. Sceglie sempre di portere il numero che ha l'esponente più piccolo verso quello più grande ma così facendo shifta la mantissa del numero più piccolo verso destra e c'è il rischio che venga troncata.

    Si sceglie di portere l'esponente ppiù piccolo al più grande perchè se facessimo il contrario andremmo a troncare il numero che è più grande tra i due, perdendo maggiore informazione.

- **Errore di Incolonnamento** (Controllo avvenuto troncamento): Se sommiamo (o sottraiamo) un numero grande con un numero piccolo rischiamo troncamento.

    $$ x + y = x \text{ anche se } y \ne 0 $$

    Formula errore di incolonnamento:

    $$ |y| = \frac{u}{\beta}|x| $$

    In particolare se il **numero più piccolo è minore rispetto alla precisione di macchina**, è come se il primo numero rimane **invariato**.

    Il **bias** viene aggiunto all'esponente in IEEE 754 perchè permette di **confrontare più facilmente i due esponenti** nel caso di una operazione di macchina che richiede riallineamento.

# (4) Lezione 02-03-2026 | s 61..86 | Precisione di Macchina, Proprietà operazioni Floating Point

- **Non validità della proprietà associativa (somma)**: (Slide 67) Vogliamo trovare la somma dei tre numer $x$, $y$ e $z$. L'unica cosa che possiamo cambiare è l'ordine. Il troncamento avviene prima dell'effettuazione dell'operazione; durante il riallineamento dell'esponente più piccolo.

    $$ fl(x + fl(y + z)) \ne fl(fl(x + y) + z) $$

    Algoritmi che sulla carta dovrebbero restituire lo stesso risultato, in realtà hanno risultati diversi (esempio slides).

- **Non validità della proprietà distributiva (prodotto)**: (Slide 69)

    $$ fl(x \cdot fl(y + z)) \ne fl(fl(x \cdot y) + fl(x \cdot z)) $$

- **Legge di annullamento del prodotto**: Dobbiamo calcolare $x \cdot y$, il problema è che entrambi i numeri sono piccolissimi e si trovano tra 0 e 1 ma ancora rappresentabili. Il risultato ottenuto dalla loro moltiplicazione restituirà un numero così piccolo che non è più rappresentabile (underflow).

    $$ fl(xy) = 0 \text{ anche se } x,y \ne 0 $$

### Relazione tra: Errore Relativo e Precisione di Macchina

(Slide 61). L'errore relativo di una operazione (come lo abbiamo definito) non può essere più grande della precisione di macchina. Questo vale per un qualsiasi numero reale, ed in particolare per i numeri ottenuti come risultato delle operazioni di macchina.

$$ \frac{|fl(x \bullet y ) - (x \bullet y)|}{|x \bullet y|} \le k\beta^{1-t} $$

- Dove k = 1/2 oppure k = 1 a seconda che la rappresentazione sia ottenuta per arrotondamento o per troncamento rispettivamente.
- `k = 1/2`: In caso di **Arrotondamento**, la precisione di macchina viene dimezzata (consideriamo un bit in più a destra). Quindi, con il formato IEEE 754 a precisione singola, l'approssimazione viene effettuata sul 24° bit.
- La prof ha cancellato questa parte a slide 61. Forse è sbagliata. Contrlla.

### Correttezza (Accuratezza) del Risultato

Criteri di confronto tra algoritmi. Generalmente si guarda a quanto un algoritmo esegue velocemente. Ma in campi come Il Calcolo Numerico è importante considerare anche la correttezza del risultato.

- Gli algoritmi verranno valutati non solo in termini di **Efficienza**, ma anche di **Stabilità** (sinonimo di Accuratezza/Correttezza/Consistenza).

## Analisi degli Errori (slide 73)

### Peso e Propagazione degli Errori (slide 75)

Ci interessa ricordare $fl(s) = s(1+\epsilon), \text{ con } |\epsilon| \le u$. Ogni volta che operiamo un troncamento di una manisssa $s$ otteniamo un numero Floating Point `fl(s)` nella forma espressa sopra.

Vorremmo calcolare: $\alpha = x + y + z$. L'idea è quello di confrontare l'$\alpha$ esatto con quello calcolato dal calcolatore.

- **PRIMO ALGORITMO**: (x + y) + z

    Consideriamo sia l'**errore sugli input**, sia l'**errore sull'operazione**.

    $$\begin{array}{l}
        \alpha = x + y + z \\
        \alpha^* = fl(fl(fl(x) + fl(y)) + fl(z)) \\
    \end{array}$$

    L'analisi dell'errore consiste nel confrontare il valore reale $\alpha$ e il valore con errore ottenuto dal calcolatore $\alpha^*$.

    Abbiamo quindi:

    - $fl(x) = x(1 + \epsilon_x), \text{ con } |\epsilon_x| \le u$
    - $fl(y) = y(1 + \epsilon_y), \text{ con } |\epsilon_y| \le u$
    - $fl(z) = z(1 + \epsilon_z), \text{ con } |\epsilon_z| \le u$

    Procedimento:

    1. $fl(fl(x) + fl(y)) = (fl(x) + fl(y))(1 + \epsilon_1), \text{ con } |\epsilon_1| \le u$
    - $= \left( x(1+\epsilon_x) + y(1+\epsilon_y) \right)(1 + \epsilon_1)$
    - $= x + x\epsilon_x + y + y\epsilon_y + x\epsilon_1 + x\textcolor{lightgreen}{\epsilon_x\epsilon_1} + y\epsilon_1 + y\textcolor{lightgreen}{\epsilon_y\epsilon_1}$
    - $\simeq x + y + x\epsilon_x + y\epsilon_y + (x + y)\textcolor{lightgreen}{\epsilon_1}$
    2. $fl(fl(fl(x) + fl(y)) + fl(z)) = (fl(fl(x) + fl(y)) + fl(z))(1 + \epsilon_2), \text{ con } |\epsilon_2| \le u$
    - $\simeq \left(x + y + x\epsilon_x + y\epsilon_y + (x + y)\epsilon_1 + z(1+\epsilon_z)\right)(1 + \epsilon_2)$
    - $\dots$

    Dove $\epsilon_1$ è l'errore dovuto alla prima operazione effettuata. L'approssimazione in verde è di solito applicata in modo da facilitare il raccoglimento per $\epsilon_1$. Stessa cosa avverrà per la stessa procedura sulla seconda somma.

    A slide 76 vediamo l'errore che è dato da una somma pesata dei singoli pesi. Se io moltiplico i singoli pesi per qualcosa di molto grande, l'errore potrebbe diventare grande anche lui. Quindi dipende da quali sono i dati. Si tratta di una somma pesata. Il peso di ogni singolo errore è piccolo, ma è direttamente proporzionale all'input. Se l'input è grande anche l'errore sarà grande. L'errore si propaga e viene ricombinato da tutte le operazioni che vengono dopo (Propagazione dell'errore).

    $$ E_r = E_{in} + E_{alg} $$

    Abbiamo che l'$\alpha$ con errore è:

    $$ \alpha^* \simeq x + y + z + x\epsilon_x + y\epsilon_y + z\epsilon_z + (x + y)\epsilon_1 + (x + y + z)\epsilon_2 $$

    normalizzando l'errore per $x + y + z$ otteniamo che l'errore relativo:

    $$ E_r \simeq \textcolor{lightblue}{\frac{x}{x + y + z}\epsilon_x + \frac{y}{x + y + z}\epsilon_y + \frac{z}{x + y + z}\epsilon_z} + \textcolor{yellow}{\frac{x + y}{x + y + z}\epsilon_1 + \epsilon_2} $$

    In blue abbiamo l'errore dovuto alla rappresentazione dei dati. Mentre in giallo l'errore dovuto alle operazioni, e quindi all'algoritmo utilizzato.

    > NOTA: In una macchina che elabora in aritmetica infinita (perfetta) propagherà l'errore dovuto a come sono rappresentati i dati!

### Stabilità e Condizionamento (slide 78)

- **Stabilità**: modo in cui l'algoritmo reagisce agli errori sulle operazioni.

- **Condizionamento**: legato al fatto che vorremmo risolvere problemi matematici, ma lostrumento che abbiamo a disposizione ci fa perdere l'esattezza dei dati. 

    > **Definizione di condizionamento**: Un problema si dice ben condizionato se a piccole perturbazioni dei dati corrispondono altrettanto piccole variazioni delle soluzioni. Viceversa, un problema si dice mal condizionato se a piccole perturbazioni dei dati corripondono (relativamente) grandi variazioni delle soluzioni.
    > - Il condizionamento è una proprietà della funzione che lega i dati alla
    soluzione di un problema, non dipende da come queste vengano calcolate.
    > - Il condizionamento è una caratteristica del problema che dipende fortemente dai dati.

    **Esempio** (slide 79): Si mostra come l'errore sul dato differisce dall'errore sulla soluzione.
    - Si tratta di un problema **mal condizionato**: partendo da dati con un errore relativo nell'ordine del $10^-6$ ed arrivando a soluzioni con errore relativo nell'ordine del $10^-3$, cioè mille volte maggiore.

    Dato un problema, come lo **approcciamo**?
    1. Prima di tutto bisogna accertarsi che la soluzione che vogliamo calcolare esista. Ci interessa anche capire se la soluzione che cerchiamo è unica.
    2. Poi ci chiederemo se il problema è mal condizionato oppure no. Spesso la risposta dipende dai dati. Il condizionamento è una caratteristica del problema ma che dipende dai dati.

    **Considerazione**: Dobbiamo sommare dei numeri: alcuni sono grandi, mentre altri sono piccoli. Conviene sommare prima i numeri più piccoli, in questo modo evitiamo per quanto possibile l'errore di incolonnamento. Sommando numeri fp i quali esponenti sono vicini riduce l'errore di incolonnamento e otteniamo un numero più grande che potrà essere sommato con gli altri numeri... 

---
