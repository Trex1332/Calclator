def main():
    try:
        num1 = float(input("First Number: "))
        func = input("Would your Like to +, *, - or /: ")
        num2 = float(input("Second Number: "))
    except:
        print("Invalid")
        main()
    if func == "+":
        print(add(num1,num2))
        main()
    elif func == "/":
        print(div(num1,num2))
        main()
    elif func == "*":
        print(mult(num1,num2))
        main()
    elif func == "-":
        print(sub(num1,num2))
        main()
    else:
        print("Invalid")
        main()


def add(a,b):
    return  a+b
def sub(a,b):
    return a -b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b





main()

