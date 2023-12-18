lines = open(r"C:\Users\RodriguesAT\Downloads\day15.txt").read()
# lines="rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
tot =0
for seq in lines.split(','):
    j=0
    tot+=[(j:=((j+c)*17)%256) for c in map(ord,seq)][-1]
    j=0

    
print(tot)

#one liner
# print(sum([[(j:=0),list(((j:=((j+c)*17)%256) for c in map(ord,seq)))[-1]][1] for seq in open(r"C:\Users\RodriguesAT\Downloads\day15.txt").read().split(',') ]))

