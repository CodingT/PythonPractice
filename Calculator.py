# Simple Console Calculator
num1 = float (input ("Enter a number: "))
op = input ("Please enter an operator +-*/ : ")
num2 = float (input ("Enter another number: "))

if op == "+": print(num1 + num2)
elif op == "-": print(num1 - num2)
elif op == "*": print(num1 * num2)
elif op == "/": print(num1 / num2)
else: print("Invalid operator")


