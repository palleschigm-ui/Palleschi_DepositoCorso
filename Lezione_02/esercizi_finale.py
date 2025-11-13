########################## Esercizio 1 ################################

numeri=[]
somma=0
while True:
    new=int(input("Inserisci un numero intero: "))
    if new==0: 
        break # Se è 0 esco
    else:
        numeri.append(new)  # Aggiungo il numero alla lista
        somma = somma + new # Aggiorno la somma totale

print(f"La somma dei numeri risulta essere: {somma}")

###################### Esercizio 2 ######################################

parola=input("Inserisci la parola: ")

# Ciclo su ogni carattere della parola
for i in parola:
    print(i, end=" ")
print()

###################### Esercizio 3 ##########################################

n=int(input("Numero: "))
step=int(input("Step: "))

# Stampa i numeri da 0 a n (incluso), avanzando di "step"

for i in range(0,n+1,step):
    print(i)
