class PyConverter:
    def __init__(self, num: float, unit: str) -> None:
        self.num = num
        self.unit = unit

    def toKms(self) -> float:
        match self.unit:
            case "kilometers":
                return self.num
            case "meters":
                return self.num / 1000.0
            case "centimeters":
                return self.num / (1000.0 * 100.0)
            case _:
                return 0.0

    def toMeters(self) -> float:
        match self.unit:
            case "kilometers":
                return 1000.0 * self.num
            case "meters":
                return self.num
            case "centimeters":
                return self.num / 100.0
            case _:
                return 0.0

    def toCentimeters(self) -> float:
        match self.unit:
            case "kilometers":
                return 1000.0 * 100.0 * self.num
            case "meters":
                return 100.0 * self.num
            case "centimeters":
                return self.num
            case _:
                return 0.0


def main() -> None:
    ob = PyConverter(9, "kilometers")

    print(f"to process: {ob.num} {ob.unit}")
    print(f"to centimeters: {ob.toCentimeters():.2f}")
    print(f"to meters: {ob.toMeters():.2f}")
    print(f"to kms: {ob.toKms():.2f}")


if __name__ == "__main__":
    main()
