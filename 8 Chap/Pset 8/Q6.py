#inches to cms

def inch_to_cms(inch):
    return inch * 2.54

n = int(input("enter inch:"))

print(f"{n} inch = {inch_to_cms(n)} cm")