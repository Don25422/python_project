# create a simple calculator (+,-,/,*) else entered an invalid operator
# first, operator, second

first_num = int(input("Enter first number: "))
operator = input("Enter operator: ")
second_num = int(input("Enter second number: "))

if operator == "+":
    result = first_num + second_num
    print(result)
elif operator == "-":
    result = first_num - second_num
    print(result)
elif operator == "*":
    result = first_num * second_num
    print(result)
elif operator == "/":
    result = first_num / second_num
    print(result)
else:
    print("entered an invalid operator")