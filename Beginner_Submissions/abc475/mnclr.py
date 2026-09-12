S = input("")
n = len(S)
res = ""
for char in range(n - 1):
    res += S[char] + "o"
res = res + S[n-1]
print(res)