n = -1
while(n < 0):
    n = int(input("Nhap gia tri n: "))

d = dict()
for i in range(1,n+1):
    d[i] = i*i
print (d)
    