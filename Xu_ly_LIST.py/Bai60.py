#hãy kiểm tra xem L có được sắp xếp từ bé đến lớn hay không
L = input("Nhập L: ")
L = L.split(".")
for i in range(len(L)-1):
    if L[i] > L[i+1]:
        print('L không được sắp xếp từ bé đến lớn')
        break
else:
    print('L được sắp xếp từ bé đến lớn')

    