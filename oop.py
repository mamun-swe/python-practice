class Person:
    name = "john"
    age = 23

    def personInfo():
        return "Hello"


isinstance = Person

print(isinstance.personInfo())


class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)


# init()
class InitFUnctionCLass:
    def __init__(self, number):
        self.number = number

    def returnNumber(self):
        return self.number


var = InitFUnctionCLass(10)
print(var.returnNumber())


# Exercise
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def __init__(self, name, color, value):
        self.name = name
        self.color = color
        self.value = value

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (
            self.name,
            self.color,
            self.kind,
            self.value,
        )
        return desc_str


# your code goes here
car1 = Vehicle("Fer", "red", 60000.00)
car2 = Vehicle("Jump", "blue", 10000.00)


# test code
print(car1.description())
print(car2.description())
