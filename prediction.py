# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:14:22 2019

@author: moconnor
"""
from collections import defaultdict
import csv

sem = input("Semester: ")

file = f"{sem}/rosters.csv"
active = f"{sem}/active.csv"

active_list = []

with open(active) as activecsv:
    reader=csv.reader(activecsv)
    for row in reader:
        active_list.append(row[0])


d=defaultdict(list)

with open(file) as activecsv:
    reader = csv.reader(activecsv)
    for row in reader:
        if row[0] in active_list:
            if (row[3] in ['A','B+','B','C+','C','IP'] and 
                row[2] not in d[(row[0],row[1])]):  
                    d[(row[0],row[1],row[4])].append(row[2])


for s in d:
    stem = "{};{};{};".format(s[0],s[1],d[s])
    if len(d[s])>0:
        if len(d[s])>=4:
            if 'ARCH564' in d[s] or 'ARCH506G' in d[s]:
                print(stem+"Done")
            else:
                print(stem+"Integrated")
        elif len(d[s])==3:
            if 'ARCH564' in d[s] or 'ARCH506G' in d[s]:
                print(stem + "Summer Options?") # for Fall predictions
                #print(stem+"Options") # for Spring predictions
            else:
                print(stem+"Integrated")
        elif len(d[s])==2:
            if 'ARCH564' in d[s] or 'ARCH506G' in d[s]:
                print(stem+"Options")
            else:
                print(stem+"Options") # for Fall predictions
                #print(stem+"Summer Options?") # for Spring Predictions
        else:
            print(stem+"Options")
