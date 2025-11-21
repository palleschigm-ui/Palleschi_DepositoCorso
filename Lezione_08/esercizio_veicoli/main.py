from veicoli import Camion, Furgone, Motocarro, GestoreFlotta


def main():
    # Creiamo alcuni veicoli di esempio
    c1 = Camion("AA123BB", 10000, numero_assi=4)
    f1 = Furgone("CC456DD", 3000, "diesel")
    m1 = Motocarro("EE789FF", 1500, anni_servizio=5)

    # Creiamo la flotta
    flotta = GestoreFlotta([c1, f1, m1])

    while True:
        print("\n--- MENU FLOTTA ---")
        print("1. Mostra veicoli")
        print("2. Aggiungi veicolo")
        print("3. Rimuovi veicolo")
        print("4. Carica un veicolo")
        print("5. Scarica un veicolo")
        print("6. Costo totale manutenzione")
        print("7. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            flotta.descrizione()

        elif scelta == "2":
            print("Che tipo di veicolo aggiungere?")
            print("a. Camion")
            print("b. Furgone")
            print("c. Motocarro")
            tipo = input("Scelta: ")

            targa = input("Inserisci targa: ")
            peso = int(input("Inserisci peso massimo: "))

            if tipo == "a":
                assi = int(input("Numero assi: "))
                nuovo = Camion(targa, peso, assi)
            elif tipo == "b":
                alim = input("Alimentazione (diesel/elettrico): ")
                nuovo = Furgone(targa, peso, alim)
            elif tipo == "c":
                anni = int(input("Anni di servizio: "))
                nuovo = Motocarro(targa, peso, anni)
            else:
                print("Tipo non valido")
                continue

            flotta.aggiungi_veicolo(nuovo)

        elif scelta == "3":
            targa = input("Inserisci targa del veicolo da rimuovere: ")
            flotta.rimuovi_veicolo(targa)

        elif scelta == "4":
            targa = input("Targa del veicolo da caricare: ")
            peso = int(input("Peso da caricare: "))

            trovato = False
            for v in flotta.veicoli:
                if v.targa == targa:
                    v.carica(peso)
                    trovato = True
                    break
            if not trovato:
                print("Veicolo non trovato")

        elif scelta == "5":
            targa = input("Targa del veicolo da scaricare: ")
            trovato = False
            for v in flotta.veicoli:
                if v.targa == targa:
                    v.scarica()
                    trovato = True
                    break
            if not trovato:
                print("Veicolo non trovato")

        elif scelta == "6":
            print("Costo totale manutenzione:", flotta.costo_totale_manutenzione())

        elif scelta == "7":
            print("Uscita dal programma...")
            break

        else:
            print("Scelta non valida")


if __name__ == "__main__":
    main()
