### Play and experiment with TensorFlow basic concepts:
### Link: https://www.tensorflow.org/versions/r0.12/get_started/basic_usage.html
### 1. Computation graph
### 2. Variables
### 3. Fetch 


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
# sess = tf.Session()


# Evaluate the computation graph 
# print(sess.run(mul))

### Variables maintain state across executions
### of graph. When you train a model, you use
### variables to hold & update parameters

### Variables can be saved to disk during or
### after training so that it can be retrieved
### for later use

### Link: https://www.tensorflow.org/versions/r0.12/how_tos/variables/index.html

# Create a counter 
state = tf.Variable(0, name="counter")

one = tf.constant(1)
new_value = tf.add(state, one) # state represents output of tf.add ops
update = tf.assign(state, new_value)

# Variable must be initialized
init_op = tf.global_variables_initializer()

# Launch graph and run ops
with tf.Session() as sess:
    # Run init op
    sess.run(init_op)
    # Run update ops
    for _ in range(3):
        sess.run(update)

    print(sess.run(state))
    
