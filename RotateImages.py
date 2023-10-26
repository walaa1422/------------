import os
from PIL import Image

def rotate_image(image, angle):
    rotated_image = image.rotate(angle, resample=Image.BICUBIC, expand=True)
    return rotated_image

# Path to the folder containing the images
folder_path = 'path_to_folder'

# Path to the folder to save the rotated images
output_folder = 'path_to_output_folder'

# Initial rotation angle
initial_angle = 10

# Angle increment for each iteration
angle_increment = 10

# Number of iterations
num_rotations = 360 // angle_increment

# Read each image in the folder, perform rotation, and save it
for file_name in os.listdir(folder_path):
    image_path = os.path.join(folder_path, file_name)
    image = Image.open(image_path)

    angle = initial_angle
    for i in range(num_rotations):
        rotated_image = rotate_image(image, angle)
        rotated_image_path = os.path.join(output_folder, f'{file_name}_{i}.jpg')
        rotated_image.save(rotated_image_path)
        angle += angle_increment
