# 1
'''Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
'''
# 2
f = open("demofile.txt", "r")
print(f.read())

# 3
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

# 4
f = open("demofile.txt", "r")
print(f.read(5))

# 5
f = open("demofile.txt", "r")
print(f.readline())

# 6
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# 7
f = open("demofile.txt", "r")
for x in f:
  print(x)

# 8
f = open("demofile.txt", "r")
print(f.readline())
f.close()