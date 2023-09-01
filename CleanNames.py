#تنظيف الأسماء غير المرغوب فيها: - زبط معايا بس مدري صح ولالا
import os
import re

def clean_file_names(dataset_path):
    for filename in os.listdir(dataset_path):
        file_path = os.path.join(dataset_path, filename)
        if os.path.isfile(file_path):
            cleaned_filename = re.sub('[^\w\s.-_]', '', filename)  # إزالة الأحرف غير المرغوب فيها
            cleaned_file_path = os.path.join(dataset_path, cleaned_filename)
            os.rename(file_path, cleaned_file_path)
            print(f"تم تنظيف اسم الملف: {file_path} -> {cleaned_file_path}")

# تحديد مسار مجموعة البيانات
dataset_path = "C:/Users/USER/OneDrive/Desktop/archive (6)/train/fractured"

# استدعاء الدالة لتنظيف أسماء الملفات
clean_file_names(dataset_path)
