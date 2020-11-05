# Faire la saisie d’un entier qui sera une durée en secondes. Faire les instructions pour convertit cette valeur en heures, minutes, secondes. Par exemple 12334 deviendra 3 heures, 25 minutes et 34 secondes.

valeurInitiale = int(input("Insérer les secondes à convertir "))

heure = valeurInitiale // 3600
reste = valeurInitiale % 3600
minute = reste // 60
secondes = valeurInitiale % 60

print(heure, "heures", minute, "mins", secondes, "secondes")

