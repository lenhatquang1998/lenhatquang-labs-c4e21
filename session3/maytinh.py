while True:
    x = int(input("x= "))
    op = input("operation(+, -, *, /)")
    y = int(input("y= "))
    if op == "+":
        tong = x+y
        print(x, "+", y, "=", tong)
    elif op == "-":
        hieu = x-y
        print(x, "-", y, "=", hieu)
    elif op == "*":
        tich = x*y
        print(x, "*", y, "=", tich)
    elif op == "/":
        thuong = x/y
        print(x, "/", y, "=", thuong)
    else :
        print("k co")