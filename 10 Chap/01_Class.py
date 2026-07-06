### OPPS IN PYTHON ###
class Employee:
    name = "Kaihan"
    language = "Py"
    salary = 12000

kaihan = Employee()
print(kaihan.name,kaihan.language,kaihan.salary)

######################################################
class Employee:
    
    language = "Py" #This is a class attribute
    salary = 12000

kaihan = Employee()
kaihan.name = "Kaihan" #This is an instance attribute 
print(kaihan.name,kaihan.language,kaihan.salary)

kabir = Employee()
kabir.name = "Kabir"
print(kabir.name,kabir.language,kabir.salary)
