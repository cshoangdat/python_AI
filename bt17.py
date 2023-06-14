chuoi = [x for x in input("nhap chuoi").split(' ')]
result = sorted(list(set(chuoi)),key = lambda x: x[0])
print(result)