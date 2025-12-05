import os
import shutil
import time
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

# 📥 Kullanıcıdan bilgi al
start_number = input("📂 Başlangıç klasör numarası? (örnek: 00123): ").strip()
count = int(input("🔢 Kaç klasör işlenecek?: ").strip())

base_path = r"E:\0001_all_500"
target_base_folder = os.path.join(base_path, "Date")
unknown_root_folder = os.path.join(target_base_folder, "Unknown_Or_Double")
video_folder = os.path.join(unknown_root_folder, "Video")

# 📸 Desteklenen uzantılar
image_extensions = ['.jpg', '.jpeg', '.png']
video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.3gp', '.mts', '.m4v']
all_valid_extensions = image_extensions + video_extensions

# 📅 EXIF tarihini alma (kilitlenme hatası engellenir)
def get_date_taken(filepath):
    try:
        image = Image.open(filepath)
        exif_data = image._getexif()
        image.close()  # Mutlaka kapat!
        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == "DateTimeOriginal":
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception:
        pass
    return None

# 🔁 Güvenli taşıma (kilitli dosya varsa tekrar dener)
def safe_move(src, dst, retries=2, delay=0.5):
    for attempt in range(retries):
        try:
            shutil.move(src, dst)
            return True
        except PermissionError:
            time.sleep(delay)
    print(f"❌ Dosya taşınamadı (kilitli): {os.path.basename(src)}")
    return False

start_int = int(start_number)
total_time = 0

for offset in range(count):
    start_time = time.time()

    folder_index = offset + 1
    folders_left = count - folder_index
    folder_number = f"{start_int + offset:05d}"
    source_folder = os.path.join(base_path, folder_number)
    unknown_folder = os.path.join(unknown_root_folder, f"Unknown_Or_Double_{folder_number}")

    print(f"\n🚀 [{folder_index}/{count}] Klasör işleniyor: [{folder_number}]")

    if folder_index > 1:
        avg_time = total_time / (folder_index - 1)
        est_remaining = avg_time * folders_left
        print(f"⏳ Ortalama süre: {avg_time:.1f} sn | Kalan tahmini süre: ~{int(est_remaining)} sn")

    if not os.path.exists(source_folder):
        print(f"⛔️ Atlanıyor: '{folder_number}' klasörü yok!")
        continue

    os.makedirs(unknown_folder, exist_ok=True)
    os.makedirs(video_folder, exist_ok=True)

    files_moved = 0
    files_unknown = 0
    files_video = 0

    file_list = os.listdir(source_folder)
    total_files = len(file_list)

    if total_files == 0:
        print(f"📁 [{folder_number}] Klasör boş, atlanıyor.")
        continue

    for index, filename in enumerate(file_list, start=1):
        filepath = os.path.join(source_folder, filename)
        percent_done = int((index / total_files) * 100)

        if percent_done % 10 == 0 and index != total_files:
            print(f"  → %{percent_done} tamamlandı...", end="\r")

        file_lower = filename.lower()

        # 🎥 VİDEO DOSYALARI
        if any(file_lower.endswith(ext) for ext in video_extensions):
            if safe_move(filepath, os.path.join(video_folder, filename)):
                files_video += 1
            continue

        # 📷 FOTOĞRAFLAR
        if any(file_lower.endswith(ext) for ext in image_extensions):
            date_taken = get_date_taken(filepath)
            if date_taken:
                folder_name = f"{date_taken.year}_{date_taken.month:02d}"
                target_folder = os.path.join(target_base_folder, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                target_file_path = os.path.join(target_folder, filename)

                if os.path.exists(target_file_path):
                    safe_move(filepath, os.path.join(unknown_folder, filename))
                    files_unknown += 1
                else:
                    if safe_move(filepath, target_file_path):
                        files_moved += 1
                    else:
                        safe_move(filepath, os.path.join(unknown_folder, filename))
                        files_unknown += 1
            else:
                safe_move(filepath, os.path.join(unknown_folder, filename))
                files_unknown += 1
        else:
            safe_move(filepath, os.path.join(unknown_folder, filename))
            files_unknown += 1

    duration = time.time() - start_time
    total_time += duration

    print(f"\n✅ [{folder_number}] TAMAMLANDI ✔️")
    print(f"📷 Fotoğraflar: {files_moved} başarılı")
    print(f"⚠️  Bilinmeyen foto: {files_unknown}")
    print(f"🎥 Videolar: {files_video}")
    print(f"⏱️ Süre: {duration:.1f} saniye")

    # 🏁 DONE_ klasör ismi
    done_folder_name = f"DONE_{folder_number}"
    done_folder_path = os.path.join(base_path, done_folder_name)

    try:
        os.rename(source_folder, done_folder_path)
        print(f"🔄 '{folder_number}' → '{done_folder_name}' olarak yeniden adlandırıldı")
    except Exception as e:
        print(f"❌ Yeniden adlandırma hatası: {e}")
