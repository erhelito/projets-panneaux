from turtle import*
from panneaux import*

# preparation de l'affichage
resetscreen()
speed(1000000000)
screensize(2000,5000)
up()

# fonction de reinitialisation du stylo
def position():
    setposition(-300,150)
    horizontal()
    pensize(1)
    pencolor("black")

# deplacement du stylo pour l'affichage du texte
def position_texte():
    setposition(-700,175)
    horizontal()
    pensize(1)
    pencolor("black")


# panneau priorite par rapport a la circulation inverse
position()
priorite_circulation_inverse()

# panneau impasse
position()
forward(150)
impasse() 

# panneau circulation a sens unique
position()
forward(300)
circulation_sens_unique()

# panneau parking
position()
forward(450)
parking()

# panneau autoroute
position()
right(90)
forward(150)
horizontal()
autoroute()

# panneau hopital (urgences)
position()
right(90)
forward(150)
horizontal()
forward(150)
hopital_croix()

# panneau hopital
position()
right(90)
forward(150)
horizontal()
forward(300)
hopital_h()

# panneau retrecissement de voie
position()
right(90)
forward(300)
horizontal()
retrecissement()

# panneau ceder le passage a droite
position()
right(90)
forward(300)
horizontal()
forward(150)
ceder_passage_droite()

# panneau d'intersection prioritaire
position()
right(90)
forward(300)
horizontal()
forward(300)
intersection_prioritaire()

# panneau de signal de position
position()
right(90)
forward(195)
horizontal()
forward(550)
triangle_inverse()

# panneau de circulation interdite
position()
right(90)
forward(450)
horizontal()
forward(50)
circulation_interdite()

# panneau sens interdit
position()
right(90)
forward(450)
horizontal()
forward(200)
sens_interdit()

# panneau de limitation de vitesse a 50 km/h
position()
right(90)
forward(450)
horizontal()
forward(350)
limitation_50()

# panneau de fin d'interdicion ou de limitation
position()
right(90)
forward(450)
horizontal()
forward(500)
fin_interdiction()

# panneau de route prioritaire
position()
right(90)
forward(650)
horizontal()
forward(50)
losange()

# panneau de fin de route prioritaire
position()
right(90)
forward(650)
horizontal()
forward(250)
losange_barre()

# panneau stop
position()
right(90)
forward(650)
horizontal()
forward(400)
color("black")
down()
panneaux_stop()

# panneau obligation tourner a droite
position()
right(90)
forward(850)
horizontal()
forward(50)
obligation_tourner_droite()

# panneau obligation contournement par la gauche
position()
right(90)
forward(850)
horizontal()
forward(200)
contourner_gauche()

# panneau obligation tourner a gauche
position()
right(90)
forward(850)
horizontal()
forward(350)
tourner_gauche()

# panneau interdiction de depasser
position()
right(90)
forward(850)
horizontal()
forward(500)
interdiction_depasser()



# ecriture des indications
position_texte()
write("Panneaux bonus + idéogrammes\n+ panneaux challenge :", font=("L1", 20, "normal"))

position_texte()
right(90)
forward(300)
horizontal()
write("Panneaux danger ou priorités :", font=("L1", 20, "normal"))

position_texte()
right(90)
forward(450)
horizontal()
write("Panneaux d'interdiction ou\nfin d'interdiction :", font=("L1", 20, "normal"))

position_texte()
right(90)
forward(650)
horizontal()
write("Panneaux stop et priorité :", font=("L1", 20, "normal"))

position_texte()
right(90)
forward(850)
horizontal()
write("Panneaux d'obligation\n+ challenge :", font=("L1", 20, "normal"))

# fin de l'affichage
ht()
exitonclick()