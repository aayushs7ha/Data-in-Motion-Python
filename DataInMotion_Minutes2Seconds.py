
# Problem 1: Write a function that takes in an integer, minutes, and converts it into seconds
def minutesInseconds(minutes):
    return minutes * 60
try:
    minutes = int(input("Enter Minutes : "))
except ValueError:
    print("String is not a valid entry")
else:
    print(f'{minutes} Minutes is {minutesInseconds(minutes)} seconds : ')

