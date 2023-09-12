# FizzBuzz Implementation
#
# The rules are as follows:
# - If a number is divisible by both 3 and 5, print "FizzBuzz"
# - If a number is divisible by 3, print "Fizz"
# - If a number is divisible by 5, print "Buzz"
# - If a number is not divisible by either, print the number itself
#
# This program will print the results for numbers 1 through 100.

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)