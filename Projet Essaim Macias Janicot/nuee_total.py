# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 13:30:45 2022

@author: Fred
"""


import tkinter
import time
from random import randint, random
from math import sqrt, cos, sin, pi, asin, acos
from classe_nuee_chasse import *
from classe_predateur import *


LARGEUR_FENETRE = 800
HAUTEUR_FENETRE = 800
RAFRAICHISSEMENT = 0.01

def animate_ball(nuee, faucon):
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

    taille = faucon.taille
    sprite_p = canvas.create_oval(faucon.position.x - taille,
            faucon.position.y - taille,
            faucon.position.x + taille,
            faucon.position.y + taille,
            fill="red", outline="red",
            width=1)
    
    # Le cercle suivant, caché l'absence de frontière (outline = ''), permettra de générer
    # les explosions de proies. Il y a une option qui semble plus naturelle
    # pour ne pas afficher une forme qui existe (disabledoutline). J'ai la flemme
    # de tester
    boum = canvas.create_oval(50,50,100,100, outline = "", width = 2)

    # Variables pour l'explosion (!) d'une proie
    kaboom = False
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    t = 0
    
    while True :
        if faucon.duree_plane > faucon.t_entre_chasse :
            mange, indice, x_proie, y_proie = faucon.chasse(nuee)
            if mange :
                canvas.delete(sprites[indice])
                sprites.pop(indice)
                x1 = int(x_proie) - 2
                y1 = int(y_proie) - 2
                x2 = int(x_proie) + 2
                y2 = int(y_proie) + 2
                canvas.itemconfig(boum, outline = 'black')
                canvas.coords(boum, x1, y1, x2, y2)
                kaboom = True
        else :
            faucon.plane()
        nuee.mouvement(faucon)
        
        if kaboom :
            t += 1
            if t < 50 :
                x1 -= 1
                y1 -= 1
                x2 += 1
                y2 += 1
                canvas.coords(boum, x1, y1, x2, y2)
                canvas.itemconfig(boum, dash = (2, int((4 + 2*i)*2/5)))
            else :
                canvas.itemconfig(boum, outline = '')
                kaboom = False
                x1 = 0
                y1 = 0
                x2 = 0
                y2 = 0
                t = 0

        for i in range(len(nuee.essaim)) :
            #canvas.move(sprites[i], mvts[i].x , mvts[i].y)
            canvas.coords(sprites[i],
                          nuee.essaim[i].position.x - taille,
                          nuee.essaim[i].position.y - taille,
                          nuee.essaim[i].position.x + taille,
                          nuee.essaim[i].position.y + taille)
            canvas.coords(sprite_p,
                          faucon.position.x - taille,
                          faucon.position.y - taille,
                          faucon.position.x + taille,
                          faucon.position.y + taille)

        fenetre.update()
        time.sleep(RAFRAICHISSEMENT)



l_univers = LARGEUR_FENETRE - 100
h_univers = HAUTEUR_FENETRE - 100
nuee = Nuee(50, l_univers, h_univers)       # nombre d'animaux à modifier suivant puissance de l'ordi
faucon = Predateur(l_univers, h_univers)


fenetre = tkinter.Tk()
fenetre.title("Nuée d'oiseaux / banc de poisson / essaim d'insectes")
fenetre.geometry(f'{LARGEUR_FENETRE}x{HAUTEUR_FENETRE}')

canvas = tkinter.Canvas(fenetre, width = l_univers, height = h_univers, bg = "cyan")
canvas.pack(anchor = tkinter.CENTER, expand=True)


animate_ball(nuee, faucon)
