# Faire un programme python qui demande à un utilisateur d’entrer un entier positif. Le programme indique ensuite si l’entier positif est pair ou impair ? Le programme vérifie et redemande l’entier si ce n’est pas un entier positif.

valeurInitiale = int(input("Choississez un nombre "))

while valeurInitiale < 0:
    
    valeurInitiale = int(input("Veuillez saisir un entier positif "))
    
if valeurInitiale % 2 == 0: 
        print("Le nombre est pair")
else:
        print("Le nombre est impair")    
    