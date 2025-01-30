#function for Greatest of three num
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    elif(c>a and c>b):
        return c
    
a = 25
b = 3
c = 8
print(greatest(a,b,c))
