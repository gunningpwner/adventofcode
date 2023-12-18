from collections import OrderedDict,defaultdict
import re
lines = open(r"C:\Users\RodriguesAT\Downloads\day15.txt").read()

boxes=defaultdict(OrderedDict)

for seq in lines.split(','):
    label,op,foc = re.search('([a-z]+)([-=])(\d?)',seq).groups()
    j=0
    box=[(j:=((j+c)*17)%256) for c in map(ord,label)][-1]
    if op=='=':
        boxes[box][label]=int(foc)
    else:
        boxes[box][label]=1
        del boxes[box][label]
tot=sum([(num+1)*sum([ (i+1)*foc for i,foc in enumerate(box.values())  ]) for num,box in list(boxes.items())])
print(tot)
    