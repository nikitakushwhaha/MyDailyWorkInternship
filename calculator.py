#Calculator
#Prompting user to provide 2 variables 
num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second Number: "))
function = input("Choose the operation that you want to perform: ")
def Operartion(num1,num2): 
    if function == "+":
        sum = num1+num2
        return sum
    elif function == "-":
        dif = num1-num2
        return dif
    elif function == "/":
        div = num1/num2
        return div
    elif function == "//":
        Fdiv = num1//num2
        return Fdiv
    elif function == "%":
        remainder = num1%num2
        return remainder
    elif function == "*":
        multi = num1*num2
        return multi
    elif function == "**":
        pow = num1**num2
        return pow
    else:
        return (num1 , num2)
print(Operartion(num1,num2))

# # Quit professional Simple Calculator

# # Function to perform addition
# def add(x, y):
#     return x + y

# # Function to perform subtraction
# def subtract(x, y):
#     return x - y

# # Function to perform multiplication
# def multiply(x, y):
#     return x * y

# # Function to perform division
# def divide(x, y):
#     # Check for division by zero
#     if y == 0:
#         return "Error! Division by zero."
#     return x / y

# # Main program
# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# # Take input from the user
# choice = input("Enter choice (1/2/3/4): ")

# # Input two numbers
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# # Perform the selected operation
# if choice == '1':
#     print(f"The result is: {add(num1, num2)}")
# elif choice == '2':
#     print(f"The result is: {subtract(num1, num2)}")
# elif choice == '3':
#     print(f"The result is: {multiply(num1, num2)}")
# elif choice == '4':
#     print(f"The result is: {divide(num1, num2)}")
# else:
#     print("Invalid input! Please select a valid operation.")
