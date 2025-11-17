soluong=0
n = int(input("Nhập vào số nguyên dương n: "))
while n>0:
    a=n%10
    soluong+=1
    n=n//10
print("Số lượng chữ số của số đó là",soluong)
