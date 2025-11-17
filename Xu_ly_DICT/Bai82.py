# def tim_key_lon_nhat(d):
#     kq = None
#     for i in d:
#         if kq == None or d[kq] < d[i]:
#             kq = i
#     return kq

# d = {'a': 10, 'b': 20, 'c': 30}
# print("Key có giá trị lớn nhất là:", tim_key_lon_nhat(d))

def tim_key_lon_nhat(d):
    kq = None
    for i in d:
        if kq == None:
            kq = i
        elif d[kq] < d[i]:
            kq = i
    return kq

n = int(input("Nhập số lượng phần tử: "))
d = {}
for i in range(n):
    key = input("Nhập key: ")
    value = int(input(f"Nhập giá trị cho {key}: "))
    d[key] = value

print("Key có giá trị lớn nhất là:", tim_key_lon_nhat(d))
