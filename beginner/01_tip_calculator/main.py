"""Calculate a tip and split the bill between diners."""


def get_number(prompt: str, *, minimum: float = 0) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value < minimum:
                print(f"Please enter at least {minimum}.")
                continue
            return value
        except ValueError:
            print("That doesn't look like a number. Try again.")


def main() -> None:
    print("\nTip Calculator\n------------")
    bill = get_number("Bill total: $", minimum=0.01)
    tip_percent = get_number("Tip percentage: ")
    people = int(get_number("How many people? ", minimum=1))
    tip = bill * tip_percent / 100    total = bill + tip
    print(f"\nTip: ${tip:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Each person pays: ${total / people:.2f}")


if __name__ == "__main__":
    main()
