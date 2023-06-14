import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
print('load data from MNIST')
mnist = tf.keras.datasets.mnist
(x_train,y_train), (x_test,y_test) = mnist.load_data()
dig = np.array([1,3,5,7,9,11,13,15,17,19]) # get the digit 0 - 9
x = x_train[dig,:,:]
y = np.eye(10,10)
plt.subplot(121)
plt.imshow(x[0])
plt.subplot(122)
plt.imshow(x[1])
x = np.reshape(x,(-1,784))/255
def sigmoid(x):
  return 1./(1.+np.exp(-x))
W = np.random.uniform(-0.1,0.1,(10,784))
o = sigmoid(np.matmul(x,W.transpose())) # matrix multiplication
print('output of first neuron with 10 digits ', o[:,0])
fig = plt.figure()
plt.bar([i for i, _ in enumerate(o)],o[:,0])
plt.show()

#training process
n = 0.05
num_epoch = 10
for epoch in range(num_epoch):
 o = sigmoid(np.matmul(x,W.transpose()))
 loss =np.power(o-y,2).mean() 
 #calculate update for all wegihts in matrix
 dW =np.transpose((y-o)*o*(1-o))@x 
 #update
 W=W+n*dW
 print(loss)
o = sigmoid(np.matmul(x,W.transpose()))
print('output of the first neuron with 10 input digits ', o[:,0])
fig = plt.figure()
plt.bar([i for i, _ in enumerate(o)],o[:,0])
plt.show()