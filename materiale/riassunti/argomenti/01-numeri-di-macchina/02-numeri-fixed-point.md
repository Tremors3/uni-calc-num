## Rappresentazione Fixed Point dei Numeri Macchina

### ▸ Definizione

La **rappresentazione fixed point** (a punto fisso) rappresenta gli interi utilizzando un numero **fisso di bit**.

Il formato è caratterizzato dal parametro **(t)**: vengono riservati **(t+1) bit** di memoria; i formati più comuni sono:

  * (t+1 = 16) bit;
  * (t+1 = 32) bit.

---

### ▸ Rappresentazione di un numero positivo

Se $N \ge 0$ si memorizzano le **(t+1) cifre meno significative** della rappresentazione binaria di (N), aggiungendo eventuali zeri a sinistra.

**Procedura**

1. Convertire (N) in binario.
2. Aggiungere eventuali zeri iniziali fino ad avere almeno (t+1) bit.
3. Conservare solamente gli ultimi (t+1) bit.

---

### ▸ Rappresentazione di un numero negativo

Se $N < 0$ si rappresenta il numero mediante il **complemento a 2** su (t+1) bit.

**Procedura**

1. Scrivere il valore assoluto (|N|) in binario.
2. Considerare le ultime (t+1) cifre (aggiungendo zeri iniziali se necessario).
3. Calcolare il **complemento a 2**:

   * invertire tutti i bit;
   * sommare (1).

---

### ▸ Regola generale

* Se il numero è **positivo**, si memorizzano le ultime (t+1) cifre della sua rappresentazione binaria.

* Se il numero è **negativo**, si memorizzano le ultime (t+1) cifre del suo **complemento a 2**.

---

### ▸ Alcuni Esempi

> ◇ **Esempio** Rappresentazione di numero (base dieci) in Fixed Point.
> 
> $1235_{10}=10011010011_2$
> 
> $-1235_{10}=-(10011010011)_2$
> 
> La rappresentazione effettiva dipende dal numero di bit disponibili (t+1).

> ◇ **Esempio**. Con (t+1=4).
> 
> In questo caso sono disponibili **4 bit**, quindi:
> 
> | Rappresentazione | Numero |
> | :--------------: | :----: |
> |       1111       |   −1   |
> |       1110       |   −2   |
> |       1101       |   −3   |
> |       1100       |   −4   |
> |       1011       |   −5   |
> |       1010       |   −6   |
> |       1001       |   −7   |
> |       1000       |   −8   |
> |       0111       |    7   |
> |       0110       |    6   |
> |       0101       |    5   |
> |       0100       |    4   |
> |       0011       |    3   |
> |       0010       |    2   |
> |       0001       |    1   |
> |       0000       |    0   |
> 
> Da questa tabella si osserva che l'intervallo dei numeri rappresentabili **non è simmetrico** rispetto allo zero.

---

### ▸ Intervallo di esatta rappresentazione

Con (t+1) bit è possibile rappresentare esattamente gli interi appartenenti all'intervallo

$$
[-2^t,;2^t-1]
$$

---

### ▸ Overflow e Underflow

#### ⚠️ Overflow intero

Si verifica quando $N > 2^t-1$ cioè il numero è **troppo grande** per essere rappresentato.

#### ⚠️ Underflow intero

Si verifica quando $N < -2^t$ cioè il numero è **troppo piccolo** (troppo negativo) per essere rappresentato.

---

### ▸ Conseguenze di Overflow e Underflow

Quando un numero esce dall'intervallo

$$
[-2^t,;2^t-1]
$$

la sua rappresentazione **perde informazione**.

Di conseguenza:

* il numero viene **memorizzato in modo errato**;
* anche il **risultato** delle operazioni aritmetiche che lo coinvolgono **risulta errato**.
