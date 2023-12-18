# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 08:15:01 2023

@author: gunni
"""
import numpy as np
from shapely import Polygon,points,covers
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('qt5agg')
lines=open(r"C:\Users\gunni\Downloads\day18.txt")
# lines="""R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)""".split('\n')
     
coords=np.array([[0,0]])
directions = {'R': np.array([[1,0]]),
              'L': np.array([[-1,0]]),
              'U': np.array([[0,1]]),
              'D': np.array([[0,-1]]),}

for l in lines:
    dire,num,rgb=l.split()
    num=int(num)
    new_coords=coords[-1,:]+directions[dire]*np.arange(1,num+1)[:,np.newaxis]
    coords=np.vstack([coords,new_coords])
coords-=coords.min(0)

pol = Polygon(coords)
testers = [a.reshape(-1) for a in np.meshgrid(*[range(int(a)+1) for a in pol.bounds[2:]])]

print(sum(covers(pol,points(*testers))))
# plt.plot(coords[:,0],coords[:,1],linestyle='None',marker='*')
# plt.show()