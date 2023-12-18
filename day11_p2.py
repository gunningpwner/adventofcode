# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:44:17 2023

@author: RodriguesAT
"""

import numpy as np
from itertools import combinations

lines=open(r"C:\Users\RodriguesAT\Downloads\day11.txt").read()

# lines="""...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#....."""

lines = lines.translate(str.maketrans('.#','01'))
arr = np.array([list(map(int,l)) for l in lines.split('\n')])

# new_dims = [arr.shape[i]+sum(~arr.any(i)) for i in [0,1]][::-1]

new_idx = [np.arange(arr.shape[i])+np.cumsum(~arr.any(i))*(999999) for i in [0,1]][::-1]
new_idx=np.stack(new_idx)

galaxies = [*zip(*np.where(arr))]
galaxies=new_idx[(0,1),galaxies]

a,b = zip(*combinations(galaxies,2))
ans=np.sum(np.abs(np.array(a)-np.array(b)),dtype=np.int64)
print(ans)
