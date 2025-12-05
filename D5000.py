import os
import shutil
import math
import time

# 📌 Klasörler
kaynak_klasor = r"E:\0001_Photos\Tarih\2009_07\D5000"

# 🔍 Tüm dosyaları al (sadece dosyalar)
dosyalar = [f for f in os.listdir(kaynak_klasor) if os.path.isfile(os.path.join(kaynak_klasor, f))]

# 📛 Dosya adlarının son 6 harfine göre sırala
dosyalar.sort(key=lambda x: x[-6:].lower())

toplam = len(dosyalar)
blok_boyutu = 500
blok_sayisi = math.ceil(toplam / blok_boyutu)

print(f"📦 Toplam {toplam} dosya bulundu. {blok_sayisi} klasöre taşınacak.\n")

# ⏱️ Başlangıç
baslangic = time.time()
tasinan = 0

for i in range(blok_sayisi):
    baslangic_index = i * blok_boyutu
    bitis_index = min(baslangic_index + blok_boyutu, toplam)
    grup_dosyalar = dosyalar[baslangic_index:bitis_index]

    hedef_klasor = os.path.join(kaynak_klasor, f"{i + 1:04}")
    os.makedirs(hedef_klasor, exist_ok=True)

    for j, dosya in enumerate(grup_dosyalar):
        kaynak_yolu = os.path.join(kaynak_klasor, dosya)
        hedef_yolu = os.path.join(hedef_klasor, dosya)

        # Aynı isim varsa yeniden adlandır
        k = 1
        while os.path.exists(hedef_yolu):
            ad, ext = os.path.splitext(dosya)
            hedef_yolu = os.path.join(hedef_klasor, f"{ad}_copy{k}{ext}")
            k += 1

        try:
            shutil.move(kaynak_yolu, hedef_yolu)
            tasinan += 1
        except Exception as e:
            print(f"❌ Hata: {dosya} → {e}")
            continue

        # Yüzdelik ilerleme
        toplam_kalan = toplam - tasinan
        yuzde = (tasinan / toplam) * 100
        print(f"✅ {tasinan}/{toplam} taşındı | % {yuzde:.1f} | Kalan: {toplam_kalan}")

sure = int(time.time() - baslangic)
print(f"\n🎉 İşlem tamamlandı. Toplam {tasinan} dosya taşındı. Süre: {sure} sn.")
