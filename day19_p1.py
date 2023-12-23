# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 11:01:35 2023

@author: gunni
"""
import re

lines=open(r"C:\Users\gunni\Downloads\day19.txt").read().replace('in','start')
# lines="""px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}

# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}""".replace('in','start')


workflows, parts = lines.split('\n\n')
parts=[l[1:-1].replace(',','\n') for l in parts.split('\n')]
# parts = [[a.split('=') for a in l[1:-1].split(',')] for l in parts.split('\n')]
# parts = [dict([(a,int(b)) for a,b in c]) for c in parts]


# parsed_workflows=dict()
parsed_workflows=[]
for l in workflows.split('\n'):
    match=re.match('([a-z]+){(.+)}', l)
    name=match[1]
    inst=match[2]
    
    part2=''
    # print(name, inst)
    llen=len(inst.split(','))-1
    for i,ins in enumerate(inst.split(',')):
        if i !=llen:
            cond, do = ins.split(':')
        else:
            do = ins
            
        if do=='R':
            do='ret.append(False)'
        elif do=='A':
            do = 'ret.append(True)'
        else:
            do=f'ret.append(t[0] if (t:={do}(string)) else t)'
        
        if i==0:
            state='if'
        elif i==llen:
            state='else'
            cond=''
        else:
            state= 'elif'
        
        part2+=f"{state} {cond}:\n\t{do}\n"
    compiled=f'def {name}(string):\n\texec(string)\n\tret=[]\n\texec("""{part2}""")\n\treturn ret'
    parsed_workflows.append(compiled)

for func in parsed_workflows:
    exec(func)

tot=0
for s in parts:
    if start(s)[0]:
        tot+=sum(map(int,[a.split('=')[1] for a in s.split('\n')]))
        
print(tot)