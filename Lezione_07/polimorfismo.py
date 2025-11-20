#==============================
#         POLIMORFISMO
#==============================

#Terza regola fondamentale
#Utilizzata per cambiare forma e/o comportamento di un elemento senza cambiare l'elemento stesso
#In Python, il polimorfismo si manifesta principalmente attraverso l'overriding (sovrascrittura) dei metodi

#==============================
# Overrriding dei Metodi
#==============================

#L'overriding dei metodi avviene quando una sottoclasse fornisce una specifica
#implementazione di un metodo che è già definito nella sua superclasse. 
#Questo permette di specializzare il comportamento di un metodo in base alla
#sottoclasse che lo implementa.

print("--------------------------------------------")

class Animale:
    def emetti_suono(self):
        print("Questo animale fa un suono")

class Cane(Animale):
    def emetti_suono(self):
        print("Bau")

class Gatto(Animale):
    def emetti_suono(self):
        print("Miao")

fido=Cane()
fido.emetti_suono()


#Simulazione dell'Overloading

class Stampa:
    def mostra(self,a=None,b=None):
        if a is not None and b is not None:
            print(a+b)
        elif a is not None:
            print(a)
        else:
            print("Niente da mostrare")



#==============================
# Polimorfismo Passivo e Duck Typing
#==============================
#Il polimorfismo passivo è una forma di polimorfismo in cui il comportamento di un oggetto è determinato dai metodi che possiede, 
# non dalla sua appartenenza a un tipo o a una gerarchia di classi.

#In altre parole, non importa che tipo di oggetto sia, ma solo che sappia fare ciò che gli viene richiesto.

#È definito "passivo" perché:

# 1)non richiede una relazione esplicita tra le classi (come l’ereditarietà);
# 2)il linguaggio non controlla i tipi in modo rigido;
# 3)il programmatore “si fida” che l’oggetto abbia il metodo corretto.
#Il duck typing è un principio che implementa il polimorfismo passivo.

print("--------------------------------------------")

class Cane:
    def parla(self):
        return "Bau!"
class Gatto:
    def parla(self):
        return "Miao!"
def fai_parlare(animale): #Accetta qualsiasi oggetto che possiede un metodo parla()
    #Non importa che tipo di animale sia
    print(animale.parla())

cane=Cane()
gatto=Gatto()

fai_parlare(cane)
fai_parlare(gatto)

#==========================================================
# Polimorfismo Passivo
#==========================================================

# Nel polimorfismo passivo conta cosa un oggetto PUÒ FARE,
# non da quale classe proviene o se esiste ereditarietà.

class Cane:
    def parla(self):
        return "Bau!"

class Gatto:
    def parla(self):
        return "Miao!"

class Robot:
    def parla(self):
        return "Salve, umano."

# Funzione che usa polimorfismo passivo:
# accetta QUALSIASI oggetto che possiede il metodo 'parla'
def fai_parlare(oggetto):
    # Non controlla il tipo dell'oggetto
    print(oggetto.parla())

# Creiamo gli oggetti
c = Cane()
g = Gatto()
r = Robot()

# Funziona per tutti perché hanno lo stesso metodo
fai_parlare(c)
fai_parlare(g)
fai_parlare(r)

#==========================================================
# Duck Typing
#==========================================================

# Il duck typing non richiede che gli oggetti appartengano
# alla stessa classe. Serve solo che abbiano i metodi necessari.

class Anatra:
    def cammina(self):
        return "L'anatra cammina lentamente."

    def verso(self):
        return "Quack!"

class Cane:
    def cammina(self):
        return "Il cane corre veloce."

    def verso(self):
        return "Bau!"

# Funzione che si basa sul duck typing:
# si aspetta solo che l'oggetto abbia cammina() e verso()
def descrivi(oggetto):
    print(oggetto.cammina())
    print(oggetto.verso())

a = Anatra()
c = Cane()

# Funziona per entrambi anche senza relazione tra classi
descrivi(a)
descrivi(c)

#--------------------------------------------
#Altro esempio di Duck typing

class Cerchio:
    def disegna(self):
        print("Disegno un cerchio")

class Rettangolo:
    def disegna(self):
        print("Disegno un rettangolo")

def disegna_figura(figura):
    # Anche qui, basta che 'figura' abbia il metodo 'disegna'
    figura.disegna()

figure = [Cerchio(), Rettangolo()]     # figure[0]=Cerchio() / figure[1]=Rettagolo()


# Iteriamo e disegniamo ogni figura

for figura in figure:

    disegna_figura(figura)

######################################################
######################################################

#La funzione len() è un esempio eclatante di polimorfismo



#    Cosa significa __name__=="__main__"?
#Controllo che viene effettuato per capire se un elemento è stato importato oppure no
#Creo una funzione def main()
# if __name__=="__main__":
#      main()
#Evita problematica funzionale quando un elemento viene richiamato in un posto in cui non è congruo che funzioni
#Difesa dagli errori di import