import numpy as np
from itertools import combinations

lines=open(r"C:\Users\RodriguesAT\Downloads\day11.txt").read()
lines = lines.translate(str.maketrans('.#','01'))

arr = np.array([list(map(int,l)) for l in lines.split('\n')])
new_dims = [arr.shape[i]+sum(~arr.any(i)) for i in [0,1]][::-1]
new_idx = [np.arange(arr.shape[i])+np.cumsum(~arr.any(i)) for i in [0,1]][::-1]
new_arr = np.zeros(new_dims)
new_arr[np.ix_(*new_idx)]=arr

galaxies = [*zip(*np.where(new_arr))]
a,b = zip(*combinations(galaxies,2))
ans=np.sum(np.abs(np.array(a)-np.array(b)))
print(ans)
