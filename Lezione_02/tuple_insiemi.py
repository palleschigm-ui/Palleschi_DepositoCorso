#Esempi di tuple
punto=(3,4)
colore_rgb=(255,128,0)
informazioni_persona=("Alice",25,"Donna")

#Possiamo accedere agli elementi allo stesso modo che facciamo con le liste

print(punto[0]) 

# punto[0]=3 mi darebbe errore, perchè le liste sono immutabili.


#Esempi insiemi

set1=set([1,2,3,4,5]) #Converto una lista in un insieme
set2={1,2,3,4,5} #Definisco direttamente un insieme mettendo le parentesi graffe

#Gli insieme non contengono elementi duplicati
set3={1,2,3,4,4,2,3,4,5,5,6}
print(set3) #Output: {1,2,3,4,5,6}
print(len(set3)) #Output: 6

t=(1,["a","b","c"],"word")
print(t[1][0])
t[1][0]=99 #Non mi dà errore
#t[0]=99 mi darebbe errore