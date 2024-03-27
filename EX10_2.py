T = int(input("Entrer la taille N des vecteurs : "))
a = []
b = []
print("les éléments de vecteur a :")
for i in range(T):
    nombre = int(input(f"Entrer nombre n {i+1}: "))
    a.append(nombre)

print("les éléments de vecteur b :")
for i in range(T):
    nombre = int(input(f"Entrer nombre n {i+1}: "))
    b.append(nombre)

s = 0
p = 1
for i in range(T):
    p = a[i]*b[i]
    s+= p

print("a = ",a)
print("b = ",b)

# Affichage du résultat
print("Le produit scalaire des deux vecteurs est :", s)


