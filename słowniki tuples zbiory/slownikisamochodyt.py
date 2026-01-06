Audi = {"Przebieg": 120000, "rocznik": 2019, "automat": True}
Volkswagen = {"Przebieg": 198100, "rocznik": 2015, "automat": False}
Fiat = {"Przebieg": 90000, "rocznik": 2022, "automat": False}

Samochody = {"Audi": Audi, "Volkswagen": Volkswagen, "Fiat": Fiat}

dane = input("Podaj markę ")
if dane in Samochody:
    print(f"Przebieg: {Samochody[dane]["Przebieg"]} km")