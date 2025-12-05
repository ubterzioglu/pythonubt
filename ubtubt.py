import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

# === 📥 Kullanıcıdan klasör numarası al ===
folder_number = input("📂 Hangi klasörü işlemek istiyorsun? (örnek: 00123): ").strip()

base_path = r"E:\0001_all_500"
source_folder = os.path.join(base_path, folder_number)
target_base_folder = os.path.join(base_path, "Date")
unknown_folder = os.path.join(target_base_folder, "Unknown_Or_Double")

image_extensions = ['.jpg', '.jpeg', '.png']

def get_date_taken(filepath):
    try:
        image = Image.open(filepath)
        exif_data = image._getexif()
        image.close()
        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == "DateTimeOriginal":
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception:
        pass
    return None

if not os.path.exists(source_folder):
    print(f"\n❌ HATA: '{source_folder}' klasörü bulunamadı!")
else:
    os.makedirs(unknown_folder, exist_ok=True)
    files_moved = 0
    files_unknown = 0

    print(f"\n🔍 İşleniyor: {source_folder}\n")

    for filename in os.listdir(source_folder):
        filepath = os.path.join(source_folder, filename)

        if any(filename.lower().endswith(ext) for ext in image_extensions):
            date_taken = get_date_taken(filepath)

            if date_taken:
                folder_name = f"{date_taken.year}_{date_taken.month:02d}"
                target_folder = os.path.join(target_base_folder, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                target_file_path = os.path.join(target_folder, filename)

                if os.path.exists(target_file_path):
                    shutil.move(filepath, os.path.join(unknown_folder, filename))
                    files_unknown += 1
                    print(f"⚠️ '{filename}' → Unknown_Or_Double (Aynı isimde dosya var)")
                else:
                    try:
                        shutil.move(filepath, target_file_path)
                        files_moved += 1
                        print(f"📁 '{filename}' → {folder_name}")
                    except Exception:
                        shutil.move(filepath, os.path.join(unknown_folder, filename))
                        files_unknown += 1
                        print(f"⚠️ '{filename}' → Unknown_Or_Double (Taşıma hatası)")
            else:
                shutil.move(filepath, os.path.join(unknown_folder, filename))
                files_unknown += 1
                print(f"⚠️ '{filename}' → Unknown_Or_Double (EXIF yok)")
        else:
            shutil.move(filepath, os.path.join(unknown_folder, filename))
            files_unknown += 1
            print(f"⚠️ '{filename}' → Unknown_Or_Double (Geçersiz uzantı)")

    print("\n✅ TAMAMLANDI")
    print(f"📦 Taşınan dosyalar (tarih klasörlerine): {files_moved}")
    print(f"🟡 Unknown_Or_Double klasörüne taşınanlar: {files_unknown}")

    # 🔁 Klasörü DONE_ ile yeniden adlandır
    done_folder_name = f"DONE_{folder_number}"
    done_folder_path = os.path.join(base_path, done_folder_name)

    try:
        os.rename(source_folder, done_folder_path)
        print(f"\n🔄 Kaynak klasör yeniden adlandırıldı: {done_folder_name}")
    except Exception as e:
        print(f"\n❌ Klasör yeniden adlandırılamadı: {e}")
