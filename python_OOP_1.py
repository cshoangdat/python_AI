class Car(): #co the thay self = this
    def __init__(self,xuatxu,namradoi):
        self.xuat_xu = xuatxu
        self.nam_ra_doi = namradoi
    def thuonghieu(self,x):
        return x
    def xuat_xu(self):
        return self.xuat_xu

# BMW = Car() #Instance: The hien cho lop car
# BMW.xuatxu = "Germany" #thuoc tinh cho instance
# BMW.namradoi = 1969

BMW = Car("VietNam",2018)
print(BMW.xuat_xu)
# print(type(BMW))
# print(BMW.xuatxu)
# print(BMW.thuonghieu("VietNam")