input_value = [x for x in input("Nhap gia tri nhi phan: ").split(",")]
sum = 0
d = dict()
for i in range(len(input_value)):
    length = len(input_value[i])
    sum = 0
    for j in range(len(input_value[i])):
        while (length >= 1):
            if(length == len(input_value[i])):
                gia_tri_tach = int(input_value[i]) // (10**(length-1))
            else:
                du = int(input_value[i]) % (10**(length))
                gia_tri_tach = du //(10**(length-1))
            if(gia_tri_tach == 1):
                sum += 2**(length-1)
            length -= 1
    key = input_value[i]
    d[key] = sum
print(d)