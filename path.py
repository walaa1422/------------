#plt.inshow(img)يطلع الصوره مع الاحداثيات
#for image_class in os.listdir(اسم الملف)
#    for image in os.listdir(os.path.join(اسم الملف,التصنيفر))
#        image_path = os.path.join(اسم الملف,التصنيف,الصور)
#        try:
#            img = cv2.imread(image_path)
#            tip = imghdr.what(image_path)
#            if tip not in image_exts:
#                print('img not ext'.format(image_path))
#                os.remove(image_path)
#        except Exception as e:
#            print('issue with image {}'.format(image_path))