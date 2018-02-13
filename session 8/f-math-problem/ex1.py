def eval(x,y,op):# parameter
    result = 0

    if op ==  "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y

    return (result)

# a = int(input("Please input 1st operand: "))
# operator = input("Please insert one of this operators (+ - * /): ")
# b = int(input("Please input 2st operand: "))
#
# result = eval(a,b,operator)
# print ('{}{}{}={}'.format(a,operator,b,result))
# #
# a = int(input("Please input 1st operand: "))
# operator = input("Please insert one of this operators (+ - * /): ")
# b = int(input("Please input 2st operand: "))
#
#
# result = 0
# if operator == "+":
#     result = a + b
# elif operator == "-":
#     result = a - b
# elif operator == "*":
#     result = a*b
# elif operator == "/":
#     result = a / b
# print ('{}{}{}={}'.format(a,operator,b,result))
