from Sinhvien import Sinhvien

class QuanLySinhVien():
    list_sinhvien = []
    #ID la ma sinh vien tu dong tang khi them vao:
    def generate_id(self):
        max_id = 1
        if(self.count_sinhvien() != 0):
            self.list_sinhvien[0].id = max_id
            for sv in self.list_sinhvien:
                if (max_id < sv.id):
                    sv.id = max_id
                max_id = max_id + 1
        return max_id
    
    def count_sinhvien(self):
        return  self.list_sinhvien.__len__()
    
    #diem trung binh la gia tri trung binh 3 mon:
    def gpa_score(self,sv:Sinhvien):
        result =  (sv.math_score + sv.chemist_score + sv.physic_score)/3
        result = round(result,2)
        sv.gpa = result
        return result
    
    def review(self,sv:Sinhvien):
        if(self.gpa_score(sv) >= 8 ):
            sv.review = "Gioi"
        elif(self.gpa_score(sv) >= 6.5 and self.gpa_score(sv) <8):
            sv.review = "Kha"
        elif(self.gpa_score(sv) >= 5 and self.gpa_score(sv) <6.5):
            sv.review = "Trung Binh"
        else:
            sv.review = "Yeu"
            
    def add_sinhvien(self):
        id = self.generate_id()
        name = input("Nhap ho va ten sinh vien: ")
        age = int(input("Nhap tuoi cua sinh vien: "))
        sex = input("Nhap gioi tinh: ")
        math_score = float(input("Nhap diem toan: "))
        physic_score = float(input("Nhap diem ly: "))
        chemist_score = float(input("Nhap diem hoa: "))
        sv = Sinhvien(id,name, age, sex, math_score, physic_score, chemist_score)
        self.gpa_score(sv)
        self.review(sv)
        self.list_sinhvien.append(sv)
        
    def finding_id(self, id):
        result = None
        if(self.count_sinhvien() > 0):
            for sv in self.list_sinhvien:
                if (sv.id == id):
                    result = sv
        return result
    
    def update_sinhvien(self,id):
        sv:Sinhvien = self.finding_id(id)
        if (sv != None):
            name = input("Nhap ho va ten sinh vien: ")
            age = int(input("Nhap tuoi cua sinh vien: "))
            sex = input("Nhap gioi tinh: ")
            math_score = float(input("Nhap diem toan: "))
            physic_score = float(input("Nhap diem ly: "))
            chemist_score = float(input("Nhap diem hoa: "))  

            sv.name = name
            sv.age = age
            sv.sex = sex
            sv.math_score = math_score
            sv.physic_score = physic_score
            sv.chemist_score = chemist_score
            self.gpa_score(sv)
            self.review(sv)
        else:
            print(f"Sinh vien co ma ID: {id} khong ton tai")
            
    def remove_sinhvien(self,id):
        sv:Sinhvien = self.finding_id(id)
        is_delete = False
        if(sv != None):
            self.list_sinhvien.remove(sv)
            is_delete = True
        else:
            print(f"Sinh vien co ma ID: {id} khong ton tai")
        return is_delete
    #tim kiem theo ten:
    def finding_name(self,name):
        listSV = []
        if(self.count_sinhvien() > 0):
            for sv in self.list_sinhvien:
                if(name.upper() in sv.name.upper()):
                    listSV.append(sv)
        return listSV
    
    def sort_by_gpa(self):
        if(self.count_sinhvien() >0):
            self.list_sinhvien.sort(key = lambda x: x.gpa)
            
    def sort_by_name(self):
        if(self.count_sinhvien()>0):
            self.list_sinhvien.sort(key = lambda x: x.name)
            
    def sort_by_ID(self):
        if(self.count_sinhvien()>0):
            self.list_sinhvien.sort(key = lambda x: x.id)
    def display_sinhvien_list(self,listSV):
        
        # hien thi tieu de cot
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Age", "Toan", "Ly", "Hoa", "Diem TB", "Hoc Luc"))
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                      .format(sv.id, sv.name, sv.sex, sv.age, sv.math_score, sv.physic_score, sv.chemist_score, sv.gpa, sv.review))
        print("\n")
        
    def get_list_sinhvien(self):
        return self.list_sinhvien
    
    
            
    
        
            
        
    