#=========================================
# Esempio di contenimento/incapsulamento
#=========================================
#L'incapsulamento serve a proteggere l’oggetto e controllare come vengono modificati i suoi dati.

class Computer:
    def __init__(self):
        self.__processore="Intel i5" #Attributo privato, name mangling
    def get_processore(self): #Metodo Getter che permette di ottenere gli attributi privati
        return self.__processore
    def set_processore(self,processore): #Metodo Setter che permette di modificare gli attributi privati
        self.__processore=processore

pc=Computer()
#print(pc.__processore) questa riga mi darebbe errore
print(pc.get_processore())
#Accede all'attributo privato tramite il getter
pc.set_processore("AMD Ryzen 5")
#Modifica l'attributo privato tramite il setter
print(pc.get_processore())

#Vedere utilizzo di @property


#=========================================
# Esempio di contenimento/incapsulamento
#=========================================
print("################################")
class Computer:
    def __init__(self,nome_proc):
        self.__processore=nome_proc #Attributo privato, name mangling
    def get_processore(self): #Metodo Getter che permette di ottenere gli attributi privati
        return self.__processore
    def set_processore(self,processore): #Metodo Setter che permette di modificare gli attributi privati
        self.__processore=processore

pc=Computer("Intel i5")
#print(pc.__processore) questa riga mi darebbe errore
print(pc.get_processore())
#Accede all'attributo privato tramite il getter
pc.set_processore("AMD Ryzen 5")
#Modifica l'attributo privato tramite il setter
print(pc.get_processore())


# ============================================================
# ESEMPIO DI VARIABILE GLOBALE, LOCALE E NONLOCAL
# ============================================================
# Esempio sui livelli di visibilità (o socpe delle variabili)
#In Python i principali livelli di visibilità sono: globale, locale e non-locale

print("################################")



# Variabile globale
num = 10


def funzione_esterna():
    # Variabile locale nella funzione esterna
    num = 5
    print("Numero dentro funzione_esterna (locale):", num)

    def funzione_interna():
        # 'nonlocal' permette di modificare la variabile
        # della FUNZIONE ESTERNA (non quella globale)
        nonlocal num
        num = 3
        print("Numero dentro funzione_interna (nonlocal):", num)

    funzione_interna()

    # Qui num è stato modificato dalla funzione interna
    print("Numero in funzione_esterna dopo funzione_interna:", num)


print("Numero nel main (globale):", num)

funzione_esterna()

# La variabile globale NON cambia perché è stata modificata solo la variabile locale della funzione esterna
print("Numero nel main dopo chiamata (globale NON cambiato):", num)



# ============================================================
# Variabili e Metodi Privati
# ============================================================

#Le variabili o metodi privati sono definiti con due trattini bassi __ all'inizio
#del loro nome. Questo attiva un meccanismo chiamato name mangling, dove il nome
#della variabile viene trasformato per includere il nome della classe che lo
#rende meno accessibile da codice esterno alla classe. 

#Questo non impedisce l'accesso, ma è un forte indicativo che tale variabile o
#metodo non dovrebbe essere accesso o modificato dall'esterno della classe.

print("################################")

class MiaClasse:
    def __init__(self):
        self.__variabile_privata="Sono privata"

    def __metodo_privato(self):
        return "Questo è un metodo privato"

class SottoMia(MiaClasse):
    def __init__(self):
        super().__init__()
        print(self.__variabile_privata)  #Quando proverò a chiamare questa sottoclasse, qui avrò errore
        


obj=MiaClasse() #Credo un oggetto per la mia classe
#Stampando direttamente la variabile privata solleverà un'eccezione
# print(obj.__variabile_privata) #AttributeError

#L'accesso corretto (che dovrebbe essere evitato) sarebbe:
print(obj._MiaClasse__variabile_privata) #Funzionerà, ma NON è buona prassi
#Funzionerà perchè:
#In Python, i nomi con doppio underscore (__) vengono name-mangled.
#Significa che non puoi accedere a __variabile_privata o __metodo_privato da una sottoclasse usando lo stesso nome, 
# perché Python li riscrive internamente come:
#  _MiaClasse__variabile_privata
#  _MiaClasse__metodo_privato
#Cioè Python li salva con questo nome


# sotobj=SottoMia() #Mi genera errore, perchè non riesce ad eseguire print(self.__variabile_privata) 



# ============================================================
# Variabili e Metodi Protetti
# ============================================================

#Le variabili o metodi protetti sono indicati con un singolo trattino basso _
#all'inizio del loro nome. 

#Questo è meno restrittivo rispetto al doppio trattino basso e serve più come
#un suggerimento agli sviluppatori che quel membro dovrebbe essere usato solo
#all'interno della classe e delle sue sottoclassi. 

#Non ci sono meccanismi tecnici che impediscono l'accesso da codice esterno.

print("################################") 

class ClasseBase:
    def __init__(self):
        self._variabile_protetta="Sono protetta"

class SottoClasse(ClasseBase):
    def __init__(self):
        super().__init__()
        print(self._variabile_protetta) #Accesso consentito

obj=SottoClasse()
#Accesso da fuori la classe (non consigliato, ma possibile)
print(obj._variabile_protetta)




