import classi_elettrodomestici   # Importa il modulo che contiene Elettrodomestico e le sue sottoclassi

class TicketRiparazione:
    def __init__(self,id_ticket:int|str,elettrodomestico:classi_elettrodomestici.Elettrodomestico,stato:str,note:list[str]=None):
        # id del ticket: può essere int o stringa
        self.__id_ticket=id_ticket
        
        # oggetto Elettrodomestico associato al ticket
        self.__elettrodomestico=elettrodomestico
        
        # stato del ticket ("aperto", "in lavorazione", "chiuso")
        self.__stato=stato
        
        # note del ticket: lista di stringhe; di default None
        # (sarà gestito come lista altrove)
        self.__note=note
    
    def get_stato(self):
        # Restituisce lo stato corrente del ticket
        return self.__stato

    def get_note(self):
        # Restituisce la lista delle note
        return self.__note

    def set_stato(self,nuovo_stato):
        # Cambia lo stato solo se è tra quelli validi
        if nuovo_stato.lower()=="aperto" or nuovo_stato.lower()=="in lavorazione" or nuovo_stato.lower()=="chiuso":
            self.__stato=nuovo_stato
        else:
            pass   # Stato non valido → non fa nulla

    def set_note(self,nuova_note):
        # Imposta l'intera lista delle note solo se è una lista di stringhe
        if isinstance(nuova_note, list) and all(isinstance(n, str) for n in nuova_note):
            self.__note=nuova_note

    def aggiungi_nota(self):
        # Chiede all'utente una nuova nota e la aggiunge alla lista
        print("Inserire la nuova nota: ")
        nuova_nota=input(">")
        self.get_note().append(nuova_nota)

    def calcola_preventivo(self, *voci_extra):
        # Calcola il preventivo:
        # costo base dell'elettrodomestico + somma delle voci extra passate come argomenti
        return self.__elettrodomestico.stima_costo_base()+sum(voci_extra)




    
        