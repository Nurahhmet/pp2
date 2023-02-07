n = int(input())
sum = 1
result = 1
while n != 0:
    prev = n
    n = int(input())
    if prev == n:
        sum += 1
        if sum > result:
            result = sum
    else:
        sum = 1
print(result)
