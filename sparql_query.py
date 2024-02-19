#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:51:30 2024

@author: maxbld
"""

from rdflib import Graph

g = Graph()

g.parse("data/flux-19287-202401180748.ttl")

#%% Query all distinct classes

q = """
    SELECT DISTINCT ?classes
    WHERE {
        ?subject rdf:type ?classes .
    }
"""

q_response = g.query(q)

for row in q_response:
    print(f"{row.classes}")
    
#%% Query all Hotel entities

q = """
    SELECT DISTINCT ?subject
    WHERE {
        ?subject rdf:type <https://www.datatourisme.fr/ontology/core#Hotel> .
    }
"""

q_response = g.query(q)

for row in q_response:
    print(f"{row.subject}")
    
#%% Query all Restaurant entities

q = """
    SELECT DISTINCT ?subject
    WHERE {
        ?subject rdf:type <https://www.datatourisme.fr/ontology/core#Restaurant> .
    }
"""

q_response = g.query(q)

for row in q_response:
    print(f"{row.subject}")
    
#%% Query all PointOfInterest entities

q = """
    SELECT DISTINCT ?subject
    WHERE {
        ?subject rdf:type <https://www.datatourisme.fr/ontology/core#PointOfInterest> .
    }
"""

q_response = g.query(q)

for row in q_response:
    print(f"{row.subject}")