#Esempi di input ed output in Python
#Esempi di operazioni di base per la lettura e scrittura di file in Python
import os
print("Sto leggendo da:", os.getcwd())
os.chdir("C:/Users/Gianmario/Desktop/Python/Esercitazioni/Corso_GiGroup/Palleschi_DepositoCorso/Lezione_08/lettura_file")

#Utilizziamo la funzione open() per aprire il file
#Questa funzione accetta due paramentri principali
#1) Il percorso del file
#2) La modalità di apertura (lettura,scrittura,aggiunta,ecc...)

#Se chiamo un file che non esiste o non trova mi darà errore
#FileNotFoundError: [Errno 2] No such file or directory: 'nome.txt'
nome_con_cui_denominero_il_file = open("dati.txt","r") # "r" indica modalità lettura
#La riga di sopra non stampa nulla, e non legge nulla
#Serve solo a preparare il file per la lettura
#Restituisce semplicemente un oggetto file

print(nome_con_cui_denominero_il_file) #Output: <_io.TextIOWrapper name='dati.txt' mode='r' encoding='cp1252'>

#Se voglio leggere il contenuto devo usare .read()
contenuto=nome_con_cui_denominero_il_file.read()
print(contenuto)

#Quindi dopo aver aperto un file in modalità lettura, è possibile leggere il suo contenuto
#Possiamo utilizzare il metodo read() o il metodo readline()

#Il metodo read() legge l'intero contenuto del file come una singola stringa
#Il metodo readline() legge una singola riga alla volta

contenuto=nome_con_cui_denominero_il_file.read() #Legge l'intero contenuto del file
riga=nome_con_cui_denominero_il_file.readline() #Legge una singola riga del file

print(riga) #Non stamperà nulla perchè sono arrivato alla fine con il cursore


nome_con_cui_denominero_il_file.seek(0)  # torna all'inizio

prima_riga = nome_con_cui_denominero_il_file.readline()
print("PRIMA RIGA:")
print(prima_riga)

#Importante chiudere il file dopo aver finito di lavorarci utilizzando il metodo close()
#La chiusura del file libera le risorse associate e consente ad altri programmi o processi di accedere al file

nome_con_cui_denominero_il_file.close() #Chiusura del file


file=open("dati.txt","w")
file.write("Questo è un esempio di scrittura su un file.")
file.close()


file=open("dati.txt","r")
print(file.read())
file.close()

#Per semplificare la gestione dei file e garantire la chiusura automatica del file alla fine è possibile utilizzare il blocco with
#Questo blocco si occupa automaticamente della chiusura del file una volta che il blocco è stato eseguito

with open("dati.txt","r") as file:
    contenuto=file.read()
    print(contenuto)

#Il file viene chiuso automaticamente al termine del blocco "with"


with open("nuovi_dati.txt","w") as file: #apre il file in scrittura, se esiste già cancella tutto il contenuto
    file.write("Ciaoooo")
    file.write("Di nuovo ciaooooo")










quit()


#==============================
# Modalità di apertura
#==============================

#"w" write
#Crea il file se non esiste
#Sovrascrive completamente il file se esiste già

file=open("file.txt", "w") 

#"a" append
#Crea il file se non esiste
#Non sovrascrive, aggiunge le righe in fondo

file=open("file.txt","a")

#"x" create only
#Crea il file
#Se il file esiste già → solleva un errore

file=open("file.txt","x")

#"r" read
#Se il file non esiste → errore
#Se esiste → lo apre il lettura

file=open("file.txt","r")


#Poi ci sono le modalità miste, ma non stiamo qui a vedere tutto