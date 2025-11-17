#Nhập vào số nguyên dương a, kiểm tra xem a có phải là số nguyên tố hay không
a = int(input("Nhập a: "))
if a > 1:
    dem=0
    #Đếm ước
    for i in range (1, a+1):
        if a % i == 0:
            dem += 1
    #Đếm xong kiểm tra nếu =2 thì là SNT và ngược lại
    if dem == 2:
        print(a,"Là số nguyên tố")
    else: 
        print(a, "Không là số nguyên tố!")
else:
    print(a, "Không là số nguyên tố!")

