### Play and experiment with TensorFlow

import tensorflow as tf

### Create ops node in computation graph
### tensorflow ops node will return an object
### which represents output of its computation,
### then we can pass this object to other computation nodes 

# make tf constant nodes which is 1x2 and
# 2x1 constant matrices 
a = tf.constant([[2., 3.]]) # a represents output of this node      
b = tf.constant([[4.], [5.]]) # b represents output of this node 

# make tf matrix multiplication node
# in which it takes output of two
# previous nodes, do its computation
# and produce mul as its output 
mul = tf.matmul(a,b)

# Session object: map the computational graph
# to devices, such as GPU, CPU
sess = tf.Session()


# Evaluate the computation graph 
print(sess.run(mul))
