# Classe base Elettrodomestico 
# Rappresenta un generico elettrodomestico con attributi comuni a tutti i modelli

class Elettrodomestico:
    def __init__(self,marca:str,modello:str,anno_acquisto:int,guasto:str):
        # Attributi privati (con doppio underscore)
        self.__marca=marca              # marca dell'elettrodomestico
        self.__modello=modello          # modello dell'elettrodomestico
        self.__anno_acquisto=anno_acquisto  # anno di acquisto
        self.__guasto=guasto            # descrizione del guasto
    
    # --- GETTER ---
    def get_marca(self):
        return self.__marca

    def get_modello(self):
        return self.__modello

    def get_anno_acquisto(self):
        return self.__anno_acquisto

    def get_guasto(self):
        return self.__guasto
    
    # --- SETTER ---
    def set_marca(self,nuova_marca):
        # Cambia la marca solo se è una stringa
        if isinstance(nuova_marca,str):
            self.__marca=nuova_marca

    def set_modello(self,nuovo_modello):
        # Cambia il modello solo se è una stringa
        if isinstance(nuovo_modello,str):
            self.__modello=nuovo_modello

    def set_anno_acquisto(self,nuovo_anno):
        # L'anno deve essere un intero e non può essere nel futuro
        if isinstance(nuovo_anno,int) and nuovo_anno<2026:
            self.__anno_acquisto=nuovo_anno

    def set_guasto(self,nuovo_guasto):
        # Cambia il guasto solo se la descrizione è una stringa
        if isinstance(nuovo_guasto,str):
            self.__guasto=nuovo_guasto

    # Ritorna una descrizione leggibile dell’elettrodomestico
    def descrizione(self):
        return (
            f"Marca: {self.get_marca()}, "
            f"Modello: {self.get_modello()}, "
            f"Anno: {self.get_anno_acquisto()}, "
            f"Guasto: {self.get_guasto()} "
        )

    # Costo base di riparazione generico per ogni elettrodomestico
    def stima_costo_base(self):
        # L'idea è che più l'elettrodomestico è vecchio, più costa la riparazione
        return self.get_anno_acquisto() * (1000/2025)


# --- SOTTOCLASSI ---

class Lavatrice(Elettrodomestico):
    # Aggiunge capacità e giri di centrifuga
    def __init__(self, marca, modello, anno_acquisto, guasto,capacita_kg:int,giri_centrifuga:int):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.capacita_kg=capacita_kg              # capacità di carico
        self.giri_centrifuga=giri_centrifuga      # giri massimi

    # Polimorfismo: sovrascrive il metodo della classe base
    def stima_costo_base(self):
        # alla formula base aggiunge un costo proporzionale alla capacità
        return self.get_anno_acquisto()*(1000/2025) + self.capacita_kg*0.5


class Frigorifero(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto,litri:int,ha_freezer:bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.litri=litri                # capacità in litri
        self.ha_freezer=ha_freezer      # True se ha un freezer separato
    
    def stima_costo_base(self):
        # Aggiunge costo per freezer e per grande capacità
        # ha_freezer e (self.litri > 100) sono bool → si comportano come 1 o 0
        return (
            self.get_anno_acquisto()*(1000/2025)
            + self.ha_freezer*100
            + (self.litri>100)*100
        )
    

class Forno(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto,tipo_alimentazione:str,ha_ventilato:bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.tipo_alimentazione=tipo_alimentazione  # "gas" o "elettrico"
        self.ha_ventilato=ha_ventilato              # True se ha ventilazione

    def stima_costo_base(self):
        # Aggiunge costo se ventilato e se elettrico
        # Sottrae un po' se alimentazione a gas
        tipo = self.tipo_alimentazione.lower()
        return (
            self.get_anno_acquisto()*(1000/2025)
            + self.ha_ventilato*100
            + (tipo=="elettrico")*100
            - (tipo=="gas")*30
        )

