import math

arrA = []
arrB = []
i = 0
j = 0
while(i<10):
    a = int(input(f"Nhap gia tri thu {i} cua mang A: "))
    i+=1
    arrA.append(a)

while(j<10):
    b = int(input(f"Nhap gia tri thu {j} cua mang B: "))
    j+=1
    arrB.append(b)

def euclid(n,m):
    result = 0
    for i in range(0,10):
        value = (n[i] - m[i])**2
        value +=value
        result = math.sqrt(value)
    return result

print(euclid(arrA,arrB))
