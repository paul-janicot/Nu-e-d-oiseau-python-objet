#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:19:12 2022

@author: frederic
"""
from classe_vecteur import *
from random import random, randint, uniform
from math import sqrt

class Animal:
    """
    Attribut de classe :
        v_max : norme maximale du vecteur vitesse
        v_init : norme du vecteur vitesse lors de la création de l'objet
        force_max = force maximale s'exerçant sur l'animal. Pour un comportement réaliste,
                    un animal ne peut pas par exemple faire un demi-tour immédiatement
    Attributs :

        position :      vecteur de coordonnées x, y aléatoires, dans les limites de la fenêtre d'affichage
        vitesse :       vecteur  sous la forme d'une liste de flottants
        taille :        rayon en pixels de l'animal. C'est comme en physique, tout est
                         une sphère parfaite (ici un cercle puisqu'en 2D)
        perception :    liste des rayons de perception de l'animal. Noter que l'animal ne
            perçoit pas ce qui se passe derrière lui. On suppose qu'il a une
            vision à 300 degrés, soit +/- 150 degrés par rapport à sa direction.
            La liste comprend 3 éléments qui correspondent aux trois règles de déplacement.

    Méthodes :
        force_alea : crée une force de déplacement aléatoire qui va
                    s'appliquer sur l'animal
        maj_position : déplace l'animal suivant sa vitesse.
        distance : revoie la distance avec un autre Animal

    """
    v_max = 4
    v_init = 2
    force_max = 0.5




    def __init__(self, l_univers, h_univers):
        self.taille = 2
        self.l_univers = 100
        self.h_univers = 100

        x = randint( 10+self.taille , l_univers-(10+self.taille) )
        y = randint( 10+self.taille , h_univers-(10+self.taille) )



        self.position = Vecteur(x, y)
        self.vitesse = Vecteur(0, 0)

        # Modifier les deux lignes après le while
        while self.vitesse.est_nul() :          # génération d'une vitesse aléatoire
            self.vitesse.x = uniform(-1,1)
            self.vitesse.y = uniform(-1,1)
        self.vitesse.prodk(self.v_init/self.vitesse.norme()) # on met la norme de la vitesse à v_init
        self.perception = [25, 50, 100]     # separation, alignement, cohesion
        self.force = Vecteur(0, 0)

    def force_alea(self):
        self.force.x = uniform(-1,1)
        self.force.y = uniform(-1,1)


        # On maximisera la force aléatoire exercée, décommenter les lignes suivantes
        if self.force.norme() != 0 :
           self.force.prodk(self.force_max/self.force.norme())

    def maj_position(self):


        if self.vitesse.norme()>Animal.v_max:
            self.vitesse.prodk(Animal.v_max/self.vitesse.norme())

        if self.vitesse.norme()<Animal.v_init:
            self.vitesse.prodk(Animal.v_init/self.vitesse.norme())



        if (self.position.x<0):

            self.vitesse.x*=-1
            #self.position.x = 0

        if (self.position.x>900):
            self.vitesse.x*=-1
            #self.position.x = 900



        if (self.position.y<0):
            self.vitesse.y*=-1
            #self.position.y = 0

        if (self.position.y>900):
           # self.position.y = 900
            self.vitesse.y*=-1


        (self.position).somme(self.vitesse)
        (self.vitesse).somme(self.force)




        return


    def distance(self, autre):
        return sqrt(((self.position.x)-(autre.position.x))**2 + ((self.position.y)-(autre.position.y))**2)





    def __repr__(self):
        chaine = "Position : (" + str(self.position.x) + " , " + str(self.position.y) + ")\n"
        chaine += "Vitesse : (" + str(self.vitesse.x)  + " , " + str(self.vitesse.y) + ")\n"
        chaine += "Acceleration/force : (" + str(self.force.x)  + " , " + str(self.force.y) + ")\n"
        return chaine



