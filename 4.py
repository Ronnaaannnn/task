# 4. A school has following rules for grading system:
# Below 25 - F, 25 to 45 - E, 45 to 50 - D, 50 to 60 - C, 60 to 80 - B, Above 80 - A
marks = int(input("Enter marks: "))
if marks < 25:
    print("F")
elif marks <= 45:
    print("E")
elif marks <= 50:
    print("D")
elif marks <= 60:
    print("C")
elif marks <= 80:
    print("B")
else:
    print("A")
