myList = []

myList.append(1)
myList.append(2)
myList.append(3)

print(myList[0])
print(myList[1])
print(myList[2])

# Loop in a list
for x in myList:
    print(x)

# Accessing an index which does not exist generates an exception (an error).
# print(myList[10])  # This will show error

# Exercise
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = None
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
