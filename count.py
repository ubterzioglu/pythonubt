import os

klasor_yolu = r"E:\GPALL"
dosya_sayisi = sum(len(dosya_listesi) for _, _, dosya_listesi in os.walk(klasor_yolu))

print(f"Toplam dosya sayısı: {dosya_sayisi}")