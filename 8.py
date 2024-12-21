# 8. Write a Python program that takes an integer input n.
# From given number, check if it is divisible by both 3 and 5, and print "FizzBuzz" if true.
# If the number is divisible only by 5, print "Buzz." If it is divisible only by 3, print "Fizz."
# Finally, if the number is not divisible by either 3 or 5, print the number itself.
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    print(num)
