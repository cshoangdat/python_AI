#Ham Enumerate
fruits = ["banana", "orange", "lemon", "watermelon", "apple"]

for index, fruit in enumerate(fruits):
    print(f"Number of {index} is {fruit}")

my_list = [1,3,5, 7, 9 ,12, 23,45]
print(list(reversed(my_list))) #khong thay doi my_list còn my_list.reverse() có thay đổi
print(my_list)
print(max(my_list))
print(min(my_list))
print(my_list[::-1])