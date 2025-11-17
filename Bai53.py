L = input('Nhập vào list số nguyên: ')
L = L.split(',')
max = 0
for i in L:
    if max < int(i):
        max += i
        print(max)
