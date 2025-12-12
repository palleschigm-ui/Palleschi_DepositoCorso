import sqlite3
import os

# Nome del file database
db_filename = 'libreria_esempio.db'

# Rimuovo il file se esiste già per avere un ambiente pulito ad ogni esecuzione
if os.path.exists(db_filename):
    os.remove(db_filename)

# 1. CREAZIONE E CONNESSIONE
# Se il file non esiste, viene creato. Se esiste, viene aperto.
print(f"--- Connessione a {db_filename} ---")
conn = sqlite3.connect(db_filename)

# 2. CREAZIONE DEL CURSORE
# Il cursore è il "braccio operativo" della connessione
cursor = conn.cursor() #Crea il legame tra Python e la tabella

# 3. CREAZIONE TABELLA (DDL)
# Usiamo le triple quotes per scrivere SQL su più righe in modo pulito
sql_create_table = """
CREATE TABLE IF NOT EXISTS libri (
id INTEGER PRIMARY KEY AUTOINCREMENT,
titolo TEXT NOT NULL,
autore TEXT NOT NULL,
anno INTEGER,
prezzo REAL
);
"""
#La stringa di cui sopra contiene il codice SQL e lui da solo capisce 
cursor.execute(sql_create_table) #Crea la tabella
print("Tabella 'libri' creata con successo.")

# 4. INSERIMENTO DATI (INSERT) - Metodo Singolo
# NOTA: Uso '?' come placeholder per sicurezza (evita SQL Injection)
sql_insert = "INSERT INTO libri (titolo, autore, anno, prezzo) VALUES (?, ?, ?, ?)" #Definisci come deve essere la struttura dei dati, notare come non passiamo l'id che viene autogestito
dati_libro = ("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 25.50)

cursor.execute(sql_insert, dati_libro)
print("Inserito un singolo libro.")
conn.commit()

#Si usa SQL piuttosto che CSV perchè:
# possiamo fare collegamenti fra tabelle (ogni tabella è come un oggetto) ha la struttura logica in tabelle. Rispecchia meglio la programmazione a oggetti
#Risparmio spazio perchè evito di riscrivere tutta la stringa ma solo gli indici
#Tecniche di ottimizzazione per ricerca ed inserimento 

# Si usa SQL piuttosto che CSV perché:

# 1. Struttura relazionale: possiamo creare più tabelle collegate tra loro
#    tramite chiavi primarie e chiavi esterne. Ogni tabella rappresenta un oggetto
#    (ad es. libri, autori, editori) e il database rispecchia molto bene la
#    logica della programmazione a oggetti.

# 2. Riduzione della ridondanza: evitiamo di ripetere dati uguali molte volte.
#    In un CSV l'autore "Tolkien" comparirebbe in ogni riga; in SQL lo salviamo
#    una sola volta e i libri lo referenziano tramite un ID. Questo riduce lo
#    spazio occupato e mantiene i dati più coerenti.

# 3. Efficienza nelle ricerche e negli inserimenti:
#    i database usano indici, ottimizzazioni e motori di query che rendono
#    SELECT, UPDATE e INSERT molto più veloci rispetto alla scansione completa
#    di un file CSV.

# 5. INSERIMENTO MULTIPLO (executemany) - Molto più veloce per tanti dati
lista_libri = [
("1984", "George Orwell", 1949, 12.00),
("Il Piccolo Principe", "Antoine de Saint-Exupéry", 1943, 9.50),
("Dune", "Frank Herbert", 1965, 18.90),
("Python Crash Course", "Eric Matthes", 2019, 35.00)
]

cursor.executemany(sql_insert, lista_libri) #Notare come adesso uso executemany
print(f"Inseriti {cursor.rowcount} libri in blocco.")

# 6. SALVATAGGIO (COMMIT)
# Fondamentale! Senza questo, i dati verrebbero persi alla chiusura.
conn.commit()
print("Modifiche committate (salvate) nel DB.")

# 7. LETTURA DATI (SELECT)
print("\n--- Lettura di tutti i libri ---")
cursor.execute("SELECT * FROM libri")

# fetchall() recupera tutte le righe rimanenti come una lista di tuple
tutti_i_libri = cursor.fetchall()

for libro in tutti_i_libri:
# libro è una tupla: (id, titolo, autore, anno, prezzo)
    print(f"ID: {libro[0]} | Titolo: {libro[1]} | Prezzo: {libro[4]}€")

# 8. LETTURA FILTRATA E AGGIORNAMENTO (UPDATE)
print("\n--- Aggiornamento Prezzo per Orwell ---")
# Cerchiamo l'ID di 1984
cursor.execute("SELECT id FROM libri WHERE autore = ?", ("George Orwell",))
id_orwell = cursor.fetchone()[0] # fetchone restituisce una singola tupla o None

# 9. CANCELLAZIONE (DELETE)
print("\n--- Cancellazione libri vecchi ---")
cursor.execute("DELETE FROM libri WHERE anno < ?", (1950,))
print(f"Cancellati {cursor.rowcount} libri pubblicati prima del 1950.")
conn.commit()

# 10. CHIUSURA CONNESSIONE
# Rilascia le risorse del file
conn.close()
print("\nConnessione chiusa.")