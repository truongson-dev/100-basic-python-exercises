#Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b
a = int(input('Nhập vào a:'))
b = int(input('Nhập vào b:'))
UCLN = 1 
for i in range (1,a+1):
    if i > b:
        break
    if a % i == 0 and b % i == 0:
        UCLN = i
print(UCLN)
