from keras.models import load_model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator

# تحديد مسار ملف النموذج المدرب مسبقًا بصيغة .h5
pretrained_model_path = 'C:/Users/USER/OneDrive/Desktop/inception2_model.h5'

# تحميل النموذج المدرب مسبقًا من ملف .h5
pretrained_model = load_model(pretrained_model_path)

# تحديد مسارات مجلدي التدريب والاختبار
train_data_dir = 'C:/Users/USER/OneDrive/Desktop/data-3part/data3/train3'
test_data_dir = 'C:/Users/USER/OneDrive/Desktop/data-3part/data3/test3'

# تحديد عدد الفئات
num_classes = 2

# تجميع النموذج وتحديد معلمات التدريب
pretrained_model.compile(optimizer=Adam(learning_rate=0.0001),
                         loss='categorical_crossentropy',
                         metrics=['accuracy'])

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
history = pretrained_model.fit(train_generator, epochs=10, validation_data=test_generator)

# استخدام دالة evaluate لحساب الدقة على مجموعة الاختبار
test_loss, test_accuracy = pretrained_model.evaluate(test_generator)
test_accuracy_percentage = test_accuracy * 100
print("Test Accuracy:", test_accuracy_percentage, "%")

# حفظ النموذج مع التغييرات على نفس ملف النموذج القديم
pretrained_model.save(pretrained_model_path)

