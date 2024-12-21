# 22. Write a program to check whether the given number is between 1 and 100 or not.
num = int(input("Enter a number: "))
if 1 <= num <= 100:
    print(f"{num} is between 1 and 100")
else:
    print(f"{num} is not between 1 and 100")
