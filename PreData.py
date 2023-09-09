import cv2
import os

# دالة لتحسين الجودة وتغيير حجم الصور وتطبيق تصفية الصورة

def process_image(image):

    
    #Improve quality
    enhanced_image = cv2.equalizeHist(image)
    #Resize the image
    resized_image = cv2.resize(enhanced_image, (224, 224))
    #Apply image filter
    filtered_image = cv2.GaussianBlur(resized_image, (5, 5), 0) 


    return filtered_image


# مجلد المصدر للصور الشعاعية
source_folder = 'مسار_مجلد_المصدر'

# مجلد الوجهة للصور المعالجة
destination_folder = 'مسار_مجلد_الوجهة'

# قراءة الصور من المجلد المصدر
image_files = [f for f in os.listdir(source_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]

# معالجة الصور وحفظها في مجلد الوجهة
for filename in image_files:
    image_path = os.path.join(source_folder, filename)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # اقرأ الصورة كصورة رمادية

    # معالجة الصورة
    processed_image = process_image(image)

    # حفظ الصور المعالجة في مجلد الوجهة
    destination_path = os.path.join(destination_folder, filename)
    cv2.imwrite(destination_path, processed_image)

print(f'تم معالجة وتصفية {len(image_files)} صورة وحفظها في مجلد الوجهة.')
