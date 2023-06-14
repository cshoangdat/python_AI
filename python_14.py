#list comprehension: Giúp lấy ra 1 list phần tử theo mong muốn
#new list[<action> for <item> in <interator> if <some condition>]
hello = "hello world"
print([char for char in hello])
print([number for number in range(0,10) if (number % 2 == 1)])
list_price = [100,120,200,300]
VAT = 0.08
def price_product(price):
    return price + price*VAT
print([price_product(price) for price in list_price])