# def gia_tri_lon_nhat(L,a):
#     for i in range(a):
#         for j in range(len(L)):
#             if L[j]!=None:
#                 if vt_max == None or L[vt_max]<L[i]:
#                     vt_max = j
#                 if i == a - 1:
#                     return(L[vt_max])
#                 else:
#                     L[vt_max]=None
#     print(gia_tri_lon_nhat)
# print(gia_tri_lon_nhat([7 8 9 2 3 1],3))
def gia_tri_lon_nhat(L, a):
    if a <= 0 or a > len(L):
        return None  
    n = len(L)
    for i in range(n):
        for j in range(0, n-i-1):
            if L[j] < L[j+1]:
                L[j], L[j+1] = L[j+1], L[j] 
    return L[a - 1]

L = [4, 2, 7, 7, 5, 9, 1]
a = 9 
result = gia_tri_lon_nhat(L, a)
print(f"Giá trị lớn thứ {a} trong danh sách là: {result}")
