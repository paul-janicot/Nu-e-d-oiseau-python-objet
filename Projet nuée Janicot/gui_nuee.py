# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 13:30:45 2022

@author: Fred
"""


import tkinter
import time
from random import randint, random
from math import sqrt, cos, sin, pi, asin, acos
from classe_nuee import *


LARGEUR_FENETRE = 1000
HAUTEUR_FENETRE = 1000
RAFRAICHISSEMENT = 0.01

def animate_ball(nuee):
    global canvas, fenetre

    taille = nuee.essaim[0].taille
    sprites = []
    for i in range(len( nuee.essaim)):
         sprites.append(canvas.create_oval(nuee.essaim[i].position.x - taille,
            nuee.essaim[i].position.y - taille,
            nuee.essaim[i].position.x + taille,
            nuee.essaim[i].position.y + taille,
            fill="Black", outline="Black",
            width=1))

    # Test des voisins : enlever les triples guillemets pour le bloc ci-dessous

    canvas.itemconfig(sprites[0], fill='green3', outline = "green3",
                      width = 2)
    cercle_0 = canvas.create_oval(
            nuee.essaim[0].position.x - nuee.essaim[0].perception[0],
            nuee.essaim[0].position.y - nuee.essaim[0].perception[0],
            nuee.essaim[0].position.x + nuee.essaim[0].perception[0],
            nuee.essaim[0].position.y + nuee.essaim[0].perception[0],
            outline="deep pink", width=1)
    cercle_1 = canvas.create_oval(
            nuee.essaim[0].position.x - nuee.essaim[0].perception[1],
            nuee.essaim[0].position.y - nuee.essaim[0].perception[1],
            nuee.essaim[0].position.x + nuee.essaim[0].perception[1],
            nuee.essaim[0].position.y + nuee.essaim[0].perception[1],
            outline="lightpink", width=1)
    cercle_2 = canvas.create_oval(
            nuee.essaim[0].position.x - nuee.essaim[0].perception[2],
            nuee.essaim[0].position.y - nuee.essaim[0].perception[2],
            nuee.essaim[0].position.x + nuee.essaim[0].perception[2],
            nuee.essaim[0].position.y + nuee.essaim[0].perception[2],
            outline="magenta", width=1)


    while True :

        mvts = nuee.mouvement()
        if len(mvts) != len(sprites):

            raise IndexError("pas le même nombre de sprites et d'animaux")

        # Test des voisins : enlever les triples guillemets pour le bloc ci-dessous

        mat_sep, mat_align, mat_coh = nuee.voisins()
        for i in range(1, len(mat_sep)):
            if mat_sep[0][i] :
                canvas.itemconfig(sprites[i], fill='deep pink', outline = 'deep pink', width = 1)
            elif mat_align[0][i] :
                canvas.itemconfig(sprites[i], fill='lightpink', outline = 'lightpink', width = 1)
            elif mat_coh[0][i] :
                canvas.itemconfig(sprites[i], fill='magenta', outline = 'magenta', width = 1)
            else :
                canvas.itemconfig(sprites[i], fill='black', outline="Black", width=1)

        for i in range(len(mvts)) :
            #canvas.move(sprites[i], mvts[i].x , mvts[i].y)   # non fonctionnel (erreurs d'arrondi
                                                                # s'accumulant)
            canvas.coords(sprites[i],
                          nuee.essaim[i].position.x - taille,
                          nuee.essaim[i].position.y - taille,
                          nuee.essaim[i].position.x + taille,
                          nuee.essaim[i].position.y + taille)
        # Test des voisins : enlever les triples guillemets pour le bloc ci-dessous

        canvas.coords(cercle_0,
                      nuee.essaim[0].position.x - nuee.essaim[0].perception[0],
                      nuee.essaim[0].position.y - nuee.essaim[0].perception[0],
                      nuee.essaim[0].position.x + nuee.essaim[0].perception[0],
                      nuee.essaim[0].position.y + nuee.essaim[0].perception[0])
        canvas.coords(cercle_1,
                      nuee.essaim[0].position.x - nuee.essaim[0].perception[1],
                      nuee.essaim[0].position.y - nuee.essaim[0].perception[1],
                      nuee.essaim[0].position.x + nuee.essaim[0].perception[1],
                      nuee.essaim[0].position.y + nuee.essaim[0].perception[1])
        canvas.coords(cercle_2,
                      nuee.essaim[0].position.x - nuee.essaim[0].perception[2],
                      nuee.essaim[0].position.y - nuee.essaim[0].perception[2],
                      nuee.essaim[0].position.x + nuee.essaim[0].perception[2],
                      nuee.essaim[0].position.y + nuee.essaim[0].perception[2])

        fenetre.update()
        time.sleep(RAFRAICHISSEMENT)

l_univers = LARGEUR_FENETRE - 100
h_univers = HAUTEUR_FENETRE - 100
nuee = Nuee(20, l_univers, h_univers)       # nombre d'animaux à modifier suivant puissance de l'ordi


fenetre = tkinter.Tk()
fenetre.title("Nuée d'oiseaux / banc de poisson / essaim d'insectes")
fenetre.geometry(f'{LARGEUR_FENETRE}x{HAUTEUR_FENETRE}')

canvas = tkinter.Canvas(fenetre, width = l_univers, height = h_univers, bg = "cyan")
canvas.pack(anchor = tkinter.CENTER, expand=True)

animate_ball(nuee)