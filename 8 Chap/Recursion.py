#Recursion in python
'''
factorial of 1 = 1
factorial of 2 = 2 x 1
factorial of 3 = 3 x 2 x 1
factorial of 4 = 4 x 3 x 2 x 1
factorial of 5 = 5 x 4 x 3 x 2 x 1
factorial of n = n x n-1 x.....3 x 2 x 1

factorial (n) = n * factorial(n-1) 
'''
def factorial(n):
    if (n==1 or n==0):
         return 1
    return n * factorial(n-1)


n = int(input("enter a num:"))
print(f"the factorial of this num is :{factorial(n)}")