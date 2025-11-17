n = int(input("Nhập vào số nguyên dương n: "))
sochan = sole = 0
while n > 0:
    a = n % 10
    n = n // 10 
    if a % 2 ==0: 
        sochan+=1
    else:
        sole+=1
print('Chữ số có',sochan,'số chẵn')
print('Chữ số có',sole,'số lẻ')
