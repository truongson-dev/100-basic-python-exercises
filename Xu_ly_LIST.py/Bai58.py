# #Cách1
# L = input('Nhập L: ')
# L = L.split(",")
# x = int(input("Nhập x: "))
# kq=0
# for i in L:
#     if kq == 0 or abs(kq-x)<abs(int(i)-x):
#         kq=int(i)
# print("Giá trị xa x nhất là",kq)

#Cách2
L=input("nhập vào list mà bạn muốn :")
K = L.split(".")
K = (int(i) for i in K)
x=int(input("nhập vào giá trị x :"))
vi_tri=0
khoang_cach=0
for i in K:
    a=int(i)
    h=abs(x-a)
    if h > khoang_cach:
        khoang_cach=h
        vi_tri=i
print(f"số {vi_tri} có vị trí xa nhất với {x} với khoảng cách {khoang_cach}")