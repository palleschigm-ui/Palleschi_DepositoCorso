#Sistema ripetibile che simula un teatro

#Classe base: posto
class Posto:
    def __init__(self,numero:int,fila:str,occupato:bool=False):
        self._numero=numero
        self._fila=fila
        self._occupato=occupato
    
    def prenota(self):
        if not self._occupato:
            print("Hai prenotato il posto")
            self._occupato=True
        else:
            print("Il posto è già occupato")

    def libera(self):
        if self._occupato:
            print("Hai liberato il posto")
            self._occupato=False
        else:
            print("Il posto era già libero")
    def get_numero(self):
        return self._numero
    def get_fila(self):
        return self._fila
    def get_occupato(self):
        return self._occupato

class PostoVip(Posto):
    def __init__(self, numero, fila, occupato = False,servizi_extra:str=None):
        super().__init__(numero, fila, occupato)
        self.servizi_extra=servizi_extra
    def prenota(self):
        super().prenota()
        print("Servizio extra? (s/n)")
        scelta=input().lower()
        if scelta=="n":
            pass
        else:
            print("Scegliere extra:")
            print("1) Accesso al lounge")
            print("2)Servizio in posto")
            scelta=int(input)
            while True:
                if scelta==1:
                    self.servizi_extra="Accesso al lounge"
                    break
                elif scelta==2:
                    self.servizi_extra="Servizio in posto"
                    break
                else:
                    print("Scelta non valida, riprovare.")
                    scelta=int(input())
class PostoStandard(Posto):
    def __init__(self, numero, fila,costo:float, occupato = False):
        super().__init__(numero, fila, occupato)
        self.costo=costo


