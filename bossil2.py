import os

def delete_empty_folders(root_dir):
    # En derin klasörden başlayarak yukarı doğru gitmesi için tersine sıralama yapılır
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        try:
            if not dirnames and not filenames:  # Klasör tamamen boşsa
                os.rmdir(dirpath)
                print(f"Silindi: {dirpath}")
        except Exception as e:
            print(f"Hata ({dirpath}): {e}")

# Kullanım
delete_empty_folders("E:\\")
