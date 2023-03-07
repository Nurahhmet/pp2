# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
txt = str(input())
x = re.search('ab*', txt)

if x:
    print("Match found!")
else:
    print("No match found.")

# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re

txt = input("Enter a string: ")
x = re.search('ab{2,3}', txt)
if x:
    print("Match found! ")
else:
    print("None")

# Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
txt = str(input("Enter smth: "))
x = re.findall('[a-z]+_[a-z]+', txt)
print(x)
if x:
    print("Match found! ")
else:
    print("None")

# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
txt = str(input())
x = re.search('[A-Z]+[a-z]+$', txt)
if x:
    print("Match found!")
else:
    print("No match found.")

# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
txt = str(input())
x = re.search('a.*b$', txt)
if x:
    print("Match found!")
else:
    print("No match found.")

# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

txt = str(input("Enter a string: "))
x = re.sub('[ ,.]', ":", txt)
print(x)

# Write a python program to convert snake case string to camel case string.
import re
def snake2camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


txt = str(input("Enter smth: "))
print(snake2camel(txt))

# Write a Python program to split a string at uppercase letters.
import re
text = input("Enter a string: ")
print(re.findall('[A-Z][^A-Z]*', text))

# Write a Python program to insert spaces between words starting with capital letters.
import re
text = input("Enter a string: ")
x = re.sub(r"(\w)([A-Z])", r"\1 \2", text)

print(x)

# Write a Python program to convert a given camel case string to snake case.
import re
def camel2snake(txt):
    x = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', txt)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', x).lower()

txt = str(input("Enter a string: "))
print(camel2snake(txt))