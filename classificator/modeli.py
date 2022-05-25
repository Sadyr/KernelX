from PIL import Image

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Распечатать фигуру
print(train_images.shape)# 60 000 строк изображений размером 28 x 28 пикселей
print(test_images.shape) # 10 000 строк изображений размером 28 x 28 пикселей

# Просмотр тренировочного изображения
img_index = 2 #<<< Вы можете обновить это значение, чтобы посмотреть другие изображения
img = train_images[img_index]
print("Метка изображения: " + str(train_labels[img_index]))
#plt.imshow(img)
imgplot = plt.imshow(img)
plt.axis('off')
plt.show()

#Build the model
# 3 layers, 1 layer to flatten the image to a 28 x 28 = 784 vector
#           1 layer with 128 neurons and relu function
#           1 layer with 10 neurons and softmax function
#Create the neural network model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])
