p = open("poem.txt")
poem = p.read()
if("jonny" in poem):
    print("jonny is present in the poem")
else:
    print("jonny is not present in the poem")
p.close() 