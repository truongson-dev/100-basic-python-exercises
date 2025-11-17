L = list(map(int, input('Nhập list số nguyên L: ').split('.')))
a = int(input('Nhập 1 số nguyên dương: '))

def TB(L,a):
    tong = 0
    for i in range (0,a):
        tong += L[i]
    return tong/a
print(TB(L,a))