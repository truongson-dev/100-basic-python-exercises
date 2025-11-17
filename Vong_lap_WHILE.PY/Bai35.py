#Nhập n
#Cho S(k) = 1 + 2 + 3 + … + k
#Tìm k sao cho S(k) lớn nhất nhưng nhỏ hơn n
n = int(input("Nhập giá trị của n: "))
Sk = 0
S = 0
while S + Sk + 1 < n:
    Sk += 1
    S += Sk
print("Giá trị lớn nhất của Sk nhưng nhỏ hơn n là",Sk)
print("Tổng S(k) là: ",S)
