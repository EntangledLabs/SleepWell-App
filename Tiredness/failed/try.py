import tensorflow.compat.v1 as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

# 数据直接放在keras.datasets.fashion_mnist中
fashion_dataset = keras.datasets.fashion_mnist
# load_data 返回了四个Number数组
(train_images, train_labels), (test_images, test_labels) = fashion_dataset.load_data()

# 上方train_label 与 test_labels 数组中存放的是index,比如为0就是上衣T恤，1就是裤子以此类推。
class_names = ['上衣/T恤', '裤子', '套衫',
               '裙子', '外套', '凉鞋', '衬衫', '运动鞋', '包包', '踝靴']

# 这个命令是输出它矩阵的形状，例如 3*3*3 的矩阵，5*5的矩阵。
print(train_images.shape)
# 这个输出的结果是60000*28*28的矩阵，有60000个样本，每一个样本是28*28，我们可以看上方的图片
# ，每个图片是由28*28个像素组成的，给神经网络的数据我们都是喂给它吃数值型的。

# 我们查看一下里面的像素点，这里的像素点都是0-255直接
print(train_images[10])

# 我们使用matplotlib去打印出它，可以将这些数值转换成为图片
plt.figure()
plt.imshow(train_images[10])
plt.colorbar()
plt.grid(False)

# 我们需要将所有的数值转换成为0-1类型的值

train_images = train_images / 255.0
test_images = test_images / 255.0

# 现在开始构建模型，通常我们创建了模型，就相当于我们设计了一个智能机器人，然后之后的工作就是喂它吃数据

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

# 我们传入的单个样本是28*28的，Flatten作用就是将这个矩阵转换称为一位数组
# Dense就是全连接层，暂时不做主要的了解，只需要了解28*28=784，784个数字
# 进到keras.layers.Dense(128, activation=tf.nn.relu)之后出来就是
# 128个数字，然后第接着最后出来就是10个数字，依次为class_names中每一类的
# 可能性。

# 现在要进行编译模型，这个过程就是给它吃数据

model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# optimization为优化器
# loss为损失函数
# metrics为提取标准


# 开始正式吃数据，epoch是用原有数据反复训练的次数，理解成羊吃草吧
model.fit(train_images, train_labels, epochs=5)


test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)

def jpg_image_to_array(image_path):
  """
  Loads JPEG image into 3D Numpy array of shape 
  (width, height, channels)
  """
  with Image.open(image_path) as image:         
    im_arr = np.fromstring(image.tobytes(), dtype=np.uint8)
    im_arr = im_arr.reshape((image.size[1], image.size[0], 3))                                   
  return im_arr

def rgb2gray(rgb):
        return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])
    
my_operator = Operation()

test_img = rgb2gray(jpg_image_to_array('333.jpeg'))
print(test_img.shape)

test_img = test_img / 255.0

prediction = model.predict(test_img.reshape(1, 28, 28))

print(class_names[np.argmax(prediction)])
