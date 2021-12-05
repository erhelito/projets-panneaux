# Fichier comportant les fonctions des formes de base

# import du module turtle
from turtle import *

# fonction pour les panneaux triangulaires
def triangle():
    # CONTOUR BLANC

    # descendre le crayon
    down()

    # boucle pour faire le triangle blanc
    for i in range(3):
        # avance de 110 pixels (= taille cote)
        forward(110)

        # pour les arrondis
        # comprendre circle.(rayon, angle)
        circle(5, 120)

    # BORDURE ROUGE

    # relever le crayon
    up()

    # deplacement
    forward(7)
    left(90)
    forward(7)
    right(90)

    # descendre le crayon
    down()
    # couleur du stylo
    color("red")
    # epaisseur du crayon
    pensize(7)

    # boucle pour faire le triangle en rouge
    for i in range(3):
        # avance de 95 pixels (= taille cote)
        forward(95)

        # pour les arrondis
        # comprendre circle.(diametre, angle)
        circle(2, 120)

    # relever le crayon
    up()


# fonction pour les panneaux losanges
def losange():
    # CONTOUR BLANC

    down()

    # initialise la couleur du crayon
    pencolor("black")

    # rotation pour le debut du dessin
    left(45)

    # boucle pour chaque cote
    for i in range(4):
        forward(100)
        circle(5, 90)

    # LOSANGE JAUNE

    up()

    # deplacement
    left(45)
    forward(20)

    down()

    # definition des couleurs de crayon et de remplissage
    pencolor("black")
    fillcolor("yellow")

    # debut du remplissage
    begin_fill()

    # rotation pour le losange
    right(45)

    # boucle pour chaque cote
    for i in range(4):
        forward(70)
        circle(5, 90)

    # fin du remplissage
    end_fill()

    up()


# fonction pour les panneaux ronds
def rond(couleur):
    # CONTOUR BLANC

    down()  # descendre le crayon

    circle(55)

    # BORDURE DE COULEUR

    # relever le crayon
    up()

    left(90)
    forward(5)
    right(90)

    down()

    # definir la coleur du stylo et du remplissage (en fonction de la couleur donnee)
    pencolor("black")

    if couleur == "rouge":
        fillcolor("red")

    if couleur == "blanc":
        fillcolor("red")

    if couleur == "bleu":
        fillcolor("blue")

    if couleur == "noir":
        pensize(3)

    # commencer le remplissage si la couleur est differente de noir
    if couleur != "noir":
        begin_fill()

    circle(50)

    #fin du remplissage
    end_fill()

    if couleur == "blanc":
        # deplacement
        up()
        left(90)
        forward(15)
        right(90)

        # definir la coleur du stylo et du remplissage
        pencolor("black")
        fillcolor("white")

        # commencer le remplissage
        begin_fill()

        # faire le troisième cercle
        down()
        circle(35)

        #fin du remplissage
        end_fill()

    up()

# fonction pour les panneaux carres
def carre(couleur):
    # CONTOUR BLANC
    down()

    # boucle pour le carre blanc
    for i in range(4):
        forward(101)
        circle(5, 90)

    # INTERIEUR DE COULEUR

    # deplacement pour le carre interieur
    up()
    forward(3)
    left(90)
    forward(5)
    right(90)

    # crayon en position d'ecriture
    down()

    # definir la couleur du crayon et du remplissage
    pencolor("black")

    # debut du remplissage si la couleur est bleu
    if couleur == "bleu":
        fillcolor("blue")
        begin_fill()

    # changement de taille de crayon si la couleur est noir
    if couleur == "noir":
        pensize(5)

    # boucle pour le carre interieur
    for i in range(4):
        forward(95)
        circle(3, 90)

    # fin du remplissage si la couleur est bleu
    if couleur == "bleu":
        end_fill()

    up()


def octogone():
    # boucle octogone exterieur
    for i in range(8):
        forward(45)
        left(45)

    up()
    left(90)
    forward(6)
    right(90)
    forward(3)

    down()
    pencolor("black")
    fillcolor("red")

    begin_fill()

    # boucle octogone interieur
    for i in range(8):
        forward(40)
        left(45)

    end_fill()
    up()

###################
# AUTRES FONCTIONS
###################

# fonction  de remise a 0 de l'angle
def horizontal():
    rotation = heading()
    left(-rotation)


def voiture(couleur):
    if couleur == ("noir"):
        fillcolor("black")

    if couleur == ("rouge"):
        fillcolor("red")

    begin_fill()

    down()
    
    # dessin de la voiture
    forward(4)
    left(90)
    forward(6)
    right(90)

    forward(13)
    right(90)

    forward(6)
    left(90)
    forward(4)
    left(90)
    forward(6)

    right(90)
    forward(2)
    left(90)
    forward(8)
    left(90)
    forward(2)

    right(75)
    forward(9)
    left(75)
    forward(16)
    left(75)
    forward(9)

    right(75)
    forward(2)
    left(90)
    forward(8)
    left(90)
    forward(2)
    right(90)
    forward(6)

    end_fill()
    up()

    left(90)
    forward(5)
    left(90)
    forward(12)

    fillcolor("white")
    begin_fill()

    # ajout de la vitre

    down()
    right(90)
    forward(13)
    left(105)
    forward(8)
    left(75)
    forward(10)
    left(77)
    forward(8)
   
    end_fill()
    up()