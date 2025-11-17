class Automobile:
    numero_di_ruote=4
    def __init__(self,marca,modello): #init è il costruttore
        self.marca=marca
        self.modello= modello #init serve solo come placeholder
    def stampa_info(self): #il self è un placeholder per il nome dell'oggetto
        print("L'automobile è una ",self.marca,self.modello)

auto1= Automobile("Fiat","500")
auto2=Automobile("BWC","X3")

auto1.stampa_info()
auto2.stampa_info()

print(auto1)