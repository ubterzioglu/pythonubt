import os
import shutil

# ✅ Klasör yollarını belirt
kaynak_kok_klasor = r'E:\Google_Photos_16032025'
hedef_klasor = r'E:\GPALL'

# Hedef klasörü oluştur (varsa sorun çıkarmaz)
os.makedirs(hedef_klasor, exist_ok=True)

# 🚀 Dosyaları taşı
def tum_dosyalari_tasi():
    sayac = 0
    for kok, alt_klasorler, dosyalar in os.walk(kaynak_kok_klasor):
        for dosya in dosyalar:
            kaynak_yol = os.path.join(kok, dosya)
            hedef_yol = os.path.join(hedef_klasor, dosya)

            # Aynı isimli dosya varsa isim çakışmasını önle
            if os.path.exists(hedef_yol):
                dosya_adi, uzanti = os.path.splitext(dosya)
                i = 1
                while os.path.exists(hedef_yol):
                    yeni_dosya_adi = f"{dosya_adi}_{i}{uzanti}"
                    hedef_yol = os.path.join(hedef_klasor, yeni_dosya_adi)
                    i += 1

            shutil.move(kaynak_yol, hedef_yol)
            sayac += 1

    print(f"Toplam {sayac} dosya '{hedef_klasor}' klasörüne taşındı.")

if __name__ == "__main__":
    tum_dosyalari_tasi()