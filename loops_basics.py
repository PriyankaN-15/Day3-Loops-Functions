# Day 3 - Loop Basics

# for loop with list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# for loop with range
for i in range(1, 6):
    print(i)

# while loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# break example
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# continue example
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# pass example
for i in range(3):
    pass
