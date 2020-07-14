import os
annee = input("Saisissez une année : ")

annee = int(annee)
bissextile = False


if annee % 400 == 0:
    bissextile = True
elif annee % 100 == 0:
    bissextile = False
elif annee % 4 == 0:
    bissextile = True
else:
    bissextile = False

if bissextile:
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")
os.system("pause")