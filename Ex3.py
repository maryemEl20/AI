
temps = int(input("Entrer le temps en seconde :\n"))
heure = temps //3600
minut = (temps % 3600) // 60
seconde = temps % 60
print(f"Il ya {heure} heures,{minut} minutes ,{seconde} seconds.")
