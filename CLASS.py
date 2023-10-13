#كود الكلاسيفير - المممممممهههههههمممممممممممم - شغال 

import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.preprocessing.image import ImageDataGenerator

# Set the paths of the two folders
train_data_dir = 'C:/Users/96655/Desktop/Datasetsplitter/training'
test_data_dir = 'C:/Users/96655/Desktop/Datasetsplitter/testing'

# Define the size of images and batches
image_size = (224, 224) 
batch_size = 32

# Define the architecture of the CNN model
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(2, activation='softmax')])

# Define accuracy as a measure of performance
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Prepare data combination for optimization and data augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,   
    shear_range=0.2,  
    zoom_range=0.2,   
    horizontal_flip=True)   

# Download and prepare data
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='sparse')   
test_datagen = ImageDataGenerator(rescale=1./255)   
test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='sparse')   

# Train the model
model.fit(train_generator, epochs=10, validation_data=test_generator)

# Evaluate the model and calculate accuracy
test_loss, test_accuracy = model.evaluate(test_generator)
print("Test accuracy:", test_accuracy)
model_save_path = 'C:/Users/96655/Desktop/Datasetsplitter/modelold2.h5'
model.save(model_save_path)
