def tim_vi_tri_phan_tu(lst, k):
    for i in range(len(lst)):
        if lst[i] == k:
            return i
    return -1

# Ví dụ sử dụng hàm:
lst = (input('Nhập list:').split('.'))
lst = [int(x) for x in lst]
k = int(input('Nhập số nguyên dương k: '))
vi_tri = tim_vi_tri_phan_tu(lst, k)
if vi_tri != -1:
    print(f'Phần tử đầu tiên có giá trị {k} nằm ở vị trí: {vi_tri}')
else:
    print(f'Không tìm thấy phần tử có giá trị {k} trong danh sách')
