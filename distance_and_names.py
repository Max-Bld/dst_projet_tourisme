#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:14:42 2024

With names displayed on the map

@author: maxbld
"""


import matplotlib.pyplot as plt
import random
from distance_functions import distances_euclidiennes
import math
import time
import pandas as pd
import warnings 

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

data = [] # va contenir le jeu de données

entree2=input("""
Choisissez le mode de génération du jeu de données :
    
    (a) aléatoire
    (b) liste de tuples (.txt)
    (c) fichier .csv
""")

if entree2=="a":

        # Fake geolocalisation dataset

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
        time.sleep(0.01)

elif entree2=="b":

    # Real DATAtourisme dataset

        # Lat-Lon tuples

    print("\nLes coordonnées des points qui vont être affichés sur la carte :")
    time.sleep(2)
    
    with open("geoloc_datatourisme_query.txt", "r") as f:
        for line in f:
            couple_lat_lon = tuple(map(float, line.split(',')))
            data.append(couple_lat_lon)
            print(couple_lat_lon)
            time.sleep(0.01)

    data.append(maLatLon)

elif entree2=="c":

            # csv file
    
    df = pd.read_csv("datatourisme_restaurants_geoloc.csv", sep=";")
    print("\nVoici quelques établissements qui vont être affichés sur la carte :")
    print("\n", df.head(20))
    
    df = df.append({"nom":"ma géolocalisation", "latitude":latitude, "longitude":longitude}, ignore_index=True)
    data = df[["latitude", "longitude"]].values.tolist()
    
else:
    print("Mauvaise entrée")
    exit()

#%% Euclidean Distances

distances=distances_euclidiennes(data)
affichage=sum(distances)/len(distances)

minimum_distance=min(distances)

shortest_distance_point = data[distances.index(minimum_distance)]

#%% Data Visualisation

input("\nAppuyez sur une touche pour afficher la carte.")

w=1/math.cos(math.radians(60.0)) # permet un ratio correct pour l'affichage géographique

lat, lon = zip(*data)

    # avec le fichier csv, on affiche les noms

if entree2=="c":
    figure, axes = plt.subplots()
    cercle = plt.Circle(maLatLon, perimetre, edgecolor='black', alpha=0.2)
    plt.scatter(lat[:-1], lon[:-1])
    plt.scatter(lat[-1], lon[-1], marker="*")
    plt.plot([lat[-1], shortest_distance_point[0]], [lon[-1], shortest_distance_point[1]])
    axes.add_artist(cercle)
    axes.set_aspect(w)
    
    # plt.xlim(lat[-1]-(affichage),lat[-1]+(affichage))
    # plt.ylim(lon[-1]-(affichage),lon[-1]+(affichage))
    plt.annotate("Ma géolocalisation", (lat[-1]+(affichage/20), lon[-1]-(affichage/20)))
    for n in range(len(data[:-1])):
        plt.annotate(f"{df['nom'][n]}", (data[n][0]+(affichage/20), data[n][1]-(affichage/20)), color="darkgrey")
    plt.title(f"{df['nom'][distances.index(minimum_distance)]} est l'établissement le plus proche\n à une distance de {round(minimum_distance, 2)} km.")
    plt.grid()
    plt.show()
    
    # Sinon on a que le numéro des points
    
else:
    figure, axes = plt.subplots()
    cercle = plt.Circle(maLatLon, perimetre, edgecolor='black', alpha=0.2)

    plt.scatter(lat[:-1], lon[:-1])
    plt.scatter(lat[-1], lon[-1], marker="*")
    plt.plot([lat[-1], shortest_distance_point[0]], [lon[-1], shortest_distance_point[1]])
    axes.add_artist(cercle)
    axes.set_aspect(1)

    # plt.xlim(lat[-1]-(affichage),lat[-1]+(affichage))
    # plt.ylim(lon[-1]-(affichage),lon[-1]+(affichage))
    plt.annotate("Ma géolocalisation", (lat[-1]+(affichage/20), lon[-1]-(affichage/20)))
    for n in range(len(data[:-1])):
        plt.annotate(f"Point {n}", (data[n][0]+(affichage/20), data[n][1]-(affichage/20)), color="darkgrey")
    plt.title(f"Le point le plus proche est le point {distances.index(minimum_distance)} à une distance de {round(minimum_distance, 2)*10} km.")
    plt.grid()
    plt.show()