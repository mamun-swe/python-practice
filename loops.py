count = 0
while count < 5:
    print(count)
    count += 1
    if count >= 3:
        break

# nested loop
names = ["john", "Jane"]
foods = ["pizza", "sushi", "burgers"]

for name in names:
    for food in foods:
        print(name + " likes " + food)

# print only even numbers using a loop
for x in range(10):
    if x % 2 != 0:
        continue
    print(x)

# loops will run exactly 10 iterations
for n in range(10, 20, 1):
    print(n)

a = 2
b = 3
while a < 10:
    b += a
    a += 2

print("b: ", b)

# correct way to iterate over a range of numbers
for x in range(5):
    print("range", x)
