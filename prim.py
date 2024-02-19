#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:06:27 2024

@author: maxbld
"""

from rdflib import Graph
import requests
from pprint import pprint
import pandas as pd
import json
import matplotlib.pyplot as plt

r = requests.get("https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/line_reports/", headers={"apiKey":"VP3jZPCpid41BDj2Iy5YUV5nmDV62jfy"})

print("Status code:", r.status_code)
print("Content type:", r.headers['content-type'])

data=(r).json()

pprint(data, depth=2)


plt.scatter(data["regions"][0]["shape"])


#%%

r2 = requests.get("https://api.navitia.io/v1/coverage/sandbox/lines", headers={"Authorization: 53db3ab2-e8b4-4ba0-8847-5bbeb1b6dc16"})
