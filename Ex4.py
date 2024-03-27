sexe = input("Entre le sexe d'un habitant (H ou F): ").upper()
age = int(input("Entre l'age d'un habitant: "))

if sexe != "H" and sexe !="F":
  print("Erreur : le sexe doit etre H ou F ")
else:
  if sexe =='H' and age >= 20:
    print("Tu es imposable")
  elif sexe =='F' and age >=18 and age <=35:
    print("Tu es imposable")
  else:
    print("Tu n'es pas imposable")
  
  