################################# Esempi base di funzioni ##########################################

# Definisce una funzione che prende un nome e stampa un saluto personalizzato
def saluta(nome):
    print(f"Ciao {nome}")

# Chiamata della funzione "saluta"
saluta("Gianmario")


# Funzione che calcola e restituisce il quadrato di un numero
def quadrato(numero):
    return numero * numero

# Stampa il risultato della funzione quadrato applicata a 10
print(quadrato(10))



################################## Indovina il numero #######################################
import random

# Funzione che implementa il gioco "Indovina il numero"
def indovina():

    # Genera un numero casuale tra 1 e 100 che il giocatore dovrà indovinare
    target = random.randint(1, 100)

    # Ciclo infinito che continua finché l'utente non indovina o decide di fermarsi
    while True:

        # Chiede all'utente di inserire un tentativo
        # Siccome la funzione non riceve parametri, il guess deve essere chiesto qui
        guess = int(input("Tentativo: "))

        # Verifica se il tentativo è corretto
        if guess == target:
            print("Hai vinto!")
            break   # Esce dal ciclo e la funzione termina

        else:
            # Indica se il tentativo è troppo alto o troppo basso
            if guess > target:
                print("Sei troppo alto")
            else:
                print("Sei troppo basso")

            # Chiede se l'utente vuole continuare
            print("Vuoi continuare a giocare: ")
            scelta = input(" ")

            if scelta.lower() == "no":
                # L'utente decide di fermarsi → esce dal ciclo
                break
                

# Stampa un messaggio iniziale
print("Indovina il numero da 1 a 100")

# Avvio del gioco: la funzione non riceve parametri
# perché richiede i tentativi direttamente al suo interno
indovina()




####################################### Fibonacci ###########################################

# Funzione che costruisce la sequenza di Fibonacci da 0 fino a n
def fibonacci(n):

    # Crea una lista lunga n+1, inizialmente piena di zeri
    sequenza = [0] * (n + 1)

    # Riempie la lista con i valori corretti della sequenza
    for i in range(n + 1):

        if i == 0:
            # F(0) = 0
            sequenza[i] = 0

        elif i == 1:
            # F(1) = 1
            sequenza[i] = 1

        else:
            # Formula ricorsiva di Fibonacci: F(n) = F(n-1) + F(n-2)
            sequenza[i] = sequenza[i - 1] + sequenza[i - 2]
    
    return sequenza   # Restituisce la lista completa


# Lista che conterrà tutte le sequenze calcolate
record_fibonacci = []

while True:

    # Chiede all'utente quale n vuole calcolare
    n = int(input("Inserire il numero di cui si vuole calcolare la sequenza di Fibonacci: "))

    # Calcola la sequenza da 0 a n
    risultato_fibonacci = fibonacci(n)

    # Salva sia n che la sequenza generata
    record_fibonacci.append([n, risultato_fibonacci])

    # Stampa a schermo la sequenza
    print(risultato_fibonacci)


    # Chiede se si vuole calcolare un'altra sequenza
    print("Vuoi calcolare un' altra sequenza: ")
    scelta = input(" ")

    if scelta.lower() == "no":
        break   # Esci dal ciclo principale

# Stampa tutte le sequenze calcolate durante l'esecuzione
print(record_fibonacci)
