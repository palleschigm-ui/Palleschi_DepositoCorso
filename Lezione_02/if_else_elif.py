################# ESERCIZIO 1 ########################

# Chiedo all’utente la sua età e la converto in intero
età = int(input("Età: "))

# Se è minore di 18 anni non può vedere il film
if età < 18:
    print("Non puoi vedere questo film")
else:
    # Altrimenti ha abbastanza anni per vederlo
    print("Puoi vedere questo film")


################## ESERCIZIO 2 ########################

# Creo una lista vuota in cui inserirò i numeri forniti dall’utente
vettore = []

# Chiedo quattro numeri all’utente, li converto in float
# e li aggiungo al vettore
a = float(input("Primo numero: "))
vettore.append(a)

b = float(input("Secondo numero: "))
vettore.append(b)

c = float(input("Terzo numero: "))
vettore.append(c)

d = float(input("Quarto numero: "))
vettore.append(d)

# Stampo il menu delle operazioni possibili
print("Che operazione vuoi fare?")
print("+ Addizione")
print("- Sottrazione")
print("* Moltiplicazione")
print("/ Divisione")

# L’utente sceglie l’operazione
operazione = input("Operazione: ")

# Controllo quale operazione è stata scelta e la eseguo

# Operazione di addizione
if operazione == "+":
    print(a + b + c + d)

# Operazione di sottrazione
elif operazione == "-":
    print(a - b - c - d)

# Operazione di moltiplicazione
elif operazione == "*":
    print(a * b * c * d)

# Operazione di divisione
elif operazione == "/":
    # Prima controllo che i divisori non siano zero
    if b != 0 and c != 0 and d != 0:
        print(a / b / c / d)
    else:
        print("Non puoi dividere per zero")

# Caso in cui l’utente scrive un’operazione non valida
else:
    print("Non ho capito che operazione vuoi fare")
