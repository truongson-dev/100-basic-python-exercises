chuoi = input('Nhập chuỗi: ')
a = chuoi.find(' ')
tu_dau_tien = chuoi[:a]
print('Từ đầu tiên là: ', tu_dau_tien)

#từ cuối cùng
chuoi = input("nhập chuỗi: ")
a = chuoi.rfind(' ')
tu_cuoi_cung = chuoi[a:]
print('Từ cuối cùng là: ',tu_cuoi_cung)