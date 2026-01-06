wyraz = input("Podaj wyraz: ")
samogloski = ['a', 'ą', 'e', 'ę','i', 'o', 'u', 'ó', 'y']
lsamoglosek = 0
lspolglosek = 0
for i in wyraz:
    if i.isalpha():
        if i in samogloski:
            lsamoglosek += 1
        else:
            lspolglosek += 1

print(f"liczba samogłosek: {lsamoglosek}")
print(f"liczba spółgłosek: {lspolglosek}")