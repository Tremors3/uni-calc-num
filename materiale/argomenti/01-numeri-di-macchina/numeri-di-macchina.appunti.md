## (1) Lezione 23-02-2026 | s 1..28 | Intro al corso

- Introduzione al corso.

## (2) Lezione 24-02-2026 | s 29..49 | Rappresentazione numeri reali virgola fissa.

- Lezione saltata causa esame.

## (3) Lezione 25-02-2026 | s 49..68 | Rappresentazione numeri floating point virgola mobile.

$$ F(2,3, -2,1) = \{ \pm 1.a_2a_3 \cdot 2^r, a_2,a_3 \in \{0,1\}, r \in {-2,-1,0,1} \} $$

### Rappresentazione IEEE 754 $\mid$ Numeri Reali

**Slide 47**. Per rappresentare lo zero il formato IEEE 754 prevede un'altra configurazione specifica. Formato dei numeri generici per mantissa (lunga t) e esponente (r):

$$ \pm (1.a_2\dots a_t)_\beta \cdot \beta^r $$

Sulle slide abbiamo visto la suddivisione dei bit per il formato IEEE 754, in forma 32 bit e 64 bit.

**Slide 49**. I formati standard fissano anche il numero di bit totali che ogni singolo numero reale occupa in un calcolatore. Precisione singola 32 bit, e doppia a 64 bit. Questa rappresentazione coincide con quella scientifica per i numeri reali.

In riferimento alla precisione semplice, anche se la mantissa occupa 23 bit, in realtà la precisione è a 24 bit. Il motivo è semplice, il primo bit si sà essere sempre uno $\Rightarrow$ lo si omette.

Perchè all'esponente viene **aggiunto un bias**? Sappiamo che gli esponenti possono essere positivi o negativi. Per rappresentare il segno si somma all'esponente un bias (127 per precisione singola). La alu lo interpreterà correttamente.

Visto esempio traduzione numero reale decimale in IEEE 754 (32 bit).

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

- **Esempio somma numeri fp con esponenti differenti** (Slide 64). Il calcolatore per operare su due numeri floating point deve riallineare gli esponenti. Sceglie sempre di portere il numero che ha l'esponente più piccolo verso quello più grande ma così facendo shifta la mantissa del numero più piccolo verso destra e c'è il rischio che venga troncata.

    Si sceglie di portere l'esponente ppiù piccolo al più grande perchè se facessimo il contrario andremmo a troncare il numero che è più grande tra i due, perdendo maggiore informazione.

- **Errore di Incolonnamento** (Controllo avvenuto troncamento): Se sommiamo (o sottraiamo) un numero grande con un numero piccolo rischiamo troncamento.

    $$ x + y = x \text{ anche se } y \ne 0 $$

    Formula errore di incolonnamento:

    $$ |y| = \frac{u}{\beta}|x| $$

    In particolare se il **numero più piccolo è minore rispetto alla precisione di macchina**, è come se il primo numero rimane **invariato**.

    Il **bias** viene aggiunto all'esponente in IEEE 754 perchè permette di **confrontare più facilmente i due esponenti** nel caso di una operazione di macchina che richiede riallineamento.

- **Non validità della proprietà associativa**: ...
