# Chưa xong
#  l = list(map(int,input('Nhập list: ').split('.')))
# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if (l[i]+l[j]) % 2 == 0:
#             print('Không phải là list chẵn lẻ')
#         break
# print ('list chẵn lẻ')


n = int(input('Nhập số lượng phần tử: '))
lst = []
for i in range(n):
    lst.append(int(input('Nhập số: ')))

is_chan_le = True
for i in range(len(lst)):   
    for j in range(i + 1, len(lst)):
        if (lst[i] + lst[j]) % 2 == 0:
            print('Không phải là list chẵn lẻ')
            is_chan_le = False
            break
    if not is_chan_le:
        break

if is_chan_le:
    print('Danh sách là list chẵn lẻ')

