class Osoba:
    def __init__(self, imie, nazwisko, data_urodzenia, nr_dowodu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia
        self.nr_dowodu = nr_dowodu

    def pokaz_dane_osoby(self):
        print(f"Imię: {self.imie}")
        print(f"Nazwisko: {self.nazwisko}")
        print(f"Data urodzenia: {self.data_urodzenia}")
        print(f"Numer dowodu: {self.nr_dowodu}")


class Student(Osoba):
    def __init__(self, imie, nazwisko, data_urodzenia, nr_dowodu,
                 rok_rozpoczecia, rok_zakonczenia, aktywny, kierunek, rok_studiow):
        super().__init__(imie, nazwisko, data_urodzenia, nr_dowodu)
        self.rok_rozpoczecia = rok_rozpoczecia
        self.rok_zakonczenia = rok_zakonczenia
        self.aktywny = aktywny
        self.kierunek = kierunek
        self.rok_studiow = rok_studiow

    def pokaz_dane_studenta(self):
        self.pokaz_dane_osoby()
        print(f"Rok rozpoczęcia studiów: {self.rok_rozpoczecia}")
        print(f"Rok zakończenia studiów: {self.rok_zakonczenia}")
        print(f"Czy aktywny: {self.aktywny}")
        print(f"Kierunek: {self.kierunek}")
        print(f"Rok studiów: {self.rok_studiow}")



class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, data_urodzenia, nr_dowodu,
                 start_zatrudnienia, staz_pracy, stanowisko, zwolnienie):
        super().__init__(imie, nazwisko, data_urodzenia, nr_dowodu)
        self.start_zatrudnienia = start_zatrudnienia
        self.staz_pracy = staz_pracy
        self.stanowisko = stanowisko
        self.zwolnienie = zwolnienie

    def pokaz_dane_pracownika(self):
        self.pokaz_dane_osoby()
        print(f"Start zatrudnienia: {self.start_zatrudnienia}")
        print(f"Staż pracy: {self.staz_pracy}")
        print(f"Stanowisko: {self.stanowisko}")
        print(f"Czy na zwolnieniu: {self.zwolnienie}")


class Manager(Pracownik):
    def __init__(self, imie, nazwisko, data_urodzenia, nr_dowodu,
                 start_zatrudnienia, staz_pracy, stanowisko, zwolnienie,
                 oddzial, ilosc_pracownikow):
        super().__init__(imie, nazwisko, data_urodzenia, nr_dowodu,
                         start_zatrudnienia, staz_pracy, stanowisko, zwolnienie)
        self.oddzial = oddzial
        self.ilosc_pracownikow = ilosc_pracownikow

    def pokaz_dane_managera(self):
        self.pokaz_dane_pracownika()
        print(f"Oddział: {self.oddzial}")
        print(f"Ilość pracowników: {self.ilosc_pracownikow}")


osoba1 = Osoba("Jan", "Nowak", "2004-05-11", "ABC123")
osoba1.pokaz_dane_osoby()
print("-----------------------")

student = Student("Karol", "Jakistam",  "2005-01-24", "RCB324",2024,
                  2027, True,  "Zarządzanie",
                  3)
student.pokaz_dane_studenta()
print("-----------------------")

pracownik = Pracownik("Marcin", "Wazon", "24-06-17", "ACD2084",
                      "18-12-2023", "2 lata", "Kucharz", False)
pracownik.pokaz_dane_pracownika()
print("-----------------------")

manager = Manager("Jan", "Nowak", "2004-05-11", "ABC123", "18-12-2023", "2 lata",
                  "Manager", False, "A1", "12")
manager.pokaz_dane_managera()
print("-----------------------")