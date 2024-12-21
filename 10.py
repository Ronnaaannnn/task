# 10. Write a Python program to input marks and determine the grade based on the following conditions:
# 90-100: A, 80-89: B, 70-79: C, Below 70: Fail
marks = int(input("Enter marks: "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("Fail")
