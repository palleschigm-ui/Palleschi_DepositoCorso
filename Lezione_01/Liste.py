#############################
# DEFINIZIONE DELLE LISTE
#############################

numeri = [1, 2, 3, 4, 5]
nomi = ["Alice", "Bob", "Franco"]
mix = [1, 2, "uno", "Alice", 5]

# Stampo il primo elemento della lista
print(numeri[0])

# Stampo il secondo elemento della lista
print(nomi[1])

# len() restituisce la lunghezza della lista
print(len(mix))

# append() aggiunge un elemento alla fine
numeri.append(100)
print(numeri)

# insert(posizione, valore) inserisce un elemento in una posizione specifica
numeri.insert(2, 100000)
print(numeri)

# remove() rimuove un valore specifico dalla lista
numeri.remove(100)                  # Rimuove l'elemento '100'
numeri.remove(numeri[3])            # Rimuove l’elemento in posizione 3


#############################
# ESERCIZIO PASSWORD
#############################

print("###################### ESERCIZIO PASSWORD ####################################")

print("Registrati:")
username_corretto = input("Quale username vuoi scegliere? ")
password_corretta = input("Quale password vuoi scegliere? ")

print("Perfetto! Ti sei registrato.")

# Login dell’utente
nome_utente = input("Qual è il tuo nome utente? ")
password_utente = input("Qual è la tua password? ")

# Verifica delle credenziali
if nome_utente == username_corretto and password_utente == password_corretta:

    print("Benvenuto!")

    # Scelta della domanda segreta
    print("Scegli una domanda segreta:")
    print("1 - Qual è il tuo animale preferito?")
    print("2 - Qual è il tuo colore preferito?")

    domanda_scelta = int(input("Scegli un numero: "))

    if domanda_scelta == 1:
        animale = input("Scrivi il tuo animale preferito: ")
        print(f"Il tuo animale preferito è il {animale}")
    
    elif domanda_scelta == 2:
        colore = input("Scrivi il tuo colore preferito: ")
        print(f"Il tuo colore preferito è il {colore}")

    else:
        print("Errore: scelta non valida.")

else:
    print("Le credenziali sono errate.")


#############################
# ESEMPIO DI pop()
#############################

print(numeri)

# pop() rimuove e restituisce l’ultimo elemento della lista
ultimo_elemento = numeri.pop()
print(ultimo_elemento)



