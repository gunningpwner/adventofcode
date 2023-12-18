# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:38:01 2023

@author: RodriguesAT
"""

import numpy as np

lines=open(r"C:\Users\RodriguesAT\Downloads\day9.txt")
# lines = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45""".split('\n')

tot = 0

for l in lines:
    tmp = np.array([*map(int,l.split())])
    frst = [tmp[0]]
    
    while tmp.any():
        tmp = np.diff(tmp)
        frst.append(tmp[0])
    run = 0 
    for n in frst[::-1]:
        run = n-run
        # print(run)
    tot+=run
    # tot+=np.cumsum(frst[::-1])[-1]

print(tot)