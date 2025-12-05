import os
import shutil

kaynak_klasor = r"E:\tumu_tek_klasorde"
hedef_klasor = r"E:\UD_ALL"
double_klasor = r"E:\UD_ALL_DOUBLE"

# Hedef klasördeki tüm dosya adlarını topla
print("🎯 Hedef klasördeki tüm dosyalar taranıyor...")
hedef_dosyalar = set()
for alt_kok, _, dosyalar in os.walk(hedef_klasor):
    for dosya in dosyalar:
        hedef_dosyalar.add(dosya.lower())
print(f"✅ Hedef klasörde {len(hedef_dosyalar)} dosya tespit edildi.\n")

# Kaynak klasördeki tüm dosya yollarını al
print("📦 Kaynak klasördeki tüm dosyalar toplanıyor...")
kaynak_dosya_yollari = []
for alt_kok, _, dosyalar in os.walk(kaynak_klasor):
    for dosya in dosyalar:
        kaynak_dosya_yollari.append(os.path.join(alt_kok, dosya))

toplam_dosya = len(kaynak_dosya_yollari)
print(f"✅ Kaynak klasörde toplam {toplam_dosya} dosya bulundu.\n")

# İşlem başlasın
for i, kaynak_dosya_yolu in enumerate(kaynak_dosya_yollari, start=1):
    dosya_adi = os.path.basename(kaynak_dosya_yolu)

    if dosya_adi.lower() in hedef_dosyalar:
        try:
            os.remove(kaynak_dosya_yolu)
            islem = "🗑️ Silindi"
        except Exception as e:
            islem = f"❌ Silme Hatası: {e}"
    else:
        os.makedirs(double_klasor, exist_ok=True)
        hedef_dosya_yolu = os.path.join(double_klasor, dosya_adi)

        # Çakışma varsa yeniden adlandır
        j = 1
        while os.path.exists(hedef_dosya_yolu):
            ad, uzanti = os.path.splitext(dosya_adi)
            hedef_dosya_yolu = os.path.join(double_klasor, f"{ad}_copy{j}{uzanti}")
            j += 1

        try:
            shutil.move(kaynak_dosya_yolu, hedef_dosya_yolu)
            islem = "📁 Taşındı"
        except Exception as e:
            islem = f"❌ Taşıma Hatası: {e}"

    # İlerleme göster
    kalan = toplam_dosya - i
    print(f"{islem} → ({i}/{toplam_dosya}) | Kalan: {kalan} dosya")

print("\n✅ Tüm işlemler tamamlandı.")
