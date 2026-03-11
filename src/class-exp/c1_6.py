"""Compute factorial of a non-negative integer."""

num = int(input("Input a number: "))

result = 1
for i in range(2, num + 1):
    result *= i

print(f"Factorial of {num} is {result}.")
