dic={"user1":"123456",
     "user2":"123456",
     "user3":"123456",
     "user4":"123456",
     "Sơn":"Son@2006",
     "Trương Thanh Sơn":"123456",
     "user7":"123456",
     "user8":"123456",
     "user9":"123456",
     "user10":"123456",
     }
user = input("Nhập tên: ")
password = input("Nhập mật khẩu: ")
if user not in dic:
    print('Tên không hợp lệ!')
elif dic[user]!=password:
    print("Mật khẩu sai!")
else:
    print("Đăng nhập thành công")