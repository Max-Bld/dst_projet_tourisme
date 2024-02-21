#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:51:30 2024

@author: maxbld
"""
import rdflib
from rdflib import Graph
import os

g = Graph()

g.parse("data/flux-19287-202401180748.ttl")
#%%
for ns in g.namespaces():
    print(ns)
#%%

q = """

    SELECT DISTINCT ?subject
    WHERE {
        ?subject rdf:type core:Region .
    }
    """

q_response = g.query(q)

for row in q_response:
    print(f"{row.subject}")
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
    
#%% Query one entity
#%%% Classes it belongs to

q = """
    SELECT ?c
    WHERE {
        <https://data.datatourisme.fr/10/ff109d76-1293-3d06-b324-7e4ee19f1cf4> rdf:type ?c.
    }
"""

q_response = g.query(q)

for row in q_response:
    print(f"{row.c}")
    
#%%% Relationships

q = """
    SELECT DISTINCT ?r
    WHERE {
        <https://data.datatourisme.fr/10/ff109d76-1293-3d06-b324-7e4ee19f1cf4> ?r ?c.
    }
"""

q_response = g.query(q)

for row in q_response:
    print(f"{row.r}")
    
#%%% Description

q = """
    SELECT ?result
    WHERE {
        <https://data.datatourisme.fr/10/ff109d76-1293-3d06-b324-7e4ee19f1cf4> <https://www.datatourisme.fr/ontology/core#hasDescription> ?description.
        ?description <https://www.datatourisme.fr/ontology/core#shortDescription> ?result.
    }
"""

q_response = g.query(q)

for row in q_response:
    print(f"{row.result}")
    
description = str(row.result)
    
#%%% Name

q = """
    SELECT ?label
    WHERE {
        <https://data.datatourisme.fr/10/ff109d76-1293-3d06-b324-7e4ee19f1cf4> rdfs:label ?label.
        
    }
"""

q_response = g.query(q)

for row in q_response:
    print(f"{row.label}")
    
name = str(row.label)
    
#%%% Géolocalisation et addresse

q = """
    SELECT ?lat ?lon
    WHERE {
        <https://data.datatourisme.fr/10/ff109d76-1293-3d06-b324-7e4ee19f1cf4> <https://www.datatourisme.fr/ontology/core#isLocatedAt> ?localisationuri.
        ?localisationuri <http://schema.org/geo> ?geouri.
        ?geouri <http://schema.org/latitude> ?lat ; <http://schema.org/longitude> ?lon.
        
    }
"""

q_response = g.query(q)

for row in q_response:
    print(f"{row.lat} {row.lon}")
    
latitude=str(row.lat)
longitude=str(row.lon)
    
#%%

import folium

from folium import Popup

m = folium.Map([latitude, longitude], zoom_start=12)

html = f"""
    <h1> {name}</h1>    
    <p>
    {description}
    </p>
    """

folium.Marker(
    location=[latitude, longitude],
    tooltip=name,
    popup=html,
    icon=folium.Icon(icon="home"),
).add_to(m)

m.save("dst_map_example.html")

#%%

# Récupérer toutes les données géographiques de la BDD

q = """
    SELECT ?lat ?lon
    WHERE {
        ?subject core:isLocatedAt ?localisationuri.
        ?localisationuri schema1:geo ?geouri.
        ?geouri schema1:latitude ?lat ; schema1:longitude ?lon.
        
    }
"""

q_response = g.query(q)

if os.path.isfile("geoloc_datatourisme_query.txt"):
    os.remove("geoloc_datatourisme_query.txt")

for row in q_response:
    print(f"{row.lat} {row.lon}") 
    with open('geoloc_datatourisme_query.txt', 'a') as f:
        f.writelines(f"{row.lat},{row.lon}\n")
        
#%%

# Restaurants: nom et géoloc dans un CSV

q = """
    SELECT ?name ?lat ?lon
    WHERE {
        ?restaurant rdf:type core:Restaurant.
        ?restaurant rdfs:label ?name.
        ?restaurant core:isLocatedAt ?localisationuri.
        ?localisationuri schema1:geo ?geouri.
        ?geouri schema1:latitude ?lat ; schema1:longitude ?lon.
        
    }
"""

q_response = g.query(q)

if os.path.isfile("datatourisme_restaurants_geoloc.csv"): # supprime le fichier si il existe
    os.remove("datatourisme_restaurants_geoloc.csv")


with open('datatourisme_restaurants_geoloc.csv', 'a') as f:
    f.writelines("nom;latitude;longitude\n")

for row in q_response:
    print(f"{row.name};{row.lat};{row.lon}")
    with open('datatourisme_restaurants_geoloc.csv', 'a') as f:
        f.writelines(f"{row.name};{row.lat};{row.lon}\n")