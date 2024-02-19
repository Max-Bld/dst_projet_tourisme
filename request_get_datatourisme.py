#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 08:01:28 2024

@author: maxbld
"""

import requests
from rdflib import Graph


print("Requesting to: https://diffuseur.datatourisme.fr/webservice/a0aebcf1f3da8ee3bb42b5c764501413/893b3ad7-8ff3-49ed-a6ef-ad2aa777b7c9 ...")
r = requests.get('https://diffuseur.datatourisme.fr/webservice/a0aebcf1f3da8ee3bb42b5c764501413/893b3ad7-8ff3-49ed-a6ef-ad2aa777b7c9')

g = Graph()
g = g.parse(r.content)
print(g.serialize(format="turtle"))

#%% SPARQL query

query = """
CONSTRUCT { 
  ?res <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <urn:resource>. 
} WHERE { 
<http://www.bigdata.com/queryHints#Query> <http://www.bigdata.com/queryHints#optimizer> "None".
  ?res <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://www.datatourisme.fr/ontology/core#PointOfInterest>.
  ?res <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?65b7e1d2ec536.
  VALUES (?65b7e1d2ec536) {
    (<https://www.datatourisme.fr/ontology/core#CulturalSite>)
  }
  ?res <https://www.datatourisme.fr/ontology/core#isLocatedAt> ?65b7e1d2ec5e2.
  ?65b7e1d2ec5e2 <http://schema.org/address> ?65b7e1d2ec65d.
  ?65b7e1d2ec65d <https://www.datatourisme.fr/ontology/core#hasAddressCity> ?65b7e1d2ec6c5.
  ?65b7e1d2ec6c5 <https://www.datatourisme.fr/ontology/core#isPartOfDepartment> ?65b7e1d2ec728.
  VALUES (?65b7e1d2ec728) {
    (<https://www.datatourisme.fr/resource/core#France4455>)
  }
}
"""
#%%


for n in g(query):
    print(n)
    

#%%

g = Graph().parse('https://diffuseur.datatourisme.fr/webservice/a0aebcf1f3da8ee3bb42b5c764501413/893b3ad7-8ff3-49ed-a6ef-ad2aa777b7c9')

for n in g(query):
        print(n)    