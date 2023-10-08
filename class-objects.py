class Person:
    name = "john"
    age = 23


# isinstance(age, Person)

my_list = [1, 2, 3, 4]
try:
    my_list[5] = 0
except IndexError:
    print("error")
