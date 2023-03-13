# 1

import os
path = 'C:\\Users\\nurma\\Downloads\\pp2\\labs'
print("Only directories:")
print([name for name in os.listdir(path)
      if os.path.isdir(os.path.join(path, name))])
print("\nOnly files:")
print([name for name in os.listdir(path)
      if not os.path.isdir(os.path.join(path, name))])
print("\nAll directories and files :")
print([name for name in os.listdir(path)])


# 2

import os
print('Exist:', os.access('C:\\Users\\nurma\\Downloads\\pp2\\labs\\lab5\\row.txt', os.F_OK))
print('Readable:', os.access(
    'C:\\Users\\nurma\\Downloads\\pp2\\labs\\lab5\\row.txt', os.R_OK))
print('Writable:', os.access(
    'C:\\Users\\nurma\\Downloads\\pp2\\labs\\lab5\\row.txt', os.W_OK))
print('Executable:', os.access(
    'C:\\Users\\nurma\\Downloads\\pp2\\labs\\lab5\\row.txt', os.X_OK))


# 3

import os
print("Test a path exists or not:")
path = r'C:\\Users\\nurma\\Downloads\\pp2\\labs\\lab5\\row.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))


# 4

def file_length(fname):
    with open(fname, 'r') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print("Number of lines in the file: ", file_length('C:\\Users\\nurma\\Downloads\\pp2\\labs\\lab6\\lol.txt'))


# 5

fruits = ['apple', 'cherry', 'banana']
with open('a.txt', 'a') as a:
    for i in fruits:
        a.write("\n")
        a.write(i)
text = open('a.txt')
print(text.read())


# 6

import string
for letter in string.ascii_uppercase:
    with open(letter + ".txt", "w") as f:
        f.write(letter)


# 7

from shutil import copyfile
copyfile('C.txt', 'D.txt')


# 8

import os

if os.path.exists('C:\\Users\\nurma\\Downloads\\pp2\\labs\\lab6\\dir-and-files\\textfile.txt'):
    os.remove('C:\\Users\\nurma\\Downloads\\pp2\\labs\\lab6\\dir-and-files\\textfile.txt')
else:
    print("Such file does not exist!")