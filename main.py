# Write a python calculator program that takes two numbers and an operator as input and returns the result of the operation.
# The program should keep running until the user enters 'exit'.


def calculator():
    while True:
        num1 = input("Enter first number: ")
        if num1 == "exit":
            break
        num2 = input("Enter second number: ")
        if num2 == "exit":
            break
        operator = input("Enter operator: ")
        if operator == "exit":
            break
        if operator == "+":
            print(int(num1) + int(num2))
        elif operator == "-":
            print(int(num1) - int(num2))
        elif operator == "*":
            print(int(num1) * int(num2))
        elif operator == "/":
            print(int(num1) / int(num2))
        else:
            print("Invalid operator")
        
calculator()
