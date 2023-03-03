# 1
def gensquares(N):
    for i in range(N):
        yield i ** 2
n = int(input("enter a number:"))
for x in gensquares(n):
    print(x)

# 2
def genevens(N):
    for i in range(N):
        if i%2==0:
            yield i
n = int(input("enter a number:"))
for x in genevens(n):
    print(x)

# 3
def gen3(N):
    for i in range(N):
        if i%3==0 and i%4==0:
            yield i
n = int(input("enter a number:"))
for x in gen3(n):
    print(x)

# 4
c = int
def gensquares(n,m):
    for i in range(n,m):
            yield i**2
k = int(input("enter a number 1:"))
e = int(input("enter a number 2:"))
for x in gensquares(k,e):
    print(x)

# 5
def genlow(N):
    for i in range(N,0,-1):
        yield i
n = int(input("enter a number:"))
for x in genlow(n):
    print(x)