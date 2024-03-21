#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 09:35:42 2022

@author: frederic
"""
from classe_animal import *
from classe_vecteur import *
from random import random, randint

class Nuee:
    """
    Attribut de classe :
        vecteur_nul : comme son nom l'indique, objet de type Vecteur égal au vecteur nul
        max_voisins : nombre maximum de voisins. Non utilisé
    Attributs :
        essaim : liste d'objets de type Animal. Le nombre est donné en paramètre du constructeur
        l_univers, h_univers : entiers, largeur et hauteur
            de l'univers/la grille (en pixels) dans laquelle évolue la nuée
        force_vent : une force qui change de temps en temps, qui exprime un vent
                ou une direction dominante à suivre pour l'essaim
    Méthodes :
        mouvement :
            Met à jour la position de tous les animaux de la nuée
        regles :
            Applique à chaque animal les réègles de séparation, cohésion et alignement
        voisins :
            Etant donnée une distance de voisinage, renvoie trois listes de tous
            les voisins de chaque animal. Il y a une liste par distance de perception :
            une pour la distance de séparation, une pour la distance d'alignement, et
            une pour la distance de cohésion.
            Ces listes sont sous la forme d'une liste de liste de
            booléens : booléen[i][j] est vrai si l'animal i a pour voisin j.
            Attention ces matrices ns pas symétriques, si l'on considère que
            les animaux ont un champ de vision de moins de 360 degrés.
        separation : permet aux animaux de ne pas s'approcher trop près. Pour
            chaque animal, l'éloigne des animaux trop proches
        alignement : permet aux animaux d'aller dans la même direction.
            Chaque animal se rapproche de la direction moyenne de ses voisins
        cohesion : permet aux animaux de se rapprocher.
            Chaque animal se rapproche de la position moyenne de ses voisins
        centripete : modifie les vitesses des animaux.
        fuite : en présence d'un prédateur, le fuit à un angle aléatoire entre
            -90 et +90 degrés. Annule toutes les modifications dues aux fonctions
            séparation, alignement et cohésion

    """

    max_voisins = 10            # non utilisé dans cette version
    vecteur_nul = Vecteur(0, 0) # non utilisé dans cette version

    def __init__(self,nombre, l_univers, h_univers):
        self.essaim = []
        for i in range (nombre):
            self.essaim.append(Animal(l_univers,h_univers))
        '''
        self.force_vent = Vecteur(random()*2 - 1, random()*2 - 1)
        while self.force_vent == 0 :
            self.force_vent = Vecteur(random()*2 - 1, random()*2 - 1)
        self.force_vent.prodk(self.essaim[0].force_max/self.force_vent.norme())
        #print(self.force_vent)
        self.force_vent.prodk(1/20)
        '''

    def mouvement(self):

        for i in (self.essaim):
            #i.force_alea()
            self.regles(i)
            i.maj_position()



        return self.essaim



    def regles(self, animal):

        '''
        if randint(1, 100) == 1 :
            self.force_vent = Vecteur(random()*2 - 1, random()*2 - 1)
            while self.force_vent == 0 :
                self.force_vent = Vecteur(random()*2 - 1, random()*2 - 1)
            self.force_vent.prodk(self.essaim[0].force_max/self.force_vent.norme())
            print(self.force_vent)
            self.force_vent.prodk(1/20)
        '''

        vois_sep, vois_align, vois_coh = self.voisins()

        for i in range(len(self.essaim)) :

            force_alignement = self.alignement(self.essaim[i], vois_align[i])
            force_alignement.prodk(1/8)
            animal.force.somme(force_alignement)

            '''
            force_cohesion = self.cohesion(self.essaim[i], vois_coh[i])
            force_cohesion.prodk(1/100)
            animal.force.somme(force_cohesion)
            '''

            '''
            force_separation = self.separation(self.essaim[i], vois_sep[i])
            force_separation.prodk(1/10)
            animal.force.somme(force_separation)
            '''



            if self.essaim[i].force.norme() != 0 :
                self.essaim[i].force.prodk(self.essaim[i].force_max/self.essaim[i].force.norme())

            '''
            force_centripete = self.centripete(self.essaim[i])
            force_centripete.prodk(1/700)
            animal.force.somme(force_centripete)
            '''




        return





    def voisins(self) :

        vois_sep = []
        vois_align = []
        vois_coh = []

        for i in range (len(self.essaim)):

            vois_align.append([''])
            vois_sep.append([''])         #on crée les matrices
            vois_coh.append([''])

            #vois_align[i][0]=self.essaim[i]
            #vois_sep[i][0]=self.essaim[i]       #dans la premiere cas de chaque ligne se trouve l'animal concerné
            #vois_coh[i][0]=self.essaim[i]

            conditions_align=[]
            conditions_sep=[]                   #dans ces listes vont se trouver les booléens qui précise si l'animal va subir des forces ou non. Il va y en avoir autant qu'il y a d'animaux dans l'essaim.
            conditions_coh=[]                   #Par exemple si l'oiseau [0] se trouve à 50 pixel de l'oiseau[1], conditions_align = [False,True,False,False] (pour un essaim de 4 animaux)
                                                #On ne sait pas si c'était la bonne méthode et si elle n'est pas trop longue donc responsable du crash du programme gui.nuee.py
            for j in range(len(self.essaim)):

                if ((Animal.distance(self.essaim[i],self.essaim[j])) < (self.essaim[i].perception[1]) ) and self.essaim[i]:           #align
                    conditions_align.append(True)
                else:
                    conditions_align.append(False)

                if  (Animal.distance(self.essaim[i],self.essaim[j])) < (self.essaim[i].perception[0]):          #sep
                    conditions_sep.append(True)
                else:
                    conditions_sep.append(False)

                if (Animal.distance(self.essaim[i],self.essaim[j])) < (self.essaim[i].perception[2]):          #coh
                    conditions_coh.append(True)
                else:
                    conditions_coh.append(False)


            vois_align[i]=conditions_align
            vois_sep[i]=conditions_sep
            vois_coh[i]=conditions_coh


        return vois_sep, vois_align, vois_coh



    def alignement(self, animal, liste_vois) :

        force_alignement = Vecteur(0, 0)


        s_poids=0

        for i in range(len(self.essaim)):

            if liste_vois[i] == True:
                force_alignement.somme(self.essaim[i].vitesse)
                s_poids+=1



        if s_poids != 0:
            force_alignement.prodk((1/s_poids))
            force_alignement.diff(animal.vitesse)
        else:
            print('nombre de voisins = 0')

        return force_alignement




    def separation(self, animal, liste_vois):
        force_separation = Vecteur(0, 0)
        for i in range(len(self.essaim)):
            if liste_vois[i] == True:
                force_separation.somme(Vecteur((animal.position.x - self.essaim[i].position.x),(animal.position.y - self.essaim[i].position.y)))



        return force_separation




    def cohesion(self, animal, liste_vois):

        force_cohesion = Vecteur(0, 0)

        s_poids=0

        for i in range(len(self.essaim)):

            if liste_vois[i] == True:
                force_cohesion.somme(self.essaim[i].position)
                s_poids+=1



        if s_poids != 0:
            force_cohesion.prodk((1/s_poids))
            force_cohesion.diff(animal.vitesse)
        else:
            print('nombre de voisins = 0')

        return force_cohesion



    def centripete(self, animal):

        force_centripete = Vecteur(-animal.vitesse.x, -animal.vitesse.y)

        return force_centripete




gregoire=Animal(100,100)

Essaim_gregoire=Nuee(6,100,100)

vois_sep, vois_align, vois_coh = Essaim_gregoire.voisins()

#print(gregoire)
#print(vois_align[1])


print(gregoire.vitesse)






