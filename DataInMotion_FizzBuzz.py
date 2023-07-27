def Fizzbuzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print('Neither a Fizz, Nor a Buzz')

try:
    num = int(input("Enter an Integer : "))
except ValueError:
    print("Strings are not accepted")
else:
    Fizzbuzz(num)