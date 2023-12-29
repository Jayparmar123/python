t=(0,1,4,7,5,6,2,3)
i=int(input("enter number to verify:"))
t=list(t)

# for j in t:
#     if j==i:
#          print("yes available:",j)
#     else:
#           print("not availabale")

b=-1
found=False
for j in t:
        b=b+1
        if i==j:
            print(b)
            found=True
if found==False:
      print("not found")