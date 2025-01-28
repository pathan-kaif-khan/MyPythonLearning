a = int(input("enter num:"))
b = int(input("enter num:"))
c = int(input("enter num:"))
d = int(input("enter num:"))
# Initialize the largest variable
largest = a

# Compare each number
if b > largest:
    largest = b
if c > largest:
    largest = c
if d > largest:
    largest = d

# Print the largest number
print("The largest number is:", largest)

#my code
# if(a>b & b>c & c>d ):
#     print(a)
# elif(b>c & c>d ):
#     print(b)
# elif(c>d ):
#     print(c)
# elif(d)