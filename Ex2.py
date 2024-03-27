import math

print("Le programme va afficher les solutions d'une equation du second degré de forme ax^2 + bx + c= 0 \n")
a = float(input("Entrer la valeur de a : "))
b = float(input("Entrer la valeur de b : "))
c = float(input("Entrer la valeur de c : "))
delta = b**2 - 4*a*c
if delta < 0:
  print("Il n'y a pas de solution")
elif delta == 0:
  x = -b/(2*a)
  print("Il y a une solution : ",x)
else:
  # x1 = (-b-delta**0.5)/(2*a)
  # x2 = (-b+delta**0.5)/(2*a)
  x1 = (-b + math.sqrt(delta)) / (2*a)
  x2 = (-b - math.sqrt(delta)) / (2*a)
  print(f"Les solutions de l'équation {a}x^2+ {b}x + {c} = 0 sont : {x1} et {x2}")