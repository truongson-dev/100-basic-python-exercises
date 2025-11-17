n = int(input("Nhập n: "))
f1=1
f2=0
f = f1 + f2
while f <=n:
    f1=f2
    f2=f
    f = f1 + f2
print(f2)
    