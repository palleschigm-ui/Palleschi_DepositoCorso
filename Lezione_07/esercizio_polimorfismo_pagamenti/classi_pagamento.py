#Nei metodi di istanza di una classe in Python, self va sempre messo.
#Perché Python prova a passare automaticamente self
#TypeError: saluta() takes 0 positional arguments but 1 was given

class MetodoPagamento:
    def effettua_pagamento(self,importo): #Devo mettere self 
       return f"Hai deciso di effetturare un pagamento di {importo}"
class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self,importo): #Devo mettere self 
        pagamento= super().effettua_pagamento(importo) #Qui mi ero scordato di passargli importo come input
        return f"{pagamento} con la carta di credito"
  
class Paypal(MetodoPagamento):
    def effettua_pagamento(self,importo): #Devo mettere self 
        pagamento= super().effettua_pagamento(importo)
        return f"Hai deciso di effetturare un pagamento di {importo} con Paypal"
    
class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self,importo): #Devo mettere self 
        return f"Hai deciso di effetturare un pagamento di {importo} con bonifico bancario"
    
def tipologia(tipo_pagamento,importo):
        return tipo_pagamento.effettua_pagamento(importo)    


#if __name__ == "__main__":
#    raise RuntimeError(
#       "Questo modulo non è eseguibile direttamente. "
#        "Avvia il programma da main.py."
#    )