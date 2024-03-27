nombre = int (input("Entrer un nombre : \n"))
print("Les dix nombres suivants de ",nombre," : ")
# Boucle Pour:

# for i in range(1,11):
for i in range(10):
  nombre += 1
  print(nombre)

print(f"Les dix nombres suivants de {nombre} : ") 
i = 0
# Boucle tant que :
while i < 10:
    print(nombre + i + 1)
    i+= 1
    



