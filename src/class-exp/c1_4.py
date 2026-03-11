# Swapping b/w two numbers without a third variable
num1 = int(input("Input the 1st number: "))
num2 = int(input("Input the 2nd number: "))

print(f"Before swap: {num1}, {num2}")

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"After swap: {num1}, {num2}")
