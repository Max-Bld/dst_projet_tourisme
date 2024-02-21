#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 18:55:47 2024

@author: maxbld
"""
from numpy import sqrt

def distances_euclidiennes(data):
    mylatlon=data[-1]
    distances=[]
    
    for n in data[:-1]:
        distances.append(sqrt((n[0]-mylatlon[0])**2 + (n[1]-mylatlon[1])**2))
        
    return distances