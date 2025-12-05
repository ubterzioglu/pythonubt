import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

source_folder = r"C:\Users\ubter\OneDrive\Desktop\00001"  # Fotoğrafların olduğu klasör
target_folder = r"C:\Users\ubter\OneDrive\Desktop\00001"  # Sıralanmış klasörlerin oluşturulacağı yer

image_extensions = ['.jpg', '.jpeg', '.png']

def get_date_taken(filepath):
    try:
        image = Image.open(filepath)
        exif_data = image._getexif()
        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == "DateTimeOriginal":
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception:
        pass
    return None

# Dosyaları işle
for filename in os.listdir(source_folder):
    if any(filename.lower().endswith(ext) for ext in image_extensions):
        filepath = os.path.join(source_folder, filename)
        date_taken = get_date_taken(filepath)

        if date_taken:
            folder_name = f"{date_taken.year}_{date_taken.month:02d}"  # Örn: 2010_01
        else:
            folder_name = "UNKNOWN_DATE"

        target_path = os.path.join(target_folder, folder_name)
        os.makedirs(target_path, exist_ok=True)

        shutil.move(filepath, os.path.join(target_path, filename))

print("✅ Fotoğraflar YYYY_MM formatında klasörlendi.")
