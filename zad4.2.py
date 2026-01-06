class Charakter:
    def __init__(self, hp, name, type, x, y):
        self.hp = hp
        self.name = name
        self.type = type
        self.x = x
        self.y = y
    def move(self, a, b):
        self.x =+ a
        self.y =+ b
    def interakcja(self, type):
        print(f"Typ interakcji: {self.type}")
    def wyswietl(self):
        print(f"Nazwa: {self.name}")
        print(f"Hp: {self.hp}")
        print(f"Pozycja {self.x}, {self.y}")
        print(f"Typ interakcji: {self.type}")

bohater = Charakter(100, "Ciri", "przyjazny", 0, 0 )
bohater.move(2,6)
bohater.interakcja(type)
bohater.wyswietl()
