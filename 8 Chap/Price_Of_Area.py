#Price of Area/Plot

def Area(l,w):   
    return l * w
l = float(input("enter len"))
w = float(input("enter wid"))
result =Area(l,w)
print(result)
pri = float(input("enter per square feet area price:"))
plot_Price = pri*result
print("price of your plot :",plot_Price)