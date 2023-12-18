# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 07:40:02 2023

@author: RodriguesAT
"""
import re
from itertools import product
import time
from multiprocessing import Pool




def calculate(line):
    tot=0
    start=time.time()
    springs,groups = line.split()
    counts=list(map(int,groups.split(',')))
    # springs = '?'.join([springs]*5)
    # counts=counts*5
    # [m for m in re.findall('\.(#+\??)|(\??#+)\.',springs) if '?' not in m]
    
    groups=['.#' if a=='?' else a for a in springs]
    poss = product(*groups)
    for p in poss:
        p=''.join(p)
        if [len(a) for a in re.findall('#+',p)] == counts:
            tot+=1
    print(line)
    print(start-time.time())
    print(tot,'\n')
    return tot

if __name__=='__main__':
    lines = open(r"C:\Users\RodriguesAT\Downloads\day12.txt")

    lines = """???.### 1,1,3
    .??..??...?##. 1,1,3
    ?#?#?#?#?#?#?#? 1,3,1,6
    ????.#...#... 4,1,1
    ????.######..#####. 1,6,5
    ?###???????? 3,2,1""".split('\n')
    with Pool(20) as p:
        print(p.map(calculate,lines))