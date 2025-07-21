'''
1 2 3
1 2 3
1 2 3

'''

def loop_example():
    for _ in range(3):
        num = ''
        for digit in str(123):
            num += digit + ' '
        print(num.strip())

loop_example()