#يسوي عملية التدريب لنفس المدل 10 مرات - شغال 

import tensorflow as tf 
from tensorflow import keras 
from keras.preprocessing.image import ImageDataGenerator 
 
# تعيين مسار المجلد التدريب 
train_data_dir = 'C:/Users/96655/Desktop/Datasetsplitter/training' 
 
# حجم الصور المستهدف 
target_image_size = (224, 224)  # يمكن أن تكون الأبعاد None لاستخدام الصور بحجمها الأصلي 
 
batch_size = 32 
epochs_per_iteration = 10 
total_iterations = 10 
 
model = None  # تعريف النموذج الأولي 
 
# تكرار عملية التدريب 10 مرات 
for iteration in range(total_iterations): 
    print(f"Iteration {iteration + 1}/{total_iterations}") 
 
    if iteration == 0: 
        # إذا كانت هذه هي المرة الأولى، قم بإنشاء النموذج 
        model = keras.Sequential([ 
            keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(target_image_size[0], target_image_size[1], 3)), 
            keras.layers.MaxPooling2D((2, 2)), 
            keras.layers.Conv2D(64, (3, 3), activation='relu'), 
            keras.layers.MaxPooling2D((2, 2)), 
            keras.layers.Conv2D(128, (3, 3), activation='relu'), 
            keras.layers.MaxPooling2D((2, 2)), 
            keras.layers.Flatten(), 
            keras.layers.Dense(128, activation='relu'), 
            keras.layers.Dense(2, activation='softmax') 
        ]) 
        # إعداد توليفة البيانات للتحسين وزيادة البيانات 
        train_datagen = ImageDataGenerator( 
            zoom_range=0.2  # تكبير/تصغير الصور 
        ) 
    else: 
        # إذا لم تكن هذه هي المرة الأولى، قم بتحميل النموذج السابق 
        model = keras.models.load_model(f'C:/Users/96655/Desktop/Datasetsplitter/model_{iteration}.h5') 
 
    # تحميل البيانات وتحضيرها مع تحديد حجم الصور المستهدف 
    train_generator = train_datagen.flow_from_directory( 
        train_data_dir, 
        target_size=target_image_size, 
        batch_size=batch_size, 
        class_mode='sparse' 
    ) 
 
    # تجميع النموذج 
    model.compile(optimizer='adam', 
                  loss='sparse_categorical_crossentropy', 
                  metrics=['accuracy']) 
 
    # تدريب النموذج 
    model.fit(train_generator, epochs=epochs_per_iteration) 
 
    # حفظ النموذج بعد كل جولة تدريب 
    model.save(f'C:/Users/96655/Desktop/Datasetsplitter/model_{iteration + 1}.h5')