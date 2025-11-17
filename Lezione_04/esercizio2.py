##################################################################################################################
class libro:
    def __init__(self,titolo,autore,pagine):
        self.titolo=titolo
        self.autore=autore
        self.pagine=pagine

    def descrizione(self):
        print(f"Il libro {self.titolo} è stato scritto da {self.autore} ed ha {self.pagine} pagine")
    


libro1=libro("Papà","Pirandello",300)
libro1.descrizione()
print(libro1)

#################################################################################################################
class biblioteca:
    def __init__(self,libri):
        self.libri=libri
    
    def crea_libro(self):
        while True:
            scelta=input("Vuoi aggiungere un libro alla biblioteca: (s/n)")
            if scelta=="s":
                titolo=input("Titolo: ")
                self.libri.append(titolo)
            else: break
    
    def stampa(self):
        print(self.libri)

alessandria=biblioteca([])
alessandria.crea_libro()
print(alessandria.__dict__)
print("asdfghjkl")
alessandria.stampa()
