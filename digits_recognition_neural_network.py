# -*- coding: utf-8 -*-
"""digits_recognition_neural_network.ipynb

Automatically generated by Colaboratory.


<h2 style="color:blue" align="center">Handwritten digits classification using neural network</h2>

In this notebook we will classify handwritten digits using a simple neural network which has only input and output layers. We will than add a hidden layer and see how the performance of the model improves
"""

# Commented out IPython magic to ensure Python compatibility.
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np

(X_train, y_train) , (X_test, y_test) = keras.datasets.mnist.load_data()

len(X_train)

len(X_test)

X_train[0].shape

X_train[0]

plt.matshow(X_train[0])

y_train[0]

X_train = X_train / 255
X_test = X_test / 255

X_train[0]

X_train_flattened = X_train.reshape(len(X_train), 28*28)
X_test_flattened = X_test.reshape(len(X_test), 28*28)

X_train_flattened.shape

X_train_flattened[0]

"""<h3 style='color:purple'>Very simple neural network with no hidden layers</h3>

<img src="digits_nn.jpg" />
"""

model = keras.Sequential([
    keras.layers.Dense(10, input_shape=(784,), activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train_flattened, y_train, epochs=5)

model.evaluate(X_test_flattened, y_test)

y_predicted = model.predict(X_test_flattened)
y_predicted[0]

plt.matshow(X_test[0])

"""**np.argmax finds a maximum element  from an array and returns the index of it**"""

np.argmax(y_predicted[0])

y_predicted_labels = [np.argmax(i) for i in y_predicted]

y_predicted_labels[:5]

cm = tf.math.confusion_matrix(labels=y_test,predictions=y_predicted_labels)
cm

import seaborn as sn
plt.figure(figsize = (10,7))
sn.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')

"""<h3 style='color:purple'>Using hidden layer</h3>"""

model = keras.Sequential([
    keras.layers.Dense(100, input_shape=(784,), activation='relu'),
    keras.layers.Dense(10, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train_flattened, y_train, epochs=5)

model.evaluate(X_test,y_test)

y_predicted = model.predict(X_test_flattened)
y_predicted_labels = [np.argmax(i) for i in y_predicted]
cm = tf.math.confusion_matrix(labels=y_test,predictions=y_predicted_labels)

plt.figure(figsize = (10,7))
sn.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')

"""<h3 style='color:purple'>Using Flatten layer so that we don't have to call .reshape on input dataset</h3>"""

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(100, activation='relu'),
    keras.layers.Dense(10, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10)

model.evaluate(X_test,y_test)

y_predicted = model.predict(X_test)
y_predicted = [np.argmax(i) for i in y_predicted]

plt.matshow(X_test[906])
y_predicted[906]
