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
