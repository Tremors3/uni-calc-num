# Interpolazione

## Motivazione e applicazioni

L’interpolazione nasce dall’esigenza di **ricostruire informazioni intermedie a partire da dati noti**. In molti contesti applicativi non interessa conoscere solamente alcuni valori iniziali e finali, ma anche descrivere ciò che avviene tra questi dati.

Un esempio è il **movimento di un braccio robotico**. Date una configurazione iniziale e una finale, si vogliono determinare le configurazioni intermedie che descrivono il movimento nel tempo. L’interpolazione permette quindi di costruire una traiettoria continua nello spazio delle configurazioni, ottenendo ad esempio un’animazione fluida attraverso la generazione dei frame intermedi.

Un altro esempio riguarda l’**elaborazione delle immagini**. Supponiamo di avere un’immagine rappresentata da una matrice di pixel di dimensione $n\times n$ e di volerla ingrandire ottenendo una nuova matrice di dimensione $m\times m$, con $m=2n$. I nuovi pixel introdotti non hanno inizialmente un valore assegnato. L’interpolazione permette di stimare tali valori utilizzando le informazioni disponibili nei pixel vicini.

In generale, l’interpolazione consente quindi di **passare da dati discreti a una rappresentazione più densa o continua**. È utilizzata, ad esempio, nell’animazione, nelle simulazioni fisiche e nell’elaborazione delle immagini.

## Problema dell’interpolazione

Il problema dell’interpolazione consiste nel **costruire una funzione che passi esattamente per un insieme finito di punti dati**.

I dati sono costituiti da $n+1$ coppie

$$
(x_i,y_i),
\qquad i=0,\ldots,n,
$$

dove gli $x_i$ rappresentano le ascisse, tipicamente distinte tra loro, mentre gli $y_i$ sono le corrispondenti ordinate.

L’obiettivo è costruire una funzione $g(x)$ che soddisfi

$$
\boxed{
g(x_i)=y_i,
\qquad i=0,\ldots,n
}
$$

cioè una funzione che passi esattamente per tutti i punti dati.

Una volta costruita $g(x)$, è possibile utilizzarla per stimare il valore della funzione in punti non presenti tra i dati. Dato un punto $\tilde{x}$, si calcola infatti

$$
\tilde{y}=g(\tilde{x}).
$$

In questo modo il valore $\tilde{y}$ viene stimato a partire dalle informazioni contenute nei punti noti.

---