import os
import shutil
from PIL import Image

kaynak_klasor = r"E:\UD_ALL"
hedef_klasor = os.path.join(kaynak_klasor, "500_500_Kucuk")
os.makedirs(hedef_klasor, exist_ok=True)

resim_uzantilari = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp", ".heic"]
piksel_limiti = 250000  # 500x500 = 250000

tasinan = 0

print("🔍 250.000 pikselden küçük görseller taranıyor...\n")

for root, _, files in os.walk(kaynak_klasor):
    for file in files:
        if file.lower().endswith(tuple(resim_uzantilari)):
            kaynak_yolu = os.path.join(root, file)

            try:
                with Image.open(kaynak_yolu) as img:
                    width, height = img.size
                    alan = width * height

                    if alan < piksel_limiti:
                        hedef_yolu = os.path.join(hedef_klasor, file)

                        # Aynı isim varsa yeniden adlandır
                        i = 1
                        while os.path.exists(hedef_yolu):
                            ad, ext = os.path.splitext(file)
                            hedef_yolu = os.path.join(hedef_klasor, f"{ad}_copy{i}{ext}")
                            i += 1

                        shutil.move(kaynak_yolu, hedef_yolu)
                        tasinan += 1
                        print(f"📁 Taşındı: {file} ({width}x{height} = {alan} px)")

            except Exception as e:
                print(f"❌ Hata ({file}): {e}")

print(f"\n✅ Toplam {tasinan} küçük boyutlu görsel '{hedef_klasor}' klasörüne taşındı.")
