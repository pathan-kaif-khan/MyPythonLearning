#function for multiplication table

def mul_table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

a = int(input("enter num:"))
mul_table(a)