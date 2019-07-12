import tensorflow as tf

if str(tf.__version__).startswith('1'):
	a = tf.constant(1)
	b = tf.constant(1)
	sess = tf.Session()
	print(sess.run(a + b))
else:
	a = tf.constant(1)
	b = tf.constant(1)
	print(a + b)