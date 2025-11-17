n = int(input("Nhập vào n: "))
n1=n #gán n vào n1 để in ra mới đúng số đó, vì n sẽ bị thay đổi
while n % 2 == 0: #nếu số đó còn chia được cho 2
    n = n/2 #thì cứ đem đi chia
if n == 1: #Khi nào =1 là đúng
    print(n1, "Là số có dạng 2^k")
else:
    print(n1, "Không là số có dạng 2^k")
