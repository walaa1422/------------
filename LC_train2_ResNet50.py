import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator

# تحميل المودل الأساسي
model = tf.keras.models.load_model("C:/Users/96655/Desktop/m/model5.h5")

# تحديد الدالة الخطأ وخوارزمية التحديث
optimizer = tf.keras.optimizers.Adam()

# تحديد مسارات مجلدات البيانات الجديدة
train_data_dir = "C:/Users/96655/Downloads/Telegram Desktop/data-part2/data-part2/data6/train6"
test_data_dir = "C:/Users/96655/Downloads/Telegram Desktop/data-part2/data-part2/data6/test6"

# تحديد حجم الصور وعدد الفئات
image_size = (224, 224)  # حجم الصور المتوقع
batch_size = 32  # حجم الدُفعة (batch size)

# استخدام ImageDataGenerator لتحميل البيانات
train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='sparse'  # إذا كان لديك فئات غير متوازنة، استخدم 'categorical'
)

test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='sparse'
)

# عدد الحلقات (epochs) للتدريب
epochs = 5

# عملية التدريب
model.fit(
    train_generator,
    epochs=epochs,
    validation_data=test_generator
)

# حساب دقة المودل بعد عملية التدريب على البيانات الجديدة
test_loss, test_accuracy = model.evaluate(test_generator)

# طباعة دقة المودل
print("Test accuracy:", test_accuracy)
model.save('C:/Users/96655/Desktop/m/model6.h5')
