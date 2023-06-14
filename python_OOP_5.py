class Employee:
    co_salary = 1.04
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
    def __repr__(self): #developer kiem tra dung k
        return f"Employee {self.first}, {self.last}, {self.pay}"
    def __str__(self): #in ra cho nguoi dung xem
        return f"{self.fullname()} - {self.email}"
    def __add__(self, other):  #Cong 2 doi tuong object
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())
emp1 = Employee("Hoang", "Dat", 1000)
emp2 = Employee("Dat", "Hoang Pro",5000)
print(emp1.__len__())
print(len(emp1))
print (emp1+emp2) 
print(str(emp1))
print(repr(emp1))   