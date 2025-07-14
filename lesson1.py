my_str = 'word1 word2'

print(my_str[2])

words = my_str.split()
print(words[1])

print(my_str.title())
print(my_str.upper())

my_list = my_str.split()
print(my_list)

print(my_list.count('word1'))
my_list.append('word3')
print(my_list)


print(my_list[0][2])
print(my_list[::-1])

my_dict = {'dogs': 3, 'cats': 4, 'alpacas': 100}
my_dict = {'dogs': 3, 'cats': 4, 'alpacas': 100, 'frogs': 5}
print(my_dict)

my_dict.update({'birds': 7}) 
print(my_dict)

print(my_dict['dogs'])

def return_10(anything):
    return 10
print(return_10('hello'))