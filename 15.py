# 15. Write a Python program to give advice based on the temperature:
# Temperature > 30°C: "It's hot, stay hydrated!"
# Temperature between 15-30°C: "Enjoy the weather!"
# Temperature < 15°C: "It's cold, wear warm clothes!"
temperature = float(input("Enter the temperature in Celsius: "))
if temperature > 30:
    print("It's hot, stay hydrated!")
elif 15 <= temperature <= 30:
    print("Enjoy the weather!")
else:
    print("It's cold, wear warm clothes!")
