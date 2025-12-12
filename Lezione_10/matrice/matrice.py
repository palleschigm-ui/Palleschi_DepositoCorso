import numpy as np

LOG_FILE = "operazioni_matrici.txt"


def crea_matrice(r,c):
    matrix=np.random.rand(r,c)
    return matrix

def sotto_matrice(matrice):
    sotto_matrice_centrale=matrice[1:-1,1:-1]
    return sotto_matrice_centrale

def trasposta(matrice):
    matrice_trasposta=matrice.T
    return matrice_trasposta

def somma_elementi_matrice(matrice):
    somma=np.sum(matrice)
    return somma

def moltiplicazione(matrice1,matrice2):
    prodotto=matrice1*matrice2
    return prodotto

def salvataggio_matrice(titolo,matrice):
    with open(LOG_FILE,"a") as file:
        file.write(titolo + "\n")
        np.savetxt(file, matrice, fmt="%.4f")
        file.write("\n")

def salvataggio_valore(titolo,valore):
    with open(LOG_FILE,"a") as file:
        file.write(f"{titolo}: {valore} \n\n")

def calcolo_determinante(matrice):
    righe,colonne=matrice.shape
    if righe==colonne:
        determinante=np.linalg.det(matrice)
        return determinante
    else:
        print("Impossibile, la matrice non è quadrata")
        return None
        
def media_elementi_matrice(matrice):
    media=np.mean(matrice)
    return media



