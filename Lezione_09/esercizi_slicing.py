import numpy as np

matrice=np.random.randint(1,101,size=(6,6))

sotto_matrice=matrice[1:5,1:5]

inverti_sotto_matrice=sotto_matrice[::-1]

diag_invertita=np.diag(inverti_sotto_matrice)

#Metodo con Fancy index

elementi_diag=np.arange(inverti_sotto_matrice.shape[0]) #Calcolo il numero delle righe
diagonale_matrice_invertita=inverti_sotto_matrice[elementi_diag,elementi_diag]

print(diag_invertita.shape)
inv_copy=inverti_sotto_matrice.copy()
inv_copy[inv_copy % 3 == 0] = -1




