
n = int(input("Entrer un entier n positif : "))
if n < 0 :
  print("l'entier doit etre positif")
else :
    somme = 0
    i= 0
    while i <= n : 
        somme+= 10 ** i
        i+=1

    print(somme)
