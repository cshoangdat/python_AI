#list
list_test = ["Thanh", 123456, True]
print(len(list_test))
#len() -> ktr do dai cua chuoi
print(len('Hello'))
list_test.append("Dat dep trai")
#list.append -> them phan tu trong list
print(list_test)
list_test.extend([85,6,4,False])
#list.extend -> them mang vao trong mang
print(list_test)
list_test.pop(1)
#list.pop() -> bo phan tu thu() cua mang
print(list_test)
print(list_test[0])
#list[] -> truy cap vao phan tu cua mang
list_test[1] = "DatPro"
print(list_test)
list_test = ["Thanh", 123456, True, [123,"pro", False, [2345,"Dat"]]]
print(list_test)
x = list_test[:]
#giu nguyen gia tri cua x thay vi list cu
list_test[0] = "hello"
print(x,list_test)

#tuples -> mang co dinh, k them bot, sua mang duoc
tuple_test = ("Thanh", 123456, True)