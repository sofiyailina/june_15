for n in range(4, 2000):
    s = '3' + '5'*n
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '32', 1)
        if '355' in s:
            s = s.replace('355', '25', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    summ = 0
    for d in s:
        summ += int(d)

    if summ == 17:
        print(n)
        break