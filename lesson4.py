#Ex 1
for i in range(10, 0, -1):
    print(i)

#Ex 2
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print("Sum:", total)

#Ex 3
for i in range(1, 20, 3):
    print(i)

#Ex 4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = 101
while True:
    if is_prime(n):
        print("First prime over 100:", n)
        break
    n += 1

#Ex 5
list = [1, 2, 3, 4, 5]
rev = []
for i in list[::-1]:
    rev.append(i)
print(rev)

#Ex 6
list = ["this", "is", "a", "word"]
iter = iter(list)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

#Ex 7
students = [("Alice", [90, 95]), ("Bob", [85, 88])]
for name, grades in students:
    print(name)
    for grade in grades:
        print("->", grade)

#Ex 8
list = []
for i in range(0, 21, 2):
    list.append(i)
print(list)

#Ex 9
num = 1
while num <= 1000:
    print(num)
    num *= 2

#Ex 10
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(index, color)

#Ex 11
squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(squares)

#Ex 12
cubes = {x: x**3 for x in range(1, 6)}
print(cubes)

#Ex 13
text = "comprehension in python"
vowels = {ch for ch in text if ch in "aeiou"}
print(vowels)

#Ex 14
gen = (x**2 for x in range(1, 11))

for value in gen:
    print(value)

#Ex 15
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

for num in fibonacci(100):
    print(num)