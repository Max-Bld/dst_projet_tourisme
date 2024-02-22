#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:29:43 2024

@author: maxbld

Affiche des informations à l'utilisateur.

Permet à l'utilsateur d'entrer des préférences qui modifieront
la requête SPARQL.

"""

from sys import exit
# from generate import latitude_user, longitude_user, perimetre_user

def interface_utilisateur(latitude_user, longitude_user, perimetre_user):
    
        # Géolocalisation de l'utilisateur
    
    entree=input("""Choisissez le mode de géolocalisation :
        
        (a) manuel
        (b) aléatoire
    """)
    
    if entree=="a": # manual
        try: 
            latitude_user = float(input("Choisissez une latitude : "))
            longitude_user = float(input("Choisissez une longitude : "))
        except:
            print("Mauvaise entrée.")
            exit()
            
    elif entree=="b": #random
    
        print(f"Ma géolocalisation générée aléatoirement dans le département de la Meuse : \n{latitude_user}, {longitude_user}")
    
    else:
        
        print("Mauvaise entrée.")
        exit()
    
        # Périmètre
    
    entree=input("""\nChoisissez le périmètre :
        
        (a) manuel
        (b) aléatoire
    """)
    
    if entree=="a":
    
        try:
            perimetre_user = int(input("\nPérimètre de déplacement : "))
        except:
            print("Mauvaise entrée.")
            exit()
    
    
    elif entree=="b":
        
        print(f"\nMon périmètre de déplacement généré aléatoirement : {perimetre_user}")
    
    else:
        
        print("Mauvaise entrée.")
        exit()
        
    
        # Préférences de l'utilisateur
        
    entree=input("""\nQue cherchez vous :
        (a) Restaurant
        (b) Hôtel
        (c) Point d'intérêt touristique
          """)
    
    if entree=="a":
        query_element="Restaurant"
    elif entree=="b":
        query_element="Hotel"
    elif entree=="c":
        query_element="PointOfInterest"
    else:
        print("Mauvaise entrée.")
        exit()
        
    return query_element
