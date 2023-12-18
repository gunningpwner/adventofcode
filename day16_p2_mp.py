# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 12:03:08 2023

@author: gunni
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 10:27:09 2023

@author: gunni
"""
import numpy as np
from itertools import product
from tqdm import tqdm
from tqdm.contrib.concurrent import process_map

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


def propagate_beam(s):
    
    beams = np.array([s],int)
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
    
    return np.unique(history[:,:2],axis=0).shape[0]


if __name__=="__main__":
    tiles=[]
    #left goign right
    lr = np.tile([0,-1,0,1],(len(lines),1))
    lr[:,0]=range(len(lines))

    #right going left
    rl = np.tile([0,len(lines),0,-1],(len(lines),1))
    rl[:,0]=range(len(lines))
    #top going down
    td = np.tile([-1,0,1,0],(len(lines[0]),1))
    td[:,1]=range(len(lines[0]))

    #bottom going up
    bu = np.tile([len(lines[0]),0,-1,0],(len(lines[0]),1))
    bu[:,1]=range(len(lines[0]))
    
    starts = np.vstack([lr,rl,td,bu])
    ans = process_map(propagate_beam,starts,max_workers=5)
    print(max(ans))
    # sleep(1000)