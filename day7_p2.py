# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:17:42 2023

@author: RodriguesAT
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 07:45:04 2023

@author: RodriguesAT
"""
from collections import Counter
from operator import itemgetter
import re
import time

start = time.time()
lines=open(r"C:\Users\RodriguesAT\Downloads\input.txt").read()
# lines="""32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""

# lines="""AAAAA 2
# 22222 3
# AAAAK 5
# 22223 7
# AAAKK 11
# 22233 13
# AAAKQ 17
# 22234 19
# AAKKQ 23
# 22334 29
# AAKQJ 31
# 22345 37
# AKQJT 41
# 23456 43
# 55J66 21
# 55666 20"""


# lines = """JJAAK 1
# 22AQK 5
# 2JAQK 6
# 33558 5
# AAAAK 2
# AQA9K 2
# JJJJJ 488
# AJJAA 6
# KKJKJ 9"""


subs = [('A', 'E'), ('K', 'D'), ('Q', 'C'), ('J', '1'), ('T', 'A')]
reverse_subs=[(a[1],a[0]) for a in subs[::-1]]

def to_hex(card):
    for key,rep in subs:
        card=card.replace(key,rep)
    return card

def from_hex(card):
    for key,rep in reverse_subs:
        card=card.replace(key,rep)
    return card

lines=to_hex(lines).split('\n')


# def compare(hand1,hand2):
    
    
#     hand1=hand1[0]+'F'
#     hand2=hand2[0]+'F'
    
#     c1 = [a[1] for a in Counter(hand1).most_common(2)]
#     c2 = [a[1] for a in Counter(hand2).most_common(2)]
    
#     score1 = c1[0]+c1[1]/4
#     score2 = c2[0]+c2[1]/4
    
#     if score1==score2:
#         return int(to_hex(hand1),16) - int(to_hex(hand2),16)
#     else:
#         return score1-score2
    
def fitness(hand1):
    hand1=hand1[0]+'F'
    
    com = Counter(hand1.replace('1', '')).most_common(1)[0][0].upper()
    hand_subbed = hand1.replace("1",com)
    
    #print(hand1,hand_subbed, int(hand1,16))
    hand_subbed = hand_subbed[:-1]+'B'
    c1 = [a[1] for a in Counter(hand_subbed).most_common(2)]
    #calculate most common letter sub jokers for that
    # then calc card ammount score
    
    # hand1=hand1+'F'*int(2*c1[0]+c1[1])
    return int(hand1,16)<<4*int(2*c1[0]+c1[1])

    
    
hands = [l.split() for l in lines]

hands=sorted(hands,key=fitness)


score = sum([int(a[1])*(i+1) for i,a in enumerate(hands)])

hands = [(from_hex(h),bet) for h,bet in hands]

# print(hands)
#print([(a[0],a[1],i+1) for i,a in enumerate(hands)])
print(score)
print(time.time()-start)
