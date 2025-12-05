import os
import shutil

# 📁 Klasör yolları
kaynak_klasor = r'E:\GPALL'
hedef_ana_klasor = r'E:\NEWCLASS'

# ⚙️ Ayarlar
paket_boyutu = 500
baslangic_klasor_numarasi = 71

def dosyalari_paketle():
    # Sadece dosyaları al
    dosyalar = [f for f in os.listdir(kaynak_klasor) if os.path.isfile(os.path.join(kaynak_klasor, f))]
    dosyalar.sort()  # Alfabetik sıraya koymak istersen

    toplam = len(dosyalar)
    print(f"Toplam {toplam} dosya bulundu.")

    for i in range(0, toplam, paket_boyutu):
        paket = dosyalar[i:i+paket_boyutu]
        klasor_numarasi = baslangic_klasor_numarasi + (i // paket_boyutu)
        klasor_adi = f"{klasor_numarasi:05d}"  # 00071 formatı
        klasor_yolu = os.path.join(hedef_ana_klasor, klasor_adi)

        os.makedirs(klasor_yolu, exist_ok=True)

        for dosya in paket:
            kaynak_yol = os.path.join(kaynak_klasor, dosya)
            hedef_yol = os.path.join(klasor_yolu, dosya)

            # Aynı isim varsa üzerine yazmasın
            if os.path.exists(hedef_yol):
                dosya_adi, uzanti = os.path.splitext(dosya)
                j = 1
                while os.path.exists(hedef_yol):
                    yeni_ad = f"{dosya_adi}_{j}{uzanti}"
                    hedef_yol = os.path.join(klasor_yolu, yeni_ad)
                    j += 1

            shutil.move(kaynak_yol, hedef_yol)

        print(f"{len(paket)} dosya {klasor_adi} klasörüne taşındı.")

if __name__ == "__main__":
    dosyalari_paketle()
