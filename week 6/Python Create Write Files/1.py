# 1
'''"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content'''

# 2
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

# 3
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

# 4
'''"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist'''

# 5
f = open("myfile.txt", "x")

# 6
f = open("myfile.txt", "w")
