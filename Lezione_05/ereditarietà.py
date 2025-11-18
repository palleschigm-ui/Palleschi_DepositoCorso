#Esempi di classe ( ereditarietà)
#Ricordo che un padre può avere infiniti figli
#Ricordo che anche un figlio può avere infiniti padri
#=======================================
# Ereditarietà
#=======================================
#Classe animale

class Animale:
    def __init__(self,nome): #Questo metodo è detto il costruttore
        self.nome=nome
    
    def parla(self):
        print(f"{self.nome} fa suono generico")

#Classe derivata (eredita da Animale)
class Cane(Animale): #Qui non aggiungiamo super() perchè non stiamo aggiungendo nulla
    def parla(self):
        print(f"{self.nome} abbaia!")

animale_generico=Animale("AnimaleGenerico")
cane=Cane("Fido")

animale_generico.parla()
cane.parla()


#==============================================
# Ereditarietà multipla
#==============================================
print("#################################################################################")
print("                        NUOVO ESERCIZIO/ESEMPIO                                                     ")
print("#################################################################################")


class Veicolo:
    def __init__(self,marca,modello):
        self.marca=marca
        self.modello=modello
    
    def mostra_informazioni(self):
        print(f"Veicolo marca {self.marca},modello {self.modello}")

class DotazioniSpeciali:
    def __init__(self,dotazioni):
        self.dotazioni=dotazioni

    def mostra_dotazioni(self):
        print(f"Dotazioni speciali:{','.join(self.dotazioni)}")

#Ogni padre dà ai suoi figli il suo tipo ed i suoi metodi ed attributi
#Ogni classe figlio è sia una classe figlio che una classe padre
#Nell'esempio di prima, la classe cane è sia classe cane che classe Animale

class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello,dotazioni,cavalli): #Non abbiamo sovrascritto ma abbiamo fatto una unione
        super().__init__(marca, modello)
        DotazioniSpeciali.__init__(self,dotazioni) #Stessa cosa di super()
        self.cavalli=cavalli
    def mostra_informazioni(self):
        #Alla riga successiva uso super perchè l'abbiamo sovrascritto, dato che il metodo mostra_informazioni esisteva già nella classe padre
        super().mostra_informazioni() #Abbiamo sovrascritto il metodo della classe padre, se levassi questa riga quando chiamo il figlio è come se il metodo del padre non esistesse qui, quindi in questa riga stiamo dicendo esegui anche quello del padre
        print(f"Potenza: {self.cavalli} CV")
        self.mostra_dotazioni() #Non essendo sovrascritto, abbiamo già questo metodo perchè mio padre me lo ha già fornito
        #Se entrambi le classi avessero il metodo mostra_dotazioni, per far capire quale voglio devo chiamare la classe:
        #DotazioniSpeciali.mostra_dotazioni() 
        #Veicolo.mostra_dotazioni()

#=====================================
#Esercizio Ereditarietà Singola
#=====================================
print("#################################################################################")
print("                        NUOVO ESERCIZIO/ESEMPIO                                                     ")
print("#################################################################################")
#Creare una classe base Animale e diverse classi derivate che rappresentano diversi tipi di animali in uno zoo
#Ogni classe deivata avrà attributi e metodi specifici che riflettono le caratteristiche e comportamenti unici degli animali che rappresentano

class Animale:
    def __init__(self,nome,eta,velocita):
        self.nome=nome
        self.eta=eta
        self.velocita=velocita
    
    def fai_suono(self):
        print(f"{self.nome} fa suono generico")

class Leone(Animale):
    def __init__(self, nome, eta,velocita,peso,razza="leone"):
        super().__init__(nome, eta,velocita)
        self.razza=razza
        self.peso=peso
    
    def caccia(self,preda):
        print("Attenzione il leone sta cacciando...")
        print(f"Il leone {self.nome} sta per attaccare una {preda.razza}, povera {preda.nome}")
        if self.velocita>preda.velocita:
            print("Il leone ha catturato la preda")
        else: print("La preda è scappata")

class Giraffa(Animale):
    def __init__(self, nome, eta,velocita,lunghezza_collo,razza="giraffa"):
        super().__init__(nome, eta,velocita)
        self.lunghezza_collo=lunghezza_collo
        self.razza=razza
    def colazione(self):
        print(f"La giraffa {self.nome} sta facendo colazione")

class Pinguino(Animale):
    def __init__(self, nome, eta, velocita,sposato,razza="pinguino"):
        super().__init__(nome, eta, velocita)
        self.sposato=sposato
        self.razza=razza
    def sei_sposato(self):
        if self.sposato:
            print(f"Il pinguino {self.nome} è sposato")
        else: print(f"Il pinguino {self.nome} non è sposato")
    def che_eta(self):
        print("Il pinguino ha ",self.eta)

leone=Leone("Fifone",30,80,200)
giraffa=Giraffa("Molly",10,50,2)
leone.caccia(giraffa)
leone.fai_suono()
pingu=Pinguino("Paolo",1,25,True)
pingu.sei_sposato()
pingu.che_eta()
giraffa.colazione()
giraffa.velocita=100
leone.caccia(giraffa)


#====================================
# Esercizio Ereditarietà Singola
#====================================
print("#################################################################################")
print("                        NUOVO ESERCIZIO/ESEMPIO                                                     ")
print("#################################################################################")

#Creare una casse base MembroSquadra e diversi classi figlie che rappresentano
#ruoli specifici all'interno della squadra di calcio

class MembroSquadra: #Le iniziali delle classi in maiuscolo
    def __init__(self,nome,eta):
        self.nome=nome
        self.eta=eta

    def descrivi(self):
        print(f"Nome: {self.nome}   Età: {self.eta}")

class Giocatore(MembroSquadra):
    def __init__(self, nome, eta,ruolo,numero_maglia):
        super().__init__(nome, eta)
        self.ruolo=ruolo
        self.numer_maglia=numero_maglia
    
    def gioca_partita(self):
        match self.ruolo:
            case "attaccante":
                print(f"{self.nome} ha appena segnato uno splendido goal!!")
            case "difensore":
                print(f"{self.nome} ha appena commesso un fallo")
            case "portiere":
                print(f"{self.nome} ha appena fatto una parata straordinaria")

class Allenatore(MembroSquadra):
    def __init__(self, nome, eta,anni_di_esperienza):
        super().__init__(nome, eta)
        self.anni_di_esperienza=anni_di_esperienza
    
    def dirige_allenamento(self):
        print(f"{self.nome} grazie ai suoi {self.anni_di_esperienza} anni di esperienza dirige in maniera eccellente l'allenamento")

class Assistente(MembroSquadra):
    def __init__(self, nome, eta,specializzazione):
        super().__init__(nome, eta)
        self.specializzazione=specializzazione

    def supporta_team(self,allenatore):
        print(f"{self.nome} aiuta l'allenatore {allenatore.nome} come {self.specializzazione}")


attaccante=Giocatore("Messi",40,"attaccante",10)
attaccante.gioca_partita()
portiere=Giocatore("Buffon",50,"portiere",1)
portiere.gioca_partita()
lippi=Allenatore("Lippi",70,40)
lippi.descrivi()
lippi.dirige_allenamento()
assistente=Assistente("Francesco Garzano",40,"analista di gioco")
assistente.supporta_team(lippi)
