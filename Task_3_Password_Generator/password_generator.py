import string
import secrets


def get_yes_no(message):
    while True:
        answer = input(message).strip().lower()

        if answer in ["yes", "no"]:
            return answer

        print("Please enter only yes or no.")


def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    password_characters = ""
    password = []

    if use_uppercase == "yes":
        password_characters += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))

    if use_lowercase == "yes":
        password_characters += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))

    if use_digits == "yes":
        password_characters += string.digits
        password.append(secrets.choice(string.digits))

    if use_symbols == "yes":
        password_characters += string.punctuation
        password.append(secrets.choice(string.punctuation))

    if password_characters == "":
        print("You must select at least one character type.")
        return None

    if length < len(password):
        print(f"Password length must be at least {len(password)}.")
        return None

    for _ in range(length - len(password)):
        password.append(secrets.choice(password_characters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


print("--- PASSWORD GENERATOR ---")

while True:
    try:
        length = int(input("\nEnter password length: "))

        if length <= 0:
            print("Password length must be greater than zero.")
            continue

        use_uppercase = get_yes_no("Include uppercase letters? (yes/no): ")
        use_lowercase = get_yes_no("Include lowercase letters? (yes/no): ")
        use_digits = get_yes_no("Include numbers? (yes/no): ")
        use_symbols = get_yes_no("Include symbols? (yes/no): ")

        generated_password = generate_password(
            length,
            use_uppercase,
            use_lowercase,
            use_digits,
            use_symbols
        )

        if generated_password is not None:
            print(f"\nGenerated Password: {generated_password}")

    except ValueError:
        print("Invalid input. Please enter a valid whole number.")

    again = get_yes_no("\nGenerate another password? (yes/no): ")

    if again == "no":
        print("Thank you for using the Password Generator!")
        break
