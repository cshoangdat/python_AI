def nhap():
    a = int(input("A:"))
    while(a<0):
        print("Nhap lai gia tri a: ")
        a = int(input("A:"))

    b = int(input("B:"))
    while(b<0):
        print("Nhap gia tri b: ")
        b = int(input("B:"))
    return a,b

a,b = nhap()
while(a>b):
    print("Nhap lai gia tri a,b: ")
    a,b = nhap()

for i in range(a,b+1,1):
    count = 0
    for j in range(1,i+1):
        if(i%j == 0): 
            count += 1
    if(count == 2): 
        print(i,"la so nguyen to")

     