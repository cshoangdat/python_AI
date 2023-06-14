import numpy as np
import tensorflow as tf
from IPython.display import clear_output
import matplotlib.pyplot as plt

print("Load MNIST dataset")
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = np.reshape(x_train,(60000,784))/255.0
x_test = np.reshape(x_test,(10000,784))/255.0
y_train = np.matrix(np.eye(10)[y_train])
y_test = np.matrix(np.eye(10)[y_test])
print(x_train.shape, y_train.shape)

#Khởi tạo mạng neuron:
learningRate = 0.5
epoch = 100
numTrainSamples = 60000
numTestSamples = 10000
numInputs = 784
numHiddenUnits = 512
numClasses = 10

#Khởi tạo lớp ẩn:
Wh = np.matrix(np.random.uniform(-0.5,0.5,(numHiddenUnits,numInputs)))
bh = np.random.uniform(0,0.5,(1,numHiddenUnits))
dWh = np.zeros((numHiddenUnits,numInputs))
dbh = np.zeros((1,numHiddenUnits))

#Khởi tạo lớp ngõ ra:
Wo = np.matrix(np.random.uniform(-0.5,0.5,(numClasses,numHiddenUnits)))
bo = np.random.uniform(0,0.5,(1,numClasses))
dWo = np.zeros((numClasses,numHiddenUnits))
dbo = np.zeros((1,numClasses))

#Định nghĩa các hàm:

def sigmoid(x):
    return 1.0/(1+np.exp(-x))
def softmax(x):
    # return np.divide(np.matrix(np.exp(x)),np.mat(np.sum(np.exp(x),axis = 1)))
    return (np.exp(x))/(np.sum(np.exp(x),axis=1))
def forwardPass(x,Wh,bh,Wo,bo):
    zh = x@Wh.T + bh
    a = sigmoid(zh)
    z = a@Wo.T + bo
    o = softmax(z)
    return o
def accTest(label,prediction):
    outMaxArg = np.argmax(prediction,axis=1)
    lableMaxArg = np.argmax(label,axis=1)
    accuracy = np.mean(outMaxArg == lableMaxArg)
    return accuracy

#Test:
prediction = forwardPass(x_train,Wh,bh,Wo,bo)
acc = accTest(y_train,prediction)
print(acc)

#training batch gradient descent
# loss = []
# acc = []
# for ep in range(epoch):
#     x = x_train
#     y= y_train
#     zh = x@Wh.T + bh
#     a = sigmoid(zh)
#     z = a@Wo.T + bo
#     o = softmax(z)
#     loss.append(-np.sum(np.multiply(y,np.log10(o))))
#     d = o - y
#     dh = d@Wo
#     dhs = np.multiply(np.multiply(dh,a),(1-a))
#     dWo = np.matmul(np.transpose(d),a)
#     dbo = np.mean(d)
#     dWh = np.matmul(np.transpose(dhs),x)
#     dbh = np.mean(dhs)
#     Wo = Wo - learningRate*dWo/numTrainSamples
#     bo = bo - learningRate*dbo

# prediction = forwardPass(x_train,Wh,bh,Wo,bo)
# acc = accTest(y_train,prediction)
# print(acc)

#training mini batch size Gradient descent
loss = []
acc = []
batch_size = 200
stochastic_sample = np.arange(numTrainSamples)
for ep in range(epoch):
    np.random.shuffle(stochastic_sample)
    for ite in range(0,numTrainSamples,batch_size):
        batch_sample = stochastic_sample[ite : ite+batch_size]
        x = x_train[batch_sample,:]
        y = y_train[batch_sample,:]
        zh = x@Wh.T + bh
        a = sigmoid(zh)
        z = a@Wo.T + bo
        o = softmax(z)
        #tính hàm loss:
        loss.append(-np.sum(np.multiply(y,np.log10(o))))
        #tính hàm sai số ở ngõ ra:
        d = o - y
        #back propagation error:
        dh = d@Wo
        dhs = np.multiply(np.multiply(dh,a),(1-a))
        #update trọng số:
        dWo = np.matmul(np.transpose(d),a)
        dbo = np.mean(d)
        dWh = np.matmul(np.transpose(dhs),x)
        dbh = np.mean(dhs)
        Wo = Wo - 2*learningRate*dWo/batch_size
        bo = bo - learningRate*dbo
        Wh = Wh - 2*learningRate*dWh/batch_size
        bh = bh - learningRate*dbh
        #test accuracy with radom init weights:
    prediction = forwardPass(x_test,Wh,bh,Wo,bo)
    acc.append(accTest(y_test,prediction))
    print("epoch: ", ep)
    print("Accuracy: ", accTest(y_test,prediction))
