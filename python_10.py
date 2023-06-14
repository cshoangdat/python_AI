#functions

def func():
    print("dat dz")
    def func1():
        print("hello")
    func1()
func()

def functions(x,y, z = None):
    print(x,y,z)
    return x+z, x*y

#functions(6,7)
#print(functions(3,4)[0]) #tra ve 1 tuples

res1 , res2 = functions(5,6, 9.2)
print(res1,res2)
