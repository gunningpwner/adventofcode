# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 08:39:24 2023

@author: RodriguesAT
"""
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

# a one liner 
# sum([ sum([ (i+1) for i,b in enumerate(reversed('#'.join( 
#     [''.join(sorted(g,reverse=True)) for g in row.split('#')] ))) if b=='O' ])
#     for row in [''.join(a) for a in zip(*lines)][::-1]])



cols = [''.join(l) for l in zip(*lines)]

tot=0
for c in cols:
    dist=len(c)
    col_load=0
    for i in c.split('#'):
        # print(dist)
        rocks = i.count('O')
        col_load+=sum([dist-r for r in range(rocks)])
        dist-= len(i)+1
        # dist-=1
    # print(c,col_load)
    tot+=col_load
print(time.time()-startt)