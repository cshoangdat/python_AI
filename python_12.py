a =[] #mảng rỗng
#a = [x for x in range(0,5)] #mang co gia tri tong quat la x

#nhap gia tri cho mang tu ban phim:
# n = int(input("so phan tu cua mang: "))
# for i in range(n):
#     a.append(int(input("Phan tu thu %d: " %(i+1))))
# print(a)

#sap xep mang khong sd thu vien co san:
b = [8,1,3,4,2,6,8,5,9]
# for i in range(len(b)):
#     for j in range(i):
#         if(b[i]<b[j]):
#             temp = b[i]
#             b[i] = b[j]
#             b[j] = temp

#Su dung thu tuc co san:
# b.sort() #sap xep tang dan = b.sort(reverse=False)
# b.sort(reverse=True) #sap xep theo giam dan
# print(b)

#xuat tung phan tu cua mang:
for i in range(len(b)):
    print(b[i], " ", end = "")

print(b)#xuat tat ca phan tu cua mang

