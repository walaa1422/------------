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