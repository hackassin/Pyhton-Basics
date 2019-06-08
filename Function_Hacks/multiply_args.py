def multiply(*args):
    mult = 1
    for i in args:
        mult *= i
    print(mult)


multiply(5, 6, 10)
