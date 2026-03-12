# Palindrome of numbers

def isPalindrome(num: int) -> bool:
    if num < 0:
        return False

    temp = num
    rev = 0
    while temp > 0:
        rev = (10 * rev) + temp % 10
        temp //= 10

    return num == rev


num = int(input("Input a number: "))
print(
    f"The number {num} is {"" if isPalindrome(num) else "not "}a palindrome.")
