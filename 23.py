# Faire un programme python qui demande à un utilisateur un entier. Le programme fait la somme des carrées des entiers compris entre 1 et la valeur donnée.

valeurInitiale = int(input("Choissisez un nombre "))
somme = 0
for nombre in range(0, valeurInitiale+1):
    somme += (nombre ** 2)


if valeurInitiale == 1:
    somme = 1

print(somme)

