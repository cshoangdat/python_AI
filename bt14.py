n = -1
m = -1
while(n < 0 or m < 0):
    if(n<0): n = int(input("Nhap gia tri n: "))
    if(m<0): m = int(input("Nhap gia tri m: "))

multilist =[[0 for j in range(m)] for i in range(n)] #tao mang 2 chieu

for i in range(n):
    for j in range(m):
        multilist[i][j] =i*j

print(multilist)