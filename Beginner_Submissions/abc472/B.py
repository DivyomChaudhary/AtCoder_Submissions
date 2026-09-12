n = int(input(""))
lengths = list(map(int, input("").split(" ")))
prefix_sum = lengths.copy()
for i in range(1,n):
    prefix_sum[i] += prefix_sum[i-1]
left_ptr = 0
half = prefix_sum[n-1]//2
values = [0]* n
while (left_ptr <= n-1):
    val = half - prefix_sum[left_ptr]
    values[left_ptr] = val
    if val < 0:
        break
print(values)
rem = prefix_sum[left_ptr+1::]
print(prefix_sum[left_ptr], sum(rem))
print(abs(prefix_sum[left_ptr] - sum(rem)))