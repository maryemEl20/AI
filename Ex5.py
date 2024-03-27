
nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))
Op = input("Entrez l'opérateur (+, -, *, /) : ")
if Op == '+':
    resultat = nombre1 + nombre2
elif Op == '-':
    resultat = nombre1 - nombre2
elif Op == '*':
    resultat = nombre1 * nombre2
elif Op == '/':
    # Vérifier si le diviseur est différent de zéro
    if nombre2 != 0:
        resultat = nombre1 / nombre2
    else:
        resultat = "Division par zéro !"
else:
    resultat = "Opérateur non valide !"

print("Résultat :", resultat)
