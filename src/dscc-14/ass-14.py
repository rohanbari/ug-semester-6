import math


def find_roots(a, b, c):
    # Calculate discriminant
    discriminant = (b ** 2) - (4 * a * c)

    # Find roots based on discriminant
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)

        print("Roots are real and different.")
        print("Root 1 =", root1)
        print("Root 2 =", root2)

    elif discriminant == 0:
        root = -b / (2 * a)

        print("Roots are real and equal.")
        print("Root =", root)

    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)

        print("Roots are complex.")
        print("Root 1 =", real_part, "+", imaginary_part, "i")
        print("Root 2 =", real_part, "-", imaginary_part, "i")


def main():
    # Input coefficients
    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))
    c = float(input("Enter value of c: "))

    # Check valid quadratic equation
    if a == 0:
        print("Coefficient 'a' cannot be zero.")
    else:
        find_roots(a, b, c)


if __name__ == "__main__":
    main()
