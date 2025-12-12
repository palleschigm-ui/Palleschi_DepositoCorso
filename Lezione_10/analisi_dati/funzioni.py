import numpy as np      # NumPy serve per trasformare i blocchi in matrici vere (array 2D)
import re               # "re" serve per riconoscere con una regex se una riga è numerica o no


def estrai_matrici(path):
    """
    Legge un file che contiene sia testo che numeri e
    estrae automaticamente TUTTI i blocchi numerici consecutivi,
    trasformandoli in matrici NumPy 2D.
    Restituisce una LISTA di matrici.
    """

    # --- 1) APRIAMO IL FILE E LEGGIAMO TUTTE LE RIGHE ---

    with open(path, "r") as f:
        lines = f.readlines()    # Lista: ogni elemento è una riga del file


    # --- 2) LISTE DI SUPPORTO ---
    
    matrici = []          # Qui metteremo tutte le matrici finali trovate nel file
    blocco_corrente = []  # Qui accumuliamo righe numeriche consecutive
    #Lista temporanea per accumulare le righe numeriche consecutive che appartengono alla stessa matrice.
    #   In pratica:
    #quando trovi una riga numerica → la aggiungi a blocco_corrente
    #quando incontri una riga NON numerica → chiudi il blocco e lo trasformi in matrice

    # --- 3) SCORRIAMO IL FILE RIGA PER RIGA ---

    for line in lines:

        # ---------------------------------------------------------
        # VERIFICHIAMO SE LA RIGA È COMPLETAMENTE NUMERICA
        # ---------------------------------------------------------
        #
        # La regex usata significa:
        #  - la riga contiene UNO O PIÙ numeri separati da spazi
        #  - nessun testo
        #
        # Esempi che la regex accetta:
        #   "1 2 3"
        #   "0.25 0.66 0.77"
        #   " -2.4   3.1   5 "
        #
        # Esempi che NON accetta:
        #   "Matrice"
        #   "Somma totale"
        #   "1 2 testo"
        #
        # ---------------------------------------------------------

        if re.match(r"^\s*([+-]?\d+(\.\d+)?\s+)+[+-]?\d+(\.\d+)?\s*$", line):

            # --- 3A) LA RIGA È NUMERICA ---
            # Convertiamo la riga in una lista di float

            pulita = line.strip()           # Togliamo spazi e newline
            stringhe_numeri = pulita.split() # Divide ogni numero in una stringa separata
            valori = [float(x) for x in stringhe_numeri]  # Converte ogni stringa in numero float

            # Aggiungiamo questa "riga numerica" al blocco corrente
            blocco_corrente.append(valori)

        else:

            # --- 3B) LA RIGA NON È NUMERICA ---
            # Questo significa che *si è concluso un blocco numerico*

            if blocco_corrente:
                # Trasformiamo il blocco in una matrice NumPy 2D e lo aggiungiamo alla lista finale
                matrice = np.array(blocco_corrente)
                matrici.append(matrice)

                # Reset del blocco, per iniziare un nuovo gruppo numerico
                blocco_corrente = []


    # --- 4) DOPO L'ULTIMA RIGA, POTREBBE ESSERCI UN BLOCCO APERTO ---
    #
    # Esempio:
    #   <numeri>
    #   <numeri>
    #   EOF
    #
    # Non c'è una riga di testo finale che chiuda il blocco, quindi dobbiamo farlo ora
    #

    if blocco_corrente:
        matrice = np.array(blocco_corrente)
        matrici.append(matrice)


    # --- 5) RESTITUIAMO LA LISTA DELLE MATRICI ---
    #
    # matrici è una lista di array NumPy 2D, ad esempio:
    #
    # [
    #   array([[...], [...], ...]),   # Matrice principale
    #   array([[...], [...], ...]),   # Sotto matrice
    #   array([[...], [...], ...]),   # Trasposta
    #   ...
    # ]
    #

    return matrici

