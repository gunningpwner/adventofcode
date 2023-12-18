# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 07:40:02 2023

@author: RodriguesAT
"""
import re
from itertools import product
lines = open(r"C:\Users\RodriguesAT\Downloads\day12.txt")

# lines = """???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1""".split('\n')

tot=0
for l in lines:
    springs,groups = l.split()
    counts=list(map(int,groups.split(',')))
    
    # [m for m in re.findall('\.(#+\??)|(\??#+)\.',springs) if '?' not in m]
    
    groups=['.#' if a=='?' else a for a in springs]
    poss = [''.join(a) for a in product(*groups)]
    for p in poss:
        if [len(a) for a in re.findall('#+',p)] == counts:
            tot+=1
            
print(tot)