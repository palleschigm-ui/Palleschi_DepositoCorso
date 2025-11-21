#=======================================================
#             IL CONCETTO DELL'ASTRAZIONE
#=======================================================

#Il concetto dell'astrazione ha molte implicazione teoriche
#L' astrazione è la capacità di dividere le parti utili al contesto esecutivo da quelle utile al contesto logico

#Abbiamo uno zoo, arriva un animale e dobbiamo registrarlo
#Non lo registreremo mai come un animale generico, ma come animale specifico
#Sarà sicuramente un Animale (nel senso di classe padre) ma poi lo chiameremo Tigre (ad esempio)

#L'unica applicazione pratica dell'astrazione è nelle classi e metodi astratte
#Il metodo astratto è un metodo che nel padre può essere lasciato con il pass
#Stiamo dicendo che chiunque sia figlio di quel padre, deve sovrascrivere quel metodo
#Stiamo forzando il polimorfismo
#Le classi astratte non posso istanziare oggetti da loro stesse
#Le classi astratte possono avere anche attributi e metodi reali, ma non può essere istanziata

#Concettualmente stiamo dicendo: idealmente un figlio di questa classe dovrebbe essere in grado di fare questo

#Creo una cosa non istanziabile, obbligo l'utente a lavorare con tutte e 3 le regole fondamentali
#Forzo il polimorfismo, tramite l'ereditarietà con l'incapsulamento
from abc import ABC, abstractmethod 

class Animale(ABC):
    @abstractmethod
    def muovi(self):
        pass

class Cane(Animale):
    def muovi(self):
        print("Corro")

class Pesce(Animale):
    def muovi(self):
        print("Nuovo")

#Abbiamo una classe padre, che ha il metodo "muovi", ma tanto ogni figlio poi avrà un suo metodo, non andremo mai 
#a definire un animale come animale generico, ma lo classificheremo sempre come un animale specifico (e avrà il suo metodo specifico)
#Il padre ci sta solo dando la forma.
#Immagianimamo il caso class AnimaleGenerico e abbiamo il metodo parla, ogni poi specie di animale avrà il suo metodo specifico, per un
#cane avremo abbaia e per un gatto miagola. Non salveremo mai un cane che arriva al canile come AnimaleGenerico con il metodo parla : print("fa suono generico")
#ma lo salveremo nella classe Cane con il metodo parla print("Bau bau")



#Un elemento chiave delle classi astratte è l'uso del decoratore @abstractmethod



#=====================================
# Esercizio sull'astrazione
#=====================================

class Impiegato(ABC):
    def __init__(self,nome:str,cognome:str,stipendio:int):
        super().__init__()
        self.nome=nome
        self.cognome=cognome
        self.stipendio=stipendio

    @abstractmethod
    def calcola_stipendio(self):
        pass


class Operaio(Impiegato):
    @abstractmethod
    def partita_iva(self):
        pass


class Idraulico(Operaio):
    def calcola_stipendio(self):
        return self.stipendio

    def partita_iva(self):
        return True
    

class ImpiegatoFisso(Impiegato):
    def calcola_stipendio(self):
        return self.stipendio


class ImpiegatoAProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio, vendite:int):
        super().__init__(nome, cognome, stipendio)
        self.vendite=vendite

    def calcola_stipendio(self):
        return self.stipendio + 0.05*self.vendite*(self.vendite>=0)


def stampa(impiegato:Impiegato):
    # Base comune per tutti (base è una stringa)
    base = (
        f"Nome: {impiegato.nome}, "
        f"Cognome: {impiegato.cognome}, "
        f"Stipendio: {impiegato.calcola_stipendio()}"
    )

    # Aggiungo la partita IVA solo se è un Idraulico (cioè un Operaio con quel metodo)
    if isinstance(impiegato, Idraulico):
        base += f", Ha partita IVA: {impiegato.partita_iva()}" #concatenazione di stringhe

    return base


mario=ImpiegatoFisso("Mario","Rossi",1500)
luca=ImpiegatoAProvvigione("Luca","Proietti",1800,5000)
luigi=Idraulico("Luigi","Pincopallino",1600)

print(luigi.partita_iva())
print(stampa(mario))
print(stampa(luca))
print(stampa(luigi))







#===================================
# Matrioska di classi astratte
#===================================

# Livello 1: classe astratta base
class Animale(ABC):
    @abstractmethod
    def muovi(self):
        pass


# Livello 2: classe astratta che eredita da un'altra astratta
class Mammifero(Animale):
    @abstractmethod
    def allatta(self):
        pass


# Livello 3: classe astratta ancora più specifica
class Carnivoro(Mammifero):
    @abstractmethod
    def caccia(self):
        pass


# Livello finale: classe concreta
class Leone(Carnivoro):
    def muovi(self):
        return "Il leone cammina"

    def allatta(self):
        return "Le leonesse allattano i cuccioli"

    def caccia(self):
        return "Il leone caccia una preda"
