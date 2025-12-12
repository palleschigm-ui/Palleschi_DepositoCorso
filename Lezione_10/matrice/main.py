import numpy as np
import matrice as m
LOG_FILE = "operazioni_matrici.txt"

# Inizializza il file SOLO all'avvio
with open(LOG_FILE, "w") as f:
    f.write("=== LOG OPERAZIONI MATRICE ===\n\n")

while True:
    print("======================MENU======================")
    print("1) Creare nuova matrice")
    print("2) Estrarre e stampare sotto matrice centrale")
    print("3)Trasposta e stampa")
    print("4) Somma e stampa di tutti gli elementi della matrice")
    print("5) Crea nuova matrice e moltiplica")
    print("6) Calcolo media degli elementi della matrice")
    print("7) Calcolo del determinante")
    print("0) Uscita dal programma")
    scelta=int(input(">"))
    if scelta==1:
        righe=int(input("Numero righe: "))
        colonne=int(input("Numero colonne"))
        matrice= m.crea_matrice(righe,colonne)
        m.salvataggio_matrice("Matrice",matrice)

    elif scelta==2:
        sotto_matrice=m.sotto_matrice(matrice)
        print(sotto_matrice)
        m.salvataggio_matrice("Sotto Matrice",sotto_matrice)
    
    elif scelta==3:
        trasposta=m.trasposta(matrice)
        print(trasposta)
        m.salvataggio_matrice("Trasposta",trasposta)
    
    elif scelta==4:
        somma=m.somma_elementi_matrice(matrice)
        print(somma)
        m.salvataggio_valore("Somma di tutti gli elementi della matrice",somma)
    elif scelta==5:
        nuova_matrice=m.crea_matrice(righe,colonne)
        prodotto=m.moltiplicazione(matrice,nuova_matrice)
        print(prodotto)
        m.salvataggio_matrice("Nuova matrice",nuova_matrice)
        m.salvataggio_matrice("Prodotto",prodotto)
    
    elif scelta==6:
        media=m.media_elementi_matrice(matrice)
        print(media)
        m.salvataggio_valore("Media elementi matrice",media)

    elif scelta==7:
        determinante=m.calcolo_determinante(matrice)
        print(determinante)
        m.salvataggio_valore("Determinante",determinante)
    elif scelta==0:
        break

    else:
        print("Non ho capito")


    






