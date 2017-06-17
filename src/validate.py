# Validate TensorFlow installation
import tensorflow as tf
message = tf.constant('TensorFlow installation successful!')
sess = tf.Session()
print(sess.run(message))
