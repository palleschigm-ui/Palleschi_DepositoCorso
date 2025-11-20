import classi_teatro as ct

def main():

    # Creo alcuni posti semplici
    p1 = ct.PostoStandard(1, "A", costo=10.0)
    p2 = ct.PostoStandard(2, "A", costo=12.0)
    p3 = ct.PostoVip(1, "B")

    teatro = ct.Teatro([p1, p2, p3])

    while True:
        print("\n=== MENU TEATRO ===")
        print("1) Mostra tutti i posti")
        print("2) Prenota un posto")
        print("3) Libera un posto")
        print("0) Esci")
        
        scelta = input("Scegli: ")

        if scelta == "1":
            # Mostra stato dei posti
            for p in teatro._posti:
                stato = "Occupato" if p.get_occupato() else "Libero"
                print(f"Posto {p.get_fila()}{p.get_numero()} - {stato}")

        elif scelta == "2":
            fila = input("Fila (es. A): ").upper()
            numero = int(input("Numero: "))
            teatro.prenota_posto(numero, fila)

        elif scelta == "3":
            fila = input("Fila (es. A): ").upper()
            numero = int(input("Numero: "))
            for p in teatro._posti:
                if p.get_fila() == fila and p.get_numero() == numero:
                    p.libera()
                    break
            else:
                print("Posto non trovato")

        elif scelta == "0":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()
