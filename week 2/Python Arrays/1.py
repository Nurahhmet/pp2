# 1
cars = ["Ford", "Volvo", "BMW"]

# 2
x = cars[0]

# 3
cars[0] = "Toyota"

# 4
x = len(cars)

# 5
for x in cars:
  print(x)

# 6
cars.append("Honda")

# 7
cars.pop(1)

# 8
cars.remove("Volvo")

'''
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''