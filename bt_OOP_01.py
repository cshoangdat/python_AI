class SoHoc:
    number1 = 0
    number2 = 0
    # def __init__(self,num1,num2):
    #     self.number1 = num1
    #     self.number2 = num2
    def input_info(self):
        self.number1 = int(input("Nhap so thu nhat: "))
        self.number2 = int(input("Nhap so thu hai: "))
    def print_info(self):
        print(f"So thu nhat: {self.number1}")
        print(f"Nhap so thu hai: {self.number2}")
    def addition(self):
        return self.number1 + self.number2
    def subtract(self):
        return self.number1 - self.number2
    def multi(self):
        return self.number1 * self.number2
    def division(self):
        return self.number1 / self.number2

so = SoHoc()
so.input_info()
so.print_info()
print(f"Tong: {so.addition()}")
print(f"Hieu: {so.subtract()}")
print(f"Tich: {so.multi()}")
print(f"Thuong: {so.division()}")

        