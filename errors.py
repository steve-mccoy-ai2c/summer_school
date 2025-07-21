'''
give a list of numbers write a program
1. loop through the list
2. skips any None values or non-integer values with an error message using try/except
3. raises a ValueError if it finds a negative number (stops the program)
4. collects all valid positive integers into a new list
5. prints the new list and the sum of its numbers
'''
list = [10, 20, 'hello', 5.2, 15, None, 30]

'''
once you have a solution, remove -5 and run it again
hints: 
use isinstance(item, int)
'''

positive_integers = []
for i in list:
    if not isinstance(i, int):
        print(i, "is not an integer")
    elif i < 0:
        raise Exception("Sorry, no numbers below zero") 
    elif i > 0:
        positive_integers.append(i)
print("Integers:", positive_integers)
print("Sum of integers", sum(positive_integers))
    