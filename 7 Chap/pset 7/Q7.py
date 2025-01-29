#print star pattern
n = int(input("enter num:"))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")

#for better understanding 
for i in range(1,n+1):# range is from 1 to the given num
    print("-"*(n-i),end="")#first print num-1 if num=3 then print - 2times
    print("*"*(2*i-1),end="")#then 2x1-1
    print("")