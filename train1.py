import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.preprocessing.image import ImageDataGenerator

# تعيين مسارات المجلدين
train_data_dir = "C:/Users/n67-m/Downloads/data-part/data1/train1"
test_data_dir = "C:/Users/n67-m/Downloads/data-part/data1/test1"

# تحديد حجم الصور والدُفعات
image_size = (224, 224)  # هذا ممكن نحذفه
batch_size = 32

# تحديد العمارة المعمارية للنموذج CNN
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(2, activation='softmax')  # 2 فئات: مكسورة وسليمة
])

# تحديد الدقة كمقياس للأداء
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# إعداد توليفة البيانات للتحسين وزيادة البيانات
train_datagen = ImageDataGenerator(
    rescale=1./255,  # تسوية قيم البكسل إلى مدى [0, 1]
    shear_range=0.2,  # تدوير الصور بزاوية
    zoom_range=0.2,  # تكبير/تصغير الصور
    horizontal_flip=True)  # عكس الصور أفقيًا

# تحميل البيانات وتحضيرها
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='sparse')  # تحديد الفئات على أنها sparse

test_datagen = ImageDataGenerator(rescale=1./255)  # تسوية قيم البكسل لمجموعة الاختبار
test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='sparse')  # تحديد الفئات على أنها sparse

# تدريب النموذج
model.fit(train_generator, epochs=10, validation_data=test_generator)

# تقييم النموذج وحساب الدقة
test_loss, test_accuracy = model.evaluate(test_generator)
print("Test accuracy:", test_accuracy)

# تحديد مسار حفظ النموذج كملف .h5
model_save_path = 'C:/Users/n67-m/Downloads/data-part/modelold1.h5'

# حفظ النموذج
model.save(model_save_path)