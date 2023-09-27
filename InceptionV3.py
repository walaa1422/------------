#cnn,Inception
import tensorflow as tf
from keras.applications import InceptionV3
from keras.layers import Input, Flatten, Dense
from keras.models import Model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator

# تحديد مسارات مجلدي التدريب والاختبار
train_data_dir = 'C:/Users/USER/OneDrive/Desktop/Dataset splitter/training'
test_data_dir = 'C:/Users/USER/OneDrive/Desktop/Dataset splitter/testing'

# تحديد عدد الفئات
num_classes = 2

# تحميل نموذج InceptionV3 بدون الطبقات العلوية (Top Layers)
inception_base = InceptionV3(weights='imagenet', include_top=False, input_tensor=Input(shape=(224, 224, 3)))

# تجميع النموذج الكامل مع طبقات مخصصة لمهمتك
x = inception_base.output
x = Flatten()(x)
x = Dense(512, activation='relu')(x)  # طبقة مخفية مخصصة
output = Dense(num_classes, activation='softmax')(x)  # طبقة الإخراج مخصصة

model = Model(inputs=inception_base.input, outputs=output)

# تجميع النموذج وتحديد معلمات التدريب
model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# تحديد مولد البيانات لتحميل الصور وتعديلها
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

# تدريب النموذج ومراقبة الدقة
history = model.fit(train_generator, epochs=5, validation_data=test_generator)

# استخدام دالة evaluate لحساب الدقة على مجموعة الاختبار
test_loss, test_accuracy = model.evaluate(test_generator)
print("Test Accuracy:", test_accuracy)

# تحديد مسار حفظ النموذج كملف .h5
model_save_path = 'C:/Users/USER/OneDrive/Desktop/inception2_model.h5'

# حفظ النموذج
model.save(model_save_path)
