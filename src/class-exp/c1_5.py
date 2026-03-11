n = int(input("Enter a number: "))

if n < 0:
    print("Not an Armstrong number")
    exit(0)

original = n
digits = len(str(n))
total = 0

while n > 0:
    digit = n % 10
    total += digit ** digits
    n //= 10

# For input 0, loop won't run; 0 is Armstrong
if original == 0:
    total = 0

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
