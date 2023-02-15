#THIS IS A CALCULATOR PROJECT
number1 = eval(input("Enter your first number:"))
number2 = eval(input("Enter your second number:"))

operator = input("Enter operator:")

def add(num1,num2):
    result = num1 + num2
    print(result)

def subtact(num1,num2):
    result = num1 + num2
    print(result)

def divide(num1,num2):
    result = num1 / num2
    print(result)

def multiply(num1,num2):
    result = num1 * num2
    print(result)

#CHECK OPERATOR
if operator == "+":
    add(number1,number2)
elif operator == "-":
    subtract(number1,number2)
elif operator == "/":
    divide(number1,number2)
elif operator == "*" or operator == "X" or operator == "x":
     multiply(number1,number2)
else:
    print("Invalid operator")