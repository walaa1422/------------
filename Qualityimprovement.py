#---------------------------------------------------------------------------------------------
#تحسين جودة الصور _ شغال 
import os
import cv2

def enhance_images_in_folder(input_folder, output_folder):
    def enhance_image_quality(image_path, output_path):
        # قراءة الصورة
        image = cv2.imread(image_path)

        # تحسين الجودة هنا (يمكن تطبيق تقنيات متعددة)
        blurred = cv2.GaussianBlur(image, (5, 5), 0)
        lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        l_enhanced = clahe.apply(l)
        lab_enhanced = cv2.merge((l_enhanced, a, b))
        enhanced_image = cv2.cvtColor(lab_enhanced, cv2.COLOR_LAB2BGR)

        # حفظ الصورة المحسنة
        cv2.imwrite(output_path, enhanced_image)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = os.listdir(input_folder)
    for image_file in image_files:
        if image_file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            input_image_path = os.path.join(input_folder, image_file)
            output_image_path = os.path.join(output_folder, image_file)
            enhance_image_quality(input_image_path, output_image_path)

# توجيه إلى مسار المجلد الذي يحتوي على الصور الأصلية والمسار الذي تريد حفظ الصور المحسنة فيه
input_images_folder = 'C:/Users/96655/Desktop/qqqq/test'
output_images_folder = 'C:/Users/96655/Desktop/qqqq/New folder'

# استدعاء الدالة لتحسين الصور في المجلد بالدُفعة
enhance_images_in_folder(input_images_folder, output_images_folder)

