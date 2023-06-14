import numpy as np
n = np.random.randint(100,size=20)
print("mang ban dau: ",n)
list1 = [-1 for x in n if(x%2 == 1)] + [x for x in n if(x%2 !=1)]
print("mang sau khi thuc hien: ",list1)