# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:01:15 2023

@author: RodriguesAT
"""
from collections import defaultdict
import bisect

print('the fuck?')
lines = open(r'C:/Users/RodriguesAT/Downloads/input.txt').read()
print('how')
# lines = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""

from operator import itemgetter

class fast_map():
    
    def __init__(self,lines):
        if lines is not list:
            lines=lines.split('\n')
        
        if not lines[0][0].isdigit():
            lines=lines[1:]
                
        #dest,src,rng
        rngs = [ (map(int,l.split())) for l in lines]
        rngs= [(src,src+rng-1,dest-src) for dest,src,rng in rngs]
        self.rngs = sorted(rngs,key=itemgetter(0))
        self.starts=[a[0] for a in self.rngs]
    def __getitem__(self,item):
        idx=bisect.bisect(self.starts,item)
        if idx==0:
            return item
        ranch = self.rngs[idx-1]
        if item<ranch[0]:
            print('this is fucked')
            raise AssertionError
        if item>ranch[1]:
            return item
        return item+ranch[2]
        
        
# def create_map(lines):
#     if lines is not list:
#         lines=lines.split('\n')
        
#     if not lines[0][0].isdigit():
#         lines=lines[1:]
#     mapping = better()
#     for l in lines:
#         dest,src,rng = map(int,l.split())
        
#         mapping.update(dict(zip(range(src,src+rng),range(dest,dest+rng))))
#     return mapping


    

blocks = lines.split('\n\n')

print('what')

seeds=map(int,blocks[0][7:].split())

print('starting')
maps = [fast_map(b) for b in blocks[1:]]

print('here')
for m in maps:
    seeds = [m[s] for s in seeds]


print(seeds)

print(min(seeds))