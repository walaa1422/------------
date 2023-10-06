import keras
from keras_applications.resnext import ResNeXt50
from keras.layers import Dense, Flatten
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator

# تعيين مسارات المجلدين
train_data_dir = 'C:/Users/USER/OneDrive/Desktop/data-complete1/trainN'
test_data_dir = 'C:/Users/USER/OneDrive/Desktop/data-complete1/teastT'

# تحديد حجم الصور والدُفعات
image_size = (224, 224)
batch_size = 32

# تحميل نموذج ResNeXt-50 مع الوزن المدرب مسبقًا وبدون الطبقة العلوية (Top classification layer)
model = ResNeXt50(weights='imagenet',
                  backend=keras.backend,
                  layers=keras.layers,
                  models=keras.models,
                  utils=keras.utils)

# إضافة طبقات جديدة للنموذج
x = model.output
x = Flatten()(x)
x = Dense(128, activation='relu')(x)
predictions = Dense(2, activation='softmax')(x)  # عدد الفئات هنا هو 2

# نموذج الواجهة الجديد
model = Model(inputs=model.input, outputs=predictions)

# تجميد طبقات النموذج الأساسي (ResNeXt-50) للتدريب فقط طبقات الطبقات المضافة
for layer in model.layers:
    layer.trainable = False

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
model_save_path = 'C:/Users/USER/OneDrive/Desktop/modelResNeXt50.h5'

# حفظ النموذج
model.save(model_save_path)
