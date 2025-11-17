#Viết hàm đưa vào 2 số nguyên, số nào lớn hơn thì in bảng cửu chương của số đó
def so_sanh(a,b):
    if a>b:
        for i in range (1,11):
            BCC=a*i
            print(a,"x",i ,"=",BCC)
    elif a<b:
        for i in range (1,11):
            BCC=b*i
            print(b,"x",i ,"=",BCC)
    else:
        print("Hai số bằng nhau, đây là bảng cửu chương của 2 số")
        for i in range (1,11):
            BCC=b*i
            print(b,"x",i ,"=",BCC)

a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
ket_qua=so_sanh(a,b)
print(ket_qua)