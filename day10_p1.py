# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:41:12 2023

@author: gunni
"""
import math
lines = open(r"C:\Users\gunni\Downloads\input.txt").read()

test1 = """.....
.S-7.
.|.|.
.L-J.
....."""

test2 = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

test3 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

test4 = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""







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



for c,l in zip(adjacent_coords,legal):
    print(padded[loc+c],l)
    if loc+c!=last_loc and padded[loc+c] in l :
        last_loc=loc
        loc+=c
        break
i+=1

while (padded[loc]!='S' or i<1) and i<100000:
    print(loc,last_loc,i)
    cur = padded[loc]
    for j in checks[cur]:
        c = adjacent_coords[j]
        print(padded[loc+c],legal[j])
        if loc+c!=last_loc and padded[loc+c] in legal[j]:
            last_loc=loc
            loc+=c
            break
        
    i+=1
    
print(i,math.ceil(i/2))
