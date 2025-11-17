L = input('Nhập L: ').split(',')
chuoi = None
vi_tri = None   
for i in L:
    kq = -1
    for j in range(len(i)):
        if i[j].isupper():
            kq = j
    if chuoi == None or vi_tri < kq:
        chuoi = i
        vi_tri = kq
print(chuoi)