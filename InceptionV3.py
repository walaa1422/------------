#cnn,Inception الدقة = 95 
import tensorflow as tf
from keras.applications import InceptionV3
from keras.layers import Input, Flatten, Dense
from keras.models import Model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator

# Set the paths of the two folders
train_data_dir = 'C:/Users/USER/OneDrive/Desktop/data-part2/data1/train1'
test_data_dir = 'C:/Users/USER/OneDrive/Desktop/data-part2/data1/test1'

num_classes = 2

# Load the InceptionV3 model without the Top Layers
inception_base = InceptionV3(weights='imagenet', include_top=False, input_tensor=Input(shape=(224, 224, 3)))
x = inception_base.output
x = Flatten()(x)
x = Dense(512, activation='relu')(x)  # طبقة مخفية مخصصة
output = Dense(num_classes, activation='softmax')(x)  # طبقة الإخراج مخصصة

model = Model(inputs=inception_base.input, outputs=output)

# Compile the model and define training parameters
model.compile(optimizer=Adam(learning_rate=0.0001),
 loss='categorical_crossentropy',
 metrics=['accuracy'])

# Define a data generator to load and modify images
train_datagen = ImageDataGenerator(rescale=1./255,
 shear_range=0.2,
 zoom_range=0.2,
  horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(train_data_dir,
 target_size=(224, 224),
 batch_size=32,
 class_mode='categorical')

test_generator = test_datagen.flow_from_directory(test_data_dir,
 target_size=(224, 224),
 batch_size=32,
 class_mode='categorical')

# Train the model  
history = model.fit(train_generator, epochs=10, validation_data=test_generator)

# Define accuracy as a measure of performance
test_loss, test_accuracy = model.evaluate(test_generator)
print("Test Accuracy:", test_accuracy)
model_save_path = 'C:/Users/USER/OneDrive/Desktop/inception1_model.h5'
model.save(model_save_path)
