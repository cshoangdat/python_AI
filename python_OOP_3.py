#static method và class method

class Car():
    tax = 1.5 #De goi bien su dung Car.tax
    car_number = 0
    def __init__(this,brand,model,founded_year,price):
        this.brand = brand
        this.model = model
        this.founded_year =founded_year
        this.price = price
        # this.car_number +=1
        Car.car_number +=1
    #regular method
    def Brand(this):
        return this.brand
    def GetValue(this):
        return (this.price * this.tax)
    @classmethod
    def set_tax(cls):
        cls.tax = 1.2
    
    @classmethod
    def from_string(cls, car_string):
        brand,model,founded_year, price = car_string.split('-')
        founded_year = int(founded_year)
        price = int(price)
        return cls(brand,model,founded_year, price)

    @staticmethod
    def check_price(price):
        if(price <=1000): return "This car is cheap"
        else : return "This car is expensive"
    
car_temp = "Toyota-Camry-1969-800"
car_1 = Car("VinFast", "LuxA", 2017, 1000)
car_2 = Car("BMW","i320",1916,700)
car_3 = Car.from_string(car_temp)

car_1.set_tax()
print(Car.tax)
print(car_2.GetValue())
print(car_3.brand, car_3.model, car_3.founded_year, car_3.price)
print(car_1.check_price(car_1.price))
    