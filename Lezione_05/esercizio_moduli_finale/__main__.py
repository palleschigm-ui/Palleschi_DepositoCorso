from libreria import Libro, Libreria


# Creo alcuni libri di esempio
libro1 = Libro("Il Signore degli Anelli", "Tolkien", "111")
libro2 = Libro("1984", "Orwell", "222")
libro3 = Libro("I Promessi Sposi", "Manzoni", "333")

# Creo la libreria con un catalogo iniziale
lib = Libreria([libro1, libro2, libro3])

print("\n---- TEST MOSTRA CATALOGO ----")
lib.mostra_catalogo()
lib.aggiungi_libro()
lib.cerca_per_titolo()
lib.mostra_catalogo()



