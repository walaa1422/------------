#إزالة الصور المكررة: - اشتغل 
from PIL import Image
import os
import hashlib

def remove_duplicate_images(dataset_path):
    hash_set = set()
    for filename in os.listdir(dataset_path):
        file_path = os.path.join(dataset_path, filename)
        if os.path.isfile(file_path) and filename.endswith(('.jpg', '.jpeg', '.png')):
            with open(file_path, 'rb') as file:
                image_hash = hashlib.md5(file.read()).hexdigest()
            if image_hash in hash_set:
                # قم بحذف الصورة المكررة
                os.remove(file_path)
                print(f"تم حذف الصورة المكررة: {file_path}")
            else:
                hash_set.add(image_hash)

# تحديد مسار مجموعة البيانات
dataset_path = "C:/Users/USER/OneDrive/Desktop/archive (6)/train/fractured"

# استدعاء الدالة لإزالة الصور المكررة
remove_duplicate_images(dataset_path)

#---------------------------------------------------------------------------------------------
#تحويل الصور إلى تنسيق معين: -  شغال
'''from PIL import Image
import os

def convert_images_to_format(dataset_path, output_path, output_format):
    for filename in os.listdir(dataset_path):
        file_path = os.path.join(dataset_path, filename)
        if os.path.isfile(file_path) and filename.endswith(('.jpg', '.jpeg', '.png')):
            image = Image.open(file_path)
            output_file_path = os.path.join(output_path, f"{filename.split('.')[0]}.{output_format}")
            image.save(output_file_path)
            print(f"تم تحويل الصورة: {file_path} -> {output_file_path}")

# تحديد مسار مجموعة البيانات
dataset_path = "C:/Users/USER/OneDrive/Desktop/archive (6)/train/fractured"

# تحديد مسار الناتج
output_path = "C:/Users/USER/OneDrive/Desktop/GitHub/final-project/NewPath"

# تحديد تنسيق الصور المستهدف
output_format = "jpg"

# استدعاء الدالة لتحويل الصور إلى التنسيق المحدد
convert_images_to_format(dataset_path, output_path, output_format)
'''
#---------------------------------------------------------------------------------------------
#تدوير الصور: - شغال
'''from PIL import Image
import os

def rotate_images(dataset_path, output_path, degrees):
    for filename in os.listdir(dataset_path):
        file_path = os.path.join(dataset_path, filename)
        if os.path.isfile(file_path) and filename.endswith(('.jpg', '.jpeg', '.png')):
            image = Image.open(file_path)
            rotated_image = image.rotate(degrees)
            output_file_path = os.path.join(output_path, filename)
            rotated_image.save(output_file_path)
            print(f"تم تدوير الصورة: {file_path} -> {output_file_path}")

# تحديد مسار مجموعة البيانات
dataset_path = "C:/Users/USER/OneDrive/Desktop/archive (6)/train/fractured"

# تحديد مسار الناتج
output_path = "C:/Users/USER/OneDrive/Desktop/GitHub/final-project/NewRotation"

# زاوية التدوير (بالدرجات)
degrees = 90

# استدعاء الدالة لتدوير الصور
rotate_images(dataset_path, output_path, degrees)
'''
#---------------------------------------------------------------------------------------------
#تغيير سطوع وتباين الصور: - ما اشتغل فيه ايرور
'''from PIL import Image
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
'''
#---------------------------------------------------------------------------------------------
#تطبيق تأثيرات فلتر على الصور: - شغال
'''from PIL import Image, ImageFilter
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
'''
#---------------------------------------------------------------------------------------------
#تنظيف الأسماء غير المرغوب فيها: - زبط معايا بس مدري صح ولالا
'''import os
import re

def clean_file_names(dataset_path):
    for filename in os.listdir(dataset_path):
        file_path = os.path.join(dataset_path, filename)
        if os.path.isfile(file_path):
            cleaned_filename = re.sub('[^\w\s.-_]', '', filename)  # إزالة الأحرف غير المرغوب فيها
            cleaned_file_path = os.path.join(dataset_path, cleaned_filename)
            os.rename(file_path, cleaned_file_path)
            print(f"تم تنظيف اسم الملف: {file_path} -> {cleaned_file_path}")

# تحديد مسار مجموعة البيانات
dataset_path = "C:/Users/USER/OneDrive/Desktop/archive (6)/train/fractured"

# استدعاء الدالة لتنظيف أسماء الملفات
clean_file_names(dataset_path)
'''
#---------------------------------------------------------------------------------------------
#إزالة الملفات غير الصحيحة أو التالفة:    - مازبط معايا 
'''import os

def remove_invalid_files(dataset_path):
    for filename in os.listdir(dataset_path):
        file_path = os.path.join(dataset_path, filename)
        if os.path.isfile(file_path):
            try:
                # قم بفتح الملف للتحقق من صحته
                with open(file_path, 'rb') as file:
                    pass
            except (IOError, OSError):
                # قم بحذف الملف إذا كان غير صالح
                os.remove(file_path)
                print(f"تم حذف الملف: {file_path}")

# تحديد مسار مجموعة البيانات
dataset_path = "C:/Users/USER/OneDrive/Desktop/archive (6)/train/fractured"

# استدعاء الدالة لإزالة الملفات غير الصحيحة
remove_invalid_files(dataset_path)
'''