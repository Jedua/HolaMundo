import tensorflow as tf
# crear tensor
mensaje = tf.string_join(["Hola","Mundo"])
mensaje2 = tf.string_join(["mensaje 2"])
#lanzar Sesion
with tf.Session() as sess:
	print(sess.run(mensaje))
	print(sess.run(mensaje2))
