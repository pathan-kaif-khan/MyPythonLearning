#methods in dict 
marks={
    "kaif":100,
    "kabir":55,
    "rahim":70
}
print(marks.keys())
                    #prints keys in dictonary
print(marks.values())
                    #prints values in dictonary
marks.update({"kaif":99,"sana":35})
                    #will change kaif marks to 99 and 
                    #add new value basicly its changing
                    #  its dict present in {}

print(marks)
print("######################################################")
# print(marks.get("kaif"))   -  print 99
# print(marks["kaif"])       - also print 99 
print(marks.get("kaif1"))# but  retun none 
print(marks["kaif1"])    # it will rise an error