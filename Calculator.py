num1=float(input("Enter number 1: "))
num2=float(input("Enter number 2: "))
def Add(num1,num2):
    print(num1+num2)
def Sub(num1,num2):
    print(num1-num2)
def Multi(num1,num2):
    print(num1*num2)
def Divi(num1,num2):
    print(num1/num2)
while True:
    choice=input("Do you wanna continue [Y/N]") 
    if choice=="Y":
        op=input("Enter Operation +-/*: ")
        if op=="+":
            Add(num1,num2)
        elif op=="-":
            Sub(num1,num2)
        elif op=="*":
            Multi(num1,num2)
        elif op=="/":
            Divi(num1,num2)
        else:
            break
    elif choice=="N":
        print("Thank you for using my calculator")
    break 