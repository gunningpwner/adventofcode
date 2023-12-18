# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:41:12 2023

@author: gunni
"""
import math
from shapely import Polygon,points,covers
import numpy as np
lines = open(r"C:\Users\RodriguesAT\Downloads\day10.txt").read()

test1 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

test2 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

test3 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""









using = lines

padded = ['.'+l+'.' for l in using.split('\n')]
llen = len(padded[0])

padded = '.'*llen + ''.join(padded) + '.'*llen

adjacent_coords = [-llen,llen,-1,1]
legal = ['|F7S','|LJS','-FLS','-7JS',]

checks ={'|':[0,1],
         '-':[2,3],
         'L':[0,3],
         'J':[0,2],
         'F':[1,3],
         '7':[1,2],
         }


loc = padded.find("S")
last_loc=loc

i = 0

coords = [loc]

for c,l in zip(adjacent_coords,legal):
    # print(padded[loc+c],l)
    if loc+c!=last_loc and padded[loc+c] in l :
        
        last_loc=loc
        loc+=c
        coords.append(loc)
        break
i+=1

while (padded[loc]!='S' or i<1) and i<100000:
    # print(loc,last_loc,i)
    cur = padded[loc]
    for j in checks[cur]:
        c = adjacent_coords[j]
        # print(padded[loc+c],legal[j])
        if loc+c!=last_loc and padded[loc+c] in legal[j]:
            last_loc=loc
            loc+=c
            coords.append(loc)
            break
        
    i+=1
    
print(i,math.ceil(i/2))


coords = [(i%llen,i//llen) for i in coords]
pol = Polygon(coords)
testers = [a.reshape(-1) for a in np.meshgrid(*[range(int(a)+1) for a in pol.bounds[2:]])]
testers = [t for t in zip(*testers) if t not in coords]
print(sum(covers(pol,points(testers))))
# bbox = [*zip(min(coords),max(coords))]

# inside = 0

# for x in range(bbox[0][0]+1,bbox[0][1]):
#     hits = 0
#     print(padded[x::llen])
#     for y in range(bbox[1][0]-1,bbox[1][1]+1)[::-1]:
#         # print(padded[y*llen:(y+1)*llen])
#         # print(padded[y*llen+x])
#         # print(x,y,hits,inside)
#         if (x,y) in coords:
#             if padded[y*llen+x] in '-':
#             # print(x,y,hits,inside)
#                 hits+=1
#             print(padded[y*llen+x],hits,x,y)
                
#             continue
#         print(padded[y*llen+x],hits)
#         inside+=hits%2
#     print(inside,'\n')
       