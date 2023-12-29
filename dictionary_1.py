di={
    1:"name",
    2:"true",
    3:"eye",
    4:"jay"
}
b=int(input("enter number to find key:"))

f=False
for a in di:
    if b==a:
        print("yes available")
        f=True

if f==False:
    print("not available")