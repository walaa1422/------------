#إزالة الملفات غير الصحيحة أو التالفة:    - مازبط معايا 
import os

def remove_invalid_files(dataset_path):
    for filename in os.listdir(dataset_path):
        file_path = os.path.join(dataset_path, filename)
        if os.path.isfile(file_path):
            try:
                # قم بفتح الملف للتحقق من صحته
                with open(file_path, 'rb') as file:
                    pass
            except (IOError, OSError):
                # قم بحذف الملف إذا كان غير صالح
                os.remove(file_path)
                print(f"تم حذف الملف: {file_path}")

# تحديد مسار مجموعة البيانات
dataset_path = "C:/Users/USER/OneDrive/Desktop/archive (6)/train/fractured"

# استدعاء الدالة لإزالة الملفات غير الصحيحة
remove_invalid_files(dataset_path)
