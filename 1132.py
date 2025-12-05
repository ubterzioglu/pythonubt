import os
import shutil

# Sabit kaynak klasör
kaynak_klasor = r"E:\0001_Photos\Tarih\2009_07"

# Kullanıcıdan değerler alınır
baslangic = input("🔤 Hangi ifadeyle başlayan dosyaları taşımak istersiniz? (örn: DSC_, IMG_, NIKON D80): ").strip()
hedef_klasor_adi = input("📁 Yeni klasör ismi ne olsun? (örn: D80): ").strip()

# Hedef klasör oluştur
hedef_klasor = os.path.join(kaynak_klasor, hedef_klasor_adi)
os.makedirs(hedef_klasor, exist_ok=True)

# Taşıma işlemi
tasinan = 0

for file in os.listdir(kaynak_klasor):
    kaynak_yolu = os.path.join(kaynak_klasor, file)

    if os.path.isfile(kaynak_yolu) and file.startswith(baslangic):
        hedef_yolu = os.path.join(hedef_klasor, file)

        # Çakışma varsa yeniden adlandır
        i = 1
        while os.path.exists(hedef_yolu):
            ad, ext = os.path.splitext(file)
            hedef_yolu = os.path.join(hedef_klasor, f"{ad}_copy{i}{ext}")
            i += 1

        try:
            shutil.move(kaynak_yolu, hedef_yolu)
            tasinan += 1
            print(f"✅ Taşındı: {file} → {hedef_klasor_adi}/")
        except Exception as e:
            print(f"❌ Hata ({file}): {e}")

print(f"\n🎉 İşlem tamamlandı. Toplam {tasinan} dosya '{hedef_klasor_adi}' klasörüne taşındı.")
