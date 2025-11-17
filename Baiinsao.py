h = int(input("Nhập chiều cao h: "))
space_ngoai = h-1
space_trong = 1 
for i in range (h):
    if i == 0:
        print(" " * space_ngoai + "*")
    elif i < h - 1:
        space_ngoai -= 1
        print(" " * space_ngoai + "*" + " " * space_trong + "*")
        space_trong += 2
    else:
        print("*" * (h*2 - 1)) 