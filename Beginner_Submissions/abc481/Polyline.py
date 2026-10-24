N, boundary = map(int, input().split())
A = list(map(int, input().split()))

r = 1
cross = 0

while(r < N):
    if A[r] >= boundary > A[r - 1]:
        cross +=1
        r +=1
    elif A[r] < boundary <= A[r - 1]:
        cross +=1
        r +=1
    else:
        pass

    r +=1

print(cross)