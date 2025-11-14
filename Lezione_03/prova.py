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
