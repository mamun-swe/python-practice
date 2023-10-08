x = "hello 8"
print(len(x))

if "fun" in "this is fun":
    print("available")


name = "x"
result = "John" if name == "John" else "Jane"
print(result)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is %d"

print(format_string % data)

# multi-line string
multi_line = """This is a 
Multiline string"""
print(multi_line)

# join a string with a comma delimiter
print(",".join(["foo", "bar"]))

# split a string to a list using a comma delimiter
print("foo,bar".split(","))

# print a number using a format string
number = 1123
print("%d" % number)

# print a number using an "f string"
print(f"{number}")

# print a number using the string format function
print("{number}".format(number=number))
