n = input("Nhập chuỗi: ")
a = n.find(",")
b = n.rfind(",")
so1 = int(n[:a])
so2 = int(n[a+1:b])
so3 = int(n[b+1:])
c = so1+so2+so3
print("Tổng của 3 số là", c) 