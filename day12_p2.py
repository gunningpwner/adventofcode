# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:13:44 2023

@author: RodriguesAT
"""

import re
from itertools import product
lines = open(r"C:\Users\RodriguesAT\Downloads\day12.txt").readlines()

# lines = """???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1""".split('\n')

    
    
def lpartition(elements,num):
    # Splits an array of elements such that 
    left=[e for e in elements]
    right=[]
    while sum(left)>num:
        right.insert(0,left.pop())
    return left,right

def rpartition(elements,num):
    # Splits an array of elements such that 
    left=[]
    right=[e for e in elements]
    while sum(right)>num:
        left.append(right.pop(0))
    return left,right
tot=0
for l in lines[:7]:
    springs,groups = l.split()
    counts=list(map(int,groups.split(',')))
    # groups = [[a,(0,len(springs))] for a in counts]
    
    cells = re.findall('[#\?]+',springs)
    poss = []
    
    hold = [a for a in counts]
    cell_hold = [[] for a in cells]
    
    # forward pass
    for i,cell in enumerate(cells):
        leave,hold = lpartition(hold,cell.count('#'))
        cell_hold[i]+=leave
        leave,hold=rpartition(hold,len(''.join(cells[i+1:])))
        cell_hold[i]+=leave
    # backward pass
    print(springs,counts,cell_hold,hold)
    for i in range(len(cells))[::-1]:
        cell = cells[i]
        if sum(cell_hold[i])+len(cell_hold[i])-1>len(cell):
            #got pick those bad boys up and replace them
            hold = cell_hold[i]+hold
            cell_hold[i]=[]
            
        hold,leave = rpartition(hold,cell.count('#'))
        
        cell_hold[i]=leave+cell_hold[i]
        print('\t',cell_hold,hold)   
    print(springs,counts,cell_hold,hold)
            
    # [m for m in re.findall('\.(#+\??)|(\??#+)\.',springs) if '?' not in m]
    
#     groups=['.#' if a=='?' else a for a in springs]
#     poss = [''.join(a) for a in product(*groups)]
#     for p in poss:
#         if [len(a) for a in re.findall('#+',p)] == counts:
#             tot+=1
            
# print(tot)