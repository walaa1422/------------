import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.preprocessing.image import ImageDataGenerator

# Specify the directories for the datasets
train_data_dir = 'C:/Users/96655/Desktop/trainN'
test_data_dir = 'C:/Users/96655/Desktop/teastT'

# Specify image size and batch size
image_size = (224, 224)
batch_size = 32

# Define the CNN model architecture
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(2, activation='softmax')
])

# Define the loss function and optimizer for the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Prepare data generator to augment and preprocess the data
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

# Load and prepare the training data
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='sparse')

# Prepare test data generator
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

# Make predictions on test data
predictions = model.predict(test_generator)
predicted_classes = np.argmax(predictions, axis=1)  # Convert probabilities to class labels

# Get the true class labels
true_classes = test_generator.classes

# Calculate false negatives (FN) and false positives (FP)
false_negatives = np.sum((true_classes == 1) & (predicted_classes == 0))
false_positives = np.sum((true_classes == 0) & (predicted_classes == 1))

print("False Negatives (FN):", false_negatives)
print("False Positives (FP):", false_positives)

# Save the model
model_save_path = 'C:/Users/96655/Desktop/mo1.h5'
model.save(model_save_path)
