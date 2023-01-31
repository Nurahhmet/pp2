v = int(input())
t = int(input())
s = int
s = abs(v)*t
if v > 0:
    if s > 108:
        while s < 108:
            s = s - 109
        print(s)
    else:
        print(s)
elif v < 0:
    if s > 108:
        while s < 108:
            s = abs(109 - s)
        print(s)
    else:
        print(s)
else:
    print(0)
#not finished
