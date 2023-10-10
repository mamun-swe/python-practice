phonebook = {}
phonebook["jhon"] = 1407002857
phonebook["jack"] = 1407002858
phonebook["jill"] = 1407002859

print(phonebook)

# merging two dictionaries
phonebook2 = {}
phonebook2["x"] = 1407002857
phonebook2["y"] = 1407002857

new_dict = {}
# new_dict.update(phonebook)
# new_dict.update(phonebook2)
new_dict = {**phonebook, **phonebook2}
print(new_dict)


# Iterating over dictionaries
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# Removing a value
phonebook.pop("jhon")
del phonebook["jack"]
print(phonebook)

# Exercise
phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
# your code goes here
phonebook.__setitem__("Jake", 938273443)
phonebook.pop("Jill")

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")


# fetching all keys in a dictionary
# way 1
print(phonebook.keys())

# way 2
dict_keys = []
for key in phonebook:
    dict_keys.append(key)
print(dict_keys)

# way 3
dict_keys_2 = [x for x in phonebook]
print(dict_keys_2)


# fetch all values of a dictionaries as a list
dict_values = phonebook.values()
print(dict_values)

# Make empty a dictionary
# phonebook.clear()
print(phonebook)

# get a value from a dictionary in a way that doesn't raise an exception for missing keys
v = phonebook.get("hi")
print(v)

# set a value in a dictionary in a way that doesn't override existing values
phonebook["Jack"] = 123 if "Jack" not in phonebook else None
print(phonebook)
