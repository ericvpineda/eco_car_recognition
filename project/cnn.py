from keras.layers import Dense, BatchNormalization, Conv2D, MaxPool2D, Flatten, Dropout
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 
import numpy as np

# Image constants
img_size = 128
resize_dim = (img_size, img_size)

# Use image generation to distort images to prevent overgeneralization
# Training data image generation
train_generator_data = ImageDataGenerator(
    horizontal_flip=True,
    rotation_range=7,
    zoom_range=0.05,
    rescale=1./255,
)
train_generator = train_generator_data.flow_from_directory(
    "./dataset/train",
    target_size=(img_size,img_size),
    class_mode="sparse",
)

# Training data image generation
test_generator_data = ImageDataGenerator(
    horizontal_flip=True,
    rotation_range=7,
    zoom_range=0.05,
    rescale=1./255,
)

test_generator = test_generator_data.flow_from_directory(
    "./dataset/test",
    target_size=(img_size,img_size),
    class_mode="sparse",
)

# # Initialize Convolutional Neural Network 
# model = Sequential()

# # Layer 1
# model.add(Conv2D(32, (3,3), activation='relu', input_shape=(img_size, img_size, 3)))
# model.add(BatchNormalization())

# # Layer 2
# model.add(Conv2D(64, (3,3), activation='relu'))
# model.add(BatchNormalization())
# model.add(MaxPool2D((2,2)))
# model.add(Dropout(0.3))

# # Layer 3
# model.add(Conv2D(128, (3,3), activation='relu'))
# model.add(BatchNormalization())
# model.add(MaxPool2D((2,2)))
# model.add(Dropout(0.3))

# # Convert 2D array to 1D
# model.add(Flatten())
# model.add(BatchNormalization())
# model.add(Dropout(0.3))

# # Initialize Deep Neural Network
# model.add(Dense(128, activation='relu'))
# model.add(Dropout(0.3))

# model.add(Dense(64, activation='relu'))
# model.add(Dense(7, activation='softmax'))

# # Finalize model 
# model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False), optimizer="adam", metrics=["accuracy"])

# model.fit(
#     train_generator,
#     validation_data=test_generator,
#     epochs=50
# )


# # # Check model accuracy and loss data 
# results = model.evaluate(test_generator)
# print("DEBUG: results=", results)

# CAUTION: Save data to model folder
# model.save('./model')


# Test sample accuracy

# Load model data 
model = tf.keras.models.load_model("./model")

# Names of labels used
names = list(train_generator.class_indices.keys())


# Note: test_generator is batches of 32 images (default)
images = test_generator[0][0]
labels = test_generator[0][1]

for i in range(7):
    
    # Convert PIL images to numpy array
    feature = tf.keras.preprocessing.image.img_to_array(images[i])
    # Add extra dimension to 0th axis
    feature = tf.expand_dims(feature, 0)

    # Predict based on saved model
    prediction = model.predict(feature)
    prediction_label = np.argmax(prediction)
    prediction_prob = prediction[0][prediction_label]

    print('Prediction label:', prediction_label)
    print('Expected label:', int(labels[i]))
    print('CNN predicted output label with probability:', prediction_prob)
    