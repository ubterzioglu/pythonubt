import os

klasor_yolu = r"E:\UD_ALL"
dosya_sayisi = 0

for alt_kok, _, dosyalar in os.walk(klasor_yolu):
    dosya_sayisi += len(dosyalar)

print(f"📁 '{klasor_yolu}' klasörü ve alt klasörlerinde toplam {dosya_sayisi} dosya var.")
