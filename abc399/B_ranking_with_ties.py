import numpy as np

n = int(input())
p = [int(i) for i in input().split()]

r = 1
rank = [1] * n
while r <= n:
    max_p = max(p)
    r_inc = 0
    for i in range(n):
       if p[i] == max_p:
            rank[i] = r
            r_inc += 1
            p[i] = -1
    r += r_inc
   
for i in range(n):
    print(rank[i])

