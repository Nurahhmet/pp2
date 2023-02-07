s = input()
i = s.find(' ')
s1 = s[i:] + ' ' + s[:i]
print(s1)