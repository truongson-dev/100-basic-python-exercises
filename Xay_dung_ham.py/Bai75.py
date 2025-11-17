def armstrong(a):
    do_dai = len(str(a))
    k = a
    sum = 0
    while a > 0:
        b = a % 10
        sum += b ** do_dai
        a = a // 10
    return k == sum

a = int(input('Nhập số: '))
if armstrong(a):
    print(f'Số {a} là số armstrong')
else:
    print(f'Số {a} không phải là số armstrong')
