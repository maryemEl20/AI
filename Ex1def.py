def Moyenne(note1,note2,note3):
    moyenne = (note1 + note2 + note3) / 3
    if note1 > 20 or note2 >20 or note3 >20:
        print("les notes ne peuvent pas etre superieur a 20")
    else:
        if moyenne >=16:
            print(f"La moyenne est de {moyenne} et la mention est Très bien")
        elif moyenne >=14 and moyenne < 16:
            print(f"La moyenne est de {moyenne} et la mention est bien")
        elif moyenne >= 12 and moyenne < 14:
            print(f"La moyenne est de {moyenne} et la mention est Assez bien")
        elif moyenne >=10 and moyenne < 12:
            print(f"La moyenne est de {moyenne} et la mention est Passable")
        else:
            print(f"La moyenne est de {moyenne} et la mention est Insuffisant")

note1 = float(input("Entrer la note n1 :\n"))
note2 = float(input("Entrer la note n2 :\n"))
note3 = float(input("Entrer la note n3 :\n"))

Moyenne(note1,note2,note3)


