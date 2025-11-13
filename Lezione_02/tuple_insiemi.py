# Esempi di tuple (tupla = struttura immutabile)
punto = (3, 4)
colore_rgb = (255, 128, 0)
informazioni_persona = ("Alice", 25, "Donna")

# Le tuple funzionano come le liste per quanto riguarda l'accesso agli elementi
print(punto[0])  # Stampa: 3

# punto[0] = 3 --> Questo darebbe errore,
# perché le tuple NON permettono la modifica degli elementi.


# ---------------------------- #
#        ESEMPI DI SET         #
# ---------------------------- #

# Un set è una collezione SENZA duplicati e NON ordinata

set1 = set([1, 2, 3, 4, 5])  # Converto una lista in un insieme
set2 = {1, 2, 3, 4, 5}       # Creo direttamente un insieme con parentesi graffe

# I set eliminano automaticamente i duplicati
set3 = {1, 2, 3, 4, 4, 2, 3, 4, 5, 5, 6}
print(set3)       # Output: {1, 2, 3, 4, 5, 6}
print(len(set3))  # Output: 6 perché i duplicati vengono rimossi


# ---------------------------- #
#    MUTABILITÀ NELLE TUPLE    #
# ---------------------------- #

# Una tupla può contenere anche oggetti MUTABILI, come una lista
t = (1, ["a", "b", "c"], "word")

# Posso accedere alla lista interna
print(t[1][0])   # Stampa: a

# Questa operazione è PERMESSA:
t[1][0] = 99     # Modifico un elemento della lista dentro la tupla

# Perché funziona?
# Perché la tupla è immutabile, MA contiene un oggetto mutabile (una lista).
# La tupla rimane immutabile (i suoi "puntatori" non cambiano)
# ma il contenuto interno della lista può cambiare.

# INVECE questo darebbe errore:
# t[0] = 99  --> ERRORE, la tupla non può cambiare i suoi elementi
