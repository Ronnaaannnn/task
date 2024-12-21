# 9. Write a Python program that takes a character input and checks whether it is a vowel or consonant.
char = input("Enter a character: ").lower()
if char in "aeiou":
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")
