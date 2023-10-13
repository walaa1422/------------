#اصدار اخر من القرثيم Cnn الدقة = 95 

import tensorflow as tf 
from tensorflow import keras 
from keras.preprocessing.image import ImageDataGenerator 
from keras.applications import ResNet50 
from keras.layers import GlobalAveragePooling2D, Dense, BatchNormalization 
from keras.optimizers import Adam 
from sklearn.utils.class_weight import compute_class_weight 
from keras.layers import Dropout

# Set the paths of the two folders
train_data_dir = 'C:/Users/96655/Downloads/Telegram Desktop/data-complete1/data-complete1/trainN'
test_data_dir = 'C:/Users/96655/Downloads/Telegram Desktop/data-complete1/data-complete1/teastT'

# Define the size of images and batches
image_size = (224, 224) 
batch_size = 32 
 
# Load the ResNet50 model with pre-trained weights 
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3)) 
x = base_model.output 
x = GlobalAveragePooling2D()(x) 
x = BatchNormalization()(x)   
x = Dense(128, activation='relu')(x) 
x = Dropout(0.5)(x) 
predictions = Dense(2, activation='softmax')(x) 
 
# Build the final model
model = keras.Model(inputs=base_model.input, outputs=predictions) 
 
# Assemble the model
optimizer = Adam(learning_rate=0.0001)   
model.compile(optimizer=optimizer, 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy']) 
# Improve weight distribution to handle imbalanced data
train_datagen = ImageDataGenerator( 
    rescale=1./255, 
    shear_range=0.2, 
    zoom_range=0.2, 
    horizontal_flip=True)  
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
 
# Improve the model using optimization on the training set
model.fit(train_generator, epochs=10, validation_data=test_generator) 
# Define accuracy as a measure of performance
test_loss, test_accuracy = model.evaluate(test_generator) 
print(f'Test accuracy:: {test_accuracy * 100:.2f}%')
model.save('C:/Users/96655/Downloads/ResNet_model-allData-acc.h5')
