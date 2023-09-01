#تغيير سطوع وتباين الصور: - ما اشتغل فيه ايرور
from PIL import Image
import os

def adjust_brightness_contrast(dataset_path, output_path, brightness_factor, contrast_factor):
    for filename in os.listdir(dataset_path):
        file_path = os.path.join(dataset_path, filename)
        if os.path.isfile(file_path) and filename.endswith(('.jpg', '.jpeg', '.png')):
            image = Image.open(file_path)
            adjusted_image = ImageEnhance.Brightness(image).enhance(brightness_factor)
            adjusted_image = ImageEnhance.Contrast(adjusted_image).enhance(contrast_factor)
            output_file_path = os.path.join(output_path, filename)
            adjusted_image.save(output_file_path)
            print(f"تم تعديل سطوع وتباين الصورة: {file_path} -> {output_file_path}")

# تحديد مسار مجموعة البيانات
dataset_path = "C:/Users/USER/OneDrive/Desktop/archive (6)/train/fractured"

# تحديد مسار الناتج
output_path = "C:/Users/USER/OneDrive/Desktop/GitHub/final-project/NewSotoa"

# عامل السطوع
brightness_factor = 1.5

# عامل التباين
contrast_factor = 1.2

# استدعاء الدالة لتغيير سطوع وتباين الصور
adjust_brightness_contrast(dataset_path, output_path, brightness_factor, contrast_factor)
