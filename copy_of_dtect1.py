# -*- coding: utf-8 -*-
"""Copy of Dtect1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-M9rDnzbwMQkE81knixerKFn6zQu8Ga9
"""

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout,BatchNormalization
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

input_shape = (224, 224, 3)

# create a sequential model
model = Sequential()

# add convolutional layers with pooling and dropout
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.25))

# flatten the output and add dense layers with dropout
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

# compile the model
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

# print the model summary
model.summary()

from google.colab import drive
drive.mount("/content/drive")

train_path = '/content/drive/My Drive/Dataset/Training'
test_path = '/content/drive/My Drive/Dataset/Testing'

Image_Width = 512
Image_Height = 512
Image_Size = (Image_Width, Image_Height)
Image_Channel = 3
batch_size=15

train_datagen = ImageDataGenerator(rotation_range=15,
                                  rescale=1./255,
                                  shear_range=0.1,
                                  zoom_range=0.2,
                                  horizontal_flip=True,
                                  width_shift_range=0.1,
                                  height_shift_range=0.1,)

train_generator = train_datagen.flow_from_directory('/content/drive/My Drive/Dataset/Training',
                                              target_size=Image_Size,
                                              batch_size=32,
                                              class_mode = 'categorical')


test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory('/content/drive/My Drive/Dataset/Testing',
                                                  target_size=Image_Size,
                                                  batch_size = 32,
                                                  class_mode='categorical')