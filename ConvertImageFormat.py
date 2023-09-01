#تحويل الصور إلى تنسيق معين: -  شغال
from PIL import Image
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
