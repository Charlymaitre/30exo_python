# Faire un programme python avec un affichage formaté. Pour cela vous utilisez la fonction .format(). Avec .format() faire afficher 30 étoiles sur une ligne et 2 chiffre après virgule du nombre 34.30480.

x = 30 * "*"
number = 34.30480

print("{} {:.2f}".format(x, number))
