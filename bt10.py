def giaithua(n):
    result = 0
    if(n == 0 or n == 1): result = 1
    else: result = n*giaithua(n-1)
    return result

n = -1
while(n < 0):
    n = int(input("Nhap gia tri n: "))

print(f"gia thua cua {n} la {giaithua(n)}")

