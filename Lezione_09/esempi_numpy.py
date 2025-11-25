#Iniziamo a vedere alcune librerie fondamentali per il calcolo scientifico in Python.

#Creiamo un array NumPy a partire da una lista Python

#Nell'analisi dei dati quello che ci interessa è comprovare il risultato.

#Le operazioni vettoriali sono molto più veloci con NumPy rispetto alle liste Python
#Le operazioni vettoriali sono la capacità di fare aggregazioni,somma,divisioni,ecc... con una unica operazione coerente con gli elementi.
#Senza avere il bisogno di fare cicli e iterazioni.

#Nell'analisi dei dati non interessa la qualità del codice ma la velocità di esecuzione (cioè sulla prestazione)
#Nell'analisi dei dati vogliamo solo ottimizzare le prestazioni senza tener conto della qualità del codice e della struttura/architettura dello stesso

#Chi fa sicurezza in un sistema del genere è un sistemista
#In una azienda sviluppiamo il massimo delle performance poi mettiamo in sicurezza il sistema e se il progetto è ripetiile e rivendfbile creiamo una archiettettutra per il sitema

#Il codice risolve l' obiettivo nelminor tempo possibile, ma non ha qualità nè architettura
#Il codice non è sicuro perchè non è scritto per qualità ma per performance

#L'architettura è come colleghi le parti del codice fra di loro, è il modo in cui andiamo a struttura il codice in base all'obiettivo.

#Non ci sono abbastanza soldi per fare tutto quanto
#Devo prendere troppe persone per fare un codice di analisi di dati e farlo anche sicuro
#Non c è abbastanza tempo per scrviere del codice di analisi dati sicuro e con architettura



#####################################################################################################################################
#####################################################################################################################################
# Iniziamo a vedere alcune librerie fondamentali per il calcolo scientifico in Python

# Creiamo un array NumPy a partire da una lista Python

# Nell'analisi dei dati ci interessano due cose
# la correttezza dei risultati
# e la velocità con cui il codice li produce

# Le operazioni vettoriali sono molto più veloci con NumPy rispetto alle liste Python
# Per operazioni vettoriali intendiamo somme, sottrazioni, moltiplicazioni, divisioni
# e aggregazioni applicate a tutti gli elementi con una sola istruzione
# senza dover scrivere esplicitamente cicli e iterazioni

# In molti contesti di analisi dei dati si dà molta importanza alle prestazioni
# ma non possiamo dimenticare del tutto la qualità del codice
# perché il codice deve essere leggibile, riutilizzabile e manutenibile

# Il codice focalizzato solo sulla performance può essere più difficile da capire e da estendere
# per questo nella pratica cerchiamo un equilibrio tra velocità, chiarezza e manutenibilità

# L'architettura è il modo in cui colleghiamo le varie parti del codice fra loro
# è il modo in cui strutturiamo moduli, funzioni e script in base all'obiettivo del progetto

# La sicurezza non riguarda solo l'infrastruttura di sistema
# dipende anche da come scriviamo il codice e da come gestiamo i dati
# in un semplice notebook locale la sicurezza ha un peso minore
# in un sistema aziendale invece va considerata fin dall'inizio

# In ogni progetto reale esistono limiti di tempo e di budget
# quindi non possiamo ottimizzare tutto
# di solito partiamo da un codice chiaro e corretto
# poi identifichiamo le parti lente e le ottimizziamo con strumenti come NumPy



import numpy as np

#Creazione di array unidimensionale

arr=np.array([1,2,3,4,5])

#Creazione di un array bidimensionale
arr2d=np.array([[1,2,3],[4,5,6]])

print("Forma dell'array: ",arr.shape)
arr.ndim
arr.dtype
arr.size
arr.sum()
arr.mean()
arr.max()
arr.argmax()

print(arr2d.shape)

arr=np.arange(10)
#reshape_arr=arr.reshape((2))
#print(reshape_arr)

#===========================================
# Esercizio Numpy
#===========================================

array=np.arange(10,50)
print(array.dtype)
array=array.astype(float)
print(array.dtype)
print(array.shape)

array=array.reshape(10,4)
print(array)
array=array.reshape(40)
print(array)

#Esempi di indexing e slicing

arr=np.array([1,2,3,4,5])

#Indexing
print(arr[0]) #Output 1

#Slicing
print(arr[1:3]) #Output [2 3]

#Boolean Indexing 
print(arr[arr>2])

arr_2d=np.array([[1,2,3,4],
                 [6,5,7,8],
                 [9,10,11,12]])

#Slicing sulle righe
print(arr_2d[1:3]) #Prendo la seconda e la terza riga

#Slicing sulle colonne
print(arr_2d[:,1:3]) #Prendo la seconda e la terza colonna

#Slicing misto
print(arr_2d[1:,1:3]) #Dalla seconda riga a tutto, considero la seconda e terza colonna

#Occhio a non farsi venire il mal di testa tra indici e righe
#arr[1:3] non prendo la prima riga ma la seconda

#Fancy indexing: permette di selezionare elementi di un array utilizzando array di indici interi


#======================================
#Esercizio Slicing e Fancy indexing
#======================================

print("------------------- Eserzio Slicing e Fancy indexing-------------------- ")
array=np.random.randint(10,51,20)
print(array)
primi_elementi=array[:10]
print(primi_elementi)
ultimi_elementi=array[15:20]
print(ultimi_elementi)
in_mezzo=array[5:15]
print(in_mezzo)
ogni_terzo=array[::3]
print(ogni_terzo)
array[5:10]=99

print(array)

print("------------------- Eserzio Slicing e Fancy indexing-------------------- ")
array=np.random.randint(10,51,size=(50,50))
print(array)
primi_righe=array[:10]
print(primi_righe)
ultimi_righe=array[15:20]
print(ultimi_righe)
in_mezzo=array[5:15]
print(in_mezzo)
ogni_terzo=array[::3]
print(ogni_terzo)
array[5:10]=99

print(array)

import numpy as np

# Imposto il seed per avere sempre gli stessi numeri casuali (utile per esercizi e correzioni)
np.random.seed(42)

print("------------------- Esercizio 1  Slicing su array 1D --------------------")

# Array monodimensionale di 20 interi casuali tra 10 e 49
array_1d = np.random.randint(10, 51, 20)
print("Array 1D originale:")
print(array_1d)

# Prime 10 posizioni
primi_elementi = array_1d[:10]
print("\nPrime 10 posizioni:")
print(primi_elementi)

# Ultimi 5 elementi (posizioni da 15 a 19)
ultimi_elementi = array_1d[15:20]
print("\nUltimi 5 elementi (posizioni 15–19):")
print(ultimi_elementi)

# Elementi dal quinto al quindicesimo (posizioni 5–14)
in_mezzo = array_1d[5:15]
print("\nElementi in mezzo (posizioni 5–14):")
print(in_mezzo)

# Un elemento ogni 3
ogni_terzo = array_1d[::3]
print("\nUn elemento ogni tre:")
print(ogni_terzo)

# Modifico gli elementi dalla posizione 5 alla 9 impostandoli a 99
array_1d[5:10] = 99
print("\nArray 1D dopo aver impostato 99 nelle posizioni 5–9:")
print(array_1d)


print("\n------------------- Esercizio 2  Slicing su matrice 2D --------------------")

# Matrice 50x50 di interi casuali tra 10 e 49
array_2d = np.random.randint(10, 51, size=(50, 50))
print("Matrice 50x50 originale:")
print(array_2d)

# Prime 10 righe
prime_righe = array_2d[:10] #ATTENZIONE
print("\nPrime 10 righe:")
print(prime_righe)

# Righe dalla 15 alla 19
righe_15_19 = array_2d[15:20]
print("\nRighe dalla 15 alla 19:")
print(righe_15_19)

# Righe dalla 5 alla 14
righe_5_14 = array_2d[5:15]
print("\nRighe dalla 5 alla 14:")
print(righe_5_14)

# Una riga ogni tre
righe_ogni_tre = array_2d[::3]
print("\nUna riga ogni tre:")
print(righe_ogni_tre)

# Imposto tutte le righe dalla 5 alla 9 a 99
array_2d[5:10] = 99
print("\nMatrice dopo aver impostato 99 nelle righe 5–9:")
print(array_2d)


print("\n------------------- Esercizio 3  Slicing su colonne --------------------")

# Prima colonna
prima_colonna = array_2d[:, 0]
print("\nPrima colonna:")
print(prima_colonna)

# Prime 5 colonne
prime_5_colonne = array_2d[:, :5]
print("\nPrime 5 colonne:")
print(prime_5_colonne)

# Ultime 3 colonne
ultime_3_colonne = array_2d[:, -3:]
print("\nUltime 3 colonne:")
print(ultime_3_colonne)

# Una colonna ogni due
colonne_alterate = array_2d[:, ::2]
print("\nUna colonna ogni due:")
print(colonne_alterate)


print("\n------------------- Esercizio 4  Slicing misto righe + colonne --------------------")

# Submatrice con prime 10 righe e prime 5 colonne
submatrice_10x5 = array_2d[:10, :5]
print("\nPrime 10 righe e prime 5 colonne (submatrice 10x5):")
print(submatrice_10x5)

# Blocco centrale di esempio  righe 20–29  colonne 20–29
blocco_centrale = array_2d[20:30, 20:30]
print("\nBlocco centrale (righe 20–29, colonne 20–29):")
print(blocco_centrale)

# Righe ogni 2 e colonne ogni 3
pattern = array_2d[::2, ::3]
print("\nRighe ogni due e colonne ogni tre:")
print(pattern)

# Singola riga e singola colonna
riga_7 = array_2d[7, :]
colonna_12 = array_2d[:, 12]
print("\nRiga 7 intera:")
print(riga_7)
print("\nColonna 12 intera:")
print(colonna_12)

# Modifico un blocco 5x5 (righe 30–34, colonne 10–14) impostandolo a 0
array_2d[30:35, 10:15] = 0
print("\nMatrice dopo aver impostato a 0 il blocco righe 30–34, colonne 10–14:")
print(array_2d)


