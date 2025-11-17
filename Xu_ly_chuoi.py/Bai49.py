# chuoi = input("Nhập chuỗi: ")
# a=""
# tong=0
# for i in chuoi:
#     if i.isnumeric():
#         a += i
#     else:
#         if a != "":
#             tong += int(a)
#         a = ""
# if a != "":
#     tong += int(a)
# print(a)

#Vòng While
chuoi = input("Nhap chuoi: ")
tong = 0
temp = ""
i = 0
while (i<len(chuoi)):
    if (chuoi[i].isnumeric()):
        temp += chuoi[i]
    else:
        if (temp != ""):
            tong += int(temp) 
            temp = ""
    i = i+ 1
if (temp != ""):
    tong += int(temp)
print(tong)