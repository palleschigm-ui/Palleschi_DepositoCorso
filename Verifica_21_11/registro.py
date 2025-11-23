from classi import Dipendente, Visitatore


# Registro che contiente non solo chi è presente ma anche chi è assente
# Essere nel registro non significa essere presenti
# Significa solo che è stato registrato
class RegistroAccessi:
    def __init__(self, registro: list[Dipendente | Visitatore] = None):
        self.registro = registro if registro is not None else []
    
    def aggiungi_persona(self, persona):
        """Aggiunge una persona se il suo badge non è già presente."""
        for p in self.registro:
            if p.get_badge() == persona.get_badge():
                print("Errore: badge già presente nel registro.")
                return
        
        self.registro.append(persona)
        print(f"{persona._nome} {persona._cognome} è stato/a aggiunto/a al registro.")

    def rimuovi_persona(self, id_badge):
        """Rimuove la persona in base al badge."""
        for p in self.registro:
            if p.get_badge() == id_badge:
                self.registro.remove(p)
                print(f"{p._nome} {p._cognome} è stato/a rimosso/a dal registro.")
                return
        
        print("Errore: badge non trovato nel registro.")

    def presenze(self):
        presenti = []
        for d in self.registro:
            if d.get_presente():
                presenti.append([d._nome, d._cognome, d.get_badge(), "Presente"])
                print(f"{d._nome} {d._cognome} con id_badge: {d.get_badge()} è attualmente presente")

        if not presenti:
            print("Nessuno è presente")
            return None
        return presenti
    
    def assenti(self):
        assenti = []
        for p in self.registro:
            if not p.get_presente():
                assenti.append(p)
                print(f"{p._nome} {p._cognome} con id_badge {p.get_badge()} non è attualmente presente")
        
        if not assenti:
            print("Non ci sono assenti")
            return None
        
        return assenti
    
    def registra_entrata(self, id_badge):
        for d in self.registro:
            if id_badge == d.get_badge():
                d.ingresso()
                return
        print(f"{id_badge} non presente nel registro")
        return 
    
    def registra_uscita(self, id_badge):
        for d in self.registro:
            if id_badge == d.get_badge():
                d.uscita()
                return
        print(f"{id_badge} non presente nel registro")
        return 
    
    def controllo_ad_personam(self,id_badge):
        for d in self.registro:
            if d.get_badge()==id_badge:
                print(d)
                return
        print(f"Id_badge {id_badge} non presente nel registro")
        

    def panoramica(self):
        for d in self.registro:
            print(d)
            print("-------------------------")
    
    def entrati_in_ritardo(self):
        entrati_in_ritardo = []
        for d in self.registro:
            if d.get_entrata_in_ritardo():
                print(f"{d._nome} {d._cognome} con id_badge {d.get_badge()} è entrato in ritardo")
                entrati_in_ritardo.append(d)
        if not entrati_in_ritardo:
            print("Nessuno è entrato in ritardo")
            return None
        return entrati_in_ritardo
    
    def usciti_in_anticipo(self):
        usciti_in_anticipo = []
        for d in self.registro:
            if d.get_uscita_anticipata():
                print(f"{d._nome} {d._cognome} con id_badge {d.get_badge()} è uscito in anticipo")
                usciti_in_anticipo.append(d)
        if not usciti_in_anticipo:
            print("Nessuno è uscito in anticipo")
            return None
        return usciti_in_anticipo



    

    
