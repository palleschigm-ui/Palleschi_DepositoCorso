# Pandas viene principalmente usato per la pre-analisi e la pulizia dei dati
import pandas as pd

# Percorso del file CSV
file_path = "vendite.csv"

# Caricamento dei dati nel DataFrame
df = pd.read_csv(file_path)

# Visualizzazione delle prime righe del DataFrame per conferma
print(df.head())


################################################################################
################################################################################

#Definiamo un dizionario
data={
    "Nome":["Alice","Bob","Carla"],
    "Età" :[25,30,22],
    "Città": ["Roma","Milano","Napoli"]
}

#Convertiamo il dizionario in DataFrame
df=pd.DataFrame(data)

#Stampa del Dataframe originale
print("DataFrame Originale:")
print(df)

#Selezione delle righe dove l'età è superiore a 23
df_older=df[df["Età"]>23]

#Stampa delle righe selezionate

print("\nPersone con età superiore a 23 anni: ")
print(df_older)

#Aggiungiamo una nuova colonna la persona maggiorenne
df["Maggiorenne"]=df["Età"]>=18

#Stampa del Datagrame con la nuova colonna
print("\nDataFrame con colonna Maggiorenne:")
print(df)


################################################################
################################################################

import numpy as np

#DataFrame esempio, inclusi valori mancanti e duplicati

data={
    "Nome":["Alice","Bob","Carla","Bob","Carla","Alice","None"],
    "Età":[25,30,22,30,np.nan,25,29],
    "Città":["Roma","Milano","Napoli","Milano","Napoli","Roma","Roma"]
}

df=pd.DataFrame(data)

print("DataFrame originale")
print(df)

#Rimozione dei duplicati

df=df.drop_duplicates()

#Gestione dei dati mancanti
#Rimozione delle righe dove almeno un elemento è mancante

df_cleaned=df.dropna()

#Possiamo sostituire dati mancanti con valore di default

df["Età"].fillna(df["Età"].mean(),inplace=True)

print("\nDataFrame dopo la pulizia:")
print(df_cleaned)

#Stampa del DataFrame con dati mancanti sostiuiti
print("\nDataFrame con dati mancantu sostituiti")
print(df)