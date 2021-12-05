from formes_base import *


# intersection prioritaire
def intersection_prioritaire():
    triangle()

    pencolor("black")
    fillcolor("black")
    pensize(1)

    # deplacement a la base de la fleche
    forward(47)
    left(90)
    forward(15)
    right(90 + 45)

    down()
    begin_fill()

    # partie basse droite
    forward(12)
    left(90 + 45)
    forward(20)

    # bosse droite
    right(90)
    forward(10)
    left(90)
    forward(7)
    left(90)
    forward(10)
    right(90)

    # partie haute
    forward(20)
    left(45)
    forward(12)
    left(90)
    forward(12)
    left(45)
    forward(20)

    # bosse gauche
    right(90)
    forward(10)
    left(90)
    forward(7)
    left(90)
    forward(10)
    right(90)

    # partie basse gauche
    forward(20)
    left(90 + 45)
    forward(12)

    end_fill()
    up()


# triangle inverse
def triangle_inverse():
    # CONTOUR BLANC

    # crayon en position d'ecriture
    down()

    # rotation de 180° pour dessin le triangle a l'envers
    right(180)

    # boucle pour le contours
    for i in range(3):
        # avance de 110 pixels (= taille cote)
        forward(110)
        # pour les arrondis
        # comprendre circle.(diametre, angle)
        circle(5, 120)

    # TRIANGLE ROUGE
    # deplacement pour le triangle rouge
    up()
    left(45)
    forward(10)
    right(45)

    # crayon en position d'ecriture
    down()

    # initialise la couleur du crayon et l'épaisseur
    pencolor("red")
    pensize(7)

    # boucle le triangle rouge
    for i in range(3):
        # avance de 95 pixels (= taille cote)
        forward(95)
        # pour les arrondis
        # comprendre circle.(diametre, angle)
        circle(2, 120)

    # relever le crayon
    up()


# priorite
def priorite():
    losange()


# fin priorite
def losange_barre():
    # trace le losange de base
    losange()

    # deplacement du crayon
    right(135)
    forward(15)

    # deplacement pour la bande noire
    circle(-5, 135)
    forward(37)
    right(90)

    down()

    # definir la coleur du stylo et du remplissage
    pencolor("black")
    fillcolor("black")

    # commencer le remplassige
    begin_fill()

    # commencer la bande noire
    forward(110)
    left(90)
    forward(20)
    left(90)
    forward(110)
    left(90)
    forward(20)

    #fin du remplissage
    end_fill()
    up()


# circulation interdite
def circulation_interdite():
    rond("blanc")


# sens interdit
def sens_interdit():
    rond("rouge")

    fillcolor("white")

    left(90)
    forward(37)
    left(90)
    forward(37)

    down()

    begin_fill()

    # boucle pour le rectangle blanc
    for i in range(2):
        right(90)
        forward(20)
        right(90)
        forward(74)

    #fin du remplissage
    end_fill()
    up()

# limitation 50
def limitation_50():
    rond("blanc")

    # deplacement pour l'ecriture
    right(180)
    forward(25)
    right(90)
    forward(5)

    # ecriture
    write("50", font=("L1", 35, "bold"))

# fin interdiction
def fin_interdiction():
    rond("noir")

    pensize(1)
    fillcolor("black")

    # deplacement
    left(180)
    circle(-50, 32)

    horizontal()

    left(45)

    begin_fill()

    # trait 1
    down()
    forward(98)
    up()

    # deplacement pour la partie 2
    left(90)
    forward(20)
    left(90)

    # trait 2
    down()
    forward(98)
    up()

    end_fill()


# obligation tourner a droite
def obligation_tourner_droite():
    # tracage du cercle de base
    rond("bleu")

    # deplacement a la base de la fleche
    for i in range(2):
        left(90)
        forward(42)

    pencolor("black")
    fillcolor("white")

    begin_fill()

    down()

    # debut fleche
    right(90)
    forward(10)
    right(90)
    forward(60)

    # partie haute de la fleche
    left(135)
    forward(20)
    right(45)
    forward(10)
    right(135)
    forward(40)

    # partie basse de la fleche
    right(90)
    forward(40)
    right(135)
    forward(10)
    right(45)
    forward(20)
    left(135)
    forward(60)

    end_fill()

    up()


# panneau contournement par la gauche
def contourner_gauche():
    rond("bleu")

    # deplacement en haut a droite
    left(90)
    forward(85)
    right(90)
    forward(12.5)
    right(120)

    pencolor("black")
    fillcolor("white")

    begin_fill()

    down()

    # debut de la fleche
    left(90)
    forward(10)
    right(90)
    forward(60)

    # partie haute de la fleche
    left(135)
    forward(20)
    right(45)
    forward(10)
    right(135)
    forward(40)

    # partie basse de la fleche
    right(90)
    forward(40)
    right(135)
    forward(10)
    right(45)
    forward(20)
    left(135)
    forward(60)

    # fin du remplissage
    end_fill()

    up()


# panneau direction obligatoire a gauche
def tourner_gauche():
    rond("bleu")

    pencolor("black")
    fillcolor("white")

    forward(22)
    left(90)
    forward(15)

    down()
    begin_fill()

    # cote droit
    forward(40)
    circle(12, 90)
    forward(25)

    # haut fleche
    right(90 + 45)
    forward(20)
    left(90 + 45)
    forward(12)
    left(45)
    forward(27)

    # pointe de la fleche
    left(90)

    # bas fleche
    forward(27)
    left(45)
    forward(12)
    left(90 + 45)
    forward(20)
    right(90 + 45)

    # cote gauche
    forward(22)
    circle(-6, 90)
    forward(38)

    # bas
    left(90)
    forward(9)

    end_fill()
    up()

def ceder_passage_droite():        
    triangle()

    # initialise la couleur du crayon, du remplissage et l'épaisseur
    pencolor("black")
    fillcolor("black")
    pensize(1)

    # deplacement en bas a droite
    forward(67)
    left(90)
    forward(7)
    left(90)
    forward(3.5)
    right(180)
    left(45)

    # premier rectangle
    down()
    begin_fill()

    for i in range(2):
        forward(10)
        left(90)
        forward(50)
        left(90)

    end_fill()
    up()

    # deplacement en bas a gauche
    right(45)
    left(180)
    forward(30.5)
    right(45)

    # second rectangle
    down()
    begin_fill()

    for i in range(2):
        forward(10)
        right(90)
        forward(50)
        right(90)

    end_fill()
    up()


def retrecissement():
    triangle()

    pencolor("black")
    fillcolor("black")
    pensize(1)

    # COTE DROIT
    
    # deplacement cote droit du dessin
    forward(70)
    left(90)
    forward(7)

    # cote droit
    begin_fill()
    down()

    forward(23)
    left(40)
    forward(16.5)
    right(40)
    forward(15)
    left(90)
    forward(7)
    left(90)
    forward(15)
    left(40)
    forward(16.5)
    right(40)
    forward(23)
    left(90)
    forward(7)

    end_fill()
    up()

    # COTE GAUCHE

    # deplacement cote gauche du dessin
    left(180)
    forward(45)
    right(90)

    # cote gauche
    begin_fill()
    down()

    forward(23)
    right(40)
    forward(16.5)
    left(40)
    forward(15)
    right(90)
    forward(7)
    right(90)
    forward(15)
    right(40)
    forward(16.5)
    left(40)
    forward(23)
    right(90)
    forward(7)

    end_fill()
    up()


# PANNEAUX BONNUS

# panneau impasse
def impasse():
    carre("bleu")

    forward(38)
    left(90)
    forward(5)
    right(90)

    pencolor("black")
    fillcolor("white")

    begin_fill()

    # PARTIE BLANCHE
    down()
    forward(20)
    left(90)
    forward(60)
    right(90)
    forward(15)
    left(90)
    forward(30)
    left(90)
    forward(50)
    left(90)
    forward(30)
    left(90)
    forward(15)
    right(90)
    forward(60)

    end_fill()

    up()

    right(180)
    forward(60)
    left(90)
    forward(10)
    right(90)
    forward(4)

    # PARTIE ROUGE
    pencolor("black")
    fillcolor("red")

    begin_fill()

    down()

    forward(22)
    right(90)
    forward(40)
    right(90)
    forward(22)
    right(90)
    forward(40)

    end_fill()
    up()

# panneau parking
def parking():
    carre("bleu")

    pencolor("white")

    forward(20)
    left(90)
    forward(-5)

    write("P", font=("L1", 70, "bold"))

    
def priorite_circulation_inverse():
    carre("bleu")

    forward(62)
    left(90)
    forward(5)

    # fleche banche
    pencolor("black")
    fillcolor("white")

    begin_fill()

    down()

    forward(40)
    left(90)
    forward(18)
    right(120)
    forward(50)
    right(120)
    forward(50)
    right(120)
    forward(18)
    left(90)
    forward(40)
    right(90)
    forward(15)

    end_fill()

    up()

    forward(35)
    right(90)
    forward(80)
    right(90)

    # fleche rouge
    down()
    pencolor("black")
    fillcolor("red")

    begin_fill()

    forward(5)
    right(90)
    forward(52)
    left(90)
    forward(9)
    right(120)
    forward(30)
    right(120)
    forward(30)
    right(120)
    forward(9)
    left(90)
    forward(52)

    end_fill()
    up()

def hopital_croix():
    carre("noir")

    forward(47)
    left(90)
    forward(5)
    left(90)

    down()
    pensize(1)
    pencolor("black")
    fillcolor("red")

    begin_fill()

    # boucle pour la croix
    for i in range(4):
        forward(15)
        right(90)
        forward(30)
        left(90)
        forward(30)
        right(90)
        forward(15)

    end_fill()
    up()


def hopital_h():
    carre("noir")

    forward(18)
    left(90)
    forward(10)

    down()
    pensize(1)
    pencolor("black")
    fillcolor("black")

    begin_fill()

    # boucle pour le H
    for i in range(2):
        forward(85)
        right(90)
        forward(20)
        right(90)
        forward(33)
        left(90)
        forward(20)
        left(90)
        forward(33)
        right(90)
        forward(20)
        right(90)

    end_fill()
    up()


def circulation_sens_unique():
    carre("bleu")

    forward(32)
    left(90)
    forward(5)

    down()
    pencolor("black")
    fillcolor("white")

    begin_fill()

    forward(45)
    left(90)
    forward(20)
    right(130)
    forward(55)
    right(100)
    forward(55)
    right(130)
    forward(20)
    left(90)
    forward(45)
    right(90)
    forward(32)

    end_fill()
    up()



def panneaux_stop():
    octogone()

    left(90)
    forward(27)
    left(90)
    forward(23)

    pencolor("white")

    write("STOP", font=("L1", 25, "bold"))


def autoroute():
    carre("bleu")

    fillcolor("white")
    pensize(1)

    # deplacement au miliee du dessin
    forward(48)
    left(90)
    forward(100)
    left(180)
    forward(100)
    right(90)
    forward(47.5)
    right(180)

    # BAS GAUCHE

    # deplacement
    forward(18)
    left(90)
    forward(3.5)
    right(90)

    # bas gauche
    pencolor("white")
    down()
    begin_fill()

    forward(25.5)
    left(90)
    forward(48)
    left(90)
    forward(17)
    left(80)
    forward(50)

    end_fill()
    up()

    # BAS DROIT

    # deplacement
    horizontal()

    left(180)
    forward(18)
    right(180)
    forward(97)
    left(180)
    forward(18)

    # bas droit
    down()
    begin_fill()
    
    forward(25.5)
    right(90)
    forward(49)
    right(90)
    forward(17)
    right(80)
    forward(50)

    end_fill()
    up()
    
    # PONT

    # deplacement
    horizontal()
    forward(18)
    left(90)
    forward(53)
    left(90)
    forward(6)

    # pont
    down()
    begin_fill()

    forward(7)
    left(90)
    forward(13)
    right(90)
    forward(7)
    right(90)
    forward(13)
    left(90)
    forward(58)
    left(90)
    forward(13)
    right(90)
    forward(7)
    right(90)
    forward(13)
    left(90)
    forward(7)
    right(90)
    forward(7)
    right(90)
    forward(86)
    right(90)
    forward(7)

    end_fill()
    up()
    
    # HAUT DROIT

    # deplacement
    horizontal()

    forward(6)
    left(90)
    forward(10)
    left(90)
    forward(27)

    # haut droit
    down()
    begin_fill()

    forward(17)
    right(90)
    forward(32)
    right(90)
    forward(10)
    right(77)
    forward(34)

    end_fill()
    up()

    # HAUT GAUCHE

    # deplacement
    horizontal()
    forward(27)
    left(180)
    forward(97)
    right(90)
    forward(1)

    horizontal()

    forward(27)

    # haut gauche
    down()
    begin_fill()

    forward(17)
    left(90)
    forward(32)
    left(90)
    forward(10)
    left(77)
    forward(34)

    end_fill()
    up()

def interdiction_depasser():
    rond("blanc")

    left(90)
    forward(23)
    left(90)
    forward(27)
    right(180)

    voiture("rouge")

    horizontal()

    right(90)
    forward(11)
    left(90)
    forward(13)
    forward(12)

    voiture("noir")