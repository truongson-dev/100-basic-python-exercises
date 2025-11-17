n=int(input('Nhập n:'))
sochan=0
sole=0
while n>0:
    a=n%10
    n=n//10
    if a % 2 == 0:
        sochan+=1
    else:
        sole+=1
print(sochan,sole)