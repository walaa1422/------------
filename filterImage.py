#تطبيق تأثيرات فلتر على الصور: - شغال
from PIL import Image, ImageFilter
import os

def apply_filter(dataset_path, output_path, filter_name):
    for filename in os.listdir(dataset_path):
        file_path = os.path.join(dataset_path, filename)
        if os.path.isfile(file_path) and filename.endswith(('.jpg', '.jpeg', '.png')):
            image = Image.open(file_path)
            filtered_image = apply_specific_filter(image, filter_name)
            output_file_path = os.path.join(output_path, filename)
            filtered_image.save(output_file_path)
            print(f"تم تطبيق تأثير فلتر على الصورة: {file_path} -> {output_file_path}")

def apply_specific_filter(image, filter_name):
    if filter_name == "blur":
        return image.filter(ImageFilter.BLUR)
    elif filter_name == "sharpen":
        return image.filter(ImageFilter.SHARPEN)
    elif filter_name == "edges":
        return image.filter(ImageFilter.FIND_EDGES)
    elif filter_name == "emboss":
        return image.filter(ImageFilter.EMBOSS)
    else:
        return image

# تحديد مسار مجموعة البيانات
dataset_path = "C:/Users/USER/OneDrive/Desktop/archive (6)/train/fractured"

# تحديد مسار الناتج
output_path = "C:/Users/USER/OneDrive/Desktop/GitHub/final-project/NewFilter"

# اسم التأثير الذي تود تطبيقه ("blur", "sharpen", "edges", "emboss")
filter_name = "edges"

# استدعاء الدالة لتطبيق التأثيرات الفلتر على الصور
apply_filter(dataset_path, output_path, filter_name)
