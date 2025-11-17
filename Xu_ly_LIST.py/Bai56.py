#Tìm và in ra giá trị dương đầu tiên của list
#Nếu không có giá trị dương, ta in ra -1
L = input("Nhập vào list số nguyên: ")
K = L.split(".")
K = [int(i) for i in K]
so_duong = -1
for L in K:
    if L > 0:
        so_duong = L
        break
print("Giá trị dương đầu tiên:", so_duong)
