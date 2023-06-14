#process: Da tien trinh. Cac bien cua process doc lap voi nhau
import time
import multiprocessing
from multiprocessing import process

def square(numbers):
    print("Caculate square of numbers")
    for x in numbers:
        time.sleep(1)
        print("Square: ", x*x)

def cube(numbers):
    print("Caculate cube of numbers")
    for x in numbers:
        time.sleep(1)
        print("Cube: ", x*x*x)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    process1 = multiprocessing.Process(target = square,args = (arr,))
    process2 = multiprocessing.Process(target = cube,args = (arr,))

    process1.start()
    process2.start()
    
    process1.join()
    process2.join()
    print("Done Success")