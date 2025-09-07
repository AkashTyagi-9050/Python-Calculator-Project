# Calculator using Python 

def add2numbers(a,b):
    return a+b

def subtract2numbers(a,b):
    return a-b

def multiply2numbers(a,b):
    return a*b

def divide2numbers(a,b):
    if b == 0:
        return "Error! Division by zero."
    return a/b

output = 1
#Looping Menu
while 0<output<5:
    print("\n===== Calculator Menu =====")
    output = int(input("1. add \n" \
    "2. subtract\n" \
    "3. Multiple\n" \
    "4. Divide\n" \
    "5. Exit\n" \
    "Your Response: "))

    if output == 1:
        a = int(input("Please give 1st Number: "))
        b = int(input("Please give 2st Number: "))
        result = add2numbers(a,b)
        print("Result : ", result)
        print("*****************************\n")
    
    elif output ==2:
        a = int(input("Please give 1st Number: "))
        b = int(input("Please give 2st Number: "))
        result = subtract2numbers(a,b)
        print("Result : ", result)
        print("*****************************\n")

    elif output ==3:
        a = int(input("Please give 1st Number: "))
        b = int(input("Please give 2st Number: "))
        result = multiply2numbers(a,b)
        print("Result : ", result)
        print("*****************************\n")

    elif output ==4:
        a = int(input("Please give 1st Number: "))
        b = int(input("Please give 2st Number: "))
        result = divide2numbers(a,b)
        print("Result : ", result)
        print("*****************************\n")

    else:
        break


