
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
c=0
while(c!=5):
    print("======Calculator======")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    c=int(input("Enter Your Choice : "))
    
    if(c==5):
        print("Thank You !")
        break
    elif 1<=c<5:
        a=int(input("Enter First Number : "))
        b=int(input("Enter Second Number : "))

        if(c==1):
            print(f"The Addition of {a} & {b} is ",add(a,b))
        elif(c==2):
            print(f"The Subtraction of {a} & {b} is ",sub(a,b))    
        elif(c==3):
            print(f"The Multiplication of {a} & {b} is ",mul(a,b))
        elif(c==4):
            if b==0:
                print("Division By Zero")
            else:
                print(f"The Division of {a} & {b} is ",div(a,b))
    else:
        print("Enter a Valid Choice !")
