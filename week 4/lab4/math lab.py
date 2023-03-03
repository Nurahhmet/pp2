# 1
pi=22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print("Output radian:", radian)

# 2
height = float(input("Height : "))
base1 = float(input('Base, first value: '))
base2 = float(input('Base, second value: '))
area = ((base1 + base2) / 2) * height
print("Expected output:", area)

# 3
from math import tan, pi
n_sides = int(input("Input number of sides: "))
s_length = float(input("Input the length of a side: "))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("The area of the polygon is: ",p_area)

# 4
base = float(input('Length of base: '))
height = float(input('Height of parallelogram: '))
area = base * height
print("Expected output: ", area)