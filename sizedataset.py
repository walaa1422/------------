#تغير حجم الصور ,  شغال 
from PIL import Image
import os

input_folder = "C:/Users/96655/Desktop/mm/test"
output_folder = "C:/Users/96655/Desktop/mm/New folder"
target_size = (100, 100)  # حجم الصور المستهدف

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg"):  # افترض أن الصور بتنسيق JPG
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        resized_img = img.resize(target_size, Image.ANTIALIAS)  # استخدام Image.ANTIALIAS هنا
        output_path = os.path.join(output_folder, filename)
        resized_img.save(output_path, quality=95)  # يمكن تعديل جودة الصورة حسب الحاجة
