# Problem 2: Write a function that takes two numbers as arguments and returns their sum.

def sum(a,b):
    return a+b
try:
    num1 = float(input("Enter First Number : "))
    num2 = float(input("Enter Second Number: "))
except ValueError:
    print("String is not a valid entry")
else:
    print(f'Sum of 2 Numbers {num1} and {num2} is : {round(sum(num1,num2),3)}')