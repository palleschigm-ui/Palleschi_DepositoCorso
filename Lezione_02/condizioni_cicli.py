############### Esercizio 1 ###########################

flag=True

while(flag):
    print("Vuoi inserire un numero o una stringa? ")
    print("1- Numero")
    print("2- Stringa")

    # L’utente sceglie se inserire un numero o una stringa
    scelta = int(input(" "))

    # Caso in cui l’utente inserisce un numero
    if scelta == 1:
        a = int(input("Scegli il numero "))

    # Caso in cui l’utente inserisce una stringa
    else: 
        stringa = input("Scrivi la stringa: ")
        # La variabile a diventa la lunghezza della stringa
        a = len(stringa)
        print(f"La stringa ha lunghezza {a}")

    # Verifico se il numero (o la lunghezza della stringa) è pari o dispari
    if a % 2 == 0:
        print("Pari")
    else:
        print("Dispari")
    print("Vuoi inserire un nuovo numero: ")
    scelta_1=input(" ")
    if scelta.lower()==no:
        flag=False




####################### Esercizio 2 ###########################

print("Scegli i due numeri che formano l'intervallo")
lower = int(input("Numero inferiore "))
upper = int(input("Livello superiore "))

print("Cosa vuoi sapere ")
print("1- Primi nell'intervallo ")
print("2- Non primi nell'intervallo ")
print("3- Entrambi nell'intervallo ")

# Scelta dell'utente
scelta = int(input(" "))

# Liste che conterranno primi e non primi
primi = []
non_primi = []

# Ciclo su tutti i numeri nell'intervallo
for i in range(lower, upper + 1):

    # Salto il numero 1, che non è né primo né composto
    if i == 1:
        continue

    # Caso dei numeri pari
    if i % 2 == 0:
        if i == 2:
            # 2 è l'unico numero pari primo
            primi.append(2)
        else:
            # gli altri numeri pari non sono primi
            non_primi.append(i)

    # Caso dei numeri dispari: devo controllare la primalità
    else: 
        primo = True  # flag che suppone il numero primo

        # Verifico divisori dispari fino alla radice quadrata
        for j in range(3, int(i**0.5) + 1, 2):
            if i % j == 0:           # se trovo un divisore
                non_primi.append(i)  # non è primo
                primo = False        # aggiorno il flag
                break                # esco subito dal ciclo interno

        # Se dopo tutti i test il numero è ancora primo
        if primo:
            primi.append(i)

# Scelta finale con match-case
match scelta:
    case 1:
        print("Primi nell'intervallo:", primi)
    case 2:
        print("Non primi nell'intervallo:", non_primi)
    case 3:
        print("Primi:", primi)
        print("Non primi:", non_primi)
    case _:
        print("Scelta non valida")


        








