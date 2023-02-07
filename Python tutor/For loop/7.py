n = int(input())
sum = 1
sumf = 0
for i in range(1,n+1):
    sum *= i
    sumf += sum
print(sumf)