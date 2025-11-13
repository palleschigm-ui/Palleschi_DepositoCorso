###############################################
# MATCH — ESEMPI COMPLETI E ORDINATI
# Python 3.10+
###############################################

print("====== ESEMPIO 1: MATCH BASE ======")

comando = input("Inserisci comando (start/stop/help): ")

match comando:
    case "start":
        print("Avvio")
    case "stop":
        print("Arresto")
    case "help":
        print("Mostra aiuto")
    case _:
        print("Comando non riconosciuto")


print("\n====== ESEMPIO 2: MATCH SU TIPI ======")

valore = 10

match valore:
    case 0:
        print("Hai inserito zero")
    case int():
        print("È un numero intero")
    case str():
        print("È una stringa")
    case _:
        print("Tipo non riconosciuto")


print("\n====== ESEMPIO 3: MATCH CON CONDIZIONI (GUARDS) ======")

x = int(input("Inserisci un numero per testare positivo/negativo: "))

match x:
    case n if n < 0:
        print("Numero negativo")
    case n if n == 0:
        print("Zero")
    case n if n > 0:
        print("Numero positivo")


print("\n====== ESEMPIO 4: MATCH SU TUPLE ======")

punto = (3, 0)

match punto:
    case (0, 0):
        print("Origine")
    case (x, 0):
        print("Punto sull'asse X:", x)
    case (0, y):
        print("Punto sull'asse Y:", y)
    case (x, y):
        print("Punto qualsiasi:", x, y)


print("\n====== ESEMPIO 5: MATCH SU LISTE ======")

lista = [1, 2, 3]

match lista:
    case []:
        print("Lista vuota")
    case [x]:
        print("Lista con un solo elemento:", x)
    case [x, y, *resto]:
        print("Primi due elementi:", x, y)
        print("Resto della lista:", resto)


print("\n====== ESEMPIO 6: MATCH CON ALTERNATIVE (OR) ======")

carattere = input("Inserisci una lettera: ")

match carattere:
    case "a" | "e" | "i" | "o" | "u":
        print("È una vocale")
    case _:
        print("È una consonante (o altro)")


print("\n====== ESEMPIO 7: MATCH SU TUPLE DI COMANDI ======")

comando = ("move", "left")

match comando:
    case ("move", direzione):
        print("Ti muovi verso:", direzione)
    case ("attack", bersaglio):
        print("Attacchi:", bersaglio)
    case _:
        print("Comando non valido")


print("\n====== ESEMPIO 8: MATCH SU DIZIONARI ======")

persona = {"nome": "Alice", "eta": 20}

match persona:
    case {"nome": n, "eta": e}:
        print("Nome:", n, "| Età:", e)
    case _:
        print("Formato non riconosciuto")


print("\n====== ESEMPIO 9: MINI CALCOLATRICE CON MATCH ======")

op = input("Operazione (+ - * /): ")

match op:
    case "+":
        print("Hai scelto addizione")
    case "-":
        print("Hai scelto sottrazione")
    case "*":
        print("Hai scelto moltiplicazione")
    case "/":
        print("Hai scelto divisione")
    case _:
        print("Operazione sconosciuta")
