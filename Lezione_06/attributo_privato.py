# ---------------------------------------------------------
# DOMANDA:
# "Se ho una classe con un attributo privato che è una lista,
#   nella classe figlio posso fare un metodo che mi calcola
#   la media di quella lista?"
#
# RISPOSTA:
# NO, non puoi accedere direttamente a un attributo privato
# (cioè definito con doppio underscore __) dalla sottoclasse.
# Python non lo permette.
#
# MA puoi farlo se la classe padre fornisce un metodo getter.
# ---------------------------------------------------------


# ---------------------------------------------------------
# ESEMPIO 1 — ERRORE
# La sottoclasse NON può accedere direttamente a __valori
# ---------------------------------------------------------

class Padre:
    def __init__(self):
        self.__valori = [10, 20, 30]   # attributo PRIVATO


class Figlio(Padre):
    def media(self):
        # ❌ Questo genera errore AttributeError
        # perché __valori è privato e NON accessibile
        return sum(self.__valori) / len(self.__valori)


# ---------------------------------------------------------
# ESEMPIO 2 — SOLUZIONE CORRETTA
# La classe padre offre un getter per la lista privata
# ---------------------------------------------------------

class PadreCorretto:
    def __init__(self):
        self.__valori = [10, 20, 30]   # attributo privato

    # ✔️ Getter che permette alle sottoclassi di leggere la lista
    def get_valori(self):
        return self.__valori


class FiglioCorretto(PadreCorretto):
    def media(self):
        valori = self.get_valori()     # ✔️ Accesso corretto tramite getter
        return sum(valori) / len(valori)


# ---------------------------------------------------------
# ESECUZIONE E DIMOSTRAZIONE
# ---------------------------------------------------------

print("ESEMPIO CORRETTO:")
f = FiglioCorretto()
print("La media è:", f.media())
