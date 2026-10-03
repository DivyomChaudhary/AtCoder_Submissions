import math
n, m = map(int, input().split())
max_grapes = math.ceil(m/n)
rem = m
for i in range(n):
    if max_grapes < rem:
        print(max_grapes)
        rem-= max_grapes
    else:
        print(rem)
        rem = 0