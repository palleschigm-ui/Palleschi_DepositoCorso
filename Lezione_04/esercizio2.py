class libro:
    def __init__(self,titolo,autore,pagine):
        self.titolo=titolo
        self.autore=autore
        self.pagine=pagine

    def descrizione(self):
        print(f"Il libro {self.titolo} è stato scritto da {self.autore} ed ha {self.pagine} pagine")
    
    #In Python, __str__ è un metodo speciale (detto anche dunder method, da double underscore) 
    #che serve a definire come deve essere rappresentato un oggetto quando viene convertito in stringa.
    def __str__(self):
        return f"punto({self.x}, {self.y})"

libro1=libro("Papà","Pirandello",300)
libro1.descrizione()
print(libro1)
        