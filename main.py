#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:01:31 2024

@author: maxbld

Orchestre les différents modules.

"""

from generate import latitude_user, longitude_user, perimetre_user
from cli import interface_utilisateur
from extract import data
from query import sparql_query
# from compute import distances_euclidiennes
# from display import visualize_data

query_element = interface_utilisateur(latitude_user, longitude_user, perimetre_user)

flux_datatourisme = data

queried_flux = sparql_query(query_element, flux_datatourisme)

# computed_data = distances_euclidiennes(latitude_user, longitude_user, queried_flux)

# visualize_data(data, latitude_user, longitude_user, perimetre_user)