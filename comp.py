import os
import shutil
from collections import defaultdict

ud_all_root = r"E:\UD_ALL"
photos_root = r"E:\0001_Photos"

# 🔎 0001_Photos klasöründeki dosyaları ilk 7 harfe göre haritalandır
print("📦 0001_Photos içindeki dosyalar taranıyor...")
photo_harf7_map = defaultdict(list)

for root, _, files in os.walk(photos_root):
    for file in files:
        key = file[:7].lower()  # İlk 7 harf, küçük harf karşılaştırması
        photo_harf7_map[key].append(root)

print(f"✅ {len(photo_harf7_map)} benzersiz ilk-7-harf bulundu.\n")

# 🎯 UD_ALL içindeki dosyaları işleme
tasinan = 0
atlanan = 0
toplam = 0

for root, _, files in os.walk(ud_all_root):
    for file in files:
        toplam += 1
        key = file[:7].lower()
        kaynak_yolu = os.path.join(root, file)

        if key in photo_harf7_map:
            hedef_klasorler = photo_harf7_map[key]

            for hedef_klasor in hedef_klasorler:
                hedef_yolu = os.path.join(hedef_klasor, file)

                # Aynı isim varsa yeniden adlandır
                i = 1
                while os.path.exists(hedef_yolu):
                    name, ext = os.path.splitext(file)
                    hedef_yolu = os.path.join(hedef_klasor, f"{name}_copy{i}{ext}")
                    i += 1

                try:
                    shutil.move(kaynak_yolu, hedef_yolu)
                    tasinan += 1
                    print(f"📁 Taşındı: {file} → {hedef_klasor}")
                except Exception as e:
                    print(f"❌ Taşıma Hatası ({file}): {e}")
                break  # sadece ilk eşleşmeye taşı
        else:
            atlanan += 1

        if toplam % 100 == 0:
            print(f"⏳ İşlenen: {toplam} | Taşınan: {tasinan} | Atlanan: {atlanan}")

# Özet
print("\n✅ İşlem tamamlandı.")
print(f"🔢 Toplam dosya: {toplam} | Taşınan: {tasinan} | Eşleşmeyen (Atlanan): {atlanan}")
