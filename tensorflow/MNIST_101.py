### Code for training simple feed-forward network
### neural network for handwritten digit classification
### using the (classic) MNIST data set 

### This code followed tutorials here:
### https://www.tensorflow.org/versions/r0.11/tutorials/mnist/beginners/index.html

### This code trains a neural net with only 2 layers 

### Remember that every tensorflow program will have
### 2 stages:
### 1. Graph construction: symbolic or conceptual structure of computation
### 2. Graph execution: actually run computation on computing resources


################## Graph Construction ##################

import tensorflow as tf

# download hand-written data
from tensorflow.examples.tutorials.mnist import input_data 

# read hand-written data 
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# image input 28x28 pixels
# QUESTION: What's placeholder for?
# ANSWER: placeholder is a value that we will put in
# when we run graph computation
# tf.placeholder(dtype, shape=None, name=None)
x = tf.placeholder(tf.float32,
                   [None, 784]) # None here means this dimension can be of any length

# weights, biases, and model 
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)

# using cross-entropy as loss (cost) function
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y),
                                              reduction_indices=[1]))

# minimize cross-entropy by Gradient Descent with learning rate = 0.5
# QUESTION: What tensorflow actually does behind the scene?
# ANSWER: tf adds a node in previous computation graph - optimizer node -
# then it will apply backpropagation to calculate gradient - since tf already
# knows the entire computation graph so it easily does backprop - finally it will
# update parameters - I guess it knows which parameters to update by looking at which are
# tf.Variable? 
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# initialize al tensorflow variables 
init = tf.initialize_all_variables()


################## Graph Execution ##################

# run the computation
with tf.Session() as sess:
    # initialize variables
    sess.run(init)
    
    # run training steps 1000 times
    for _ in range(1000):
        # batch_xs.shape = (100,784)
        # batch_ys.shape = (100,10)
        batch_xs, batch_ys = mnist.train.next_batch(100)
        
        # where placeholders come in
        # a value that we will feed in
        # when we run graph computation
        sess.run(train_step,
                 feed_dict={x: batch_xs, y_: batch_ys})

    # evaluate model
    correct_prediction = tf.equal(tf.argmax(y,1),
                                  tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,
                                      tf.float32))
    print(sess.run(accuracy, feed_dict={x: mnist.test.images,
                                        y_: mnist.test.labels}))

