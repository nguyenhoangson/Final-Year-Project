### Linear Regression with TensorFlow
import tensorflow as tf
import numpy as np

# Session
sess = tf.Session() 

# Create 100 random x,y data points in NumPy,
# in which y = x*0.1 + 0.3
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# We try to find out W and b such that y_data = W*x_data + b
# Although we know W = 0.1 and b = 0.3, we have tensorFlow
# figured that out for us

# When you train a model, you use variables to hold and update parameters.
# Variables are in-memory buffers containing tensors
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

# Minimize the loss (cost) function by using Gradent Descent
# with Learning Rate = 0.5 
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# Variables must be then explicitly initialized
init = tf.initialize_all_variables()
sess.run(init)

# Fit the line. And print out W and b after each 20 steps 
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))
