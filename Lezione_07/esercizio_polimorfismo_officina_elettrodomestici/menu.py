# menu.py
from classi_elettrodomestici import Elettrodomestico, Lavatrice, Frigorifero, Forno
from ticket import TicketRiparazione

def crea_elettrodomestici():
    """Crea una lista di elettrodomestici di test."""
    e1 = Lavatrice("Bosch", "Serie 4", 2020, "Non centrifuga", 8, 1200)
    e2 = Frigorifero("Samsung", "CoolMax", 2018, "Non raffredda", 300, True)
    e3 = Forno("Whirlpool", "HeatPro", 2019, "Non scalda", "elettrico", True)

    return [e1, e2, e3]


def crea_ticket(elettrodomestici):
    """Crea alcuni ticket associati agli elettrodomestici."""
    t1 = TicketRiparazione(1, elettrodomestici[0], "aperto")
    t2 = TicketRiparazione(2, elettrodomestici[1], "in lavorazione")
    t3 = TicketRiparazione(3, elettrodomestici[2], "chiuso")

    return [t1, t2, t3]


def mostra_elettrodomestici(lista):
    print("\n=== ELETTRODOMESTICI ===")
    for idx, e in enumerate(lista, start=1):
        print(f"{idx}) {e.descrizione()}")
    print()


def mostra_ticket(lista):
    print("\n=== TICKET DI RIPARAZIONE ===")
    for t in lista:
        print(f"ID: {t._TicketRiparazione__id_ticket} | Stato: {t.get_stato()} | Note: {t.get_note()}")
    print()


def aggiungi_nota_ticket(ticket):
    print(f"Aggiunta nota al ticket {ticket._TicketRiparazione__id_ticket}")
    ticket.aggiungi_nota()
    print("Nota aggiunta.\n")


def cambia_stato_ticket(ticket):
    print(f"Stato attuale: {ticket.get_stato()}")
    nuovo = input("Nuovo stato (aperto / in lavorazione / chiuso): ").lower()
    ticket.set_stato(nuovo)
    print("Stato aggiornato.\n")


def calcola_preventivo_ticket(ticket):
    print("Inserire voci extra separate da spazio (es: 50 30 20.5):")
    voci = input("> ").split()
    try:
        voci_float = [float(v) for v in voci]
    except ValueError:
        print("Errore: inserisci solo numeri.\n")
        return

    totale = ticket.calcola_preventivo(*voci_float)
    print(f"Preventivo totale: {totale} €\n")


def menu():
    elettrodomestici = crea_elettrodomestici()
    ticket = crea_ticket(elettrodomestici)

    while True:
        print("=== MENU RIPARAZIONI ===")
        print("1) Mostra elettrodomestici")
        print("2) Mostra ticket")
        print("3) Aggiungi nota a un ticket")
        print("4) Cambia stato di un ticket")
        print("5) Calcola preventivo di un ticket")
        print("0) Esci")
        
        scelta = input("Scelta: ")

        if scelta == "1":
            mostra_elettrodomestici(elettrodomestici)

        elif scelta == "2":
            mostra_ticket(ticket)

        elif scelta == "3":
            id_t = int(input("ID Ticket: "))
            trovato = next((t for t in ticket if t._TicketRiparazione__id_ticket == id_t), None)
            if trovato:
                aggiungi_nota_ticket(trovato)
            else:
                print("Ticket non trovato.\n")

        elif scelta == "4":
            id_t = int(input("ID Ticket: "))
            trovato = next((t for t in ticket if t._TicketRiparazione__id_ticket == id_t), None)
            if trovato:
                cambia_stato_ticket(trovato)
            else:
                print("Ticket non trovato.\n")

        elif scelta == "5":
            id_t = int(input("ID Ticket: "))
            trovato = next((t for t in ticket if t._TicketRiparazione__id_ticket == id_t), None)
            if trovato:
                calcola_preventivo_ticket(trovato)
            else:
                print("Ticket non trovato.\n")

        elif scelta == "0":
            print("Uscita.")
            break
        else:
            print("Scelta non valida.\n")


if __name__ == "__main__":
    pass
