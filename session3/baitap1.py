while True:
    from maytinh2 import calculate
    from random import randint, choice
    x = randint(0, 9)
    y = randint(0, 9)
    op = choice(["+", "-", "*", "/"])
    error = randint(-1, 1)
    r = calculate(x, y, op) + error
    print(x, op, y, "=", r)
    new = input("(Y/N)? ")
    op = calculate(x, y, op)
    if new == "y":
        if op == r:
            print(" dung roi`")
        if op != r:
            print("sai roi`")
    elif new == "n":
        if op == r:
            print("sai roi`")
        if op != r:
            print("dung roi`")
