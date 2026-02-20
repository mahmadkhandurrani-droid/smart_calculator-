# main.py
"""
Smart Calculator with History
CLI tool for addition, subtraction, multiplication, and division
Tracks all calculations in the current session.
"""

from calculator_utils import add, subtract, multiply, divide

def get_number(prompt):
    """Get a valid number from the user"""
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input! Please enter a number.")

def main():
    """Main loop of Smart Calculator with history"""
    history = []

    while True:
        print("\n--- Smart Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Exit")

        choice = input("Choose (1-6): ")

        if choice in ["1", "2", "3", "4"]:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == "1":
                result = add(num1, num2)
                operation = f"{num1} + {num2} = {result}"
            elif choice == "2":
                result = subtract(num1, num2)
                operation = f"{num1} - {num2} = {result}"
            elif choice == "3":
                result = multiply(num1, num2)
                operation = f"{num1} * {num2} = {result}"
            elif choice == "4":
                result = divide(num1, num2)
                operation = f"{num1} / {num2} = {result}"

            print("Result:", result)
            history.append(operation)

        elif choice == "5":
            if not history:
                print("No calculations yet.")
            else:
                print("\n--- Calculation History ---")
                for i, op in enumerate(history, 1):
                    print(f"{i}. {op}")

        elif choice == "6":
            print("Exiting Smart Calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    main()
