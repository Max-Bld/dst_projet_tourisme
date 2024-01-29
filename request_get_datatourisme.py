#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 08:01:28 2024

@author: maxbld
"""

import time
import requests
from rdflib import Graph

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