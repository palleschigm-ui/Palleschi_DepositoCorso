class punto:
    # Il costruttore: inizializza un nuovo punto con coordinate x e y
    def __init__(self, x, y):
        self.x = x      # Attributo di istanza: coordinata x
        self.y = y      # Attributo di istanza: coordinata y

    # Metodo per spostare il punto di una certa quantità
    def muovi(self, dx, dy):
        self.x = self.x + dx   # Aggiorna la x spostandola di dx
        self.y = self.y + dy   # Aggiorna la y spostandola di dy

    # Metodo che calcola la distanza del punto dall'origine (0,0)
    def distanza_da_origine(self):
        return (self.x**2 + self.y**2)**0.5   # Formula di Pitagora
    
    #In Python, __str__ è un metodo speciale (detto anche dunder method, da double underscore) 
    #che serve a definire come deve essere rappresentato un oggetto quando viene convertito in stringa.
    def __str__(self):
        return f"punto({self.x}, {self.y})"


# Creazione di un oggetto 'punto' con coordinate iniziali (10, 20)
p1 = punto(10, 20)

print(p1.__dict__)

# Spostiamo il punto: dx = 5, dy = 10
p1.muovi(5, 10)

print(p1.__dict__)
print(p1)


