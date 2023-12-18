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
    nxt = [tmp[-1]]
    
    while tmp.any():
        tmp = np.diff(tmp)
        nxt.append(tmp[-1])
    tot+=np.cumsum(nxt[::-1])[-1]

print(tot)