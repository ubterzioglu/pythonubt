import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
from collections import defaultdict

source_folder = r"C:\Users\ubter\OneDrive\Desktop\00001"  # DÜZENLE: fotoğrafların bulunduğu klasör
target_folder = r"C:\Users\ubter\OneDrive\Desktop\00001"  # DÜZENLE: sıralı klasörlerin oluşturulacağı klasör

# Desteklenen fotoğraf uzantıları
image_extensions = ['.jpg', '.jpeg', '.png']

# Fotoğrafları ay-yıl'a göre gruplayacağız
date_groups = defaultdict(list)

def get_photo_date_taken(filepath):
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

# Tüm dosyaları tarayalım
for filename in os.listdir(source_folder):
    if any(filename.lower().endswith(ext) for ext in image_extensions):
        full_path = os.path.join(source_folder, filename)
        date_taken = get_photo_date_taken(full_path)

        if date_taken:
            key = f"{date_taken.month:02d}{date_taken.year}"  # Örn: 012010
        else:
            key = "0000UNKNOWN"

        date_groups[key].append(full_path)

# Sıralı olarak klasör oluştur ve fotoğrafları taşı
sorted_keys = sorted(date_groups.keys())
for i, key in enumerate(sorted_keys, start=1):
    folder_name = f"{i:03d}{key}"  # Örn: 001012010
    full_folder_path = os.path.join(target_folder, folder_name)
    os.makedirs(full_folder_path, exist_ok=True)

    for filepath in date_groups[key]:
        shutil.move(filepath, os.path.join(full_folder_path, os.path.basename(filepath)))

print("📁 Tüm fotoğraflar ay/yıla göre klasörlendi.")
