
n = int(input("Entrer un entier non nul : "))
if n <= 0 :
  print("l'entier doit etre non nul et positif")
else :
  i = 1
  somme = 0
  while i <= n:
    somme += i ** 2
    i+=1

  print(f"La somme des {n} premiers carrés : ",somme)
  
