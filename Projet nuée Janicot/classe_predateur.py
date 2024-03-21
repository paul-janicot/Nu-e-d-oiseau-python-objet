#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 17:38:28 2022

@author: frederic
"""
# Créé par mandon, le 04/10/2022 en Python 3.7
import classe_animal as a
from classe_vecteur import *
from random import randint, random
from math import inf as infini

class Predateur(a.Animal):
    v_max = 5
    v_init = 1
    force_max = 1.5
    max_vit_max = 75
    max_vol_m_dir = 200

    def __init__(self, l_univers, h_univers):
        super().__init__(l_univers, h_univers)
        self.taille = 4
        self.duree_vit_max = 0
        self.en_chasse = False
        self.proie = None
        self.t_entre_chasse = randint(200, 1000)
        self.duree_plane = 0
        self.duree_vol_m_dir = 0

    def plane(self):
        self.duree_plane += 1
        self.duree_vol_m_dir += 1
        
        self.maj_position()

    def trouve_proie(self, nuee):
        d = infini
        

    def chasse(self, nuee):
        if self.duree_vit_max > self.max_vit_max :  # arrêt de la chasse
            self.en_chasse = False

        return False, None, None, None



