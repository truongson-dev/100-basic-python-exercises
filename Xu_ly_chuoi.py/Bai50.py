chuoi = input('Nhập mật khẩu: ')
dodai = len(chuoi)>6
dacbiet = thuong = hoa = so = False
for i in chuoi:
    if i.isnumeric():
        so = True
    elif i.isupper():
        hoa = True
    elif i.islower():
        thuong = True
    else:
        dacbiet = True
if dacbiet and thuong and hoa and so:
    print('Mật khẩu mạnh')
else:
    print('Mật khẩu yếu')