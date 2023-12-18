# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:45:24 2023

@author: RodriguesAT
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:13:21 2023

@author: RodriguesAT
"""

import re
from collections import OrderedDict,defaultdict
from itertools import product
import time

start_time = time.time()
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
start = [n for n in nodes.keys() if n.endswith('A')]

end = [n for n in nodes.keys() if n.endswith('Z')]

cur = start

rep = len(instructions.strip())


# while not all([n.endswith('Z') for n in cur]) and i <rep:
#     d = tran[instructions[i%rep]]
#     cur = [nodes[n][d] for n in cur]
#     i+=1
#     print(i)
#     print(cur)
    
def walk_graph(start,end):
    i = 0
    
    cur = start
    
    while (cur!=end or i==0) and i <100000:
        
        d = tran[instructions[i%rep]]
        cur = nodes[cur][d]
        i+=1
    return i,cur

nums = []
for (s,e) in product(start,end):
    
    i,last = walk_graph(s, e)
    # print(s,e,i,last)
    if i<100000:
        nums.append(i)
        #print(e,i)
        #print(walk_graph(last, e))

print(time.time()-start_time)
