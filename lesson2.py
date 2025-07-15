# more on data types
# reference documentation:  https://docs.python.org/3/library/stdtypes.html
# https://docs.python.org/3/reference/expressions.html#operator-summary

### booleans
# determine if the following statement is true or false
# you can test these in the interpreter or using print statements
True and True
#True
False and True
#False
True or False
#True
False and True or False
#False
False and (True or False)
#False

### converting data types
# what is the difference between implicit and explicit type conversion?
'''
implicit conversion is done automatically by Python, while explicit conversion is done by the programmer using functions like int(), float(), str(), etc.
'''

# determine if the following statements result in errors or not
5 + '5' 
error

5 + int('5') 
10
int(5.2) + int('5')
10
5.2 + float('5')
10.2

5 and '5' # bonus question, does this evaluate to true or false?
True

[1, 2] or [3, 4] # bonus question, does this evaluate true or false?
True

True + 5
6

False + 5
5

my_guess = input('Enter a guess')
print('10 times your guess is ' + 10 * my_guess)

# can you see how implicit conversions can get you in trouble...?

### binary and hexadecimal
# Convert 10 to binary
1010

# Convert 255 to binary
11111111

# Convert 0b10101 to decimal
21

# Convert 0x10101 to decimal
65793

# Perform a bitwise 'or' between 0b110101 and 0b101010, what is its decimal value
63

# Perform a bitwise 'or' between 53 and 42, what is its binary value
111111


# Do the same with a bitwise 'and'
32
100000

### string manipulation
# Convert 'hello' to bytes and then convert the bytes to an integer
# hint: use the encode method
b = 'hello'.encode()
num = int.from_bytes(b, 'big')
print(num)

# What's the difference between strip and replace?  When might you use both?
'''
strip removes leading and trailing whitespace, while replace replaces specific characters or substrings with others.
'''


# Use index, len, slicing, and concatenation to 
# replace the word 'horrible' with 'beautiful'
horrible = "It's a horrible day"
print(horrible[:7] + 'beautiful ' + horrible[16:])


# "It's a horrible day."
# "It's a beautiful day."

# scan through the 'is____' string methods in the documentation.
# how might you use those methods to clean a dataset?
'''
Filtering out unwanted rows (e.g., remove entries that aren't all digits with isdigit()).
Validating data (e.g., check if names contain only letters with isalpha()).
Standardizing case (e.g., use islower() or isupper() to check and then convert).
Removing or flagging entries with only whitespace using isspace().
'''