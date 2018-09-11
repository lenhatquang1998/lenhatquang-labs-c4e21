def calculate(x, y, op):
    result = 0
    if op == "+":
        result = x + y
    elif op == "-":
        result= x-y
    elif op == "*":
        result = x*y
    elif op == "/" :
        result= x/y
    return result
