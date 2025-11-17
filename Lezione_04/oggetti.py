##############################################################################
class Automobile:
    # Variabile di classe: condivisa da tutte le istanze
    numero_di_ruote = 4

    def __init__(self, marca, modello):
        # __init__ è il costruttore
        # Viene eseguito ogni volta che crei un nuovo oggetto Automobile
        self.marca = marca          # Attributo di istanza
        self.modello = modello      # Attributo di istanza

    def stampa_info(self):
        # Metodo di istanza
        # 'self' rappresenta l'oggetto che richiama questo metodo
        print("L'automobile è una", self.marca, self.modello)

    def __str__(self):
        # Rappresentazione leggibile dell'oggetto quando usi print()
        return f"Automobile({self.marca}, {self.modello})"


# Creiamo due oggetti Automobile (due istanze della classe)
auto1 = Automobile("Fiat", "500")
auto2 = Automobile("BMW", "X3")

# Chiamiamo un metodo di istanza su entrambe le auto
auto1.stampa_info()
auto2.stampa_info()

# Senza __str__, Python mostrerebbe l'indirizzo dell'oggetto in memoria
# Con __str__, otteniamo una rappresentazione leggibile
print(auto1) #Output: <__main__.Automobile object at 0x0000015F98A013A0>
print(auto2)


######################
# Metodo statisca
######################
#Non fa riferimento nè alla classe nè all'oggetto
class Calcolatrice:
    @staticmethod #decoratori specifici di python 
    def somma(a,b):
        return a+b
#Uso del metodo statico senza creare un'istanza
risultato=Calcolatrice.somma(5,3)
print(risultato)

########################
# Metodo decorato
########################


class Contatore:
    numero_istanza = 0  # Attributo di classe

    def __init__(self):
        Contatore.numero_istanza += 1  # Incrementa il contatore ogni volta che si crea un'istanza

    @classmethod
    def mostra_numero_istanze(cls):
        # cls si riferisce alla classe stessa
        print(f"Sono state create {cls.numero_istanza} istanze")

        
#Creazione di alcune istanze 
c1= Contatore() 
c2=Contatore() 
Contatore.mostra_numero_istanze()
