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
        (c) data
    """)

    if entree=="a":
        
        # My manual geolocalisation point and perimeter
        
        latitude = float(input("Choisissez une latitude : "))
        longitude = float(input("Choisissez une longitude : "))
        perimetre = float(input("Choisissez le périmètre de la zone : "))

    elif entree=="b":

        latitude = random.uniform(47.9,49.5)
        longitude = random.uniform(5.0,5.8)
        perimetre = random.uniform(0.2,0.3)
        
        print(f"Ma géolocalisation générée aléatoirement dans le département de la Meuse : \n{latitude}, {longitude}")
        print(f"\nMon périmètre de déplacement généré aléatoirement : \n{perimetre}")

    elif entree=="c":

        for i in data:
            print("\n\n\n Nom du restaurant :",i.name)
            print("\n Latitude : ",i.lat)
            print("\n Longitude :",i.lon)

    else:
        print("Mauvaise entrée.")
        exit()

    #maLatLon = (latitude, longitude)
