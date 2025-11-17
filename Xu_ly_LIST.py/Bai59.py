L = input("Nhập list: ")
K = L.split(".")
K = list(map(int,K))
tong = 0 
for i in K:
    tong += i
print(type(K))
trung_binh = tong / len(K)
print(trung_binh)