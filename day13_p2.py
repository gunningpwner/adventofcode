# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 07:39:50 2023

@author: RodriguesAT
"""

import numpy as np
import math

lines=open(r"C:\Users\RodriguesAT\Downloads\day13.txt").read()

lines=lines.translate(str.maketrans('.#','01'))

# lines = """#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#""".translate(str.maketrans('.#','01'))

patches = lines.split('\n\n')

tot = 0
for q,p in enumerate(patches):
    p=p.split('\n')
    rows=[int(c,2) for c in p]
    cols=[int(''.join(a),2) for a in zip(*p)]
    smudged = False
    t=0
    pows = [2**i for i in range(100)]
    for ax,mul in [(rows,100),(cols,1)]:
        
        i=0
        j=i+1
        l = len(ax)
        ps = []
        while j<l:
            
            if ax[i]==ax[j] or ax[i]^ax[j] in pows:
                ps.append([i,j])
            i+=1
            j=i+1
        if not ps:
            continue
        for a,b in ps:
            i,j=a,b
            
            s=False
            while (n:=(j<l and i>=0)) and (ax[i]==ax[j] or (not s and (s:=(ax[i]^ax[j] in pows)))):
                
                i-=1
                j+=1
                # print(ax[i],ax[j])
                # print(ax[i]^ax[j])
                # print(pows)
                # if s:
                
            if n:
                smudged=False
                continue
            smudged=s
            t=b*mul
            if smudged:
                break
            
        if smudged:
                break
    print(t,q)
    tot+=t
    # print(t)
            # tot+=b*mul
        # while i>=0 and j<l:
            
        
    
    
   # find axis of reflection
   # for i in range(math.ceil(len(rows)/2)):
       
   
       