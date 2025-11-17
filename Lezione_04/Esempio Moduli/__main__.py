# Importo il modulo 'analisi_dati' e lo rinomino come 'dati'
import analisi_dati as dati

# Creo una lista vuota che conterrà tutte le vendite inserite dall'utente
vendite = []

# Ciclo infinito per inserire più vendite
while True:
    # Chiedo all'utente di inserire una vendita
    vendita = input("Vendita: ")
    
    # Converto la vendita in intero usando la funzione del modulo dati
    vendita = dati.convetitore_ad_intero(vendita)
    
    # Aggiungo la vendita convertita alla lista
    vendite.append(vendita)
    
    # Chiedo se l'utente vuole continuare a inserire dati
    scelta = input("Vuoi inserire nuovi dati? (s/n) ")
    
    # Se scrive 'n', esco dal ciclo
    if scelta.lower() == "n":
        break

# Calcolo il totale e la media delle vendite usando la funzione del modulo
totale, media = dati.calcolo_del_totale_e_media(vendite)

# Ottengo il dizionario dei giorni con vendite sopra la media
vendite_sopra_media = dati.vendite_sopra_la_media(vendite, media)

# Stampo i risultati
print("Giorni con vendite sopra la media e corrispettiva vendita")

# Ciclo sugli elementi del dizionario (giorno, valore)
for x, y in vendite_sopra_media.items():
    print(f"Giorno {x}, Vendita {y}")



    



