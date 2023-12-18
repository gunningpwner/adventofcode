# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:13:21 2023

@author: RodriguesAT
"""

import re
from collections import OrderedDict,defaultdict
lines=open(r"C:\Users\RodriguesAT\Downloads\input.txt").read()
# lines = """RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)"""

# lines = """LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)"""

instructions,network = lines.split('\n\n')

tran = {'L':0,'R':1}

nodes = {}
for l in network.split('\n'):
    
    matches = re.findall('([A-Z]+)',l)
    nodes[matches[0]] = matches[1:]
    

i = 0
start = 'AAA'
end = 'ZZZ'

cur = start

rep = len(instructions.strip())

while cur!=end and i <100000:
    
    d = tran[instructions[i%rep]]
    
    
    cur = nodes[cur][d]
    i+=1
    
print(i)