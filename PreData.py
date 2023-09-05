#الكود كامل لعملية معالجة الصور - شغال 
from PIL import Image, ImageEnhance
import imagehash #pip install imagehash 
import os

def enhance_image_quality(image):
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1)  # زيادة التباين بنسبة 200%, اذا كان 1 م راح يفرق نفس الاصلي
    return image

def remove_duplicate_images(images):#تُستخدم لإزالة الصور المكررة من مجموعة الصور
    image_hashes = []
    unique_images = []

    for img in images:
        img_hash = str(imagehash.phash(img))

        if img_hash not in image_hashes:
            image_hashes.append(img_hash)
            unique_images.append(img)

    return unique_images

def preprocess_images(images):
    processed_images = []
    for img in images:
        # تغيير حجم الصورة إلى 200x200 بكسل
        img = img.resize((224,224))

        # تحسين الجودة
        img = enhance_image_quality(img)

        processed_images.append(img)
    return processed_images

if __name__ == "__main__":
    source_folder = 'C:/Users/96655/Desktop/bige data/train/fractured'
    target_folder = 'C:/Users/96655/Desktop/preimaeg/tr1'

    # تحميل الصور من المجلد المصدر
    images = [Image.open(os.path.join(source_folder, filename)) for filename in os.listdir(source_folder)]

    # تحسين جودة الصور
    enhanced_images = [enhance_image_quality(img) for img in images]

    # إزالة الصور المكررة
    unique_images = remove_duplicate_images(enhanced_images)

    # تطبيق عمليات معالجة الصور
    processed_images = preprocess_images(unique_images)

    # حفظ الصور المعالجة في المجلد المستهدف
    os.makedirs(target_folder, exist_ok=True)
    for i, img in enumerate(processed_images):
        image_name = f'processed_image_{i}.jpg'
        img.save(os.path.join(target_folder, image_name))

    print(f'تم تحسين جودة وتغيير حجم {len(processed_images)} صورة وحفظها في المجلد المستهدف.')

