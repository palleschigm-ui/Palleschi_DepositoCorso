def convetitore_ad_intero(stringa):
    # Prova a convertire la stringa in numero intero
    try:
        return int(stringa)
    except ValueError:
        # Se la conversione fallisce, avvisa l'utente
        print("Valore non valido")
        # Chiede un nuovo input
        vendita = input("")
        # Richiama ricorsivamente la funzione finché non ottiene un numero valido
        return convetitore_ad_intero(vendita)


def calcolo_del_totale_e_media(lista):
    # Controlla che la lista non sia vuota
    if len(lista) > 0:
        # Calcola il totale delle vendite
        totale = sum(lista)
        # Calcola la media
        media = totale / len(lista)
        # Stampa i risultati
        print(f"Il totale è {totale}")
        print(f"La media è {media}")
        # Restituisce i valori
        return totale, media
    else:
        # Caso in cui la lista è vuota
        print("La lista è vuota")
        return None, None


def vendite_sopra_la_media(lista, media):
    # Dizionario che conterrà i giorni con vendite superiori alla media
    giorni_vendite_sopra_media = {}

    # Scorre tutti gli indici della lista
    for i in range(len(lista)):
        # Se la vendita del giorno i è superiore alla media, la salva nel dizionario
        if lista[i] > media:
            # i+1 perché i giorni partono da 1, non da 0
            giorni_vendite_sopra_media[i + 1] = lista[i]

    # Se nessun giorno supera la media, stampa un messaggio
    if len(giorni_vendite_sopra_media) == 0:
        print("Ogni giorno ho lo stesso totale di vendite")

    # Restituisce il dizionario dei giorni sopra la media
    return giorni_vendite_sopra_media




    
    







