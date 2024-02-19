#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:51:30 2024

@author: maxbld
"""

from rdflib import Graph

g = Graph()

g.parse("data/flux-19287-202401180748.ttl")

# for subj, pred, obj in g:
#     if (subj, pred, obj) not in g:
#        raise Exception("It better be!")

print(f"Graph g has {len(g)} statements.")
print(g.serialize(format="turtle"))
