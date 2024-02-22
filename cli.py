#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:14:42 2024

With names displayed on the map

@author: maxbld
"""


import matplotlib.pyplot as plt
import random
#from distance_functions import distances_euclidiennes
import math
import time
import pandas as pd
import warnings 

warnings.filterwarnings("ignore") # filters out the warnings

#%% Data Loading

    # My random geolocalisation point and perimeter


def cli_test(data):


    entree=input("""Choisissez le mode de géolocalisation :
        
        (a) manuel
        (b) aléatoire
    """)


    latitude_user = 0
    longitude_user = 0
    perimetre_user = 0


    if entree=="a":
        
        # My manual geolocalisation point and perimeter
        
        latitude_user = float(input("Choisissez une latitude : "))
        longitude_user = float(input("Choisissez une longitude : "))
        perimetre_user = float(input("Choisissez le périmètre de la zone en mètres : "))

    elif entree=="b":

        # Random geolocalisation point and perimeter

        latitude_user = random.uniform(47.9,49.5)
        longitude_user = random.uniform(5.0,5.8)
        perimetre_user = random.uniform(7000,15000)
        
        print(f"Ma géolocalisation générée aléatoirement dans le département de la Meuse : \n{latitude_user}, {longitude_user}")
        print(f"\nMon périmètre de déplacement généré aléatoirement : \n{perimetre_user}")


    else:
        print("Mauvaise entrée.")
        exit()


    return latitude_user, longitude_user, perimetre_user
