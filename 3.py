number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
symbol = input("Enter symbol (+, -, * or /): ")

if symbol == "+":
    print("The sum of number: ", number1 + number2)
elif symbol == "-":
    print("The difference of number: ", number1 - number2)
elif symbol == "/":
    if number2 == 0:
        print("Error, Division by zero is not possible.")
    else:
        print("The quotient of number: ", number1 / number2)
elif symbol == "*":
    print("The product of number: ", number1 * number2)
else:
    print("Error")

