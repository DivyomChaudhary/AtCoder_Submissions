import math
n, m = map(int, input().split())
least_grapes = m // n
extra_grapes = m % n
for i in range(n):
    if i < extra_grapes:
        print(least_grapes + 1)
    else:
        print(least_grapes)