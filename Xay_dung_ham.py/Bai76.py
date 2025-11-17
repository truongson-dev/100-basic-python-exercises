def Gia_tri_lon_nhat(lst):
    max = 0
    for i in range(1,len(lst)):
        if int(lst[i]) > int(lst[max]):
            max=i
    return max
lst = (input('Nhập list: ').split('.'))
print(f'vị trí có giá trị lớn nhất trong list là: {Gia_tri_lon_nhat(lst)}')