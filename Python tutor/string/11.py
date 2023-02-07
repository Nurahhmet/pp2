s = input()
y = s.find('h')
v = s.rfind('h')
print(s[:y+1],s[y+1:v].replace('h', 'H'),s[v:],sep='')