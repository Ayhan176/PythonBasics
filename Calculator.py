a = int(input("Enter the value for a: "))

b = int(input("Enter the value for b: "))

operation = input("Choose math operation (+, -, *, /: ")

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)
else:
    print("You did not provide the correct math operation.")