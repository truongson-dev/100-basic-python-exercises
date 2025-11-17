a=int(input('Nhập số nguyên a: '))
def so_nguyen_to(a):
    if a <= 1:
            return False
    for i in range (2,a//2+1):
        if a % i == 0:
            return False
    return True
def phan_tu_la_SNT(a):
    ket_qua = []
    so = 2
    while len(ket_qua) < 0:
         if so_nguyen_to(a):
            ket_qua.append(so)
            so += 1
    return ket_qua
print(so_nguyen_to(a))
print(phan_tu_la_SNT(a))

    