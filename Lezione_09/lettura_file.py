# Nome del file che conterrà tutte le ricevute
NOME_FILE = "ricevute.txt"


def salva_ricevuta_acquisto(id_acquisto, prodotto, quantita, prezzo_unitario):
    """
    Salva una ricevuta di acquisto nel file.
    Formato riga:
    TIPO;ID;PRODOTTO;QUANTITA;PREZZO_UNITARIO;TOTALE
    """
    totale = quantita * prezzo_unitario
    riga = f"ACQUISTO;{id_acquisto};{prodotto};{quantita};{prezzo_unitario};{totale}\n"

    # Modalità 'a' per aggiungere senza cancellare il contenuto esistente
    with open(NOME_FILE, "a", encoding="utf-8") as f:
        f.write(riga)


def salva_ricevuta_ordine(id_ordine, cliente, prodotto, quantita):
    """
    Salva una ricevuta di ordine nel file.
    Formato riga:
    TIPO;ID;CLIENTE;PRODOTTO;QUANTITA
    """
    riga = f"ORDINE;{id_ordine};{cliente};{prodotto};{quantita}\n"

    with open(NOME_FILE, "a", encoding="utf-8") as f:
        f.write(riga)


def leggi_tutte_le_ricevute():
    """
    Legge e stampa tutte le righe del file delle ricevute.
    """
    try:
        with open(NOME_FILE, "r", encoding="utf-8") as f:
            contenuto = f.read()
            if contenuto.strip() == "":
                print("Nessuna ricevuta presente.")
            else:
                print("----- CONTENUTO FILE RICEVUTE -----")
                print(contenuto)
    except FileNotFoundError:
        print("Il file delle ricevute non esiste ancora. Nessuna ricevuta salvata.")


def leggi_solo_acquisti():
    """
    Legge e mostra solo le ricevute di tipo ACQUISTO.
    """
    try:
        with open(NOME_FILE, "r", encoding="utf-8") as f:
            print("----- RICEVUTE DI ACQUISTO -----")
            for riga in f:
                if riga.startswith("ACQUISTO;"):
                    print(riga.strip())
    except FileNotFoundError:
        print("Il file delle ricevute non esiste ancora.")


def leggi_solo_ordini():
    """
    Legge e mostra solo le ricevute di tipo ORDINE.
    """
    try:
        with open(NOME_FILE, "r", encoding="utf-8") as f:
            print("----- RICEVUTE DI ORDINE -----")
            for riga in f:
                if riga.startswith("ORDINE;"):
                    print(riga.strip())
    except FileNotFoundError:
        print("Il file delle ricevute non esiste ancora.")


def menu():
    """
    Semplice menu testuale per usare le funzioni di lettura e scrittura.
    """
    while True:
        print("\n=== GESTORE RICEVUTE (un solo file) ===")
        print("1. Aggiungi ricevuta di ACQUISTO")
        print("2. Aggiungi ricevuta di ORDINE")
        print("3. Visualizza TUTTE le ricevute")
        print("4. Visualizza solo ACQUISTI")
        print("5. Visualizza solo ORDINI")
        print("0. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            id_acq = input("ID acquisto: ")
            prodotto = input("Prodotto: ")
            quantita = int(input("Quantità: "))
            prezzo = float(input("Prezzo unitario: "))
            salva_ricevuta_acquisto(id_acq, prodotto, quantita, prezzo)
            print("Ricevuta di acquisto salvata.")

        elif scelta == "2":
            id_ord = input("ID ordine: ")
            cliente = input("Cliente: ")
            prodotto = input("Prodotto: ")
            quantita = int(input("Quantità: "))
            salva_ricevuta_ordine(id_ord, cliente, prodotto, quantita)
            print("Ricevuta di ordine salvata.")

        elif scelta == "3":
            leggi_tutte_le_ricevute()

        elif scelta == "4":
            leggi_solo_acquisti()

        elif scelta == "5":
            leggi_solo_ordini()

        elif scelta == "0":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida, riprova.")


if __name__ == "__main__":
    menu()
