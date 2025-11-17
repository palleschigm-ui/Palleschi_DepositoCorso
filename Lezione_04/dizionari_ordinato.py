#===========================================================
# ESEMPI SUI DIZIONARI
#===========================================================

# Nota:
# - le CHIAVI di un dizionario devono essere IMMUTABILI (stringhe, numeri, tuple)
# - i VALORI possono essere qualsiasi tipo (stringhe, numeri, liste, dizionari, ecc.)

#-----------------------------------------------------------
# Dizionario semplice
#-----------------------------------------------------------
studente = {
    "eta": 20,
    "nome": "Gianmario",
    "sesso": "Maschio"
}

# Modifica di un valore
studente["eta"] = 21

# Aggiunta di una nuova chiave
studente["città"] = "Roma"

print(studente)


#-----------------------------------------------------------
# Metodi principali dei dizionari
#-----------------------------------------------------------
print(studente.keys())      # Lista delle chiavi
print(studente.values())    # Lista dei valori
print(studente.items())     # Lista coppie (chiave, valore)
print(studente.get("sesso"))  # Valore associato a "sesso"


#===========================================================
# CICLARE SU UN DIZIONARIO
#===========================================================

studente = {
    "eta": 20,
    "nome": "Gianmario",
    "sesso": "Maschio"
}

# Metodo 1: scorrere le chiavi
for chiave in studente:
    print(chiave, studente[chiave])  # Ricorda: la chiave fa da "indice"

# Metodo 2: unpack diretto delle coppie chiave-valore
for x, y in studente.items():
    print(f"Chiave {x}, Valore {y}")


#===========================================================
# ⚠️ FORMATO ORIENTATO ALLE OSSERVAZIONI (righe)
#===========================================================

# I valori possono essere liste
dati = {
    "tipo_di_dato": ["Eta", "Pagamento", "Nome"],
    "Osservazione 1": [25, "Contanti", "Anna"],
    "Osservazione 2": [30, "Carta", "Marco"]
}
print(dati)


#===========================================================
# FORMATO CONSIGLIATO PER OSSERVAZIONI SULLE RIGHE
# Ogni chiave = una osservazione
# Ogni valore = un dizionario (colonna -> valore)
#===========================================================

dati = {
    "Osservazione 1": {"Eta": 25, "Pagamento": "Contanti", "Nome": "Anna"},
    "Osservazione 2": {"Eta": 30, "Pagamento": "Carta",  "Nome": "Marco"}
}

print(dati)


# Convertiamo in DataFrame (solo se pandas è installato)
import pandas as pd
df = pd.DataFrame(dati).T  # .T = trasposta, righe = osservazioni
print(df)


# Accesso ai dati
print(dati["Osservazione 1"]["Nome"])  # Anna
print(dati["Osservazione 2"]["Eta"])   # 30


# Aggiungere una nuova riga
dati["Osservazione 3"] = {
    "Eta": 41,
    "Pagamento": "Bonifico",
    "Nome": "Luca"
}

# Stampa riga per riga
for obs, valori in dati.items():
    print(obs, "→", valori)

# Stampa più leggibile
for obs, valori in dati.items():
    print(obs, end=" | ")
    for campo, valore in valori.items():
        print(f"{campo}: {valore}", end=" | ")
    print()


#===========================================================
# TABELLA ORDINATA STAMPATA A SCHERMO
#===========================================================

# Dizionario delle osservazioni
dati = {
    "Osservazione 1": {"Eta": 25, "Pagamento": "Contanti", "Nome": "Anna"},
    "Osservazione 2": {"Eta": 30, "Pagamento": "Carta", "Nome": "Marco"},
    "Osservazione 3": {"Eta": 41, "Pagamento": "Bonifico", "Nome": "Luca"}
}

def stampa_tabella(dati):
    # Ricava le colonne (nomi dei campi)
    colonne = list(next(iter(dati.values())).keys())
    
    # Calcola la larghezza massima per ogni colonna
    larghezze = {
        col: max(len(col), max(len(str(dati[obs][col])) for obs in dati))
        for col in colonne
    }
    
    # Larghezza massima dell’etichetta riga
    max_obs_len = max(len(obs) for obs in dati)

    # intestazione
    print(" " * (max_obs_len + 2), end="")
    for col in colonne:
        print(f"{col:<{larghezze[col] + 2}}", end="")
    print()

    # righe
    for obs, valori in dati.items():
        print(f"{obs:<{max_obs_len + 2}}", end="")
        for col in colonne:
            print(f"{str(valori[col]):<{larghezze[col] + 2}}", end="")
        print()


# Stampa tabella ordinata
stampa_tabella(dati)

#===========================================================
# DIZIONARI: TIPI DI CHIAVI CONSENTITI
#===========================================================

# In Python le chiavi di un dizionario possono essere:
# - stringhe
# - numeri (int, float)
# - tuple
# - bool
# - None
# In generale: qualsiasi oggetto IMMUTABILE.

#-----------------------------------------------------------
# Esempio con chiavi intere
#-----------------------------------------------------------
d_numeri = {
    1: "uno",
    2: "due",
    3: "tre"
}

print("Dizionario con chiavi intere:", d_numeri)
print("Valore associato alla chiave 1:", d_numeri[1])
print()


#-----------------------------------------------------------
# Esempio con chiavi di tipo misto
#-----------------------------------------------------------
d_misto = {
    1: "Numero intero",
    "nome": "Gianmario",
    3.5: "Numero float",
    True: "Booleano come chiave",
    None: "Valore associato a None"
}

print("Dizionario con chiavi di tipo misto:", d_misto)
print("Valore associato alla chiave 'nome':", d_misto["nome"])
print("Valore associato alla chiave 3.5:", d_misto[3.5])
print("Valore associato alla chiave True:", d_misto[True])
print("Valore associato alla chiave None:", d_misto[None])
print()


#-----------------------------------------------------------
# Le chiavi devono essere UNICHE
#-----------------------------------------------------------
d_duplicato = {
    1: "A",
    1: "B"   # Questa sovrascrive la precedente
}

print("Dizionario con chiavi duplicate (1 definita due volte):", d_duplicato)
# Risultato: {1: 'B'}
print()


#-----------------------------------------------------------
# Esempio di chiavi NON validhe (solo come commento)
#-----------------------------------------------------------
# Le liste NON possono essere chiavi, perché sono mutabili
# Questo darebbe errore TypeError:
#
# d_non_valido = {
#     [1, 2, 3]: "lista come chiave"  # ❌ NON CONSENTITO
# }
#
# I dizionari e i set non possono essere usati come chiavi per lo stesso motivo.

#===========================================================
# Piccolo esempio pratico: usare interi come ID
#===========================================================

studenti = {
    1: {"nome": "Anna", "eta": 21},
    2: {"nome": "Marco", "eta": 23},
    3: {"nome": "Luca", "eta": 20}
}

print("Dizionario studenti indicizzati con ID interi:")
for id_studente, info in studenti.items():
    print(f"ID {id_studente} -> Nome: {info['nome']}, Età: {info['eta']}")


#===========================================================
# 1. Metodo .pop() → rimuove una chiave e ne restituisce il valore
#===========================================================
d = {"a": 1, "b": 2, "c": 3}

val = d.pop("b")       # rimuove "b" e restituisce 2
print(d)               # {'a': 1, 'c': 3}
print(val)             # 2


#===========================================================
# 2. Metodo .popitem() → rimuove l'ULTIMA coppia inserita
#   (utile per strutture tipo stack)
#===========================================================
d = {"x": 10, "y": 20, "z": 30}
item = d.popitem()
print(item)            # ('z', 30)
print(d)               # {'x': 10, 'y': 20}


#===========================================================
# 3. Metodo .update() → unisce/aggiorna due dizionari
#===========================================================
d1 = {"a": 1, "b": 2}
d2 = {"b": 200, "c": 3}

d1.update(d2)
print(d1)              # {'a': 1, 'b': 200, 'c': 3}


#===========================================================
# 4. Metodo .setdefault() → come get(), ma crea la chiave se non esiste
#===========================================================
d = {"nome": "Anna"}

val = d.setdefault("eta", 25)
print(val)             # 25
print(d)               # {'nome': 'Anna', 'eta': 25}

# Se la chiave esiste NON la tocca
d.setdefault("nome", "Marco")
print(d)               # {'nome': 'Anna', 'eta': 25}


#===========================================================
# 5. Dictionary comprehension → costruire dizionari in una riga
#===========================================================
quadrati = {x: x*x for x in range(5)}
print(quadrati)        # {0:0, 1:1, 2:4, 3:9, 4:16}


#===========================================================
# 6. Ordinare un dizionario
#===========================================================

d = {"c": 3, "a": 1, "b": 2}

# Ordine per chiavi
ordinato_chiavi = dict(sorted(d.items()))
print(ordinato_chiavi)  # {'a': 1, 'b': 2, 'c': 3}

# Ordine per valori
ordinato_valori = dict(sorted(d.items(), key=lambda x: x[1]))
print(ordinato_valori)  # {'a': 1, 'b': 2, 'c': 3}


#===========================================================
# 7. Copia corretta: copy() evita problemi con alias e riferimenti
#===========================================================
d1 = {"a": 1, "b": [1, 2, 3]}
d2 = d1.copy()   # copia Shallow

d2["b"].append(4)
print(d1)        # {'a':1,'b':[1,2,3,4]}  ← attenzione!

# Per evitare il problema:
import copy
d3 = copy.deepcopy(d1)
d3["b"].append(5)
print(d1)        # {'a':1,'b':[1,2,3,4]}
print(d3)        # {'a':1,'b':[1,2,3,4,5]}


#===========================================================
# 8. Verificare presenza di una chiave
#===========================================================
d = {"nome": "Anna"}

print("nome" in d)    # True
print("eta" in d)     # False


#===========================================================
# 9. Creare un dizionario da liste con zip()
#===========================================================
chiavi = ["nome", "eta", "città"]
valori = ["Gianmario", 23, "Roma"]

d = dict(zip(chiavi, valori))
print(d)
# {'nome': 'Gianmario', 'eta': 23, 'città': 'Roma'}


#===========================================================
# 10. Dizionari annidati (nested dict): molto usati
#===========================================================
rubrica = {
    "Anna": {"telefono": "12345", "email": "anna@mail.com"},
    "Marco": {"telefono": "54321", "email": "marco@mail.com"}
}

print(rubrica["Anna"]["telefono"])  # 12345

# In Python i dizionari sono implementati come **hashmap**.
# Questo significa che:
# - ogni chiave viene trasformata in un "hash" (numero calcolato con hash())
# - l'hash viene usato per trovare direttamente la posizione nella memoria
# - NON serve cercare la chiave scorrendo tutto il dizionario
# ✔ I dizionari in Python sono HASHMAP
# ✔ Accesso, inserimento e cancellazione sono O(1) in media
# ✔ Le chiavi devono essere IMMUTABILI per mantenere stabile l’hash
# ✔ Gestione interna molto ottimizzata
# ✔ Caso peggiore rarissimo: O(n) per collisioni
