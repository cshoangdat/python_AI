#Decorators(chuyen ham sang ham): Khong lap lai code khong sua ham co san
import time

def cal_time(func):
    def timer(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(func.__name__ + " took: " + str((end-start)*1000) + "ms")
        return result
    return timer
        
@cal_time
def square(numbers):
    result = []
    # start = time.time()
    for number in numbers:
        result.append(number*number)
    # end = time.time()
    # print("This func took: " + str((end-start)*1000) + "ms")
    return result

@cal_time
def cube(numbers):
    result = []
    # start = time.time()
    for number in numbers:
        result.append(number*number*number)
    # end = time.time()
    # print("This func took: " + str((end-start)*1000) + "ms")
    return result


arr = range(1,100000)
out_square = square(arr)
out_cube = cube(arr)