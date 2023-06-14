value_input = [x for x in input("Nhap 20 phan tu nguyen: ").split(" ")]
arr = []
for i in value_input:
    if(int(i)%2 == 1): arr.append(i)

print(arr) 