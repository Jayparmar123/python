# 1.list
# 2.tuple
# 3.dictionary
# a=[1,2,3,4,"hi",True,12.50]
# a[0]=23

# print(a)
# print(a[4])

# in not in
# is is not
# print("h" in a) :false
# print("hi" in a) :true
# print("h" not in a) :true
# print("hi" not in a) :false




# # j=0
# # for i in a:
# #     j=j+i
# # print(j)

a=[12,24,35,47,58]
b= a[0]

for c in a:
    # Compare each number with the current largest number
    if c < b:
        b = c

print("smallest number is:",b)



# Example list of numbers
# a = [10, 5, 8, 20, 15]

# # Initialize a variable to store the largest number
# b = a[0]

# # Iterate through the list
# for c in a:
#     if c > b:
#         b = c

# # Print the result
# print("The largest number is:", b)



# 1 2 4 1 4 6 4 7 9 7

# 1-> 2
# 2-> 
# 3->

l=[1,3,4,1,6,3,4,1,7,9,2,3,1,2,5,5]

a=l[0]

for i in l:
    b=0
    if a==i:
        b=b+1

print(b)

