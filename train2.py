import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator

# تعيين مسارات المجلدين للبيانات الجديدة
new_train_data_dir = 'مسار_مجلد_التدريب_للبيانات_الجديدة'
new_test_data_dir = 'مسار_مجلد_الاختبار_للبيانات_الجديدة'

# تحديد حجم الصور والدُفعات
image_size = (224, 224)
batch_size = 32

# تحميل النموذج المحفوظ سابقًا
model_path = 'C:/Users/96655/Desktop/Datasetsplitter/modelold2.h5'
loaded_model = load_model(model_path)

# تحديث مسارات المجلدات للبيانات الجديدة
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

new_train_generator = train_datagen.flow_from_directory(
    new_train_data_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='sparse')

new_test_datagen = ImageDataGenerator(rescale=1./255)
new_test_generator = new_test_datagen.flow_from_directory(
    new_test_data_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='sparse')

# متابعة التدريب على البيانات الجديدة
epochs = 1
loaded_model.fit(new_train_generator, epochs=epochs, validation_data=new_test_generator)

# حساب الدقة على بيانات الاختبار
test_loss, test_accuracy = loaded_model.evaluate(new_test_generator)
print("Test accuracy after", epochs, "epochs:", test_accuracy)

# حفظ النموذج بعد التحديث
loaded_model.save(model_path)