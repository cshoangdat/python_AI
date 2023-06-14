n = int(input("Nhap so phan tu cua mang: "))
arr = []
for i in range(n):
    arr.append(int(input("Phan tu thu %d cua mang:" %(i+1))))

#sap xep theo thu tu tang dan cach 1:
# arr.sort()
# print(f'Sap xep mang arr theo thu tu tang dan cach 1: {arr}')

#sap xep theo thu tu tang dan cach 2:
for i in range(n):
    for j in range(i):
        if(arr[i] < arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print(f'Sap xep mang arr theo thu tu tang dan cach 2: {arr}')