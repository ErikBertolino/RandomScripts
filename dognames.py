# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 22:45:27 2021

@author: Erik Bertolino


"""
from Levenshtein import distance as levenshtein_distance
import numpy as np
import pandas as pd

def calculateLevenshteinDistance(l,s):

    #Input: l - list of strings
    #Input: s - a certain string    
    #Output: vector v of distances between string s and every element in list l
    
    
    v = np.zeros(0)
    for i in range(len(l)):
        dist = levenshtein_distance(l[i],s)
        v = np.append(v,dist)
    
    return v



DOG_NAMES = pd.read_csv("20210103_hundenamen.csv")
s = DOG_NAMES.loc[:,'HUNDENAME']

l = []
i = 1
for i in range(DOG_NAMES.shape[0]):
    l.append(s[i].strip('"'))
    
v = np.asarray(np.where(calculateLevenshteinDistance(l,'Luca') == 1))


print("The amount of dog names that have a Levenshtein Distance to the dog name Luca is %d" %v.shape[1]) 