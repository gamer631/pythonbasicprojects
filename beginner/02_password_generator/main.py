"""Generate a password from selected character groups."""
import secrets
import string



def main() -> None:
    print("Password Generator")
    try:
        length = int(input("Length (8 or more): "))
    except ValueError:
        print("Please enter a whole number.")
        return
    if length < 8:
        print("Use at least 8 characters.")
        return
    groups = []
    if input("Include lowercase? [Y/n] ").lower() != "n": groups.append(string.ascii_lowercase)
    if input("Include uppercase? [Y/n] ").lower() != "n": groups.append(string.ascii_uppercase)
    if input("Include digits? [Y/n] ").lower() != "n": groups.append(string.digits)
    if input("Include symbols? [y/N] ").lower() == "y": groups.append("!@#$%^&*()-_=+[]{}")
    if not groups:
        print("Select at least one character group.")
        return
    alphabet = "".join(groups)
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    print(f"\nGenerated password: {password}")
    print("Don't reuse passwords across accounts.")


if __name__ == "__main__":
    main()
