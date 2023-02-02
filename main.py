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

def convert_base(number, from_base, to_base):
    number = int(number, from_base)
    if to_base == 2:
        return bin(number).replace("0b", "")
    elif to_base == 8:
        return oct(number).replace("0o", "")
    elif to_base == 10:
        return str(number)
    elif to_base == 16:
        return hex(number).replace("0x", "")
    else:
        return None

def infinity_calculator():
    while True:
        num1 = input("Enter the first number: ")
        operator = input("Enter an operator (+, -, *, /, c): ")
        if operator == 'c':
            from_base = int(input("Enter the base of the first number (2, 8, 10, 16): "))
            to_base = int(input("Enter the base to convert to (2, 8, 10, 16): "))
            result = convert_base(num1, from_base, to_base)
            if result is not None:
                print("Result: ", result)
            else:
                print("Invalid conversion. Try again.")
        else:
            num2 = float(input("Enter the second number: "))
            result = perform_operation(float(num1), float(num2), operator)
            if result is not None:
                print("Result:", result)
            else:
                print("Invalid operator. Try again.")

        again = input("Do you want to continue? (YES / NO)")
        if again.lower() == 'NO':
            break

infinity_calculator()


