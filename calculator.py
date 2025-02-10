# create a simple calculator (+,-,/,*) else entered an invalid operator
# first, operator, second

first_num = int(input("Enter first number: "))
operator = input("Enter operator: ")
second_num = int(input("Enter second number: "))

if operator == "+":
    print(first_num + second_num)
elif operator == "-":
    print(first_num - second_num)
elif operator == "*":
    print(first_num * second_num)
elif operator == "/":
    print(first_num / second_num)
else:
    print("entered an invalid operator")
