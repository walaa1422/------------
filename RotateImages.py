#عملية التدوير زاويا 10 درجة 360 - شغال 
import cv2
import numpy as np
import os

def rotate_image(image, angle):
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

# تحديد المجلد الذي يحتوي على الصور
source_folder_path = "C:/Users/96655/Desktop/bone-ex/KSEAR"

# تحديد المجلد الذي ستُحفظ فيه الصور المدورة
destination_folder_path = "C:/Users/96655/Desktop/ROTACION/Fractions"

# قراءة جميع ملفات الصور في المجلد
image_files = os.listdir(source_folder_path)

# عرض الصور المدورة وحفظها
for image_file in image_files:
    image_path = os.path.join(source_folder_path, image_file)
    image = cv2.imread(image_path)

    # دوران الصورة بزواية 360 درجة بمقدار 10 درجات لكل دورة
    for angle in range(0, 360, 10):
        rotated_image = rotate_image(image, angle)

        # حفظ الصورة المدورة في المجلد الوجهة
        destination_image_path = os.path.join(destination_folder_path, f"rotated_{angle}_{image_file}")
        cv2.imwrite(destination_image_path, rotated_image)
