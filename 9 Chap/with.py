f = open("file.txt")
print(f.read())
f.close
#we can write the same code like below

with open("file.txt") as f:
    print(f.read())
#we dont have to close again and again in with statement
