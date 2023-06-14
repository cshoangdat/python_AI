x = input("X: ")
s = input("S: ")

if(len(s) == len(x)):
    a = ''
    for i in x[::-1]:
        a += i
    if(a == s):
        print("X va S doi xung")
    else: print("X va S khong doi xung")
else:
    print("X va S khong doi xung")