#Hãy tìm và in ra giá trị âm lớn nhất trong L,
#Nếu L không có giá trị âm thì ta in 0
L = input("Nhập vào một list: ")
K = L.split(".")
K = (int(i) for i in K)
So_am_lon_nhat = 0
for L in K:
    if L < 0:
        if So_am_lon_nhat == 0 or L > So_am_lon_nhat:
            So_am_lon_nhat = L
print("Giá trị âm lớn nhất trong L =",So_am_lon_nhat)