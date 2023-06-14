import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output
x = np.array([30,40,50,60])
y = np.array([500,600,600,750])
plt.plot(x,y,'o')

m = -2
b = 50

n = 0.0001
for rep in range(50):
  dm = 0
  db = 0

  for i in range(4):
    dm += 2*n*(m*x[i] + b - y[i])*x[i]
    dm += 2*n*(m*x[i] + b - y[i])

  m = m - dm/4
  b = b - db/4
  clear_output(wait = True)
  plt.plot(x,m*x+b)
  plt.plot(x,y,'o')
  plt.show()