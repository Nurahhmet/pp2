# 1
def gramtoounce(a):
    ounces = 28.3495231 * a
    return ounces

a = int(input())
print(gramtoounce(a))

# 2
def temperature(f):
    c = (5 / 9) * (f-32)
    return c
far = int(input())
print(temperature(far))

# 3
def solve(numlegs, numheads):
    for i in range(1, numheads+1):
        if (i*4)+(numheads-i)*2 == numlegs:
            ans = f"{i} rabbits,{numheads-i} chickens"
            return ans
print("Enter number of legs:")
numlegs=int(input())
print("Enter number of heads")
numheads=int(input())
print(solve(numlegs, numheads))
# 4
def filter_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("Enter size of list:")
n = int(input())
print("Enter elements of list:")
l = list()
for i in range(n):
    x = int(input())
    if filter_prime(x):
        l.append(x)
print(l)

# 5
def factorial(a):
    fact = 1
    for i in range(1, a + 1):
        fact = fact * i
    return fact

permut = str(input())
print(factorial(len(permut)))

# 6
def reverse(w):
    rev = w.split()
    return ' '.join(reversed(rev))

w = str(input())
print(reverse(w))

# 7
def has_33(nums):
    return any(nums[i + 1] == nums[i] == 3 for i in range(len(nums) - 1))

nums = list(map(int, input().split()))
print(has_33(nums))

# 8
def spy_game(nums1):
    a = ''.join(nums1)
    for i in nums1:
        if '007' in a:
            return True
    return False

nums1 = list(map(str, input().split()))
print(spy_game(nums1))

# 9
import math
def volume(r): #V = 4pir^3/3
    vol = (4*math.pi * r**3)/3
    return vol

r = float(input())
print(volume(r))

# 10
def unique_list(l):
  empty = []
  for a in l:
    if a not in empty:
      empty.append(a)
  return empty
list1 = list(map(int, input().split()))
print(unique_list(list1))
# 11
def palindrome(w):
    if w == w[::-1]:
        return "Yes, it is palindrome"
    else:
        return "Not palindrome"
w = str(input())
print(palindrome(w))


# 12
def histogram(list):
    for i in range(0, len(list)):
        print('*' * list[i])
    return
list2 = list(map(int, input().split()))
print(histogram(list2))