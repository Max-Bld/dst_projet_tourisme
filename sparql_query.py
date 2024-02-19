#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:51:30 2024

@author: maxbld
"""

from rdflib import Graph
from pprint import pprint

g = Graph()

g.parse("data/flux-19287-202401180748.ttl")

q = """
    SELECT DISTINCT ?class
    WHERE {
        ?subject rdf:type ?class .
    }
"""

q_response = g.query(q)

#%%
for row in q_response:
    print(row)