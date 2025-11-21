from abc import ABC, abstractmethod 

#Classe astratta VeicoloTrasporto
class VeicoloTrasporto(ABC):
    def __init__(self,targa:str,peso_massimo:int,carico_attuale:int=0):
        super().__init__()
        self._targa=targa
        self._peso_massimo=peso_massimo
        self._carico_attuale=carico_attuale
    @abstractmethod
    def costo_manutenzione(self): #Metodo astratto
        pass
    #Aggiungo peso al veicolo
    def carica(self,peso):
        if self._peso_massimo<self._carico_attuale+peso: #Controllo che non supero la capacità massima
            print("Il peso supera la capacità")
            return None
        else:
            self._carico_attuale+=peso
            return self._carico_attuale
    #Scarico completamente il veicolo 
    def scarica(self):
        print("Stai scaricando il veicolo...")
        self._carico_attuale=0
        return self._carico_attuale
#Classe Camion
class Camion(VeicoloTrasporto):
    def __init__(self, targa, peso_massimo,numero_assi:int, carico_attuale = 0):
        super().__init__(targa, peso_massimo, carico_attuale)
        self.numero_assi=numero_assi
        self.tipo="Camion"
    def costo_manutenzione(self):
        costo=100*self.numero_assi+self._peso_massimo
        return costo
#Classe Furgone
class Furgone(VeicoloTrasporto):
    def __init__(self, targa, peso_massimo,alimentazione:str, carico_attuale = 0):
        super().__init__(targa, peso_massimo, carico_attuale)
        self.alimentazione=alimentazione
        self.tipo="Furgone"
    
    def costo_manutenzione(self):
        return 150*(self.alimentazione=="diesel")+200*(self.alimentazione=="elettrico")
#Classe Motocarro    
class Motocarro(VeicoloTrasporto):
    def __init__(self, targa, peso_massimo,anni_servizio:int, carico_attuale = 0):
        super().__init__(targa, peso_massimo, carico_attuale)
        self.anni_servizio=anni_servizio
        self.tipo="Motocarro"
    def costo_manutenzione(self):
        return 50*self.anni_servizio

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------

#Classe GestoreFlotta
#Gestisce elenco veicoli (oggetti derivati da VeicoloTrasporto)

class GestoreFlotta:
    def __init__(self,veicoli:list[VeicoloTrasporto]):
        self.veicoli=veicoli
#Aggiungo un veicolo
    def aggiungi_veicolo(self,veicolo):
        for v in self.veicoli:
            if v._targa==veicolo._targa:
                print("Veicolo già inserito")
                return
        self.veicoli.append(veicolo)
#Data una targa, rimuovo il veicolo 
    def rimuovi_veicolo(self,targa):
        for v in self.veicoli:
            if v._targa==targa:
                self.veicoli.remove(v)
                return
        
        print("Veicolo non trovato")
#Calcolo il costo totale della manutenzione
    def costo_totale_manutenzione(self):
        costo_totale=0
        for p in self.veicoli:
            costo_totale+=p.costo_manutenzione()
        return costo_totale
    
    def descrizione(self):  #Forse sarebbe stato meglio farlo con __str__
        for p in self.veicoli:
            print(
                f"Targa: {p._targa},"
                f"Tipo: {p.tipo},"
                f"Carico attuale: {p._carico_attuale}"
            )



        



        
        



