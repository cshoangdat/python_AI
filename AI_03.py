import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
print("load data form MNIST")
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# print(x_train.shape) #x train da co do dai mang
# print(y_train[0:30]) #y train chua co do dai mang de lay gia tri data 
dig = np.array([1,3,5,7,9,11,13,15,17,19]);#lay gia tri tu 0 toi 9
x = x_train[dig,:,:]
print(x.shape)
y = np.eye(10)
print(y)
plt.subplot(121)
plt.imshow(x[0])
plt.subplot(122)
plt.imshow(x[1])
plt.show()
x = np.reshape(x,(10,784))/255 #chuan hoa kich thuoc du lieu 10 hang 784 cot
print(x.shape)

def sigmoid(x):
    return 1./(1. + np.exp(-x))
#khoi tao trong so:
w = np.random.uniform(-0.1,0.1,(10,784)) #tạo mảng 2 chiều có kích thước 10x784 với giá trị ngẫu nhiên từ -0.1 đến 0.1

o = sigmoid(np.matmul(x,w.transpose()))
print(o[:,0]) #in ra gia tri cot dau tien (neuron dau tien cho 10 mau)
plt.figure()
plt.bar([i for i,_ in enumerate(o)],o[:,0])
plt.show()

#training:
n = 0.05
for i in range(20):
    o = sigmoid(np.matmul(x,w.transpose()))
    loss = np.power(o-y, 2)
    d = (y - o)*o*(1-o)
    dw = np.transpose(d)@x
    w = w + n*dw
    print(loss)

o = sigmoid(np.matmul(x,w.transpose()))
print(o[:,0])
fig = plt.figure()
plt.bar([i for i, _ in enumerate(o)],o[:,0])
plt.show()