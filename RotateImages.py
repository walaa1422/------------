#عملية التدوير زاويا 10 درجة 360 - شغال 
import os
from PIL import Image

def rotate_image(image, angle):
    rotated_image = image.rotate(angle, resample=Image.BICUBIC, expand=True)
    return rotated_image

# مسار المجلد الذي يحتوي على الصور
folder_path = 'path_to_folder'

# مسار المجلد لحفظ الصور المدورة
output_folder = 'path_to_output_folder'

# زاوية الدوران الأولية
initial_angle = 10

# زاوية الزيادة في كل تكرار
angle_increment = 10

# عدد التكرارات
num_rotations = 360 // angle_increment

# قراءة كل صورة في المجلد وتنفيذ الدوران وحفظها
for file_name in os.listdir(folder_path):
    image_path = os.path.join(folder_path, file_name)
    image = Image.open(image_path)

    angle = initial_angle
    for i in range(num_rotations):
        rotated_image = rotate_image(image, angle)
        rotated_image_path = os.path.join(output_folder, f'{file_name}_{i}.jpg')
        rotated_image.save(rotated_image_path)
        angle += angle_increment