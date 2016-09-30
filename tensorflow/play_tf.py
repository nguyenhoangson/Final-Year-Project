### Play and experiment with TensorFlow

import tensorflow as tf

# Session object: map the computational graph
# to devices, such as GPU, CPU
sess = tf.Session()

# Constant  
a = tf.constant(10)
b = tf.constant(15)

# Evaluate the computation graph 
print(sess.run(a+b))
