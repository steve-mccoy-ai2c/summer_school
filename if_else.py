def checker(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    else:
        return "Zero"
    
num = checker(int(input("Enter a number: ")))
print(num)