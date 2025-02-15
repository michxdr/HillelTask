while True:
    operation = input("Enter operation (+, -, *, /): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero.")
            continue
    else:
        print("Invalid operation.")
        continue

    print(f"The result is: {result}")

    continue_calculating = input("Do you want to perform another calculation? (y/n): ").lower()
    if continue_calculating != 'y' and continue_calculating != 'yes':
        print("Calculator is closing.")
        break
