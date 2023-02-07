x = int(input())
y = int(input())
e = 1
while x < y:
    x += x*(0.1)
    e += 1
print(e)