from classi import Dipendente, Visitatore
from registro import RegistroAccessi   # cambia il nome se necessario


# -------------------------------------------------------
#  CREAZIONE REGISTRO DI PROVA
# -------------------------------------------------------
def crea_registro_di_prova():
    d1 = Dipendente("Mario", "Rossi", "D001", 9.00, 18.00)
    d2 = Dipendente("Lucia", "Bianchi", "D002", 9.00, 18.00)
    v1 = Visitatore("Anna", "Verdi", "V001")
    v2 = Visitatore("Carlo", "Neri", "V002")

    registro = RegistroAccessi()
    registro.aggiungi_persona(d1)
    registro.aggiungi_persona(d2)
    registro.aggiungi_persona(v1)
    registro.aggiungi_persona(v2)

    return registro


# -------------------------------------------------------
#  MENU
# -------------------------------------------------------
def stampa_menu():
    print("\n========== REGISTRO ACCESSI ==========")
    print("1) Mostra presenze")
    print("2) Mostra assenti")
    print("3) Registra entrata")
    print("4) Registra uscita")
    print("5) Panoramica completa")
    print("6) Elenco entrati in ritardo")
    print("7) Elenco usciti in anticipo")
    print("8) Aggiungi persona al registro")
    print("9) Rimuovi persona dal registro")
    print("10) Stato lavoratore / non lavoratore")
    print("11) Controllo ad personam (print dettagli per badge)")
    print("0) Esci")
    print("=======================================")


# -------------------------------------------------------
#  FUNZIONE PER CREARE UNA PERSONA VIA INPUT
# -------------------------------------------------------
def crea_persona_da_input():
    print("\nChi vuoi aggiungere?")
    print("1) Dipendente")
    print("2) Visitatore")

    tipo = input("Scelta: ")

    nome = input("Nome: ")
    cognome = input("Cognome: ")
    id_badge = input("ID Badge: ")

    if tipo == "1":
        try:
            inizio = float(input("Orario inizio turno (es. 9.0): "))
            fine = float(input("Orario fine turno (es. 18.0): "))
        except ValueError:
            print("Input orari non valido. Userò 9.0 - 18.0 come default.")
            inizio = 9.0
            fine = 18.0

        return Dipendente(nome, cognome, id_badge, inizio, fine)

    elif tipo == "2":
        return Visitatore(nome, cognome, id_badge)

    else:
        print("Scelta non valida. Persona non creata.")
        return None


# -------------------------------------------------------
#  MAIN
# -------------------------------------------------------
def main():
    registro = crea_registro_di_prova()
    print("Registro di prova creato con 4 persone.")

    while True:
        stampa_menu()
        scelta = input("Inserisci la tua scelta: ")

        # USCITA
        if scelta == "0":
            print("Chiusura programma.")
            break

        # 1) Presenze
        elif scelta == "1":
            registro.presenze()

        # 2) Assenti
        elif scelta == "2":
            registro.assenti()

        # 3) Entrata
        elif scelta == "3":
            badge = input("Inserisci ID badge per registrare l'entrata: ")
            registro.registra_entrata(badge)

        # 4) Uscita
        elif scelta == "4":
            badge = input("Inserisci ID badge per registrare l'uscita: ")
            registro.registra_uscita(badge)

        # 5) Panoramica
        elif scelta == "5":
            print("\n----------- PANORAMICA ------------")
            registro.panoramica()

        # 6) Entrati in ritardo
        elif scelta == "6":
            registro.entrati_in_ritardo()

        # 7) Usciti in anticipo
        elif scelta == "7":
            registro.usciti_in_anticipo()

        # 8) Aggiungi persona
        elif scelta == "8":
            persona = crea_persona_da_input()
            if persona:
                registro.aggiungi_persona(persona)

        # 9) Rimuovi persona
        elif scelta == "9":
            badge = input("Inserisci ID badge della persona da rimuovere: ")
            registro.rimuovi_persona(badge)

        # 10) Metodo lavoratore()
        elif scelta == "10":
            print("\n---- STATO LAVORATIVO ----")
            for p in registro.registro:
                p.lavoratore()

        # 11) Controllo ad personam
        elif scelta == "11":
            badge = input("Inserisci ID badge per il controllo: ")
            registro.controllo_ad_personam(badge)

        # SCELTA NON VALIDA
        else:
            print("Scelta non valida, riprova.")


if __name__ == "__main__":
    main()
