ds = []
#Nhập danh sách
while True:
    n = int(input('Nhập số: '))
    if (n==-1):
        break
    else:
        ds.append(n)
#Tim min bang in ds
min = ds[0]
# for i in ds:
#         if min > i:
#             min = i 
#Tim min bằng i từ 1
for i in range (1,len(ds)):
     if min > ds[i]:
          min = ds[i]
print(min)
    
