import os
import shutil

kaynak_root = r"E:\\"  # Ana klasör
hedef_klasor = r"E:\0002_Videos"

# Video uzantıları (küçük harfe dönüştürülmüş)
video_uzantilari = [
    ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".mpg",
    ".m4v", ".3gp", ".3g2", ".ts", ".mts", ".m2ts", ".ogv", ".rm", ".rmvb",
    ".divx", ".vob", ".f4v", ".asf", ".amv", ".dav", ".drc", ".bik", ".vp9",
    ".vp8", ".yuv", ".mxf", ".nut", ".nsv", ".h264", ".h265"
]

# Tüm taşınacak video dosyalarını topla (E:\0002_Videos hariç)
print("📦 Video dosyaları aranıyor...")
video_dosyalar = []
for root, _, files in os.walk(kaynak_root):
    if os.path.abspath(root).lower().startswith(os.path.abspath(hedef_klasor).lower()):
        continue  # hedef klasörün kendisini atla

    for file in files:
        if os.path.splitext(file)[1].lower() in video_uzantilari:
            video_dosyalar.append(os.path.join(root, file))

toplam = len(video_dosyalar)
print(f"\n🎞️ Toplam {toplam} video dosyası bulundu. Taşıma başlıyor...\n")

# Hedef klasör oluştur
os.makedirs(hedef_klasor, exist_ok=True)

# Taşıma işlemi
tasinan = 0
for i, kaynak_yolu in enumerate(video_dosyalar, start=1):
    dosya_adi = os.path.basename(kaynak_yolu)
    hedef_yolu = os.path.join(hedef_klasor, dosya_adi)

    # Aynı isimde dosya varsa yeniden adlandır
    k = 1
    while os.path.exists(hedef_yolu):
        isim, uzanti = os.path.splitext(dosya_adi)
        hedef_yolu = os.path.join(hedef_klasor, f"{isim}_copy{k}{uzanti}")
        k += 1

    try:
        shutil.move(kaynak_yolu, hedef_yolu)
        tasinan += 1
        print(f"✅ {i}/{toplam} Taşındı: {hedef_yolu}")
    except Exception as e:
        print(f"❌ {i}/{toplam} Hata: {e}")

print(f"\n📊 İşlem tamamlandı. Toplam: {toplam}, Taşınan: {tasinan}, Kalan: {toplam - tasinan}")
