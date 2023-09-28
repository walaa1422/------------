from PIL import Image
import os
import cv2

# المجلد الذي يحتوي على الصور الأصلية
input_folder = "C:/Users/96655/Desktop/pre/fractions"
# المجلد الذي سيتم حفظ الصور المصغرة فيه
output_folder = "C:/Users/96655/Desktop/pre/fractionspre"
# الحجم الجديد المطلوب للصور المصغرة
#new_size = (224, 224)  # (العرض, الارتفاع)

# دالة لتحسين الجودة وتغيير حجم الصور وتطبيق تصفية الصورة
def process_image(image):
    # Improve quality
    enhanced_image = cv2.equalizeHist(image)
    # Resize the image
    #resized_image = cv2.resize(enhanced_image, new_size)
    # Apply image filter
    filtered_image = cv2.GaussianBlur(enhanced_image, (5, 5), 0)
    return filtered_image

# التأكد من وجود مجلد الإخراج وإنشائه إذا لم يكن موجودًا
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# قائمة بجميع ملفات الصور في المجلد المصدر
image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]

for image_file in image_files:
    # فتح الصورة
    image_path = os.path.join(input_folder, image_file)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # اقرأ الصورة كصورة رمادية

    # معالجة الصورة
    processed_image = process_image(image)

    # حفظ الصور المعالجة في مجلد الإخراج
    output_path = os.path.join(output_folder, image_file)
    cv2.imwrite(output_path, processed_image)

print(f'تم معالجة وتغيير حجم {len(image_files)} صورة وحفظها في مجلد الإخراج.')
