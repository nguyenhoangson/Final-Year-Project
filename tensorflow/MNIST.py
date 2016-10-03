### Code for training simple feed-forward network
### neural network for handwritten digit classification
### using the (classic) MNIST data set 

### This code followed tutorials here:
### https://www.tensorflow.org/versions/r0.10/tutorials/mnist/beginners/index.html

import tensorflow as tf

# download hand-written data
from tensorflow.examples.tutorials.mnist import input_data 

# read hand-written data 
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# image input 28x28 pixels 
x = tf.placeholder(tf.float32, [None, 784])

# weights, biases, and model 
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)

# using cross-entropy as loss (cost) function
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# minimize cross-entropy by Gradient Descent with learning rate = 0.5 
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# initialize al tensorflow variables 
init = tf.initialize_all_variables()

# run session
sess = tf.Session()
sess.run(init)

# run training steps 1000 times
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})


# evaluate model
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
