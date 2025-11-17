n = int(input("Nhập vào số n: "))
print("Các số nguyên tố từ 1 đến", n, "là:", end=" ")
tong = 0
dem = 0
for num in range(2, n + 1):
    uoc = 0
    for i in range(2, num):
        if num % i == 0:
            uoc = uoc + 1
            break
    
    if uoc == 0:
        print(num, end=" ")
        tong = tong + num
        dem = dem + 1

print("\nTổng các số nguyên tố là:", tong)
print("Số lượng số nguyên tố là:", dem)