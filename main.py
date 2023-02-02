def perform_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return None


def infinity_calculator():
    while True:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        result = perform_operation(num1, num2, operator)
        if result is not None:
            print("Result:", result)
        else:
            print("Invalid operator. Try again.")

        again = input("Do you want to continue? (y/n)")
        if again.lower() == 'n':
            break


infinity_calculator()




