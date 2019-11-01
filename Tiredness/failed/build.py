import tensorflow.compat.v1 as tf
#from tensorflow import keras
#import tensorflow_datasets as tfds
#import numpy as np

fout = open ('result.txt', 'w')

# step 1
filenames = tf.constant(['image1.png', 'image2.png', 'image3.png', 'image4.png','image5.png'])
labels = tf.constant([2,2,4,1,3])

# step 2: create a dataset returning slices of `filenames`
dataset = tf.data.Dataset.from_tensor_slices((filenames, labels))

# step 3: parse every image in the dataset using `map`
def _parse_function(filename, label):
    image_string = tf.io.read_file(filename)
    image_decoded = tf.image.decode_jpeg(image_string, channels=3)
    image = tf.cast(image_decoded, tf.float32)
    return image, label

dataset = dataset.map(_parse_function)
dataset = dataset.batch(2)

# step 4: create iterator and final input tensor

iterator = dataset.make_one_shot_iterator()
images, labels = iterator.get_next()

with tf.Session(graph=tf.get_default_graph()) as sess:
    next_batch = iterator.get_next()
    sess.run ([images, labels])
