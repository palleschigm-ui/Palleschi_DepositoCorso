# Sistema ripetibile che simula un teatro

# Classe base: Posto
class Posto:
    def __init__(self, numero: int, fila: str, occupato: bool = False):
        # Attributi "protetti" (con _): convenzione, non obbligo
        self._numero = numero
        self._fila = fila
        self._occupato = occupato
    
    def prenota(self):
        # Prenota solo se non occupato
        if not self._occupato:
            print(f"Hai prenotato il posto {self._fila}{self._numero}")
            self._occupato = True
        else:
            print("Il posto è già occupato")

    def libera(self):
        # Libera solo se attualmente occupato
        if self._occupato:
            print(f"Hai liberato il posto {self._fila}{self._numero}")
            self._occupato = False
        else:
            print("Il posto era già libero")

    # Metodi getter
    def get_numero(self):
        return self._numero

    def get_fila(self):
        return self._fila

    def get_occupato(self):
        return self._occupato

    # Metodo speciale: permette confronti tra oggetti Posto basati su numero e fila
    # Serve per usare "in" o confronti come p1 == p2
    def __eq__(self, other):
        return (
            isinstance(other, Posto) and
            self._numero == other._numero and
            self._fila == other._fila
        )

    # Rappresentazione leggibile utile per debug e stampa
    def __repr__(self):
        return f"Posto({self._fila}{self._numero}, occupato={self._occupato})"


class PostoVip(Posto):
    def __init__(self, numero, fila, occupato: bool = False, servizi_extra: str | None = None):
        super().__init__(numero, fila, occupato)
        self.servizi_extra = servizi_extra  # Attributo aggiuntivo

    def prenota(self):
        # Se già occupato, esce
        if self._occupato:
            print("Il posto VIP è già occupato")
            return

        # Prenotazione base
        super().prenota()

        # Extra disponibili solo dopo prenotazione
        print("Servizio extra? (s/n)")
        scelta = input().lower()
        if scelta == "n":
            self.servizi_extra = None
            return
        
        # Ciclo per gestire la scelta corretta dell'utente
        while True:
            print("Scegliere extra:")
            print("1) Accesso al lounge")
            print("2) Servizio in posto")

            try:
                scelta_extra = int(input("> "))  # Conversione a int
            except ValueError:
                print("Inserire un numero valido.")
                continue

            if scelta_extra == 1:
                self.servizi_extra = "Accesso al lounge"
                break
            elif scelta_extra == 2:
                self.servizi_extra = "Servizio in posto"
                break
            else:
                print("Scelta non valida, riprovare.")


class PostoStandard(Posto):
    def __init__(self, numero, fila, costo: float, occupato: bool = False):
        # I parametri di default vanno alla fine
        super().__init__(numero, fila, occupato)
        self.costo = costo  # Attributo specifico del posto standard

    def prenota(self):
        # Se libero, mostra il costo prima di prenotare
        if not self._occupato:
            print(f"Costo del posto {self._fila}{self._numero}: {self.costo}€")
            scelta = input("Vuole prenotare? (s/n) ").lower()
            if scelta != "n":
                super().prenota()
            else: 
                print("Posto non prenotato")
        else:
            print("Il posto è già occupato")


class Teatro:
    def __init__(self, posti: list[Posto]):
        self._posti = posti  # Lista contenente tutti i posti del teatro

    def aggiungi_posto(self, posto: Posto):
        # Lo posso scrivere così perché esiste la funzione magica __eq__,
        # altrimenti "in" confronta gli oggetti solo per identità (is)
        if posto in self._posti:
            print("Posto già in teatro")
        else:
            self._posti.append(posto)
            print(f"Posto {posto.get_fila()}{posto.get_numero()} aggiunto al teatro")

    def prenota_posto(self, numero, fila):
        # Cerca un posto con numero e fila corrispondenti
        for p in self._posti:
            if p.get_numero() == numero and p.get_fila() == fila:
                p.prenota()  # Chiama il metodo prenota della classe corretta
                return
        print("Posto non trovato")

    def stampa_posti_occupati(self):
        trovati = False
        # Stampa solo i posti attualmente occupati
        for p in self._posti:
            if p.get_occupato():
                print(f"Posto occupato: {p.get_fila()}{p.get_numero()}")
                trovati = True
        if not trovati:
            print("Nessun posto occupato.")




    




        

        
    


