#Ham lambda(Hàm ẩn danh) (Đơn giản hóa function)
#lambda arguments: expression

test_lambda = lambda x: x+48
print(test_lambda(69))

list_sample = [-1, 1, -5,5, -6,6, -7,7, 0 ,2 , 3, 4]
print(sorted(list_sample, key = lambda x: abs(x)))

list_coor = [(0,4),(-5,6),(1,5)]
print(sorted(list_coor, key = lambda x: x[1]))