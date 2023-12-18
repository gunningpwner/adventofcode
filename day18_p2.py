# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 08:15:01 2023

@author: gunni
"""
import numpy as np
import portion as P
# from shapely import Polygon
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('qt5agg')
lines=open(r"C:\Users\RodriguesAT\Downloads\day18.txt")
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

# lines="""R 1 a
# U 1 a
# L 1 a
# D 1 a""".split('\n')

coords=np.array([[0,0]])
directions = {'R': np.array([[1,0]]),
              'L': np.array([[-1,0]]),
              'U': np.array([[0,1]]),
              'D': np.array([[0,-1]]),}
trans = {'0':'R',
         '1':'D',
         '2':'L',
         '3':'U',}
for l in lines:
    *_,rgb=l.split()
    

    num=int(rgb[2:-2],16)
    dire=trans[rgb[-2]]
    new_coords=coords[-1,:]+directions[dire]*num
    coords=np.vstack([coords,new_coords])
coords-=coords.min(0)
coords=coords[:-1,:]
a = coords[coords[:, 0].argsort()]

grouped = np.split(a[:,1], np.unique(a[:, 0], return_index=True)[1][1:])


ints = list(zip(np.unique(a[:, 0]),grouped))

last, first = ints[0]
first=np.sort(first)
area=0
vol= P.empty()
for intrvl in zip(first[::2],first[1::2]):
    area+=intrvl[1]-intrvl[0]+1
    vol=vol|P.closedopen(*intrvl)
    
for y,xs in ints[1:]:
    xs= np.sort(xs)
    # print(vol,y,last)
    border = vol
    
    for intrvl in vol:
        # print(intrvl)
        val = int(y-last-1)*int(intrvl.upper-intrvl.lower+1)
        # print('vol',val)
        area+=val
        
    for intrvl in zip(xs[::2],xs[1::2]):
        # print(intrvl)
        new =P.closedopen(*intrvl)
        vol=(vol|new)-(vol&new)
        border=border|new
        
    for intrvl in border:
        val=int(intrvl.upper-intrvl.lower+1)
        # print('bor',val)
        area+=val
         
    last = y
print(area)
# pol = Polygon(coords)
# testers = [a.reshape(-1) for a in np.meshgrid(*[range(int(a)+1) for a in pol.bounds[2:]])]

# print(sum(covers(pol,points(*testers))))
# plt.plot(coords[:,0],coords[:,1],linestyle='None',marker='*')
# plt.show()