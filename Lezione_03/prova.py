try:
    x = int("ciao")
except:
    print("Non posso convertire questa stringa in numero")
x=99
x=x*x
print(x)

tupla=(1,2,3,4)
tupla=tupla+(3,2,3,4)
print(tupla)

lista=[1,2,3]
lista=[x**2 for x in lista]
print(lista)

class Solution:
    def romanToInt(self, s: str) -> int:
        cifrario={
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        ans=0
        flag=False
        for i in range(len(s)):
            if flag:
                flag=False
                continue
            if i<(len(s)-1) and cifrario[s[i]]<cifrario[s[i+1]]:
                flag=True
                ans=ans+cifrario[s[i+1]]-cifrario[s[i]]
            else: ans=ans+ cifrario[s[i]]
        return ans 


#=================================================
# Esericizio: prendo una frase e restituisco un dizionario con ogni parola presente nella frase
# associata a quante volte compare
#=================================================

#Non sto usando la funzione .split()
#Vedere questa funzione perchè può tornare utile

#L'idea è scorrere sulla stringa, quando incontro uno spazio significa che è appena finita una parola
#Allora metto nel dizionario la parola che andrà dall'ultimo spazio che ho visto +1 fino allo spazio che ho appena visto

def frequenza_parole(frase):
   dizionario={}
   sign=-1 #sign mi segna l'ultimo spazio che ho incontrato, lo inizializzo a -1 perchè sennò ho problemi se il testo mi inizia subito con una parola
   for i in range(len(frase)):
        if frase[i]==" " or i==(len(frase)-1): #trovo uno spazio significa che è appena finita una parola
            parola=""
            if i==(len(frase)-1): #caso sono arrivato alla fine della frase
                i=i+1
            for j in range(sign+1,i):
                 parola=parola+frase[j].lower()
            if parola in dizionario and parola !="":
                  dizionario[parola]+=1
            elif parola !="": #gestisco il caso ho più spazi di seguito
                dizionario[parola]=1
            sign=i
   return dizionario
    
print(frequenza_parole("  ma zio pera ma zio pera, porcaccio il mondo"))

#Se voglio gestire la punteggiatura
#frase = frase.replace(",", "").replace(".", "")


#================================
#
#================================

def sottostrings(stringa:str)->int:
    count=0
    seen={}
    max=0
    for i in range(len(stringa)):
          if stringa[i] not in seen:
               seen[stringa[i]]=i
               count+=1
          else: 
             if count>max:
                max=count
             seen={}
             seen[stringa[i]]=i
             count=1
    return max

print(sottostrings("adcabcabdb"))