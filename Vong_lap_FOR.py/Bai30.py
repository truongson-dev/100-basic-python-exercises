#đếm số ước của a
a = int(input("Nhập a: "))
dem=0 #thêm biến đếm để in toàn bộ ước
for i in range (1, a+1):
    if a % i == 0:
        dem += 1
print(dem)
 