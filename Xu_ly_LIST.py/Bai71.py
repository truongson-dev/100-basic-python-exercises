L = input('Nhập L: ').split(',')
max = None
vi_tri = None
for i in range (len(L)):
    x = L[i].count(' ') + 1
    if max == None or max < x:
        max = x
        vi_tri = i 
print(vi_tri)