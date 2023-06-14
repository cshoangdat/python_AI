#Tinh truu tuong: truu tuong ngoai doi thanh class


#Tinh Dong goi: public, private, protected
class Employee:
    co_salary = 1.04 #__co_salary -> private, _co_salary -> protected
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '-' + last +"@gmail.com"
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_co_salary(self):
        self.pay = int(self.pay*self.co_salary)
        return self.pay

#tinh Da hinh: Cung 1 phuong thuc no co the tra ve gia tri khac nhau