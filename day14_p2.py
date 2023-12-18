# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 09:11:18 2023

@author: RodriguesAT
"""
from collections import OrderedDict
import time
startt = time.time()
lines=open(r"C:\Users\RodriguesAT\Downloads\day14.txt").readlines()


# lines="""O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....""".split('\n')

# lines="""...#
# ....
# ..#O
# ....
# #.O.""".split('\n')

# lines="""#...
# ....
# ...O
# ....""".split('\n')
# cols = [''.join(l) for l in zip(*lines)]

tot=0


def clock(mat):
    return [''.join(a) for a in zip(*mat[::-1])]

def counter(mat):
    return [''.join(a) for a in zip(*mat)][::-1]

def halfturn(mat):
    return [a[::-1] for a in mat][::-1]

def calc_load(mat):
    #assumes already north facing and rocks have been rolled
    return sum([(i+1)*row.count('O') for i,row in enumerate(mat[::-1])])

mat=lines
# print('\n'.join(mat)+'   '+str(calc_load(mat))+'\n\n')
configs= {}
loadings = OrderedDict()
loadings[hash(tuple(mat))]=calc_load(mat)

for cycle in range(1,1000+1):
    start = hash(tuple(mat))
    mat= counter(mat)
    
    
    if start in configs:
        print('ive seen this before ',cycle)
        break
        
    for _ in range(4):
        mat=['#'.join([''.join(sorted(group,reverse=True)) for group in row.split('#') ]) for row in mat]
        mat = clock(mat)
        # print('\n'.join(mat)+'\n\n')
    mat=clock(mat)
    end=hash(tuple(mat))
    configs[start]=end
    loadings[end]=calc_load(mat)
    # print('\n'.join(mat)+f"  Cycle {cycle}: {str(calc_load(mat))}"+'\n\n')


here = start
lead_up = cycle
cycles = 0
cycle_loadings = OrderedDict()
while here!=start or cycles<1:
    here=configs[here]
    cycle_loadings[here]=loadings[here]
    cycles+=1
    
target= 1000000000
ans = list(cycle_loadings.values())[((target-lead_up)%cycles)]
print(f"Load of {ans} after {target} cycles")
print(time.time()-startt)