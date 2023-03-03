def genlow(N):
    for i in range(N,0,-1):
        yield i
n = int(input("enter a number:"))
for x in genlow(n):
    print(x)