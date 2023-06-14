#map(func,obj): Transform object with function

list_temp = [7,8,9,12,15,21,42]
def sum(x):
    return x+2
print(list(map(sum,list_temp)))
print(list(map(lambda x: x*2,list_temp)))

#filter(func,obj): filter object which you want y het map =)))) dm =)))
print(list(filter(lambda x: x%2 == 1, list_temp)))
list1 = [x for x in list_temp if x%2 == 1]
print(list1)

#reduce(func,obj): return single value, function get 2 arguments
from functools import reduce
print(reduce(lambda x,y: x if(x<y) else y,list_temp))