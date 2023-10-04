#كود تاني لخوارزمية ResNet50 
from keras.applications import ResNet50
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import accuracy_score

# تحميل وتهيئة موديل ResNet50
base_model = ResNet50(weights='imagenet', include_top=False)

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(2, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# تجميع الطبقات العليا للتدريب
for layer in base_model.layers:
    layer.trainable = False

model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# تحديد مجلدات البيانات وإعداد مولدات الصور
train_data_dir = 'C:/Users/96655/Downloads/Telegram Desktop/data-complete1/data-complete1/trainN'
test_data_dir = 'C:/Users/96655/Downloads/Telegram Desktop/data-complete1/data-complete1/teastT'
img_width, img_height = 224, 224
batch_size = 32

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')

# تدريب النموذج
model.fit_generator(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    epochs=10)  # يمكنك زيادة عدد الحلقات حسب الحاجة

# حفظ النموذج
model.save('bone_fracture_resnet50_model.h5')

# تحضير بيانات الاختبار وتصنيفها
test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=(img_width, img_height),
    batch_size=1,
    class_mode='categorical',
    shuffle=False)

y_true = test_generator.classes
y_pred = model.predict_generator(test_generator, steps=test_generator.samples)

# حساب الدقة
accuracy = accuracy_score(y_true, y_pred.argmax(axis=1))
percentage_accuracy = accuracy * 100
print('Accuracy on test data:', percentage_accuracy, '%')
