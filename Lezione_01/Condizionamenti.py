# Definisco una variabile intera
numero = 10

# type() mostra il tipo di variabile
print(type(numero))


#######################################
# CONDIZIONE IF / ELSE DI BASE
#######################################

if numero > 10:
    print("Ciao, piacere di conoscerti")
else:
    print("Ciao, già ci conosciamo")

# Nota:
# Un blocco di codice in Python è determinato dall'indentazione.


#######################################
# IF ANNIDATI (NESTED IF)
#######################################

if numero > 0:
    if numero > 7:
        print("il numero (numero) è maggiore di 7")

# Nota:
# L'else NON accetta condizioni.
# Per aggiungere condizioni intermedie si usa elif.


#######################################
# IF / ELIF / ELSE
#######################################

if numero > 20:
    print("Ciao")
elif numero > 0:
    print("Ciao, piacere")
else:
    print("Già ci conosciamo")


#######################################
# ESERCIZIO 1
#######################################

input_numero = input("Che numero scegli? ")

# input() restituisce sempre una stringa
print(type(input_numero))

# Convertiamo la stringa in un intero
input_numero = int(input_numero)

# IF annidati multipli
if input_numero > 10:
    if input_numero > 20:
        if input_numero > 30:
            print("Il tuo numero è maggiore di 30")


#######################################
# ESERCIZIO 2
#######################################

scelta_pagina = int(input("Che numero di pagina vuoi leggere? "))

if scelta_pagina == 1:
    print("Hai scelto la pagina 1")

elif scelta_pagina == 2:
    print("Hai scelto la pagina 2")

else:
    print("Hai saltato le prime due pagine")


#######################################
# ESERCIZIO 1 – VERSIONE MIGLIORATA
#######################################

print("###########################   ESERCIZIO 1   ##################################")
print("Benvenuto al test a 3 livelli")

livello1 = input("Scrivi 'via' per partire: ")

if livello1 == "via":
    print("Sei entrato nel primo livello")

    livello2 = input("Scrivi 'andiamo' per passare al secondo livello: ")

    if livello2 == "andiamo":
        print("Sei entrato al secondo livello")

        livello3 = input("Scrivi 'fine' per entrare al livello 3 e vincere: ")

        if livello3 == "fine":
            print("Sei entrato in tutti e 3 i livelli, hai vinto!!")
        else:
            print("Errore al terzo livello")

    else:
        print("Errore al secondo livello")

else:
    print("Errore al primo livello")


#######################################
# ESERCIZIO 2 – VERSIONE MIGLIORATA
#######################################

print("###########################   ESERCIZIO 2   ##################################")

print("A che gioco vuoi giocare oggi:")
print("1 - Scacchi")
print("2 - Poker")
print("3 - Calcio")

scelta_gioco = int(input("Scegli il numero: "))

if scelta_gioco == 1:
    print("Hai deciso di giocare a scacchi!")
elif scelta_gioco == 2:
    print("Hai deciso di giocare a poker!")
elif scelta_gioco == 3:
    print("Hai deciso di giocare a calcio!")
else:
    print("Non vuoi giocare a nulla!")


#######################################
# COMANDO match-case (introduzione)
#######################################

comando = input("Cosa vuoi fare? ")

# match-case funziona come uno "switch" evoluto
match comando:
    case "start":
        print("Iniziamo!")
    case "stop":
        print("Fermiamoci!")
    case "pause":
        print("Prendiamoci una pausa!")
    case _:
        print("Non ho capito cosa vuoi fare!")
