class Libro():
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn

    def descrizione(self):
        print(f"-Titolo: {self.titolo} -Autore: {self.autore} -Isbn: {self.isbn}")


class Libreria():
    def __init__(self, catalogo):
        self.catalogo = catalogo
    
    def aggiungi_libro(self):
        titolo = input("Titolo: ")
        autore = input("Autore: ")
        isbn = input("Isbn: ")
        aggiungi = Libro(titolo, autore, isbn)
        self.catalogo.append(aggiungi)
    
    def rimuovi_libro(self):
        isbn_cerca = input("Isbn da rimuovere: ")

        if any(lib.isbn == isbn_cerca for lib in self.catalogo):
            libro_trovato = next(
                (lib for lib in self.catalogo if lib.isbn == isbn_cerca),
                None
            )
            self.catalogo.remove(libro_trovato)
        else:
            print("Libro non trovato")
    
    def cerca_per_titolo(self):
        cerca = input("Titolo del libro da cercare: ")

        libro_trovato = next(
            (lib for lib in self.catalogo if lib.titolo == cerca),
            None
        )

        if libro_trovato:
            libro_trovato.descrizione()
        else:
            print("Titolo non in libreria")
    
    def mostra_catalogo(self):
        for lib in self.catalogo:
            lib.descrizione()




################################################################
################################################################
# CODICE ERRATO COMMENTATO CON ERRORI FATTI
################################################################
################################################################

if False:
    class libro():
         def __init__(self,titolo,autore,isbn):
            self.titolo=titolo
            self.autore=autore
            self.isbn=isbn
         def descrizione(self):
            print(f"-Titolo: {self.titolo} -Autore: {self.autore} -Isbn: {self.isbn}")

    class libreria():
         def __init__(self,catalogo):
            self.catalogo=catalogo
        
         def aggiungi_libro(self):
            titolo=input("Titolo: ")
            autore=input("Autore: ")
            isbn=input("Isbn: ")
            aggiungi=libro(titolo,autore,isbn)
            self.catalogo.append(aggiungi)
        
         def rimuovi_libro(self):
            isbn_cerca=input("Isbn da rimuovere: ")

            # ✔️ QUESTA PARTE È CORRETTA NELLA TUA VERSIONE:

            if any(libro.isbn==isbn_cerca for libro in self.catalogo):
                libro_trovato=next(lib for lib in self.catalogo if lib.isbn==isbn_cerca)
                # ❌ ERRORE 1 – qui non usi un valore di default:
                #    se nessun libro rispetta la condizione, next() genera StopIteration
                #    meglio usare next(generator, None)

                self.catalogo.remove(libro_trovato)
            else:
                print("Libro non trovato")
        
         def cerca_per_titolo(self):
            cerca=input("Titolo del libro da cercare: ")

            # ❌ ERRORE 2 – 'cerca' è una stringa, self.catalogo è una lista DI OGGETTI
            #    quindi 'cerca in self.catalogo' sarà sempre False
            if cerca in self.catalogo:
                # ❌ ERRORE 3 – 'libro' è il nome della CLASSE, non dell'istanza
                #    libro.descrizione(cerca) NON HA SENSO: descrizione accetta self, non una stringa
                libro.descrizione(cerca)
            else:
                print("Titolo non in libreria")
        
         def mostra_catalogo(self):
            for lib in self.catalogo:
                # ❌ ERRORE 4 – di nuovo usi 'libro.descrizione' ma 'libro' è la classe
                #    devi chiamarlo sull'istanza: lib.descrizione()
                libro.descrizione(lib)
