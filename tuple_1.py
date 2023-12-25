i=(0,)
k=int(input("enter value:"))
i=list(i)

for tup1 in range(1,k+1):
    a=int(input(f"enter value {k}:"))
    i.append(a)

i=tuple(i)
print(i)
print(type(i))

s=0
for j in i:
    s=s+j
    avg=s/k

print("sum is:",s)
print("average is:",avg)