listNombre = []
print("Tapez 10 nombres :")
for i in range(10):
    nombre = int(input(f"Entrer nombre n {i+1}: "))
    listNombre.append(nombre)

est_trie = True
for i in range(len(listNombre)-1):
    if listNombre[i] > listNombre[i+1]:
        est_trie = False
        

if est_trie:
    print("Le tableau est trié dans l'ordre croissant.")
else:
    print("Le tableau n'est pas trié dans l'ordre croissant.")
