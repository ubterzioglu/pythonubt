import os

# Hedef klasör yolu
target_folder = r"E:\0001_all_500\Date\Unknown_Or_Double"

# Alt klasörleri kontrol et
for root, dirs, files in os.walk(target_folder, topdown=False):
    for dir_name in dirs:
        full_path = os.path.join(root, dir_name)
        # Eğer klasör boşsa sil
        if not os.listdir(full_path):
            try:
                os.rmdir(full_path)
                print(f"Silindi: {full_path}")
            except Exception as e:
                print(f"Hata oluştu: {full_path} - {e}")
