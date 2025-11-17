#Chưa xong nhen
n = int(input('Nhập số lượng phần tử: '))
lst = []
for i in range(n):
    lst.append(int(input('Nhập số: ')))
dem=0
max=1
for num in lst:
    if num > max:
        dem += 1
        max = num
print(dem)