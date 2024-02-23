#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:29:53 2024

@author: maxbld

Récupère les données .ttl et les parse

"""

from rdflib import Graph

data = Graph()

data.parse('C:\\Users\\Mejri Wissem\\Downloads\\flux-19287-202401180748.ttl', format='ttl')