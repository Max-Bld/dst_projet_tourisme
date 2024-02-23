#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:28:38 2024

@author: maxbld

Génère ou récupère les données de géolocalisation de l'utilisateur.

"""

import random

def generate_user_geo():
    
    latitude_user = 49.48
    longitude_user = 5.2
    perimetre_user = 20000
    
    return latitude_user, longitude_user, perimetre_user