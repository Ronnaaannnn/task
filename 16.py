# 16. Write a Python program that takes a menu option ("Pizza", "Burger", "Pasta") and prints its price:
menu = input("Enter menu option (Pizza, Burger, Pasta): ").lower()
if menu == "pizza":
    print("Price: $10")
elif menu == "burger":
    print("Price: $7")
elif menu == "pasta":
    print("Price: $8")
else:
    print("Invalid menu option")

