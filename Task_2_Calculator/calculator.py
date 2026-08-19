print("\n--- SIMPLE CALCULATOR ---")

while True:
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        operation = input("Choose operation (+, -, *, /): ")

        match operation:

            case "+":
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")

            case "-":
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")

            case "*":
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}")

            case "/":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = {result}")

            case _:
                print("Invalid operation. Please choose +, -, * or /.")

    except ValueError:
        print("Invalid input. Please enter valid numbers only.")

    again = input("\nDo you want another calculation? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for using the calculator!")
        break
