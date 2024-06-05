# Any datatypes element can be store in list unlike array in which only single data type can be stored
# Strings are immutable in python
# lists are mutable in python

marks = [94.4,87.5,95.2,66.4,45.1]
print(marks)
print(len(marks))
print(type(marks))
print(marks[4])
print(marks[0])

student = ['Abhi', 56, 'Canada']
print(student)


# List slicing 
# list_Name [starting_idx : ending_idx] ending_idx is not included
print(student[1:3])

# List methods - It chnages the original string

list = [2,1,3,3]

# add an element to the list
list.append(4)

# sorts the list in ascending order
list.sort()

# sorts the list in descending order
list.sort(reverse=True)

# insert element at an index
list.insert(3,6)

# remove first occurence of the element
list.remove(3)

# remove element at idx
list.pop(2)

# prints the list
print(list)