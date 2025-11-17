n=int(input("nhập vào số n="))
sum = 0 
number = 0
print("các số nguyên tố :")
for i in range (2,n+1):
    for i in range (2,n):
        if i % n == 0 :
            break
        else:# vì sao khi đưa else vào khối lệnh ở trong lại khong nhận 2 là số nguyên tố
            print(i,end=" ")
            sum +=i
            number +=1

print ("\ntổng các số nguyên tố",sum)
print(number,"là số chữ số nguyên tố")