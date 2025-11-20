import classi_pagamento as cp
def pomodoro():
    # ESEMPIO D'USO
    carta = cp.CartaDiCredito()
    paypal = cp.Paypal()
    bonifico = cp.BonificoBancario()

    print(cp.tipologia(carta, 100))
    print(cp.tipologia(paypal, 50))
    print(cp.tipologia(bonifico, 200))
 
if __name__=="__main__":
    pomodoro()

#"__main__" è SEMPRE questa, fissa, identica per tutti i file Python
#Non cambia in base al nome del file.
#Non dipende dal nome della funzione.
#Non va modificata.

#In Python:

#__main__ non è il nome del file
#è solo il valore che assume __name__ quando il file viene eseguito direttamente.
#Quindi devi sempre scrivere:
#if __name__ == "__main__":
#anche se il file si chiama: main1.py o qualunque nome tu voglia

#Serve per distinguere due casi:

#✔ 1. Il file è eseguito direttamente
#__name__ vale "__main__" → il blocco viene eseguito

#✔ 2. Il file è importato come modulo
#__name__ vale il nome del file → il blocco non viene eseguito