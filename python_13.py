#Lam viec voi tep trong python:
#Mo file:
    #Cu phap: ten bien file = open(ten file[,kieu truy cap][,trình đệm])
    
    #trong do:
    #kieu truy cap: 
    #r:Mo file chi de doc
    #r+ mở file để đọc và ghi
    #rb: Mở file chế độ đọc chỉ định dạng nhị phân, con trỏ tại bắt đầu của file
    #rb+: Mở file đọc và ghi dạng nhị phân
    #w: Tạo 1 file để ghi, Nếu file đã tồn tại sẽ bị ghi mới
    #w+:Tạo 1 file để đọc và ghi, Nếu file đã tồn tại sẽ bị ghi mới
    #wb:Tạo 1 file để ghi trong dạng nhị phân
    #wb+:Tạo 1 file để ghi và đọc trong dạng nhị phân
    #a: Mở file để ghi thêm vào cuối file,Nếu không tìm thấy file sẽ tạo mới 1 file để ghi mới
    #a+: Mở file để đọc và ghi thêm vào cuối file,Nếu không tìm thấy file sẽ tạo mới 1 file để ghi mới
    #ab: Mở file trong chế độ append dạng nhị phân. Con trỏ ở cuối file
    #ab+:Mở file trong chế độ append và đọc dạng nhị phân. Con trỏ ở cuối file
    
    #thuộc tính của file:
    #file.closed Trả về true nếu file đã đóng và ngược lại
    #file.mode Trả về chế độ truy cập của file đang được mở
    #file.name Trả về tên của file
    
    #vidu:
 
    
file = open("test.txt","r")
print ("Trang thai dong tep: ",file.closed)
print ("Kieu truy cap: ",file.mode)
print ("Ten tep: ",file.name)
# line = file.readline()
# print ("Dong dau tien la: ",line)
st = file.read()
print ("Noi dung cua tep la:", st)
file.close()
print ("Trang thai dong tep: ",file.closed)

    #Dong file:
    #cú pháp: Tên tệp.close
    
    #Doc File:
    #Phuong phap read: Phương thức này trả về 1 chuỗi có kích thước = size. Nếu không để size thì sẽ đọc toàn bộ nội dung file
    #Cú pháp: tên tệp.read([size]) (size là tham số tùy chọn sài hay không cũng đc)
    #Phuong pháp readline: Phương thức này cho phép đọc 1 dòng trong tệp và trả về chuỗi
    #Cú pháp: tên tệp.readline()
    
    #Ghi File: 
    #Cú pháp: Tên têp.write()
    #Phuong thức này cho phép ghi một chuỗi có nội dung là string vào vị trí của con trỏ trong tệp
    
    #Thay ten FIle:
    #Cú pháp: os.rename("<Tên tệp hiện tại>","<Tên tệp mới")
    
    #Xóa file:
    #Cú pháp: os.remove("Tên tệp")
    
    #Xác định vị trí con trỏ trong file:
    #tell(): cho biết vị trí hiện tại của con trỏ bên trong file.
    #seek(offset[,from]) thay đổi vị trí hiện tại bên trong file.
        #trong đó: 
        #offset là chỉ số byte để được di chuyển
        #from để xác định vị trí tham chiếu mà từ đó byte đc di chuyển
            #Nếu from là 0 thì sử dụng phần đầu file như vị trí tham chiếu
            #Nếu from là 2 thì sử dụng phần cuối file như là vị trí tham chiếu
    
    #VD2:
import os #để giao tiếp với hệ điều hành
# os.rename("tong.OUT","tong2so.txt")
os.remove("tong2so.txt")

#khong can close:
with open("test.txt","r") as file:
    print(file.read())
