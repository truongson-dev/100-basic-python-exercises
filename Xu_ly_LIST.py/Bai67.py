l = list(map(int, input('Nhập chuỗi: ').split()))
chan = []
so_khong=[]
le=[]
for num in l:
    if num == 0:
        so_khong.append(num)
    elif num % 2 == 0:
        chan.append(num)
    else:
        le.append(num)
ket_qua=chan+so_khong+le
print('Danh sách đã được sắp xếp là',ket_qua)
