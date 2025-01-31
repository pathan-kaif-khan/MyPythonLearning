#recursive function to calculate sum of the first n number
'''
logic 
sum(1) : 1
sum(2) : 1 + 2 
sum(3) : 1 + 2 + 3
sum(4) : 1 + 2 + 3 + 4
sum(n) : 1 + 2 + 3 .... n-1 + n
'''
#program 
def sum(n):
    if (n==1):
        return 1
    return sum(n-1) + n

a = int(input("enter a value:"))

print(sum(a))
