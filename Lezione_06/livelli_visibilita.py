# ============================================================
# PASSAGGIO DI PARAMETRI, VARIABILI LOCALI, GLOBAL, MUTABILI E IMMUTABILI
# ============================================================
#
# Questo file raccoglie tutti gli esempi e le spiegazioni su:
# - perché num resta 10 quando lo passo a una funzione
# - come far cambiare davvero il valore
# - global e nonlocal (cenno)
# - differenza tra oggetti immutabili e mutabili
# - modifiche in place su liste (e perché si vedono fuori)
# - riassegnazione del riferimento (e perché NON si vede fuori)
#
# Puoi eseguirlo e guardare gli output per capire bene cosa accade.
# ============================================================


print("=== ESEMPIO 1: il parametro è una VARIABILE LOCALE ===")

def funzione_esterna(num):
    # assegno UN NUOVO VALORE al PARAMETRO LOCALE
    num = 5
    return num

num = 10   # variabile nel "main"
funzione_esterna(num)
print("Valore di num DOPO funzione_esterna(num) SENZA assegnare:", num)
# Output: 10
#
# SPIEGAZIONE:
# 1) num = 10 → variabile esterna
# 2) funzione_esterna(num) → il valore 10 viene copiato nel parametro num della funzione
# 3) dentro la funzione num = 5 modifica SOLO la variabile locale
# 4) quando la funzione finisce, quella num locale scompare
# 5) fuori, num resta 10


print("\n=== ESEMPIO 2: usare il VALORE RESTITUITO per modificare num ===")

num = 10
num = funzione_esterna(num)   # qui USO il valore restituito
print("Valore di num DOPO num = funzione_esterna(num):", num)
# Output: 5
#
# Per modificare davvero il valore esterno, devo usare:
# num = funzione_esterna(num)


print("\n=== ESEMPIO 3: usare global (sconsigliato in generale) ===")

# ATTENZIONE: global viene mostrato solo a scopo didattico

def funzione_esterna_global():
    global num
    num = 5  # qui modifico la variabile globale num

num = 10
print("Valore iniziale di num (globale):", num)
funzione_esterna_global()
print("Valore di num DOPO funzione_esterna_global():", num)
# Output: 5
#
# global num dice a Python:
# “usa la variabile globale num, non crearne una nuova locale”


print("\n=== ESEMPIO 4: i parametri della funzione sono variabili LOCALI ===")

def f(x):
    x = 5  # modifica solo la x LOCALE

num = 10
f(num)
print("Valore di num DOPO f(num):", num)
# Output: 10
#
# Regola:
# I parametri di una funzione sono SEMPRE variabili locali.
# Assegnare x = 5 NON cambia num fuori dalla funzione.


# ============================================================
# MUTABILI vs IMMUTABILI
# ============================================================

print("\n=== ESEMPIO 5: intero (immutabile) ===")

def f_int(x):
    x = 5  # nuova assegnazione: NON cambia il valore esterno

num = 10
f_int(num)
print("num dopo f_int(num):", num)
# Output: 10
#
# int è IMMUTABILE:
# non puoi modificare “dentro” l'oggetto intero, puoi solo creare un altro valore.


#✔ Per modificare un valore esterno, devi:
#✔ restituire il valore (modo corretto)
def funzione_esterna(num):
    num = 5
    return num

num = 10
num = funzione_esterna(num)
print(num)   # stampa 5


print("\n=== ESEMPIO 6: lista (mutabile) con modifica IN PLACE ===")

def f_list_append(lista):
    lista.append(99)  # modifica l'oggetto lista IN PLACE

numeri = [1, 2, 3]
print("Lista prima di f_list_append:", numeri)
f_list_append(numeri)
print("Lista dopo f_list_append:", numeri)
# Output: [1, 2, 3, 99]
#
# lista è MUTABILE:
# lista e numeri puntano allo stesso oggetto; modificando l'oggetto, si vede fuori.


print("\n=== ESEMPIO 7: lista - modifica in place vs riassegnazione ===")

def f_in_place(l):
    # Modifica IN PLACE → si vede fuori
    l.append(1)

def f_riassegna(l):
    # Riassegnazione → crea un NUOVO oggetto, non tocca quello esterno
    l = [100]  # questa lista esiste solo dentro la funzione


x = []
print("x all'inizio:", x)
f_in_place(x)
print("x dopo f_in_place(x):", x)      # [1] → modificata in place

f_riassegna(x)
print("x dopo f_riassegna(x):", x)     # [1] → NON è cambiata
#
# l.append(1) modifica l'oggetto lista condiviso
# l = [100] cambia SOLO il riferimento locale l, non x


print("\n=== ESEMPIO 8: lista[0] = 99 (modifica in place) ===")

def f_index(l):
    l[0] = 99   # modifica l'oggetto lista IN PLACE

x = [1, 2, 3]
print("x prima di f_index:", x)
f_index(x)
print("x dopo f_index:", x)
# Output: [99, 2, 3]
#
# Anche l’assegnazione elemento-per-elemento (l[0] = 99) modifica l’oggetto lista.


print("\n=== RIEPILOGO MUTABILI vs IMMUTABILI (come commenti) ===")
"""
RIEPILOGO (teorico):

Tipo di dato | Mutabile? | Cambia fuori se modificato in place?
-------------|---------- |--------------------------------------
int          | NO        | NO
float        | NO        | NO
str          | NO        | NO
tuple        | NO        | NO
list         | SI        | SI
dict         | SI        | SI
set          | SI        | SI

Regola base:
- Se l'oggetto è MUTABILE e lo modifichi IN PLACE (append, remove, l[0] = ...),
  la modifica si vede fuori.
- Se riassegni la variabile locale (l = ...), cambi solo il riferimento locale.
"""


print("\n=== RIEPILOGO OPERAZIONI SU LISTA (come commenti) ===")
"""
Operazione            | Effetto                   | Si vede fuori?
----------------------|---------------------------|---------------
lista.append(…)       | modifica oggetto          | SI
lista[0] = 99         | modifica oggetto          | SI
lista.clear()         | modifica oggetto          | SI
lista.sort()          | modifica oggetto          | SI
lista = [1,2,3]       | cambia riferimento locale | NO
lista = lista + [1]   | crea nuova lista          | NO

Regola d’oro:
- Le modifiche IN PLACE su un oggetto mutabile si vedono sempre fuori.
- Cambiare la variabile locale (lista = ...) NON cambia l’oggetto esterno.
"""


print("\n=== FINE ESEMPI ===")
