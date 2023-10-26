import os

def delete_images_with_name(folder_path, target_name):
    # Read all image files in the folder
    image_files = os.listdir(folder_path)

    # Delete the images that contain the target name
    
    for image_file in image_files:
        if target_name in image_file:
            image_path = os.path.join(folder_path, image_file)
            os.remove(image_path)
            print(f" Deleted successfully : {image_file}")
            
 # Specify the target name of the images to be deleted
target_name = "rotated"


folder_path = "C:/Users/n67-m/Downloads/not fractured-v"
# Delete the images that contain the target name
delete_images_with_name(folder_path, target_name)