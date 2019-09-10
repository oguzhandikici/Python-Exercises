def gen(n):
    a=1
    b=1
    for x in range(n):
        yield a
        a,b = b,a+b