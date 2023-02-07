a = int(input())
if a == 0:
    print(0)
else:
    p, ne = 0, 1
    n = 1
    while ne <= a:
        if ne == a:
            print(n)
            break
        p, ne = ne, p + ne
        n += 1
    else:
        print(-1)
