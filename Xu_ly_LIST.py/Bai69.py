L = input('nhập L: ')
L = L.split(',')
so_nho_nhat = None
chuoi_lon_nhat = None
for i in range(len(L)):
    #Nếu gặp số thì chuyển thành số nguyên
    if L[i].isnumeric():
        L[i] = int(L[i])
        if so_nho_nhat == None or so_nho_nhat > L[i]:
            so_nho_nhat = L[i]
    else:
        if chuoi_lon_nhat == None or chuoi_lon_nhat < L[i]:
            chuoi_lon_nhat = L[i]
print("Chuỗi có độ dài lớn nhất:", chuoi_lon_nhat)
print("Số nguyên có giá trị nhỏ nhất:", so_nho_nhat)
