ds = [x for x in input("Nhap cac so nguyen: ").split(" ")]
value = []
for i in ds:
    arr = []
    while(int(i)>0):
        phan_du = int(i)%2
        i = int(i)//2
        arr.append(phan_du)
        arr.reverse()
    value.append(arr)
print (value)
        
    

        