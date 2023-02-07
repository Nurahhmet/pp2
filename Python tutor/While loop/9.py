a = 0
b = -1
c = -1
d = 0
while b != 0:
    b = int(input())
    c += 1
    if b > a:
        a = b
        d = c
print(d)