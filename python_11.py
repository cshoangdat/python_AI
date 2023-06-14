def func(x,y,z = "test"):
    print(x,y,z)

func (1,3, "dat")
#z la tham so mac dinh
#x y la tham so bat buoc
def func(x,y,z = "test"):
    pass #van cho phep ham khi chua co gi

func (1,2,3)

def func(x,y,z):
    print(x,y,z)

#positional arguments
func (1,6,9)
#keyword arguments
func (y = 8,z = 10, x = "hello")

#*args: co the truyen bat ki bien positional arguments
def func(x,y, *args):
    print(x,y)
    print(args)
    for x in args:
        print (x)

func (1,2,     88,"Dat", True, 9.0)

#*args: co the truyen bat ki bien keyword arguments
def func(x,y, **kargs):
    print(x,y)
    print(kargs)
    for i in kargs.items():
        print (i)

func (1,2,      a = 10, z = "hello")