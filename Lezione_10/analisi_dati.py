import numpy as np


# Genera 12 valori equidistanti tra 0 e 1
arr = np.linspace(0, 1, 12)

# Trasforma l'array in una matrice 3x4
arr2 = arr.reshape((3, 4))   # reshape con tupla

# Crea una matrice 3x4 di numeri casuali tra 0 e 1
matrix = np.random.rand(3, 4)
print("Matrice casuale:")
print(matrix)

# Somma elemento per elemento tra arr2 e matrix
somma = arr2 + matrix
print("Somma delle due matrici:")
print(somma)


###################################################
###################################################


import numpy as np

# Numero di elementi da generare
NUM_ELEMENTI = 50

# Array base da 0 a 1 con 50 valori equispaziati
base_array = np.linspace(0, 1, NUM_ELEMENTI)

def crea_array_somma():
    """Restituisce la somma tra l'array base e un array casuale."""
    array_random = np.random.random(NUM_ELEMENTI)
    return base_array + array_random

def salva_su_file(percorso, contenuto, modalità="w"):
    """Salva una riga di valori in formato leggibile dentro un file."""
    stringa = " ".join(str(x) for x in contenuto) + "\n"
    with open(percorso, modalità) as f:
        f.write(stringa)

# Contatore per i file aggiuntivi
conta_file = 1

# Creazione del primo file
array_somma = crea_array_somma()
salva_su_file("dati_generati.txt", array_somma)

while True:
    print("\nIl primo file è stato generato.")
    print("----- MENU -----")
    print("1) Aggiungi nuovi dati allo stesso file")
    print("2) Riscrivi il file da zero")
    print("3) Crea un nuovo file con un altro nome")
    print("4) Esci dal programma")

    scelta = input("Seleziona un'opzione: ")

    match scelta:
        case "1":
            array_somma = crea_array_somma()
            salva_su_file("dati_generati.txt", array_somma, "a")

        case "2":
            array_somma = crea_array_somma()
            salva_su_file("dati_generati.txt", array_somma, "w")

        case "3":
            array_somma = crea_array_somma()
            nuovo_nome = f"dati_generati_{conta_file}.txt"
            salva_su_file(nuovo_nome, array_somma, "w")
            conta_file += 1

        case "4":
            break

        case _:
            print("Scelta non riconosciuta.")
            continue

    input("Operazione conclusa. Premi Invio per proseguire...")

#####################################################################
#####################################################################

print(np.random.random((4,4)))