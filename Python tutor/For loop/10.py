n = int(input())
sum1 = 0
sum2 = 0
for i in range(1, n + 1):
    sum1 += i

for i in range(1, n):
    number = int(input())
    sum2 += number

print(sum1 - sum2)