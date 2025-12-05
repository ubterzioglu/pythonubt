import os
import shutil

# Ana klasör
root_dir = r"E:\Pictures"

# Alt klasörleri ve içindeki dosyaları dolaş
for foldername, subfolders, filenames in os.walk(root_dir, topdown=False):
    if foldername == root_dir:
        continue  # Ana klasörü atla

    for filename in filenames:
        src_path = os.path.join(foldername, filename)
        dest_path = os.path.join(root_dir, filename)

        # Aynı isimde dosya varsa yeniden adlandır
        counter = 1
        base, ext = os.path.splitext(filename)
        while os.path.exists(dest_path):
            new_filename = f"{base}_{counter}{ext}"
            dest_path = os.path.join(root_dir, new_filename)
            counter += 1

        # Taşı
        try:
            shutil.move(src_path, dest_path)
        except Exception as e:
            print(f"Hata oluştu: {src_path} -> {dest_path}\n{e}")

    # Dosyalar taşındıktan sonra boş klasörü sil
    try:
        os.rmdir(foldername)
    except OSError:
        pass  # Klasör boş değilse silinmez, sorun değil

print("Tüm dosyalar taşındı ve boş klasörler silindi.")
