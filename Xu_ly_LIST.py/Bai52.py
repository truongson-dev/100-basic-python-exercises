a = input('Nhập chuỗi a: ')
b = input('Nhập chuỗi b: ')
vt_dau=0
vt_cuoi=len(b)
while vt_cuoi <= len(a):
    if a[vt_dau:vt_cuoi]==b:
        a = a[:vt_dau] + a[vt_cuoi:]
    else:     
        vt_dau += 1
        vt_cuoi += 1
print(a)
a =input("Nhập chuỗi: ")
b=input("Nhập chuỗi: ")
d=''
if b in a:
    c=a.split(b)
    for i in range(0,len(c)):
        d=d+c[i]
print(d)


