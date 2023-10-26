
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.preprocessing.image import ImageDataGenerator

# Setting Folder Paths
train_data_dir = "C:/Users/SHAHAD/Downloads/Telegram Desktop/data-part/data-part/data1/train1"
test_data_dir = "C:/Users/SHAHAD/Downloads/Telegram Desktop/data-part/data-part/data1/test1"

# Determining Image and Batch Sizes
image_size = (224, 224) 
batch_size = 32

# Determining the Architectural Design of the CNN Model
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(2, activation='softmax')  #2 Categories: fracture and healthy bones
])

# Defining Accuracy as a Performance Metric
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Preparing Data Augmentation for Improvement and Data Increase
train_datagen = ImageDataGenerator(
    rescale=1./255,  # Normalizing Pixel Values to the Range [0, 1]
    shear_range=0.2,  # Rotating Images at an Angle
    zoom_range=0.2,  # Scaling Images Up/Down
    horizontal_flip=True)  # Flipping Images Horizontally

# Data Loading and Preparation
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='sparse')  # Defining Categories as Sparse

test_datagen = ImageDataGenerator(rescale=1./255)  # Pixel Value Normalization for the Test Set
test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='sparse')  # Defining Categories as Sparse

# Model Training
model.fit(train_generator, epochs=10, validation_data=test_generator)

# Model Evaluation and Accuracy Calculation
test_loss, test_accuracy = model.evaluate(test_generator)
print("Test accuracy: ",test_accuracy * 100,"%")

#Defining the Save Path for the Model as an .h5 File
model_save_path = 'C:/Users/SHAHAD/Downloads/Telegram Desktop/data-part/modeloldCNNlc.h5'

# Save the Model
model.save(model_save_path)