# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 11:21:37 2023

@author: gunni
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 09:10:45 2023

@author: gunni
"""

import numpy as np
from queue import PriorityQueue
lines = open(r"C:\Users\gunni\Downloads\day17.txt").read().split('\n')
# lines="""2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533""".split('\n')

dim = len(lines)

grid = np.array([*map(int,''.join(lines))]).reshape((-1,dim))

turns = [np.array([[0,1],[1,0]],int),np.array([[0,-1],[-1,0]],int)]



def djikstras(grid,goal):
    
    max_steps = 10
    min_steps = 4
    queue = PriorityQueue()
    
    queue.put([0,(0,0),(1,0),0])
    queue.put([0,(0,0),(0,1),0])
    costs = dict()
    min_cost=1e7
    i=0
    while not queue.empty():
        
        cost,loc,dir,steps = queue.get()
        
        if (loc,dir,steps) in costs and cost>=costs[(loc,dir,steps)]:
            continue
        else:
            # visited.add((loc,dir,steps))
            costs[(loc,dir,steps)]=cost
        # print(i,' start ',cost,loc,dir,steps)
        if loc==goal:
            min_cost = min(cost,min_cost)
            print(cost,min_cost, loc,dir,steps)
            continue

        
        #now we do the turns
        if steps>=min_steps:
            for t in turns:
                new_dir = tuple(dir@t)
                new_loc = tuple(sum(i) for i in zip(loc,new_dir))
                if max(new_loc)>=dim  or min(new_loc)<0:
                    continue
                new_cost = cost+grid[new_loc]
                new_steps=1
                # print(i,' added ',new_cost,new_loc,new_dir,new_steps)
                queue.put([new_cost,new_loc,new_dir,new_steps])
            
        # do the go straight
        if steps<max_steps:
            new_loc = tuple(sum(i) for i in zip(loc,dir))
            if max(new_loc)>=dim or min(new_loc)<0:
                pass
            else:
                new_cost = cost+grid[new_loc]
                new_steps=steps+1
                # print(i,' added ',new_cost,new_loc,dir,new_steps)
                queue.put([new_cost,new_loc,dir,new_steps])
        i+=1
    # print(queue.qsize(),'last')
    return min_cost,costs
min_cost,costs=djikstras(grid,(dim-1,dim-1))
print(min_cost)