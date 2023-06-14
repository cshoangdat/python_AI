#backslash \

temp = "I 'm Dat Hoang \"Pro Vip\"\
I live in VietNam"
print(temp)

#substring: Lay String tu dau toi dau =))
#mystring[start_index: end_index]

my_string = "Dat , Hoang"
print(my_string[:3]) #lay tu 0 toi 3
print(my_string[::-1])#dao nguoc chuoi
print(my_string[-1]) #lay gia tri tu phai qua trai

#Method su ly String: strip(), split(), upper(), lower(), capitalize()
#title
print(my_string.strip('t')) #loai bo cac ki tu khong mong muon nhap vao ()
print(my_string.split(',')) #tach cac ki tu neu muon tach tu , thi nhap (,)
print(my_string.upper())
print(my_string.lower())
print(my_string.capitalize())
print(my_string.title())
print(my_string.replace("Dat","Pro Dat"))
print(my_string.find("u"))