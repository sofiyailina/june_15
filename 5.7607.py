for n in range(1000):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + b[-3:]
    if n % 3 != 0:
        d = ((n % 3)*3)
        b = b + bin(d)[2:]
    if int(b, 2) >= 76:
        print(n)
        break