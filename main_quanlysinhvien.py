from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (True):
    print("\nCHUONG TRINH QUAN LY SINH VIEN Python")
    print("*************************MENU**************************")
    print("**  1. Them sinh vien.                               **")
    print("**  2. Cap nhat thong tin sinh vien boi ID.          **")
    print("**  3. Xoa sinh vien boi ID.                         **")
    print("**  4. Tim kiem sinh vien theo ten.                  **")
    print("**  5. Sap xep sinh vien theo diem trung binh (GPA). **")
    print("**  6. Sap xep sinh vien theo ten.                   **")
    print("**  7. Sap xep sinh vien theo ID.                    **")
    print("**  8. Hien thi danh sach sinh vien.                 **")
    print("**  0. Thoat                                         **")
    print("*******************************************************")

    key = int(input("Nhap tuy chon: "))
    if(key == 1):
        print("\n1. Them sinh vien.")
        qlsv.add_sinhvien()
        print("\nThem sinh vien thanh cong")
    elif(key == 2):
        if(qlsv.count_sinhvien()>0):
            print("\n2. Cap nhat thong tin sinh vien.")
            id = int(input("\nNhap ID sinh vien: "))
            qlsv.update_sinhvien(id)
        else:
            print("\nDanh sach sinh vien trong")
    elif(key == 3):
        if(qlsv.count_sinhvien()>0):
            print("\n3. Xoa sinh vien.")
            id = int(input("\nNhap ID sinh vien: "))
            if(qlsv.remove_sinhvien(id)):
                print(f"\nsinh vien voi id: {id} da bi xoa")
            else:
                print(f"\nsinh vien voi id: {id} khong ton tai")
        else:
            print("Danh sach sinh vien trong")
    elif(key == 4):
        if(qlsv.count_sinhvien()>0):
            print("\n4. Tim kiem sinh vien theo ten.")
            name = input("Nhap ten sinh vien: ")
            search_result = qlsv.finding_name(name)
            qlsv.display_sinhvien_list(search_result)
        else:
            print("Danh sach sinh vien trong")
    elif(key == 5):
        if(qlsv.count_sinhvien()>0):
            print("\n5. Sap xep sinh vien theo diem trung binh(GPA)")
            qlsv.sort_by_gpa()
            qlsv.display_sinhvien_list(qlsv.get_list_sinhvien())
        else:
            print("Danh sach sinh vien trong")   
    elif(key == 6):
        if(qlsv.count_sinhvien()>0):
            print("\n6. Sap xep sinh vien theo ten")
            qlsv.sort_by_name()
            qlsv.display_sinhvien_list(qlsv.get_list_sinhvien())
        else:
            print("Danh sach sinh vien trong")     
    elif(key == 7):
        if(qlsv.count_sinhvien()>0):
            print("\n7. Sap xep sinh vien theo ID")
            qlsv.sort_by_ID()
            qlsv.display_sinhvien_list(qlsv.get_list_sinhvien())
        else:
            print("Danh sach sinh vien trong")
    elif(key == 8):
        if(qlsv.count_sinhvien()>0):
            print("\n8. Hien thi danh sach sinh vien")
            qlsv.display_sinhvien_list(qlsv.get_list_sinhvien()) 
        else:
            print("Danh sach sinh vien trong")     
    elif (key == 0):
        print("\nBan da chon thoat chuong trinh!")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")               
    