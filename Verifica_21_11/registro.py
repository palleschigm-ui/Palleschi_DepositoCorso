from classi import Dipendente,Visitatore

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
        persona.set_presente(True)
        print(f"{persona._nome} {persona._cognome} è stato/a aggiunto/a al registro.")

    def rimuovi_persona(self, persona):
        """Rimuove la persona in base al badge."""
        for p in self.registro:
            if p.get_badge() == persona.get_badge():
                self.registro.remove(p)
                persona.set_presente(False)
                print(f"{persona._nome} {persona._cognome} è stato/a rimosso/a dal registro.")
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

    

    

    
