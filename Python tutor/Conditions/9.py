a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a - c == b - d or a - c ==(-1)*(b - d) or a == c or b == d:
    print("YES")
else:
    print("NO")