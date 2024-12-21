# 3. Write a program that asks the user for a number in the range of 1 to 12.
# The program should display the corresponding month, where 1=january, 2=february, ...
month = int(input("Enter a number between 1 and 12: "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Error: Invalid month number")
