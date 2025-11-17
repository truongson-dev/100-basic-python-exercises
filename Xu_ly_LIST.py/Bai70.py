L = input('Nhập L: ').split('.')
if len(L) % 2 == 0:
    kq = True
    #Kiểm tra từng cặp có phải xen kẽ
    for i in range(0, len(L) - 1, 2):
        if (L[i].isalpha() and L[i+1].isdigit()):
            continue
        else:
            kq = False
            print('Không thể tạo list vì không xen kẽ')
            break
    if kq:
        K = []
        for i in range(0, len(L), 2):
            K.append(L[i] * int(L[i+1]))
        print('K=', K)
    else:
        print('Không thể tạo list')
else:
    print('Không thể tạo list vì số lẻ')
