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
from extract_data import results

warnings.filterwarnings("ignore") # filters out the warnings


#%% Data Loading

    # My random geolocalisation point and perimeter

entree=input("""Choisissez le mode de géolocalisation :
    
    (a) manuel
    (b) aléatoire
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

else:
    print("Mauvaise entrée.")
    exit()

maLatLon = (latitude, longitude)

    # Locations dataset (fake or real)

data = results # va contenir le jeu de données



entree2=input("""
Voici les jeux de données, cliquez pour continuer :
    
""")


for i in data:
    print("\n\n\n Nom du restaurant :",i.name)
    print("\n Latitude : ",i.lat)
    print("\n Longitude :",i.lon)

# Fake geolocalisation dataset
"""
fake_geo_data = []

for n in range(30):
    latitude = random.uniform(-90,90)
    longitude = random.uniform(-180,180)
    fake_geo_data.append((latitude, longitude))
data = fake_geo_data

print("\nLes coordonnées des points qui vont être affichés sur la carte :")
time.sleep(2)
for n in data:
    print(n)
    time.sleep(0.01)"""