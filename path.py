#ما
#عشان نشيك على مسارات الصوروالي خارج المسار نحذفو
import os
from matplotlib import pyplot as plt
import cv2
import imghdr
data_dir = 'C:/Users/n67-m/Downloads/final-projrct/test'
image_exts = ['jpeg','jpg', 'bmp', 'png']
for image_class in os.listdir(data_dir):
    for image in os.listdir(os.path.join(data_dir, image_class)):
        image_path = os.path.join(data_dir, image_class, image)
        try:
            img = cv2.imread(image_path)
            tip = imghdr.what(image_path)
            if tip not in image_exts:
                print('img not ext'.format(image_path))
                os.remove(image_path)
        except Exception as e:
            print('issue with image {}'.format(image_path))