# ======================================================
# STAMPA DI OGNI LETTERA DEL NOME
# ======================================================
nome = "Gianmario"

for x in nome:
    print(x)
    print("*")


# ======================================================
# STAMPA DI OGNI NUMERO E UN ASTERISCO
# ======================================================
numeri = [1,2,3,4,5,1,2,3,4,5,99]

for x in numeri:
    print(x)
    print("*")

# Controllo se 99 è presente
if 99 in numeri:
    print("Caio e Sempronio")


# ======================================================
# CICLO WHILE A CONDIZIONE BOOLEAN
# ======================================================
# Usi while quando NON sai quante volte ripetere
controllo = True
i = 1

while controllo:
    print(i)
    i = i + 1
    scelta = input("Vuoi continuare: ")

    if scelta.lower() == "no":
        controllo = False


# ======================================================
# VALIDAZIONE DI UN INPUT CON WHILE
# ======================================================
numero = float(input())
while numero < 1 or numero > 11:
    numero = float(input("Il numero deve essere compreso tra 1 e 10"))


# ======================================================
# ESEMPI DI RANGE
# ======================================================
for i in range(5):
    print(i)

# Da 2 a 9
for i in range(2, 10):
    print(i)

# Da 2 a 9 con step di 2
for i in range(2, 10, 2):
    print(i)


# ======================================================
# CONTO ALLA ROVESCIA FINO A ZERO
# ======================================================
numero = int(input("Scegli un numero: "))

while numero >= 0:
    print(numero)
    numero = numero - 1


# ======================================================
# VERIFICA DI NUMERO PRIMO (VERSIONE DECENTE)
# ======================================================
numero = int(input("Scegli un numero: "))

if numero % 2 == 0:
    if numero == 2:
        print("Il numero è primo")
    else:
        print("Pari")
else:
    primo = True
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            print("Il numero non è primo")
            primo = False
            break

    if primo:
        print("Il numero è primo")


# ======================================================
# PARI O DISPARI
# ======================================================
numero = int(input("Scegli un numero: "))

if numero % 2 == 0:
    print("Pari")
else:
    print("Dispari")


# ======================================================
# CONTO ALLA ROVESCIA CON CICLO MISTO WHILE-FOR
# ======================================================
condizione = True

while condizione:
    numero = int(input("Scegli un intero positivo: "))
    for i in range(numero, -1, -1):
        print(i)

    scelta = input("Vuoi continuare: ")
    if scelta.lower() == "no":
        condizione = False


# ======================================================
# INSERIMENTO DI N NUMERI E CREAZIONE DEL VETTORE DEI QUADRATI
# ======================================================
lunghezza = int(input("Quanti numeri vuoi inserire: "))
vettore = []

for i in range(lunghezza):
    elemento_i = int(input("Inserisci il numero: "))
    vettore.append(elemento_i ** 2)

print(vettore)


# ======================================================
# TROVARE IL MASSIMO IN UNA LISTA
# ======================================================
lunghezza = int(input("Quanti numeri vuoi inserire: "))
vettore = []

for i in range(lunghezza):
    vettore.append(int(input("Inserisci il numero: ")))

if len(vettore) == 0:
    print("La lista è vuota")
else:
    massimo = vettore[0]
    for i in range(len(vettore)):
        if vettore[i] > massimo:
            massimo = vettore[i]

    print(massimo)


# ======================================================
# CONTARE GLI ELEMENTI DI UNA LISTA CON WHILE
# ======================================================
i = 0
contatore = 0

while i < len(vettore):
    contatore += 1
    i += 1






