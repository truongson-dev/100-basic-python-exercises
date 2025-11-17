chuoi = input("Nhập chuỗi: ")
tong = 0
for i in chuoi:
    if i.isdigit():
        tong += int(i)

print('Tổng các số trong chuỗi là',tong)