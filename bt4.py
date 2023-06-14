a = int(input("A:"))
count = 1
while(a>9):
    a = a/10
    x = int(a)
    count +=1

print("Do dai cua a:", count, end="\n")
print("So dau tien cua a: ",x)