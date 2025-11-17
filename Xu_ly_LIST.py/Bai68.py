L = list(map(int,input("Nhập L: ").split('.')))
vt_max, vt_min=0,0
for i in range(len(L)):
    if vt_max == 0 or L[vt_max] < L[i]:
        vt_max=i
    if vt_min == 0 or L[vt_min] > L[i]:
        vt_min=i
L[vt_min],L[vt_max]=L[vt_max],L[vt_min]
print(L) 