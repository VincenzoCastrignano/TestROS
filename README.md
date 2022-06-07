# README of the Developmental AI for ROS project
(Aucun de ces programmes ne comportent la notion d'ennuie)

## Première capture d'écran
Pour commencer ,le robot a "par défaut" l'action 0, donc il avance.
Par la suite, on regarde la valence obtenue par cette action.

Si la valence est négative, alors l'action du robot va changer pour une nouvelle action.

Si il avance, alors il ira a droite, si il va a droite, alors il ira a gauche et si il
va a gauche, il ira a droite (ce qui explique les zigzags).

Lorsqu'il percute un mur, alors le robot ira sur la gauche jusqu'au moment où il s'échappe.

## Deuxième capture d'écran
Il s'agit de la même procédure sauf que la table de valence est l'exact opposé a
celle de la première capture, alors il ira toujours devant sauf quand il rencontre
un obstacle, il va soit à droite soit à gauche pour obtenir une valence positive en allant
tout droit.