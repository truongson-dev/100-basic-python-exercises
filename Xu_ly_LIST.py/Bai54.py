K=input("Nhập vào list mà bạn muốn:")
L=K.split(".")
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
if a < b < len(L):
    min=L[a]
    for i in L[a+1:b+1]:
        if min > i:
            min = i
    print(min)
else:
    print("Không hợp lệ a, b phải nhỏ hơn độ dài list")

