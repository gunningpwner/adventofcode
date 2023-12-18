# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 07:31:28 2023

@author: RodriguesAT
"""
import math as m

lines = open(r"C:\Users\RodriguesAT\Downloads\input.txt").readlines()
# lines = """Time:      7  15   30
# Distance:  9  40  200""".split('\n')

races = [l.split(':')[-1] for l in lines]

races = [[*map(int,[''.join(l.split()) for l in races])]]

num = 1

for t,d in races:
    
    pt1=t/2
    pt2= -m.sqrt(t**2+4*-d)/2
    rt1 = m.ceil(pt1+pt2)
    if rt1*(t-rt1)<=d:
        rt1+=1
        
    rt2=m.floor(pt1-pt2)
    if rt2*(t-rt2)<=d:
        rt2-=1
        
    num*=len(range(rt1,rt2))+1
    
    # print(t,d)
    # print(rt1,rt2)
    # print(rt1*(t-rt1),rt2*(t-rt2))
    # print()
    
print(num)