a = (1,2,3,4)
print(type(a))
b = (1)#if i want to insert only 1 value in tuple it will display its type as int
print(type(b))
#to fix this i will add , to python can know this is a tuple not a int datatype
c =(1,)#here is only one value but it is now known as tuple
print(type(c))

print("************************************************")

x = (1,45,342,3424,False,45,"rohan","shivam")
print(x)
no = x.count(45)
print(no)

print(len(x))#print no of elements in x tuple
