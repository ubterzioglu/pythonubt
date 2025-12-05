import os
import shutil
import math

kaynak_klasor = r"E:\0001_Photos\2009_07"
grup_boyutu = 500
hedef_format = "500_{:03d}"

# Tüm dosyaları al, sadece dosya olanları (klasör değil)
dosyalar = [f for f in os.listdir(kaynak_klasor) if os.path.isfile(os.path.join(kaynak_klasor, f))]

# Dosyaları alfabetik sıraya koy
dosyalar.sort()

# Kaç grup olacağını hesapla
toplam_dosya = len(dosyalar)
grup_sayisi = math.ceil(toplam_dosya / grup_boyutu)

print(f"📦 Toplam {toplam_dosya} dosya bulundu. {grup_sayisi} grup oluşturulacak.\n")

# Dosyaları gruplayıp taşı
for i in range(grup_sayisi):
    grup_baslangic = i * grup_boyutu
    grup_dosyalar = dosyalar[grup_baslangic:grup_baslangic + grup_boyutu]

    hedef_klasor = os.path.join(kaynak_klasor, hedef_format.format(i + 1))
    os.makedirs(hedef_klasor, exist_ok=True)

    for dosya in grup_dosyalar:
        kaynak_yolu = os.path.join(kaynak_klasor, dosya)
        hedef_yolu = os.path.join(hedef_klasor, dosya)

        # Taşı (ad çakışması kontrolü istenirse ekleyebiliriz)
        try:
            shutil.move(kaynak_yolu, hedef_yolu)
        except Exception as e:
            print(f"❌ Hata: {dosya} taşınamadı → {e}")

    print(f"✅ {hedef_format.format(i + 1)} klasörüne {len(grup_dosyalar)} dosya taşındı.")

print("\n🎉 Tüm dosyalar başarıyla gruplandırıldı ve taşındı.")
