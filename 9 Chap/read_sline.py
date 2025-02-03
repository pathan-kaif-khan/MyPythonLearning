f = open("file.txt")

line1 = f.readline()
print(line1,type(line1))#print type as string

line2 = f.readline()
print(line2,type(line2))

line3 = f.readline()
print(line3,type(line3))

line4 = f.readline()
print(line4,type(line4))

line5 = f.readline()# print null
print(line5=="") 
f.close
