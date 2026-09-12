#3/3 public test cases passed
#5/10 private test cases passed
N = int(input(""))
A = list(map(int, input().split()))
ones = 0
tens = 0
hundreds = 0
for money in A:
    bal = 1000 - (money % 1000)
    hundreds += bal//100
    bal %= 100
    tens += bal//10
    bal %= 10
    ones += bal

print(ones, tens, hundreds)