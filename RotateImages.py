#تدوير الصور: - شغال
from PIL import Image
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
