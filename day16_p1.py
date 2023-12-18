# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 10:27:09 2023

@author: gunni
"""
import numpy as np

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('qt5agg')
lines = open(r"C:\Users\gunni\Downloads\day16.txt").read().split('\n')
# lines=r""".|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\
# ..../.\\..
# .-.-/..|..
# .|....-|.\
# ..//.|....""".split('\n')

mirrors={'\\': np.array([[0,1],[1,0]],int),
 '/':np.array([[0,-1],[-1,0]],int)}

splitters = {'|':np.array([0,1],int),
             '-':np.array([1,0],int)}

beams = np.array([[0,-1,0,1]],int)
history=[]

i = 0
while  beams.shape[0]>0:
    beams[:,:2]+=beams[:,2:]
    
    new_beams = np.empty((0,4),int)
    for b in beams:
        if (b[:2]<0).any():
            continue
        try:
            loc = lines[b[0]][b[1]]
        except IndexError:
            continue
        if (t:=tuple(b)) in history:
            continue
        else:
            history.append(t)
        # print(i,'aa',loc)
        if loc in mirrors:
            # print(i,'mmm')
            b[2:]=b[2:]@mirrors[loc]
            new_beams=np.vstack([new_beams,b])
        elif loc in splitters:
            # print(i,'ssss')
            if (np.abs(b[2:])==splitters[loc]).all():
                
                for mat in mirrors.values():
                    nb=b.copy()
                    nb[2:]=nb[2:]@mat
                    new_beams=np.vstack([new_beams,nb])
            else:
                new_beams=np.vstack([new_beams,b])
        else:
            new_beams=np.vstack([new_beams,b])
    beams=new_beams
    # print(beams)
    i+=1

history=np.array(history)
print(i)
print(np.unique(history[:,:2],axis=0).shape)

# stuffs={'\\':[],
#         '/':[],
#         '|':[],
#         '-':[],
#         }
# for i,l in enumerate(lines):
#     for j,a in enumerate(l):
#         if a!='.':
#             stuffs[a].append([i,j])
# for m,coords in stuffs.items():
#     if m=="\\":
#         m='x'
#     coords=np.array(coords)
#     plt.plot(coords[:,1],coords[:,0]*-1,linestyle='None',marker=f"${m}$",ms=10)

# plt.quiver(history[:,1],history[:,0]*-1,history[:,3],history[:,2]*-1,pivot='tip')
# plt.show()
