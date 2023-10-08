


# correct way to use the args statement
def my_func(name, age, *kwargs):
    for x in kwargs:
        print(x)
my_func('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Lambda function
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))