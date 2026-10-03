# CodSoft Task 2 - Simple Calculator

def calculator():
    print("--- Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("\nChoose operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        
        choice = input("Enter choice (+/-/ */ /): ")

        if choice == '+':
            print(f"Result: {num1 + num2}")
        elif choice == '-':
            print(f"Result: {num1 - num2}")
        elif choice == '*':
            print(f"Result: {num1 * num2}")
        elif choice == '/':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Cannot divide by zero!")
        else:
            print("Invalid operation choice!")
    except ValueError:
        print("Please enter valid numbers!")

calculator()
