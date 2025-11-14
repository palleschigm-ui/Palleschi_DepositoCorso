#####################à Esercizio finale #######################

record=[]                     # Lista che conterrà tutte le righe di risultati

while True:                   # Ciclo principale: continua finché l’utente non dice "no"
    try:
        valid=False           # Flag per controllare un input valido

        while not valid:      # Ripete finché l'utente non inserisce un numero > 0
            n=int(input("Inserire un numero: "))   # Chiede un numero e tenta la conversione
            if n>0:
                valid=True                         # Numero valido
            else:
                print("Il numero deve essere maggiore di 0")

        # Calcolo somma dei numeri pari e dispari fino a n
        somma_pari=0
        somma_dispari=0

        if n%2==0:                               # Caso: n pari
            for i in range(2,n+1,2):             # Sommo i pari da 2 a n
                somma_pari += i
            for i in range(1,n,2):               # Sommo i dispari da 1 a n-1
                somma_dispari += i
        else:                                    # Caso: n dispari
            for i in range(2,n,2):               # Sommo i pari da 2 a n-1
                somma_pari += i
            for i in range(1,n+1,2):             # Sommo i dispari da 1 a n
                somma_dispari += i

        # Controllo della primalità
        if n==1:
            print("Non è primo")
            primalità="Non è primo"

        elif n % 2 == 0:                         # Se è pari
            if n==2:                             # 2 è primo
                print("Primo")
                primalità="Primo"
            else:                                # Altri pari non sono primi
                print("Non è primo")
                primalità="Non è primo"

        else:                                    # n dispari > 2
            primo=True
            # Verifica divisibilità per tutti i numeri dispari fino alla radice quadrata
            for i in range(3, int(n**0.5)+1, 2):
                if n % i == 0:
                    print("Non è primo")
                    primalità="Non è primo"
                    primo=False                  # Non è primo
                    break
            if primo:
                print("Primo")
                primalità="Primo"

        # Stampa delle somme calcolate
        print("Somma pari: ", somma_pari)
        print("Somma dispari: ", somma_dispari)

        # Salvo i risultati in una nuova "riga" del record
        record.append([n, primalità, somma_pari, somma_dispari])

        # Chiede se si vuole proseguire
        print("Vuoi inserire un nuovo numero: ")
        scelta = input(" ")
        if scelta.lower() == "no":
            break                                # Esce dal ciclo principale

    except ValueError:
        # Questo blocco intercetta input non validi (es. lettere)
        print("Devi inserire un numero")

# Alla fine del programma stampo tutti i risultati raccolti
print(record)





