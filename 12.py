# 12. Write a Python program to check if a given character is uppercase, lowercase, or a digit.
char = input("Enter a character: ")
if char.isupper():
    print(f"{char} is uppercase")
elif char.islower():
    print(f"{char} is lowercase")
elif char.isdigit():
    print(f"{char} is a digit")
else:
    print(f"{char} is neither uppercase, lowercase, nor a digit")
