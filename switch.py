i="yes"
while(i=="yes"):
    a=int(input("enter value of a:"))
    b=int(input("enter value of b:"))
    c=input("enter +,-,*,/:")

    match c:
        case "+":print(a,"+",b,"=",a+b)

        case "-":print(a,"-",b,"=",a-b)

        case "*":print(a,"*",b,"=",a*b)

        case "/":print(a,"/",b,"=",a/b)

        case _:print("please enter any one sing from above")
    print("do you want to continue:")
    i=input("Yes or No:")
    if i=="no":
        break