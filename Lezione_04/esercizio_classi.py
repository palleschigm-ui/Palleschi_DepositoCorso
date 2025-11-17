#============================
# Esercizio ristorante
#============================
class Ristorante:
    def __init__(self,nome,tipo_di_cucina,aperto=False):
        self.nome=nome
        self.tipo_di_cucina=tipo_di_cucina
        self.aperto=aperto
        self.menu={
            "pasta":15,
            "carne":30,
            "gelato":5
        }
    def descrivi_ristorante(self):
        print(f"Il nome è {self.nome} ed ha cucina {self.tipo_di_cucina} ")

    def stato_di_apertura(self):
        if self.aperto:
            print(f"Il ristorante è aperto")
        else: print(f"Il ristorante è chiuso")

    def apri_ristorante(self):
        if not self.aperto:
            self.aperto=True
            print("Il ristorante ora è aperto")
        else: print("Il ristorante è già aperto")
    
    def chiudi_ristorante(self):
        if self.aperto:
            self.aperto=False
            print("Il ristorante ora è chiuso")
        else: print("Il ristorante è già chiuso")
    
    def aggiungi_al_menu(self):
        nuovo_piatto=input("Nuovo piatto")
        nuovo_prezzo=float(input("Prezzo del nuovo piatto"))
        self.menu[nuovo_piatto]=nuovo_prezzo

    def rimuovi_piatto(self):
        piatto_da_rimuovere=input("Quale piatto vuoi rimuovere dal menu? ")
        if piatto_da_rimuovere.lower() in self.menu:
            self.menu.pop(piatto_da_rimuovere.lower()) #Se non rimetto lower e scrive PASTA mi supera l'if perchè li ho messo lower ma poi non lo trova qua
        else: print("Il piatto non è nel menù")
    
    def stampa_menu(self):
        for piatto,prezzo in self.menu.items():
            print(piatto,prezzo)
    
rist1=Ristorante("da mamma","romana")
rist1.descrivi_ristorante()
rist1.aggiungi_al_menu()
rist1.apri_ristorante()
rist1.stampa_menu()
rist1.rimuovi_piatto()
rist1.stampa_menu()




##########################
##########################
menu={"pane":8}

if 8 in menu.values(): #Come controllare che un valore è in un dizionario
    print("C'è un piatto che costa 8€")
##########################
##########################




############################################################################################################################
    

#=====================
# Esercizio Fabbrica
#=====================


