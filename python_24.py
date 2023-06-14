#theard: xu ly song song:
import threading
import time

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

arr = [1,2,3,4,5,6,7,8,9]
t = time.time()
thread1 = threading.Thread(target=square, args=(arr,))
thread2 = threading.Thread(target=cube, args=(arr,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Done in: ", time.time()-t)