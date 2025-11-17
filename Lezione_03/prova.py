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




