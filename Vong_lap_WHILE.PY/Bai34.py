#Nhập vào số nguyên dương a, 
#Nếu nhập số âm thì yêu cầu nhập lại cho đến khi người dùng nhập đúng số dương
#Nếu người dùng nhập đúng số dương thì in ra “Bạn nhập đúng quy tắc”
while True:
    a = int(input("Nhập vào số nguyên dương a: "))
    if a > 0:
        print("Bạn nhập đúng quy tắc")
        break
    else:
        print("Số bạn nhập không phải là số nguyên dương, vui lòng nhập lại.")
