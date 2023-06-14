import numpy as np
import tensorflow as tf

print("LOAD DATA FROM MNIST")
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = np.reshape(x_train,(60000,784))/255
x_test = np.reshape(x_test,(10000,784))/255
y_train = np.matrix(np.eye(10)[y_train])
y_test = np.matrix(np.eye(10)[y_test])
print(x_train.shape,y_train.shape)

print("INIT NEURAL NETWORK")
learningRate = 0.3
epoch = 50
numInputs = 784
numHiddenUnits = 512
numClasses = 10
numTrainSamples = 60000
numTestSamples = 10000

# hidden 1:
W1 = np.matrix(np.random.uniform(-0.5,0.5,(numHiddenUnits, numInputs)))
b1 = np.random.uniform(0,0.5,(1,numHiddenUnits))
dW1 = np.zeros((numHiddenUnits, numInputs))
db1 = np.zeros((1,numHiddenUnits))

# hidden 2:
W2 = np.matrix(np.random.uniform(-0.5,0.5,(numHiddenUnits,numHiddenUnits)))
b2 = np.random.uniform(0,0.5,(1,numHiddenUnits))
dW2 = np.zeros((numHiddenUnits, numHiddenUnits))
db2 = np.zeros((1,numHiddenUnits))

# Output:
Wo = np.matrix(np.random.uniform(-0.5,0.5,(numClasses,numHiddenUnits)))
bo = np.random.uniform(0,0.5,(1,numClasses))
dWo = np.zeros((numClasses,numHiddenUnits))
dbo = np.zeros((1,numClasses))

# define functions including sigmoid, testAcc, forwardPass:
def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax(x):
    return np.divide((np.matrix(np.exp(x))),np.mat((np.sum(np.exp(x),axis= 1))))

def forwardPass(x,W1,b1,W2,b2,Wo,bo, dropout):
    z1 = np.matmul(x,W1.T) + b1
    a1 = sigmoid(z1)
    z2 = np.matmul(a1,W2.T) + b2
    a2 = sigmoid(z2)
    zo = np.matmul(a2,dropout*Wo.T) + bo
    o = softmax(zo)
    return o

def accTest(label, prediction):
    labelMaxArg = np.argmax(label, axis=1)
    outMaxArg = np.argmax(prediction, axis = 1)
    accuracy = np.mean(labelMaxArg == outMaxArg)
    return accuracy

# Test random Weight:
prediction = forwardPass(x_test,W1,b1,W2,b2,Wo,bo, 0.5)
acc = accTest(y_test,prediction)
print(acc)

# Training su dung Mini Batch SGD:
loss = []
acc = []
batch_size = 200
stochastic_samples = np.arange(numTrainSamples)
dropout_prob = 0.5
for ep in range(epoch):
    np.random.shuffle(stochastic_samples)
    for i in range(0,numTrainSamples,batch_size):
        dropout = np.random.binomial(size = (batch_size,numHiddenUnits),n = 1, p = dropout_prob)
        batch_sample = stochastic_samples[i:i+batch_size]
        x = x_train[batch_sample,:]
        y = y_train[batch_sample,:]

        # forward pass with dropout
        z1 = np.matmul(x,W1.T) + b1
        a1 = sigmoid(z1)
        a1 = np.multiply(a1,dropout)
        z2 = np.matmul(a1,W2.T) + b2
        a2 = sigmoid(z2)
        a2 = np.multiply(a2,dropout)
        zo = np.matmul(a2,Wo.T) + bo
        o = softmax(zo)
        loss.append(-np.sum(np.multiply(y,np.log10(o))))

        # backward pass
        do = o - y
        dWo = np.matmul(np.transpose(do),a2)
        dbo = np.mean(do)
        Wo = Wo - learningRate*dWo/batch_size
        bo = bo - learningRate*dbo

        d2 = do@Wo
        d2s = np.multiply(np.multiply(d2,a2),(1-a2))
        d2s = np.multiply(d2s,dropout)
        dW2 = np.matmul(np.transpose(d2s),a1)
        db2 = np.mean(d2s)
        W2 = W2 - learningRate*dW2/batch_size
        b2 = b2 - learningRate*db2

        d1 = d2@W2
        d1s = np.multiply(np.multiply(d1,a1),(1-a1))
        d1s = np.multiply(d1s,dropout)
        dW1 = np.matmul(np.transpose(d1s),x)
        db1 = np.mean(d1s)
        W1 = W1 - learningRate*dW1/batch_size
        b1 = b1 - learningRate*db1
    loss[ep] = np.mean(loss)
    prediction = forwardPass(x_test,W1,b1,W2,b2,Wo,bo, 1.0)
    acc.append(accTest(y_test,prediction))
    print("epoch: ", ep)
    print("Lost: ", loss[ep])
    print("Accuracy: ", accTest(y_test,prediction))

