import tensorflow as tf
from keras.models import load_model, Model
from  keras.layers import Dense, GlobalAveragePooling2D
from  keras.applications import ResNet50
from  keras.preprocessing.image import ImageDataGenerator
from  keras.metrics import Accuracy

# تحميل النموذج المحفوظ سابقًا
model_path = 'C:/Users/96655/Desktop/m/resnet50_model.h5'
saved_model = load_model(model_path)

# تحضير البيانات الجديدة
train_data_dir = 'C:/Users/96655/Downloads/Telegram Desktop/data-part2/data-part2/data1/train1'
test_data_dir = 'C:/Users/96655/Downloads/Telegram Desktop/data-part2/data-part2/data1/test1'

batch_size = 32

# تحميل واستعداد البيانات باستخدام ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1.0/255.0)
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical'
)

validation_datagen = ImageDataGenerator(rescale=1.0/255.0)
validation_generator = validation_datagen.flow_from_directory(
    test_data_dir,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical'
)

# إعداد الطبقات النهائية للنموذج باستخدام ResNet50
base_model = ResNet50(weights='imagenet', include_top=False)
x = base_model.output
x = GlobalAveragePooling2D()(x)
predictions = Dense(train_generator.num_classes, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=predictions)

# تجميد طبقات ResNet50 للتدريب
for layer in base_model.layers:
    layer.trainable = False

# تجميع النموذج وتحديث الأوزان باستخدام بيانات الجديدة وحساب الدقة
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=[Accuracy()])

# تدريب النموذج مع حساب دقة النموذج باستخدام بيانات الجديدة
model.fit_generator(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // batch_size,
    epochs=10  # عدد الحلقات التدريبية
)

# حساب الدقة على بيانات التحقق بعد اكتمال التدريب
accuracy = model.evaluate_generator(validation_generator, steps=validation_generator.samples // batch_size)

# طباعة نسبة الدقة
print("accuracy :  ", accuracy[1])

# حفظ النموذج المعتمد على ResNet50 بعد التدريب
model.save('C:/Users/96655/Desktop/m/modeld2.h5')
