n, v = map(int, input().split())
happiness = list(map(int, input().split()))

val = []
for i in range(n):
    val.append(happiness[i]//(i+1))
print(val)