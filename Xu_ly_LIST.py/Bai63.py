# Có hai giá trị lân cận và giá trị tại vị trí đó bằng tích hai giá trị lân cận. 
# Nếu L không tồn tại giá trị như vậy thì in ra - 1
l = list(map(int,input('Nhập L: ').split('.')))
kq = -1
for i in range(1,len(l)-1):
    #có hai giá trị lân cận 
    if l[i+1] * l[i-1] == l[i]:
        kq = i
        break
print('Vị trí thõa yêu cầu là vị trí thứ',i)


