#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:30:02 2024

@author: maxbld

Génère de nouvelles données à partir des données existantes
(géolocalisation de l'utilisateur, données du flux de 
datatourisme).

"""

from query import data_flux
from numpy import sqrt

def distances_euclidiennes(data):
    mylatlon=data[-1]
    distances=[]
    
    for n in data[:-1]:
        distances.append(sqrt((n[0]-mylatlon[0])**2 + (n[1]-mylatlon[1])**2))
        
    return distances

distances=distances_euclidiennes(data_flux)
