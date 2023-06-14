kitu = [x for x in input("Nhap chuoi: ").split(',')]
result = sorted(kitu, key=lambda x:x[0])
print(result)