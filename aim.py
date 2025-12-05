import os
import shutil

kaynak_klasor = r"E:\0001_Photos\Unknown_Or_Double"
hedef_klasor = r"E:\0001_Photos\Tumu_Tek_Klasorde"

# Hedef klasörü oluştur
os.makedirs(hedef_klasor, exist_ok=True)

# Dosya adını çakışma durumunda güncelle
def benzersiz_dosya_yolu(dosya_yolu):
    base, extension = os.path.splitext(dosya_yolu)
    i = 1
    while os.path.exists(dosya_yolu):
        dosya_yolu = f"{base}_{i}{extension}"
        i += 1
    return dosya_yolu

# Tüm alt klasörleri gez
for alt_kok, _, dosyalar in os.walk(kaynak_klasor):
    for dosya in dosyalar:
        kaynak_dosya = os.path.join(alt_kok, dosya)
        hedef_dosya = os.path.join(hedef_klasor, dosya)
        hedef_dosya = benzersiz_dosya_yolu(hedef_dosya)
        try:
            shutil.copy2(kaynak_dosya, hedef_dosya)
            print(f"Kopyalandı: {hedef_dosya}")
        except Exception as e:
            print(f"Hata ({kaynak_dosya}): {e}")
