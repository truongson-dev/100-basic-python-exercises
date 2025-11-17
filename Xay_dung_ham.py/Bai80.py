def so_nguyen_to(a):
    if a <= 1:
        return False
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return False
    return True

def asnt(L, a):
    K = []
    for i in L:
        if so_nguyen_to(i):
            K.append(i)
            if len(K) == a:
                return K
    return K

L = list(map(int, input("Nhập vào 1 danh sách số nguyên: ").split('.')))
a = int(input('Nhập một số nguyên: '))
print('Số nguyên tố:', end=' ')
print(asnt(L, a))
