def kiem_tra_dang_song(L):
#nếu list nhỏ hơn 3 phần tử thì không được
    if len(L) < 3:
        return False
    
    for i in range(1, len(L) - 1):
        if ((L[i] > L[i - 1] and L[i] > L[i + 1]) or (L[i] < L[i - 1] and L[i] < L[i + 1])):
            return True
    return False

L = list(map(int, input('Nhập list: ').split()))
print(kiem_tra_dang_song(L))
