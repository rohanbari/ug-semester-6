import math


def sine_series(x: float, terms: int) -> float:
    if terms <= 0:
        raise ValueError("Number of terms must be greater than 0.")

    result = 0.0
    term = x

    for n in range(terms):
        if n == 0:
            term = x
        else:
            term *= -1 * x * x / ((2 * n) * (2 * n + 1))
        result += term

    return result


def main() -> None:
    x_degrees = float(input("Enter angle in degrees: "))
    terms = int(input("Enter number of terms: "))

    x_radians = math.radians(x_degrees)
    approx = sine_series(x_radians, terms)

    print(f"sin({x_degrees}) using sine series = {approx:.5f}")


if __name__ == "__main__":
    main()
