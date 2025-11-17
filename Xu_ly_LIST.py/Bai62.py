L = list(map(int,input('Nhập một list: ').split()))
cong_sai = L[1]-L[0]
a=0
if len(L) < 2:
    print(None)
else:    
    for i in range(1,len(L)):
        if L[int(i)] - L[int(i)-1] != cong_sai:
            print(None)
            a+=1
            break
if a==0:
    print('Công sai là =',cong_sai)

