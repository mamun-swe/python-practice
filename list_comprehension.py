numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []

for number in numbers:
    if number > 0:
        newlist.append(number)

print(newlist)

# capitalize a list of words
sentence = "the quick brown fox jumps over the lazy dog"
capitalized = [x.capitalize() for x in sentence]
print(capitalized)

# sum the absolute values of a list
abs_sum = sum([abs(x) for x in numbers])
print(abs_sum)

# create a set of all letters used in a string
letters_used = {letter for letter in "hello"}
print(letters_used)

# get all squares of numbers 0 to 9
squares = [x**2 for x in range(10)]
print(squares)

# get a list of all numbers from 0 to 99 which are divisible by 3 and 5
divisible = [x for x in range(100) if x % 3 == 0 or x % 5 == 0]
print(divisible)


# create a list of tuples in range (0,0)-(2,2)
tuples = [(x, y) for x in range(3) for y in range(3)]
print(tuples)

# create a dictionary with capitalized keys out of another dictionary
phonebook = {}
phonebook["jhon"] = 1407002857
phonebook["jack"] = 1407002858
phonebook["jill"] = 1407002859

capitalized_d = {x[0] : x[1].capitalize() for x in phonebook.items()}
print(capitalized_d)
