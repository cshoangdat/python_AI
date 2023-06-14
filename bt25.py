import numpy as np #xu ly mang da chieu. ma tran
import pandas as pd 
import matplotlib.pyplot as plt #Ve bieu do

a= pd.Series(np.random.randint(10,size = 5))
print("A:",a)
b= pd.Series(np.random.randint(10,size = 5))
print ("B:", b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
plt.plot(a,b)
plt.xlabel("Series A")
plt.ylabel("Series B")
plt.show()