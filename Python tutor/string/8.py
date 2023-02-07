s =input()
t=s.find('h')+1
k=s.rfind('h')
g=s[t:k]
print(s[:t]+g[::-1]+s[k:])