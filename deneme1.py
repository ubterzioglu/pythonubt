import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

source_folder = r"C:\Users\ubter\OneDrive\Desktop\00001"  # 📁 Kaynak klasör
target_folder = r"C:\Users\ubter\OneDrive\Desktop\00001"  # 📁 Hedef klasör

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

for filename in os.listdir(source_folder):
    if any(filename.lower().endswith(ext) for ext in image_extensions):
        filepath = os.path.join(source_folder, filename)
        date_taken = get_date_taken(filepath)

        if date_taken:
            # Klasör ismi: 0MMYYYY
            folder_name = f"0{date_taken.month:02d}{date_taken.year}"
        else:
            folder_name = "0000000"  # EXIF verisi yoksa

        target_path = os.path.join(target_folder, folder_name)
        os.makedirs(target_path, exist_ok=True)

        shutil.move(filepath, os.path.join(target_path, filename))

print("✅ Fotoğraflar 0MMYYYY formatında klasörlendi.")
