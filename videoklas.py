import os
import shutil
import time

kaynak_klasor = r"E:\0002_Videos"

# 📥 Kullanıcıdan parametreleri al
try:
    en_az_mb = int(input("🔢 En az kaç MB? "))
    en_cok_mb = int(input("🔢 En çok kaç MB? "))
    hedef_klasor_adi = input("📁 Yeni klasör adı ne olsun? (örnek: Kucuk_Videolar) ").strip()
except ValueError:
    print("❌ Lütfen geçerli sayılar girin.")
    exit()

en_az = en_az_mb * 1024 * 1024
en_cok = en_cok_mb * 1024 * 1024
hedef_klasor = os.path.join(kaynak_klasor, hedef_klasor_adi)
os.makedirs(hedef_klasor, exist_ok=True)

# 🔍 Uygun dosyaları tespit et
uygun_dosyalar = []
for dosya in os.listdir(kaynak_klasor):
    tam_yol = os.path.join(kaynak_klasor, dosya)
    if os.path.isfile(tam_yol):
        boyut = os.path.getsize(tam_yol)
        if en_az <= boyut <= en_cok:
            uygun_dosyalar.append(dosya)

toplam = len(uygun_dosyalar)
if toplam == 0:
    print("⚠️ Belirtilen boyut aralığında dosya bulunamadı.")
    exit()

print(f"\n📦 {toplam} dosya bulundu ({en_az_mb}-{en_cok_mb} MB).\n")

# 🕒 Taşıma işlemi
tasinan = 0
baslangic_zamani = time.time()

for i, dosya in enumerate(uygun_dosyalar, start=1):
    kaynak_yolu = os.path.join(kaynak_klasor, dosya)
    hedef_yolu = os.path.join(hedef_klasor, dosya)

    # Çakışma varsa yeniden adlandır
    j = 1
    while os.path.exists(hedef_yolu):
        ad, ext = os.path.splitext(dosya)
        hedef_yolu = os.path.join(hedef_klasor, f"{ad}_copy{j}{ext}")
        j += 1

    try:
        shutil.move(kaynak_yolu, hedef_yolu)
        tasinan += 1
    except Exception as e:
        print(f"❌ Hata ({dosya}): {e}")
        continue

    # ⏱️ Süre ve yüzdelik ilerleme
    gecen = time.time() - baslangic_zamani
    ortalama = gecen / i
    kalan = toplam - i
    tahmini_kalan = kalan * ortalama
    yuzde = (i / toplam) * 100

    print(f"✅ {i}/{toplam} taşındı | % {yuzde:.1f} | Kalan: {kalan} | Tahmini kalan: {int(tahmini_kalan)} sn")

print(f"\n🎉 Tamamlandı. Toplam {tasinan} dosya '{hedef_klasor_adi}' klasörüne taşındı.")
