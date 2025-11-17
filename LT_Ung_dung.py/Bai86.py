print('Chào mừng bạn đến với nhà hàng Thanh Sơn')
print('Mời bạn nhập số lượng từng món ăn: ')
print()
sl_ga = int(input("Gà rán: "))
sl_ham = int(input("Hamburger: "))
sl_coca = int(input("Cocacola: "))
print()
def khoantrong(s):
    while len(s)<20:
        s += " "
    return s
print('Hóa đơn:')
print(khoantrong('Gà rán') + '30.000đ x' + str(sl_ga))
print(khoantrong('Hamburger') + '25.000đ x' + str(sl_ham))
print(khoantrong('Cocacola') + '10.000đ x' + str(sl_coca))
print()
print('Tổng:')

def phancachngan(a):
    a = str(a)
    i = len(a)-3
    while i>0:
        a = a[:i] + "." + a[i:]
        i -= 3
    return a
print(khoantrong('Gà rán') + phancachngan(30000*sl_ga) +'đ')
print(khoantrong('Hamburger') + phancachngan(25000*sl_ham) +'đ')
print(khoantrong('Cocacola') + phancachngan(10000*sl_coca) +'đ')
tong = 30000*sl_ga + 25000*sl_ham + 10000*sl_coca
print(khoantrong('Tổng trước thuế') + phancachngan(tong)+ 'đ')
print(khoantrong('Thuế (5%)') + phancachngan(int(tong*0.05)) + 'đ')
print(khoantrong('Tổng sau thuế') + phancachngan(int(tong*1.05)) + 'đ')







