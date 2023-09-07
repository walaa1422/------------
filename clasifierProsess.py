#كود لانشاء واجهة وطلب من المستخدم ارفاق صوره وتصنيفها وحساب الدقه _ شغال 

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
from tensorflow import keras

# تحميل النموذج المدرب
model_save_path = 'C:/Users/96655/Desktop/shapacat/model.h5'
loaded_model = keras.models.load_model(model_save_path)

# تعريف التصنيفات الممكنة (مكسورة وسليمة)
class_labels = ["يوجد كسر", "لايوجد "]

# دالة لتصنيف الصورة
def classify_image(image_path):
    # قراءة الصورة وتجهيزها
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0

    # توسيع الأبعاد لتتناسب مع شكل الإدخال المتوقع للنموذج
    img = np.expand_dims(img, axis=0)

    # استخدام النموذج المحمل للتنبؤ
    predictions = loaded_model.predict(img)

    # الحصول على فهرس الفئة ذي أعلى احتمالية
    class_index = np.argmax(predictions)
    
    # الحصول على تسمية الفئة المقابلة
    class_label = class_labels[class_index]

    # الحصول على الدقة
    accuracy = predictions[0][class_index]

    return class_label, accuracy

# دالة لفتح نافذة الملف واختيار صورة
def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    if file_path:
        load_and_display_image(file_path)
        result, accuracy = classify_image(file_path)
        result_label.config(text=f"تصنيف الصورة: {result}\nنسبة الدقة: {accuracy:.2%}")

# دالة لتحميل وعرض الصورة المحددة
def load_and_display_image(file_path):
    image = Image.open(file_path)
    image.thumbnail((300, 300))  # تحجيم الصورة لعرضها في نافذة صغيرة
    photo = ImageTk.PhotoImage(image)

    # عرض الصورة على واجهة المستخدم
    image_label.config(image=photo)
    image_label.image = photo

# إعداد نافذة التطبيق
app = tk.Tk()
app.title("تحميل وتصنيف صورة")
app.geometry("400x400")

# إنشاء زر لاختيار الصورة
open_button = tk.Button(app, text="اختيار صورة", command=open_file_dialog)
open_button.pack(pady=20)

# إنشاء عنصر لعرض الصورة المحددة
image_label = tk.Label(app)
image_label.pack()

# إنشاء عنصر لعرض تصنيف الصورة ونسبة الدقة
result_label = tk.Label(app, text="", font=("Arial", 14))
result_label.pack()

# تشغيل التطبيق
app.mainloop()
