a = int(input())
b = int(input())
c = int(input())

if a == b and c != b:
    print(2)
elif a == c and b != c:
    print(2)
elif b == c and c != a:
    print(2)
elif b == c and c == a:
    print(3)
elif b != c and c != a and b != a:
    print(0)