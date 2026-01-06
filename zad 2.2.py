rok = int(input("Podaj rok: "))
miesiac = int(input("Podaj miesiac: "))
dzien = int(input("Podaj dzien: "))


if (rok % 400 == 0) or ((rok % 4 == 0) and (rok % 100 != 0)):
    dnimiesiaca = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    dnimiesiaca = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


iledni = dnimiesiaca[miesiac - 1]


if miesiac == 12 and dzien == 31:
    rok += 1
    miesiac = 1
    dzien = 1

elif dzien == iledni:
    miesiac += 1
    dzien = 1

else:
    dzien += 1


print(f"Następny dzień to: {rok}-{miesiac:02d}-{dzien:02d}")