from classi import Dipendente, Visitatore
from registro import RegistroAccessi


def main():
    # Creazione persone
    d1 = Dipendente("Mario", "Rossi", "101")
    d2 = Dipendente("Luca", "Bianchi", "102")
    v1 = Visitatore("Giulia", "Verdi", "201")

    # Creazione registro vuoto
    registro = RegistroAccessi()

    print("\n--- INGRESSI ---")

    # Aggiungo persone (simulo ingressi)
    registro.aggiungi_persona(d1)
    registro.aggiungi_persona(d2)
    registro.aggiungi_persona(v1)

    print("\n--- PRESENZE ATTUALI ---")
    registro.presenze()

    print("\n--- USCITA DI UNA PERSONA ---")
    registro.rimuovi_persona(d2)

    print("\n--- PRESENZE DOPO USCITA ---")
    registro.presenze()

    print("\n--- TENTATIVO DI RIPETERE USCITA ---")
    registro.rimuovi_persona(d2)  # badge non più presente

    print("\n--- TENTATIVO DI AGGIUNGERE DUPLICATO ---")
    registro.aggiungi_persona(d1)  # badge già presente


if __name__ == "__main__":
    main()
