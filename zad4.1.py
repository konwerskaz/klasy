class Czas:
    def __init__(self, godziny, minuty, sekundy):
        self.godziny = godziny
        self.minuty = minuty
        self.sekundy = sekundy
    def wyswietl(self):
        print(f'{self.godziny:02d}:{self.minuty:02d}:{self.sekundy:02d}')

    def uaktualnij(self, type, value):
        if type == "h":
            self.godziny = (self.godziny + value) % 24
            print(f'{self.godziny:02d}:{self.minuty:02d}:{self.sekundy:02d}')
        elif type == "m":
                self.minuty = (self.minuty + value) % 60
                print(f'{self.godziny:02d}:{self.minuty:02d}:{self.sekundy:02d}')
        elif type == "s":
            self.sekundy = (self.sekundy + value) % 60
            print(f'{self.godziny:02d}:{self.minuty:02d}:{self.sekundy:02d}')
        else:
            print("niepoprawne dane")
x = Czas(20,45,5)
x.wyswietl()

x.uaktualnij("h", -5)