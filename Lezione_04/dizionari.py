#==========================
# Esempi dizionari
#==========================
#Nota bene: le chiavi possono essere immutabili, mentre i valori quello che voglio
studente={
    "eta":20,
    "nome":"Gianmario",
    "sesso":"Maschio"
}

studente["eta"]=21 #Modifica di un valore del dizionario
studente["città"]="Roma" # Creo una nuova chiave

print(studente)

#Abbiamo come per tutto dei metodi specifici per i dizionari
#Ricordo che la presenza delle parentesi graffe di indica che è una funzione
print(studente.keys()) #Lista di tutte le chiavi
print(studente.values()) #Lista di tutti i valori
print(studente.items()) #Tutte le coppie chiave-valore
print(studente.get("sesso")) #Valore associato alla chiave "sesso"


################## Esercizio #################
studente={
    "eta":20,
    "nome":"Gianmario",
    "sesso":"Maschio"
}

#Esempio di come ciclare su un dizionario
for chiave in studente:
    print(chiave, studente[chiave]) #Attenzione i dizionari non sono indicizzati come le liste, qui l'indice è la chiave

#Altro metodo:
for x,y in studente.items():
    print(f"Chiave {x}, Valore {y}")

# I valori possono essere liste
dati = {
    "tipo_di_dato": ["Eta", "Pagamento", "Nome"],   # ← qui serviva una virgola
    "Osservazione 1": [25, "Contanti", "Anna"],
    "Osservazione 2": [30, "Carta", "Marco"]
}

print(dati)

dati = {
    "Osservazione 1": {
        "Eta": 25,
        "Pagamento": "Contanti",
        "Nome": "Anna"
    },
    "Osservazione 2": {
        "Eta": 30,
        "Pagamento": "Carta",
        "Nome": "Marco"
    }
}

print(dati)

import pandas as pd
df = pd.DataFrame(dati).T
print(df)


print(dati["Osservazione 1"]["Nome"])  # Anna
print(dati["Osservazione 2"]["Eta"])   # 30

dati["Osservazione 3"] = {
    "Eta": 41,
    "Pagamento": "Bonifico",
    "Nome": "Luca"
}

for obs, valori in dati.items():
    print(obs, "→", valori)


for obs, valori in dati.items():
    print(obs, end=" | ")
    for campo, valore in valori.items():
        print(f"{campo}: {valore}", end=" | ")
    print()

# Dizionario con osservazioni sulle righe
dati = {
    "Osservazione 1": {"Eta": 25, "Pagamento": "Contanti", "Nome": "Anna"},
    "Osservazione 2": {"Eta": 30, "Pagamento": "Carta", "Nome": "Marco"},
    "Osservazione 3": {"Eta": 41, "Pagamento": "Bonifico", "Nome": "Luca"}
}

def stampa_tabella(dati):
    # Ricava l’elenco dei campi (colonne)
    colonne = list(next(iter(dati.values())).keys())
    
    # Calcola la larghezza massima di ogni colonna
    larghezze = {
        col: max(len(col), max(len(str(dati[obs][col])) for obs in dati))
        for col in colonne
    }
    
    # Calcola larghezza massima dell’etichetta riga
    max_obs_len = max(len(obs) for obs in dati)

    # Stampa intestazione tabella
    print(" " * (max_obs_len + 2), end="")
    for col in colonne:
        print(f"{col:<{larghezze[col] + 2}}", end="")
    print()

    # Stampa righe della tabella
    for obs, valori in dati.items():
        print(f"{obs:<{max_obs_len + 2}}", end="")
        for col in colonne:
            print(f"{str(valori[col]):<{larghezze[col] + 2}}", end="")
        print()


# Chiamata della funzione
stampa_tabella(dati)

# ⚠️ Limite del formato "orientato alle osservazioni":
# In questo formato ogni chiave rappresenta un'osservazione.
# Esempio:
dati_orientati_alle_osservazioni = {
    "Osservazione 1": {"Eta": 25, "Pagamento": "Contanti", "Nome": "Anna"},
    "Osservazione 2": {"Eta": 30, "Pagamento": "Carta", "Nome": "Marco"}
}

# Questo formato è leggibile e comodo per lavorare per riga,
# ma diventa meno pratico quando vuoi operare "per colonna".
# Per esempio:
# - ottenere tutte le età
# - calcolare medie
# - filtrare per valori di una colonna
# richiede di scorrere ogni osservazione manualmente.


# ✔ Formato alternativo consigliato (orientato alle colonne):
# Ogni chiave è una variabile e ogni valore è una lista di osservazioni.
# Questo è molto più simile a un vero dataset (tipo pandas DataFrame).
dati_orientati_alle_colonne = {
    "Eta": [25, 30],                  # Colonna delle età
    "Pagamento": ["Contanti", "Carta"],  # Colonna dei metodi di pagamento
    "Nome": ["Anna", "Marco"]         # Colonna dei nomi
}

# Vantaggi di questo formato:
# - facile ottenere tutte le età: dati_orientati_alle_colonne["Eta"]
# - strutturato come un dataset tabellare
# - adatto per calcoli statistici o filtraggio
# - più semplice da convertire in CSV o DataFrame



