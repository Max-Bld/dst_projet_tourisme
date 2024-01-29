#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 08:01:28 2024

@author: maxbld
"""

import time
import requests
from rdflib import Graph
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import networkx as nx
import matplotlib.pyplot as plt


print("Requesting to: https://diffuseur.datatourisme.fr/webservice/a0aebcf1f3da8ee3bb42b5c764501413/893b3ad7-8ff3-49ed-a6ef-ad2aa777b7c9 ...")
r = requests.get('https://diffuseur.datatourisme.fr/webservice/a0aebcf1f3da8ee3bb42b5c764501413/893b3ad7-8ff3-49ed-a6ef-ad2aa777b7c9')
time.sleep(1)
print("Status code:", r.status_code)
time.sleep(1)
print("Content type:", r.headers['content-type'])
time.sleep(1)
g = Graph()
g.parse(r.content) 
print(f"Graph g has {len(g)} statements.")
print("Content in Turtle:")
time.sleep(1)
print(g.serialize(format="turtle"))

#%% Visualisation
result = g.parse(r.content, format='turtle')
G = rdflib_to_networkx_multidigraph(result)

# Plot Networkx instance of RDF Graph
pos = nx.spring_layout(G, scale=2)
edge_labels = nx.get_edge_attributes(G, 'r')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw(G, with_labels=True)

#if not in interactive mode for 
plt.show()