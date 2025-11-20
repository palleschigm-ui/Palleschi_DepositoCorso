#=====================================
# ESERCIZIO INCAPSULAMENTO
#=====================================

print("#################################################")
print("          ESERCIZIO   CONTO BANCARIO            ")
print("#################################################")


class ContoBancario:
    # Costruttore: inizializza un conto con titolare e saldo
    def __init__(self, titolare, saldo):
        self.__titolare = titolare   # Attributo privato: nome del titolare
        self.__saldo = saldo         # Attributo privato: saldo del conto
    
    # Metodo per depositare una somma di denaro
    def deposita(self, importo):
        if importo > 0:                     # Controllo: importo deve essere positivo
            self.__saldo += importo         # Aggiorna il saldo
            print("Hai versato ", importo)
        else:
            pass                            # Non fa nulla se importo è negativo o zero
    
    # Metodo per prelevare una somma di denaro
    def preleva(self, importo):
        # Controlla che l'importo sia positivo e che il saldo sia sufficiente
        if importo > 0 and self.__saldo >= importo:
            self.__saldo -= importo         # Sottrae l'importo dal saldo
            print("Hai prelevato ", importo)
        else:
            print("Saldo non sufficiente")  # Messaggio di errore
    
    # Metodo che mostra il saldo attuale (stampa a schermo)
    def visualizza_saldo(self):
        print("Saldo attuale: ", self.__saldo)
    
    # Getter: restituisce il nome del titolare
    def get_titolo(self):
        return self.__titolare

    # Setter: modifica il titolare se il nuovo valore è valido
    def set_titolare(self, nuovo_titolare=str):
        # Controlla che sia una stringa e non vuota/spazi
        if isinstance(nuovo_titolare, str) and nuovo_titolare.strip() != "":
            self.__titolare = nuovo_titolare
        else:
            print("Nuovo titolare non valido")


# Nota: i metodi getter/setter dovrebbero fare solo una cosa e senza effetti collaterali
# come stampa o calcoli aggiuntivi, per rispettare il principio di "metodo puro".

print()


# Creazione di un conto bancario
conto = ContoBancario("Mario Rossi", 500)
#Stampa il saldo
conto.visualizza_saldo()

# Effettua un deposito
conto.deposita(200)

# Effettua un prelievo
conto.preleva(100)

#Stampa il nuovo saldo
conto.visualizza_saldo()

#Stampa il titolare del conto
print(conto.get_titolo())

#Cambia il nome del titolare
conto.set_titolare("Paperino")

#Stampa il nuovo titolare del conto
print(conto.get_titolo())




#=====================================
# ESERCIZIO INCAPSULAMENTO
#=====================================

print("#################################################")
print("             ESERCIZIO   STUDENTI              ")
print("#################################################")


# -----------------------------------------------------------
# CLASSE PERSONA (CLASSE BASE)
# Incapsula nome ed età come attributi privati.
# Offre getter e setter e un metodo di presentazione.
# -----------------------------------------------------------

class Persona:
    def __init__(self, nome: str, eta: int):
        self.__nome = nome      # attributo privato
        self.__eta = eta        # attributo privato

    # Getter
    def get_nome(self):
        return self.__nome

    def get_eta(self):
        return self.__eta

    # Setter
    def set_nome(self, nuovo_nome):
        if isinstance(nuovo_nome, str) and nuovo_nome.strip() != "":
            self.__nome = nuovo_nome
        else:
            print("Nome non valido")

    def set_eta(self, nuova_eta):
        if isinstance(nuova_eta, int) and nuova_eta >= 0:
            self.__eta = nuova_eta
        else:
            print("Età non valida")

    # Metodo
    def presentazione(self):
        print(f"Nome: {self.__nome}, Età: {self.__eta}")


# -----------------------------------------------------------
# CLASSE STUDENTE (SOTTOCLASSE DI PERSONA)
# Aggiunge un attributo privato: lista di voti.
# Override del metodo presentazione.
# Metodo per calcolare la media dei voti.
# -----------------------------------------------------------

class Studente(Persona):
    def __init__(self, nome: str, eta: int, voti: list[int]):
        super().__init__(nome, eta)
        self.__voti = voti  # attributo privato

    def calcola_media(self):
        # Gestiamo il caso lista vuota per evitare errori
        if len(self.__voti) == 0:
            return 0
        return sum(self.__voti) / len(self.__voti)

    def presentazione(self):
        super().presentazione()   # richiamo la versione della classe padre
        print("Voti:", self.__voti)
        print(f"Media voti: {self.calcola_media():.2f}")


# -----------------------------------------------------------
# CLASSE PROFESSORE (SOTTOCLASSE DI PERSONA)
# Aggiunge la materia insegnata.
# Override del metodo presentazione.
# -----------------------------------------------------------

class Professore(Persona):
    def __init__(self, nome: str, eta: int, materia: str):
        super().__init__(nome, eta)
        self.__materia = materia

    def presentazione(self):
        super().presentazione()
        print("Insegnante di:", self.__materia)


# -----------------------------------------------------------
# ESEMPIO D'USO
# -----------------------------------------------------------

print("\n--- Esempio Studente ---")
stud = Studente("Marco", 20, [28, 30, 25, 27])
stud.presentazione()

print("\n--- Esempio Professore ---")
prof = Professore("Rossi", 50, "Matematica")
prof.presentazione()

    
###########################################
###########################################
#Soluzione di Mario Roggi
#Interessante come ritorna la presentazione
#Questo è il motivo per cui la sto aggiungendo


class Persona:
    def __init__(self, nome: str, eta: int):
        # attributi "privati" con name mangling
        self.__nome = nome
        self.__eta = eta
        
    def presentazione(self):
        # ritorna una frase base con nome ed età
        return f"{self.__nome} ha {self.__eta} anni."
        
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_eta(self):
        return self.__eta      
    
    def set_eta(self, eta):
        self.__eta = eta
        
class Studente(Persona):
    def __init__(self, nome: str, eta: int, voti: list[float]):
        super().__init__(nome, eta)
        # attributo pubblico per semplicità; contiene la lista dei voti
        self.voti = voti

    def __calcola_media(self):
        # protezione contro divisione per zero se la lista dei voti è vuota
        if not self.voti:
            return 0.0
        return sum(self.voti) / len(self.voti)
        
    def presentazione(self):
        # riusa la presentazione base e aggiunge la media
        base = super().presentazione()
        media = self.__calcola_media()
        # formatta la media con 2 decimali
        return f"Lo studente {base} La sua media è: {media:.2f}."
        
class Professore(Persona):
    def __init__(self, nome: str, eta: int, materia: str):
        super().__init__(nome, eta)
        # materia insegnata dal professore
        self.materia = materia
        
    def presentazione(self):
        base = super().presentazione()
        # aggiunge la materia alla frase base
        return f"Il professore {base} Insegna {self.materia}."
        

