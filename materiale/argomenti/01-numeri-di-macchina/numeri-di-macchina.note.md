# Numeri di Macchina

## Introduzione

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

## Rappresentazione dei numeri

### Numero decimale $\Rightarrow$ Rappresentazione S.E.M.

1. **Numero dato**: $-123,987$
2. **Scomposizione in potenze di 10**:
    $$-\;(1\cdot 10^2 + 2\cdot 10^1 + 3\cdot 10^0 + 9\cdot 10^{-1} + 8\cdot 10^{-2} + 7\cdot 10^{-3})$$
3. **Per ottenere la forma S.E.M.** (Segno, Esponente, Mantissa) si scrive il numero come:
    $$\pm m \cdot 10^e$$
    con mantissa normalizzata. Nel nostro caso, con mantissa compresa tra 0 e 1:
    $$ -0,123987 \cdot 10^3 $$
4. **Otteniamo qundi**:
    $$ -123,987 = (-1) \cdot 0,123987 \cdot 10^3 $$
    Dove:
    - **Segno** = Negativo
    - **Esponente** = $3$
    - **Mantissa** = $0,123987$

---
