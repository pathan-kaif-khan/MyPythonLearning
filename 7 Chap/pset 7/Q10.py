#reversed multiplication table
n = int(input("enter num:"))

for i in range(1,11):
    print(f"{n} X {11-i}= {n*11-i}")