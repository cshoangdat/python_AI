#String Formatting
#%,.format(), f-string

my_string = "Dat ne"
age = 20
money = 12.2292929929292
hello = "Xin chao %s %d co %0.2f" %(my_string,age,money)
hihi = "Xin chao {}, {} co {:.2f}".format(my_string,age,money)
hihihi = f"Xin chao {my_string}, {age} co {money:.2f}"
print(hello)
print(hihi)
print(hihihi)