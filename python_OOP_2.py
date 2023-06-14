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
    def Brand(this):
        return this.brand
    def GetValue(this):
        return (this.price * this.tax)
# Car.tax = 2  #bien variable class co the de o ngoai
print(Car.car_number)
car_1 = Car("VinFast", "LuxA", 2017, 1000)
car_2 = Car("BMW","i320",1916,700)
print(Car.car_number)

car_2.tax = 2 #thay doi variable cua instance

# print(car_1.GetValue())
# print(car_2.GetValue())
# print(Car.__dict__)