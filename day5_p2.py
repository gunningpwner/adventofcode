# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:01:15 2023

@author: RodriguesAT
"""
from collections import defaultdict
import bisect
import portion as P
from operator import itemgetter


# print('the fuck?')
lines = open(r'C:/Users/RodriguesAT/Downloads/input.txt').read()
# print('how')
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




    

def create_dict(lines):
    if lines is not list:
            lines=lines.split('\n')
        
    if not lines[0][0].isdigit():
        lines=lines[1:]
            
    #dest,src,rng
    rngs = [ (map(int,l.split())) for l in lines]
    rngs= [(src,src+rng,dest-src) for dest,src,rng in rngs]
    
    int_dict=P.IntervalDict()
    int_dict[P.closed(0,P.inf)]=0
    
    for start,end,func in rngs:
        int_dict[P.closedopen(start,end)]=func
        
    return int_dict

blocks = lines.split('\n\n')

print('what')

seeds=[*map(int,blocks[0][7:].split())]

pairs = zip(seeds[::2],seeds[1::2])

seeds = [(p[0],p[0]+p[1]-1) for p in pairs]

interval = P.closedopen(*seeds[0])

for p in seeds[1:]:
    interval = interval | P.closedopen(*p)

if len(interval)!=len(seeds):
    print('this is fucked')
    raise AssertionError
    
    
print('starting')
# maps = [fast_map(b) for b in blocks[1:]]
maps = [create_dict(b) for b in blocks[1:]]

print(interval)
print('here')

# interval=P.
for m in maps:
    # print(m.intrvls)
    # print(m.rngs)
    
    new_seeds = []
    print(m,interval)
    for intr,func in m[interval].items():
        print(intr,func)
        lam = lambda x: (x.left, x.lower + func, x.upper + func, x.right)
        new_seeds.append(intr.apply(lam))
        
    interval = new_seeds[0]
    
    for p in new_seeds[1:]:
        interval = interval | p
    print(interval)
    print()
    
print(interval)
print(interval.enclosure)
    