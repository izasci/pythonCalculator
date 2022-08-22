from art import logo
from replit import clear
def add(a, b):
  return a + b
def subtract(a, b):
  return a - b
def multiply(a, b):
  return a * b
def divide(a, b):
  if b == 0:
    print("You can't divide by 0.")
  return a / b
def operation(a, operator, b):
  return operations[operator](a, b)

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculate():
      
  print(logo)    
  a = float(input("What's your first number?: "))
  for symbol in operations:
    print (symbol)
  should_continue = True
  while should_continue:
    operator = input("Pick an operator: ")
    while operator not in operations:
      operator = input("Pick an operator: ")
    b = float(input("What's the next number? "))
    answer = operation(a, operator, b)
    print(f"{a} {operator} {b} = {answer}")
    repeat = input(f"Type 'y' to continue with {answer} or type 'n' to start new calculation: ")
    if repeat == "n":
      clear()
      calculate()

calculate()
    
  