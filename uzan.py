import os
from collections import defaultdict

# Taranacak klasör
kok_klasor = r"E:\\"  # çift \\ önemli!

# Bildiğim tüm uzantılar
image_exts = [
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp",
    ".heic", ".heif", ".raw", ".cr2", ".nef", ".orf", ".sr2", ".arw", ".dng", ".ico", ".svg"
]
video_exts = [
    ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".mpg",
    ".m4v", ".3gp", ".3g2", ".ts", ".mts", ".m2ts", ".ogv", ".rm", ".rmvb",
    ".divx", ".vob", ".f4v", ".asf", ".amv", ".dav", ".drc", ".bik", ".vp9",
    ".vp8", ".yuv", ".mxf", ".nut", ".nsv", ".h264", ".h265"
]

tum_uzantilar = image_exts + video_exts

sayac = defaultdict(int)

print(f"📂 '{kok_klasor}' alt klasörlerinde tarama yapılıyor...\n")

# Dosyaları gez
for root, _, files in os.walk(kok_klasor):
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in tum_uzantilar:
            sayac[ext] += 1

# Sonuçları sıralı şekilde yazdır
if sayac:
    print("🎯 Bulunan dosya sayıları (uzantıya göre):\n")
    for ext, count in sorted(sayac.items(), key=lambda x: x[1], reverse=True):
        print(f"{ext:6} → {count} dosya")
else:
    print("❌ Hiçbir görsel veya video uzantısı bulunamadı.")
