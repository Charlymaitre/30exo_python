# Faire un programme python qui construit des pyramide d’étoile. Le programme demande à l’utilisateur le nombre de ligne et le programme dessine une pyramide.

valeurInitiale = int(input("Choississez votre nombre de ligne ")) 

star = 1 
space = valeurInitiale - 1
line = 0

while line < valeurInitiale:

    print(space * " ", star * "*")
    star = star + 2
    space = space - 1
    line = line + 1