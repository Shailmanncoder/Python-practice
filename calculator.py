try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = input("Choose operator (+, -, x, ÷): ")

    if c == "+":
        print("Result:", a + b)
    elif c == "-":
        print("Result:", a - b)
    elif c == "x":
        print("Result:", a * b)
    elif c == "÷":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operator. Please choose +, -, x, or ÷.")
except ValueError:
    print("Error: Please enter numbers only.")
