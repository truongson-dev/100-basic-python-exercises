def tim_key_dai_nhat(d):
    kq = None
    for key in d:
        if kq == None:
            kq = key
        elif len(key) > len(kq):
            kq = key
    return kq

n = int(input("Nhập số lượng phần tử: "))
d = {}
for i in range(n):
    key = input("Nhập key: ")
    value = input(f"Nhập giá trị cho {key}: ")
    d[key] = value

print("Key có độ dài lớn nhất là:", tim_key_dai_nhat(d))
