import os

klasor_yolu = r"E:\UD_ALL_DOUBLE"
sayac = 1

for alt_kok, _, dosyalar in os.walk(klasor_yolu):
    for dosya in dosyalar:
        eski_yol = os.path.join(alt_kok, dosya)
        ad, uzanti = os.path.splitext(dosya)
        yeni_ad = f"{ad}_{sayac}{uzanti}"
        yeni_yol = os.path.join(alt_kok, yeni_ad)

        # Aynı isim varsa sayı artır
        while os.path.exists(yeni_yol):
            sayac += 1
            yeni_ad = f"{ad}_{sayac}{uzanti}"
            yeni_yol = os.path.join(alt_kok, yeni_ad)

        try:
            os.rename(eski_yol, yeni_yol)
            print(f"🔄 Yeniden adlandırıldı: {eski_yol} → {yeni_yol}")
            sayac += 1
        except Exception as e:
            print(f"❌ Hata ({eski_yol}): {e}")
