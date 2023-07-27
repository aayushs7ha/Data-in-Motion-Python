# Week 3
#Problem 1:
# Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.
def final_price(price,discount_in_percent):
    return (price - (discount_in_percent / 100 ) * price)
try:
    initial_price = float(input("Enter the initial price : "))
    percentage = float(input("Enter the discount percentage : "))
except ValueError:
    print("Can't enter strings here")
else:
    print(f'Final Price after discount is {final_price(initial_price,percentage)}')