
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

print ("welcome to BowaCalc")
print ()

while True:
    print ("Select Operation: \n (1) - Addition \n (2) - Subtraction \n (3) - Division \n (4) Multiplication")

    operation = input("Enter your calculation function choice (1/2/3/4): ")
    num1 = float(input("Enter your  numbers: "))
    num2 = float(input("Enter your second number: "))

    if operation == '1':
        print("Output is: ", add(num1, num2))
    elif operation == '2':
        print("Output is: ", subtract(num1, num2))
    elif operation == '3':
        print("Output is: ", divide(num1, num2))
    elif operation == '4':
        print("Output is: ", multiply(num1, num2))    
    else:
        print("Invalid Operation")

    print("--------")