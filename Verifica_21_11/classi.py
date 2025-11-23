from abc import ABC, abstractmethod

# Classe astratta: rappresenta il concetto GENERICO di persona
# ------------------------------------------------------------
# Qui c'è:
# - ASTRZIONE: Persona è un modello generale, non istanziabile direttamente
# - verrà specializzata da classi concrete (Dipendente, Visitatore)
class Persona(ABC):
    def __init__(self, nome: str, cognome: str):
        # Attributi "protetti" per convenzione (un underscore):
        # fanno parte dell'INCAPSULAMENTO "leggero"
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
        orario_inizio_turno: float | None = None,
        orario_fine_turno: float | None = None
    ):
        # Attributi privati (name mangling: __nome)
        # INCPASULAMENTO: accessibili solo tramite metodi getter/setter
        self.__id_badge = id_badge
        self.__att_presente = None

        # Attributi "protetti" (un underscore) per logica interna
        self._orario_ingresso = None
        self._orario_uscita = None

        # Turni (privati)
        self.__orario_inizio_turno = orario_inizio_turno
        self.__orario_fine_turno = orario_fine_turno

        # Flag di controllo (privati)
        self.__entrata_in_ritardo = False
        self.__uscita_anticipata = False

    # Metodi getter: INCAPSULAMENTO, accesso controllato
    def get_inizio_turno(self):
        return self.__orario_inizio_turno
    
    def get_fine_turno(self):
        return self.__orario_fine_turno
    
    def get_badge(self):
        return self.__id_badge
    
    def get_presente(self):
        return self.__att_presente
    
    def get_entrata_in_ritardo(self):
        return self.__entrata_in_ritardo
    
    def get_uscita_anticipata(self):
        return self.__uscita_anticipata
    
    # Setter con controllo: INCAPSULAMENTO
    def set_presente(self, cambio: bool):
        if not isinstance(cambio, bool):
            print("Errore: valore non booleano.")
            return
        if cambio == self.get_presente():
            print("Nessuna modifica di stato (il valore è già quello corrente).")
            return
        self.__att_presente = cambio
    
    def set_entrata_in_ritardo(self, ritardo: bool):
        if not isinstance(ritardo, bool):
            print("Errore: valore non booleano.")
            return
        self.__entrata_in_ritardo = ritardo
    
    def set_uscita_anticipata(self, anticipata: bool):
        if not isinstance(anticipata, bool):
            print("Errore: valore non booleano.")
            return
        self.__uscita_anticipata = anticipata

    # Metodi di comportamento: ingresso/uscita
    def ingresso(self):
        print("Inserire orario ingresso: ")
        self._orario_ingresso = float(input())
        if self.__orario_inizio_turno is not None:
            if self._orario_ingresso > self.__orario_inizio_turno:
                self.set_entrata_in_ritardo(True)
        self.set_presente(True)
        return self._orario_ingresso

    def uscita(self):
        print("Inserire orario uscita: ")
        self._orario_uscita = float(input())
        if self.__orario_fine_turno is not None:
            if self._orario_uscita < self.__orario_fine_turno:
                self.set_uscita_anticipata(True)
        self.set_presente(False)
        return self._orario_uscita


# Classe concreta Dipendente
# --------------------------
# Qui c'è:
# - EREDITARIETÀ multipla: Dipendente eredita da Persona e Controllo
# - POLIMORFISMO: implementa il metodo astratto lavoratore()
class Dipendente(Persona, Controllo):
    def __init__(self, nome, cognome, id_badge,
                 orario_inizio_turno=9.00,
                 orario_fine_turno=18.00):

        # EREDITARIETÀ: inizializzazione Persona
        Persona.__init__(self, nome, cognome)

        # EREDITARIETÀ: inizializzazione Controllo
        Controllo.__init__(
            self,
            id_badge,
            orario_inizio_turno,
            orario_fine_turno
        )

        # Attributo privato: INCAPSULAMENTO
        self.__dipendente = True

    def get_dipendente(self):
        return self.__dipendente
    
    # Rappresentazione leggibile: __str__
    def __str__(self):
        return (
            f"Nome: {self._nome}\n"
            f"Cognome: {self._cognome}\n"
            f"ID Badge: {self.get_badge()}\n"
            f"Presente: {self.get_presente()}\n"
            f"Ingresso: {self._orario_ingresso}\n"
            f"Uscita: {self._orario_uscita}\n"
            f"Inizio turno: {self.get_inizio_turno()}\n"
            f"Fine turno: {self.get_fine_turno()}\n"
            f"Entrata in ritardo: {self.get_entrata_in_ritardo()}\n"
            f"Uscita in anticipo: {self.get_uscita_anticipata()}\n"
            f"Dipendente: {self.get_dipendente()}"
        )

    # POLIMORFISMO
    def lavoratore(self):
        if self.get_dipendente():
            print(f"{self._nome} {self._cognome} lavora nell'azienda")


# Classe concreta Visitatore
# --------------------------
# Anche qui:
# - EREDITARIETÀ multipla
# - POLIMORFISMO su lavoratore()
class Visitatore(Persona, Controllo):
    def __init__(self, nome, cognome, id_badge):

        # EREDITARIETÀ: inizializzazione Persona
        Persona.__init__(self, nome, cognome)

        # EREDITARIETÀ: inizializzazione Controllo (senza orari)
        Controllo.__init__(
            self,
            id_badge,
            orario_inizio_turno=None,
            orario_fine_turno=None
        )

        # Attributo privato: INCAPSULAMENTO
        self.__dipendente = False

    def get_dipendente(self):
        return self.__dipendente

    # POLIMORFISMO
    def lavoratore(self):
        if not self.get_dipendente():
            print(f"{self._nome} {self._cognome} non lavora nell'azienda")

    # __str__ corretto
    def __str__(self):
        return (
            f"Nome: {self._nome}\n"
            f"Cognome: {self._cognome}\n"
            f"ID Badge: {self.get_badge()}\n"
            f"Presente: {self.get_presente()}\n"
            f"Ingresso: {self._orario_ingresso}\n"
            f"Uscita: {self._orario_uscita}\n"
            f"Dipendente: {self.get_dipendente()}"
        )
