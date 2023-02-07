max = 0
element = -1
while element != 0:
    if element % 2 == 0:
        max += 1
    element = int(input())
print(max)