#يقرا الداتا سيت من جهازك للفيجول  - الكود شغال 

import cv2
import os

# المسار إلى مجلد الصور
folder_path = "مسار_المجلد"

# الحصول على قائمة بأسماء الملفات في المجلد
file_names = os.listdir(folder_path)

# استدعاء الصور وعرضها
for file_name in file_names:
    # التحقق من أن الملف هو صورة
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        # بناء مسار الصورة الكامل
        image_path = os.path.join(folder_path, file_name)
        
        # استدعاء الصورة باستخدام OpenCV
        image = cv2.imread(image_path)
        
        # عرض الصورة
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()