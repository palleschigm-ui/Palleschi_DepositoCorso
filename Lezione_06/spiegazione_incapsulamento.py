# =========================================
# ESEMPI BASE DI CLASSI, COSTRUTTORE E ATTRIBUTI
# =========================================
print("################################")

# 1) Classe con costruttore SENZA parametri
#    L'attributo viene fissato dentro __init__

class ComputerSemplice:
    def __init__(self):
        # Attributo pubblico con valore di default
        self.processore = "Intel i5"


# Uso
pc1 = ComputerSemplice()
print("ComputerSemplice, processore:", pc1.processore)
pc1.processore = "AMD Ryzen 5"  # Lo posso cambiare liberamente
print("ComputerSemplice, processore modificato:", pc1.processore)


# 2) Classe con costruttore CON parametro
#    Il valore dell'attributo viene passato dall'esterno

class ComputerConParametro:
    def __init__(self, processore):
        # Attributo pubblico, imposto dal parametro
        self.processore = processore


# Uso
pc2 = ComputerConParametro("Intel i7")
print("\nComputerConParametro, processore:", pc2.processore)


# =========================================
# ESEMPI DI INCAPSULAMENTO (PRIVATO)
# =========================================

# 3) Incapsulamento con getter e setter "classici"

class ComputerIncapsulato:
    def __init__(self, processore):
        # Attributo privato (name mangling)
        self.__processore = processore

    def get_processore(self):
        return self.__processore

    def set_processore(self, nuovo_processore):
        # Qui potresti fare controlli, es:
        # if not isinstance(nuovo_processore, str):
        #     raise ValueError("Il processore deve essere una stringa")
        self.__processore = nuovo_processore


# Uso
pc3 = ComputerIncapsulato("Intel i9")
print("\nComputerIncapsulato, processore (getter):", pc3.get_processore())
pc3.set_processore("AMD Ryzen 7")
print("ComputerIncapsulato, processore modificato (getter):", pc3.get_processore())


# 4) Incapsulamento "pythonico" con @property

class ComputerProperty:
    def __init__(self, processore):
        # Attributo privato interno
        self.__processore = processore

    @property
    def processore(self):
        # Getter "nascosto"
        return self.__processore

    @processore.setter
    def processore(self, valore):
        # Setter con eventuali controlli
        if not isinstance(valore, str) or valore.strip() == "":
            raise ValueError("Processore non valido")
        self.__processore = valore


# Uso
pc4 = ComputerProperty("Intel i5")
print("\nComputerProperty, processore:", pc4.processore)

pc4.processore = "AMD Ryzen 9"   # Passa dal setter
print("ComputerProperty, processore modificato:", pc4.processore)

# Questa riga genererebbe un errore:
# pc4.processore = ""   # ValueError: Processore non valido

# ============================================================
# NOTE COMPLETE SU __init__, PARAMETRI, ATTRIBUTI E INCAPSULAMENTO
# ============================================================

# ------------------------------------------------------------
# CONCETTO CHIAVE:
# Quando scrivi self.qualcosa = valore
# 1) CREI un attributo dell'oggetto (self.qualcosa)
# 2) gli ASSEGNI un valore (valore)
#
# I nomi dei parametri del costruttore NON devono essere uguali
# ai nomi degli attributi. Puoi fare self.cereale = pane, e va bene.
# ------------------------------------------------------------


# ============================================================
# 1) ESEMPIO: Parametro e attributo con NOMI DIVERSI
# ------------------------------------------------------------
# ✔ È assolutamente valido
# ✔ Il parametro "pane" è una variabile locale del costruttore
# ✔ L'attributo "self.cereale" è il dato dell'oggetto
# ✔ Python non richiede che abbiano lo stesso nome
# ============================================================
print("################################")

class Panificio:
    def __init__(self, pane):
        # 'pane' è il parametro (variabile della funzione)
        # 'self.cereale' è l'attributo dell'oggetto
        self.cereale = pane


# Uso
p1 = Panificio("grano duro")
print("Valore attributo cereale:", p1.cereale)
# Output atteso: grano duro


# ============================================================
# 2) ESEMPIO: Parametro e attributo con lo STESSO NOME
# ------------------------------------------------------------
# ✔ Anche questo è corretto
# ✔ È semplicemente più chiaro e leggibile
# ✔ NON è obbligatorio
# ============================================================

class PanificioChiaro:
    def __init__(self, cereale):
        # Parametro e attributo hanno lo stesso nome
        self.cereale = cereale


# Uso
p2 = PanificioChiaro("segale")
print("Valore attributo cereale:", p2.cereale)
# Output atteso: segale


# ============================================================
# 3) DIMOSTRAZIONE DEL FUNZIONAMENTO DI self.qualcosa = valore
# ------------------------------------------------------------
# ✔ self.qualcosa crea un attributo dell'oggetto
# ✔ valore viene assegnato all'attributo
# ------------------------------------------------------------
# NESSUN obbligo sui nomi!
# ============================================================

class EsempioAttributi:
    def __init__(self, x):
        # Creo un attributo chiamato 'numero'
        self.numero = x

        # Creo un attributo chiamato 'descrizione'
        self.descrizione = "Attributo creato dentro __init__"


# Uso
e = EsempioAttributi(42)
print("e.numero =", e.numero)
print("e.descrizione =", e.descrizione)
# Output:
# e.numero = 42
# e.descrizione = Attributo creato dentro __init__


# ============================================================
# SPIEGAZIONI PRINCIPALI (RIASSUNTO)
# ------------------------------------------------------------
# ✔ self.qualcosa = valore
#    → crea un attributo dell'oggetto e gli assegna un valore
#
# ✔ I nomi del parametro e dell’attributo POSSONO essere diversi
#    → def __init__(self, pane): self.cereale = pane  (corretto)
#
# ✔ Se i nomi coincidono è solo più chiaro
#    → def __init__(self, cereale): self.cereale = cereale
#
# ✔ Il parametro del costruttore NON rappresenta l'attributo
#    ma solo il valore che vuoi assegnare.
#    L'attributo vero è quello con self.
#
# ✔ __init__ può avere:
#    - zero parametri extra
#    - uno
#    - molti
#    - parametri opzionali
#
# ✔ L'importante è che dentro il costruttore tu decida quali
#    attributi avrà l'oggetto (self.qualcosa).
#
# ------------------------------------------------------------
# FINE
# ============================================================

# ============================================================
# TABELLA: Differenza tra self.qualcosa / self._qualcosa / self.__qualcosa
# ============================================================
#
# | Scrittura         | Tipo                   | Accessibilità                    | Comportamento                 |
# | ----------------- | ---------------------- | -------------------------------- | ----------------------------- |
# | self.qualcosa     | pubblico               | accessibile da fuori             | normale uso                   |
# | self._qualcosa    | protetto (convenzione) | accessibile ma “non toccare”     | avviso ai programmatori       |
# | self.__qualcosa   | privato                | non accessibile direttamente     | attiva name mangling          |
#
# ============================================================
# ESEMPI IN PYTHON
# ============================================================
print("################################")

class Esempio:
    def __init__(self):
        # Attributo pubblico: tutti lo possono leggere e modificare
        self.pubblico = "Sono pubblico"

        # Attributo protetto: si può usare, ma la convenzione dice
        # "non modificarlo dall'esterno"
        self._protetto = "Sono protetto (convenzione)"

        # Attributo privato: Python applica name mangling
        # e lo trasforma in _Esempio__privato
        self.__privato = "Sono privato"


# Creazione oggetto
obj = Esempio()

print("\n--- ACCESSO AGLI ATTRIBUTI ---")

# 1) Accesso a un attributo pubblico
print("Pubblico:", obj.pubblico)  # ✔ OK

# 2) Accesso a un attributo protetto
print("Protetto:", obj._protetto)  # ✔ OK ma sconsigliato

# 3) Accesso a un attributo privato
try:
    print("Privato:", obj.__privato)  # ❌ ERRORE: non accessibile direttamente
except AttributeError:
    print("Privato: ERRORE (attribute non accessibile direttamente)")

# 4) Accesso all’attributo privato tramite name mangling
print("Privato (name mangling):", obj._Esempio__privato)  # ✔ Funziona ma SCONSIGLIATO

# ============================================================
# FINE
# ============================================================