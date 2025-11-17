# Nhập vào một list số nguyên L, tìm và in ra giá trị lớn nhất trong L
L = input('Nhap L: ')
L = L.split('.')
max = 0
for i in L:
    if int(i) > max:
        max = int(i)
print("Số lớn nhất",max)