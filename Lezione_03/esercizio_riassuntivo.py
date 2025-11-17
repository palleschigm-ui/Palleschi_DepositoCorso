#ESERCIZIO: Simulatore di chiamate telefoniche con rubrica, numeri sconosciuti
#e sistema di blocco tramite decoratore.

#Il programma genera una rubrica telefonica casuale (numeri e nomi associati).
#Simula continuamente l’arrivo di chiamate:

#- Se il numero è in rubrica, mostra il nome del chiamante.
#- Se il numero è sconosciuto, chiede all’utente se vuole rispondere.
#- Grazie a un decoratore, al termine della chiamata viene chiesto se si vuole
#  bloccare un numero sconosciuto.
#- I numeri bloccati non faranno più squillare il telefono.
#- Dopo ogni chiamata, l’utente decide se continuare a simulare altre chiamate.



import random

# Crea la rubrica con numeri e nomi casuali
def rubrica(n):
    rubrica_telefonica = [random.randint(10000, 99999) for _ in range(n)]  # numeri a 5 cifre
    nomi_possibili = ["Gabriella","Andrea","Marco", "Giulia", "Anna", "Luca",
                      "Sara", "Paolo", "Elena","Gianmario","Carlo","Antonio",
                      "Pietro","Giovanna"]
    rubrica_nomi = [random.choice(nomi_possibili) for _ in range(n)]       # nomi casuali
    numeri_bloccati = []                                                   # lista iniziale vuota
    return rubrica_nomi, rubrica_telefonica, numeri_bloccati


# Simula l’arrivo di una chiamata
def chiamata(rubrica_telefonica):
    print("Ti stanno chiamando...")
    probabilita = random.random()

    # 80%: numero appartenente alla rubrica
    if probabilita > 0.9:
        numero_chiamata = random.choice(rubrica_telefonica)

    # 20%: numero completamente casuale
    else:
        numero_chiamata = random.randint(1, 10)

    return numero_chiamata


# Verifica se il numero è noto, sconosciuto o bloccato
def controllo_se_numero_in_rubrica(numero_chiamata, rubrica_telefonica,
                                   rubrica_nomi, numeri_bloccati):

    # Se il numero è stato precedentemente bloccato
    if numero_chiamata in numeri_bloccati:
        print(f"Chiamata rifiutata: il numero {numero_chiamata} è bloccato.")
        return None   # indica che la chiamata non deve essere gestita ulteriormente
    
    # Numero registrato nella rubrica
    if numero_chiamata in rubrica_telefonica:
        index_chiamata = rubrica_telefonica.index(numero_chiamata)
        print("Ti sta chiamando:", rubrica_nomi[index_chiamata],
              f"({numero_chiamata})")
        return False  # non è sconosciuto

    # Numero sconosciuto
    else:
        print("Il numero risulta essere sconosciuto:", numero_chiamata)
        return True   # è sconosciuto → flag True


# Chiede all’utente se vuole rispondere alla chiamata
def accetta_chiamata():
    print("Vuoi rispondere alla chiamata? (s/n)")
    scelta = input().lower()
    if scelta == "s":
        print("Hai accettato la chiamata")
    elif scelta == "n":
        print("Non hai accettato la chiamata")
    else:
        print("Scelta non valida")


# Decoratore: esegue la funzione di blocco solo se flag è True
def controlla_flag(func):
    def wrapper(flag, numero, numeri_bloccati):
        if flag:  # flag True → numero sconosciuto → posso bloccarlo
            return func(numero, numeri_bloccati)
        # Se flag False (numero noto) o None (numero già bloccato) non fa nulla
    return wrapper 


# Funzione che blocca un numero sconosciuto (decorata)
@controlla_flag
def blocco_numero(numero, numeri_bloccati):
    print("Vuoi bloccare il numero? (s/n)")
    scelta = input().lower()
    if scelta == "s":
        numeri_bloccati.append(numero)
        print(f"Numero {numero} aggiunto alla lista dei numeri bloccati.")
    else:
        print("Numero non bloccato.")


# --- PROGRAMMA PRINCIPALE ---

rubrica_nomi, rubrica_telefonica, numeri_bloccati = rubrica(10)

while True:
    # Simula una nuova chiamata
    numero_chiamata = chiamata(rubrica_telefonica)

    # Verifica natura del numero
    flag = controllo_se_numero_in_rubrica(
        numero_chiamata,
        rubrica_telefonica,
        rubrica_nomi,
        numeri_bloccati
    )

    # Se il numero era bloccato, passo alla prossima iterazione
    if flag is None:
        continue

    # Chiedo se rispondere
    accetta_chiamata()

    # Se il numero è sconosciuto (flag True), chiedo se bloccarlo
    blocco_numero(flag, numero_chiamata, numeri_bloccati)

    # Opzione per uscire dal programma
    print("Vuoi continuare a ricevere chiamate? (s/n)")
    continua = input().lower()
    if continua == "n":
        print("Programma terminato.")
        break







