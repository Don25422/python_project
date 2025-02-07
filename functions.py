# Builtin functions/Standard library functions

y = max(67,43,89,17,90)
print("THe maximum value is",y)

x = min(67,43,89,17,90)
print("The minimum value is",x)

# User-defined functions
def name():
    print("Don")
name() # calling a function

def multiply():
    x = 10
    y = 2
    print("The multiplication of",x,"and",y,"is",x*y)
multiply()

# parameter/valuable and argument
def add(a, b):
    print("The addition of",a,"and",b,"is",a+b)
add(7,90)

def employee(name,gender,position,salary,age):
    print(name,gender,position,salary,age)
employee("Jack","Male","CEO","$5600",24)
employee("John","Male","Managing director","$560",27)
employee("Mary","Female","Director","$460",26)

# A program that displays details of five students
# Use a user-define function with parameters and argument
#Fullname, age, course, gender
def student(Fullname,age,course,gender):
    print(Fullname,age,course,gender)
student("Emily Rose Anderson", 18, "MIT","Female")
student("Isabella Marie Taylor", 19, "Cybersecurity","Female")
student("Samuel Charles Morgan", 17, "MIT","Male")
student("Benjamin Thomas Davis", 20, "Datascience","Male")
student("Olivia Grace Johnson", 18, "MIT","Female")