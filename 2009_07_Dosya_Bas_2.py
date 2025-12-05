import os
import shutil
import time

kaynak_klasor = r"E:\0001_Photos\Tarih\2009_07"

# 📥 Kullanıcıdan alınan bilgiler
baslangic = input("🔤 Hangi ifadeyle başlayan dosyaları taşımak istersiniz? (örn: DSC_, IMG_, NIKON D80): ").strip()
hedef_klasor_adi = input("📁 Yeni klasör ismi ne olsun? (örn: D80): ").strip()

# Hedef klasör oluştur
hedef_klasor = os.path.join(kaynak_klasor, hedef_klasor_adi)
os.makedirs(hedef_klasor, exist_ok=True)

# 🔍 Uygun dosyaları önceden belirle
uygun_dosyalar = [
    f for f in os.listdir(kaynak_klasor)
    if os.path.isfile(os.path.join(kaynak_klasor, f)) and f.startswith(baslangic)
]

toplam = len(uygun_dosyalar)
print(f"\n🔎 {toplam} dosya bulundu. Taşımaya başlanıyor...\n")

if toplam == 0:
    print("⚠️ Uygun dosya bulunamadı.")
    exit()

# ⏱️ Başlangıç zamanı
baslangic_zamani = time.time()
tasinan = 0

for i, file in enumerate(uygun_dosyalar, start=1):
    kaynak_yolu = os.path.join(kaynak_klasor, file)
    hedef_yolu = os.path.join(hedef_klasor, file)

    # Çakışma varsa yeniden adlandır
    j = 1
    while os.path.exists(hedef_yolu):
        ad, ext = os.path.splitext(file)
        hedef_yolu = os.path.join(hedef_klasor, f"{ad}_copy{j}{ext}")
        j += 1

    try:
        shutil.move(kaynak_yolu, hedef_yolu)
        tasinan += 1
    except Exception as e:
        print(f"❌ Hata ({file}): {e}")
        continue

    # İlerleme bilgisi
    gecen_sure = time.time() - baslangic_zamani
    ortalama_sure = gecen_sure / i
    kalan = toplam - i
    kalan_sure = kalan * ortalama_sure
    yuzde = (i / toplam) * 100

    print(f"✅ {i}/{toplam} taşındı | % {yuzde:.1f} | Kalan: {kalan} | Tahmini kalan: {int(kalan_sure)} sn")

print(f"\n🎉 İşlem tamamlandı. Toplam {tasinan} dosya '{hedef_klasor_adi}' klasörüne taşındı.")
