# 6. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Your Answer is:", num1 + num2)
elif operator == "-":
    print("Your Answer is:", num1 - num2)
elif operator == "*":
    print("Your Answer is:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Your Answer is:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
