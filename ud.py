import os
import shutil

# Ayarlar
kaynak_klasor = r"E:\Unknown_Or_Double"
hedef_ana_klasor = r"E:\UD_ALL"
grup_boyutu = 1000
klasor_prefix = "UD_"

# Tüm dosya yollarını topla
tum_dosyalar = []
for alt_kok, _, dosyalar in os.walk(kaynak_klasor):
    for dosya in dosyalar:
        tum_dosyalar.append(os.path.join(alt_kok, dosya))

toplam_dosya = len(tum_dosyalar)
print(f"Toplam {toplam_dosya} dosya bulundu. Taşımaya başlanıyor...\n")

# Taşıma işlemi
grup_sayaci = 1
dosya_sayaci = 0

for i, dosya_yolu in enumerate(tum_dosyalar, start=1):
    if dosya_sayaci % grup_boyutu == 0:
        hedef_klasor = os.path.join(hedef_ana_klasor, f"{klasor_prefix}{grup_sayaci:04}")
        os.makedirs(hedef_klasor, exist_ok=True)
        grup_sayaci += 1

    # Dosyayı hedefe taşı
    dosya_adi = os.path.basename(dosya_yolu)
    hedef_dosya_yolu = os.path.join(hedef_klasor, dosya_adi)

    # Aynı isim varsa "_copy" ekle
    sayac = 1
    while os.path.exists(hedef_dosya_yolu):
        dosya_adi_adi, uzanti = os.path.splitext(dosya_adi)
        hedef_dosya_yolu = os.path.join(hedef_klasor, f"{dosya_adi_adi}_copy{sayac}{uzanti}")
        sayac += 1

    try:
        shutil.move(dosya_yolu, hedef_dosya_yolu)
    except Exception as e:
        print(f"Hata (Taşınamadı): {dosya_yolu} -> {e}")
        continue

    dosya_sayaci += 1

    # İlerleme durumu
    if i % 100 == 0 or i == toplam_dosya:
        print(f"⏳ İşlenen: {i}/{toplam_dosya} dosya ({(i / toplam_dosya * 100):.1f}%)")

print("\n✅ Tüm dosyalar başarıyla taşındı.")
