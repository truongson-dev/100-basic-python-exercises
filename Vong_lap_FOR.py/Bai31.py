#Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
for i in range (1, a+1):
    if a % i == 0 and b % i == 0:
        print(i)
     