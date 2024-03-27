nombre = int(input("Entrez un nombre entier : "))
S = 0       
for i in range(1,nombre):
    if nombre % i == 0:
        S += i

if nombre == S:
    print(nombre, "est un nombre parfait.")
else:
    print(nombre, "n'est pas un nombre parfait.")
