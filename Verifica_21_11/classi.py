from abc import ABC, abstractmethod

# Classe astratta: rappresenta il concetto GENERICO di persona
# ------------------------------------------------------------
# Qui c'è:
# - ASTRZIONE: Persona è un modello generale, non istanziabile direttamente
# - verrà specializzata da classi concrete (Dipendente, Visitatore)
class Persona(ABC):
    def __init__(self, nome: str, cognome: str):
        super().__init__()
        # Attributi "protetti" per convenzione (un underscore):
        # fanno parte dell'INCAPSULAMENTO "leggero" (non sono privati, ma segnalano uso interno)
        self._nome = nome
        self._cognome = cognome
    
    @abstractmethod
    def lavoratore(self):
        # Metodo astratto:
        # - ASTRZIONE: definisce un'interfaccia comune
        # - obbliga le sottoclassi a implementare il comportamento specifico
        pass



# Classe che gestisce i dati di controllo accessi (badge, presenze, orari)
# ------------------------------------------------------------------------
# Questa NON è astratta, ma viene riusata tramite ereditarietà multipla.
# Qui c'è:
# - INCAPSULAMENTO forte sugli attributi privati (__nome)
class Controllo:
    def __init__(
        self,
        id_badge: str,
        att_presente: bool = False,
        orario_ingresso: float | None = None,
        orario_uscita: float | None = None,
        orario_inizio_turno: float | None = None,
        orario_fine_turno: float | None = None
    ):
        # Attributi privati (name mangling: __nome)
        # INCPASULAMENTO: accessibili solo tramite metodi getter/setter
        self.__id_badge = id_badge
        self.__att_presente = att_presente
        # Questi sono "protetti" (un underscore) e fanno parte della logica interna
        self._orario_ingresso = orario_ingresso
        self._orario_uscita = orario_uscita
        self.__orario_inizio_turno = orario_inizio_turno
        self.__orario_fine_turno = orario_fine_turno

    # Metodi getter: fanno parte dell'INCAPSULAMENTO, permettono accesso controllato
    def get_inizio_turno(self):
        return self.__orario_inizio_turno
    
    def get_fine_turno(self):
        return self.__orario_fine_turno
    
    def get_badge(self):
        return self.__id_badge
    
    def get_presente(self):
        return self.__att_presente
    
    # Setter con controllo: altro esempio di INCAPSULAMENTO
    def set_presente(self, cambio: bool):
        if not isinstance(cambio, bool):
            print("Errore: valore non booleano.")
            return
        if cambio == self.get_presente():
            print("Nessuna modifica di stato (il valore è già quello corrente).")
            return
        self.__att_presente = cambio

    # Metodi di "comportamento" legati all'ingresso/uscita
    def ingresso(self):
        print("Inserire orario ingresso: ")
        self._orario_ingresso = float(input())
        self.set_presente(True)
        return self._orario_ingresso

    def uscita(self):
        print("Inserire orario uscita: ")
        self._orario_uscita = float(input())
        self.set_presente(False)
        return self._orario_uscita


# Classe concreta Dipendente
# --------------------------
# Qui c'è:
# - EREDITARIETÀ multipla: Dipendente eredita da Persona E da Controllo
# - POLIMORFISMO: implementa il metodo astratto lavoratore() in modo specifico
class Dipendente(Persona, Controllo):
    def __init__(self, nome, cognome, id_badge,
                 att_presente=False,
                 orario_ingresso=None,
                 orario_uscita=None,
                 orario_inizio_turno=None,
                 orario_fine_turno=None):
        # Chiamata esplicita ai costruttori delle classi base
        # EREDITARIETÀ: riuso di codice da Persona
        Persona.__init__(self, nome, cognome)
        # EREDITARIETÀ: riuso di codice da Controllo
        Controllo.__init__(
            self,
            id_badge,
            att_presente,
            orario_ingresso,
            orario_uscita,
            orario_inizio_turno,
            orario_fine_turno
        )
        # Attributo privato: INCAPSULAMENTO (indica se è dipendente)
        self.__dipendente = True

    def get_dipendente(self):
        return self.__dipendente

    # Implementazione concreta del metodo astratto lavoratore()
    # ----------------------------------------------------------
    # Qui c'è:
    # - POLIMORFISMO: stessa "firma" di Persona.lavoratore(),
    #   comportamento specifico per il Dipendente.
    def lavoratore(self):
        if self.get_dipendente():
            print(f"{self._nome} {self._cognome} lavora nell'azienda")


# Classe concreta Visitatore
# --------------------------
# Anche qui:
# - EREDITARIETÀ multipla da Persona e Controllo
# - POLIMORFISMO su lavoratore(), con comportamento diverso rispetto a Dipendente
class Visitatore(Persona, Controllo):
    def __init__(self, nome, cognome, id_badge,
                 att_presente=False,
                 orario_ingresso=None,
                 orario_uscita=None):
        # EREDITARIETÀ: inizializzazione parte Persona
        Persona.__init__(self, nome, cognome)
        # EREDITARIETÀ: inizializzazione parte Controllo
        # Per il visitatore non uso orari di turno
        Controllo.__init__(
            self,
            id_badge,
            att_presente,
            orario_ingresso,
            orario_uscita,
            orario_inizio_turno=None,
            orario_fine_turno=None
        )
        # Attributo privato che indica che NON è dipendente
        # Sempre INCAPSULAMENTO (informazione interna alla classe)
        self.__dipendente = False

    def get_dipendente(self):
        return self.__dipendente

    # Anche qui POLIMORFISMO:
    # stesso metodo lavoratore(), ma logica diversa rispetto a Dipendente.
    def lavoratore(self):
        if not self.get_dipendente():
            print(f"{self._nome} {self._cognome} non lavora nell'azienda")
