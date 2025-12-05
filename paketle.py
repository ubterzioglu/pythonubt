import os
import shutil

kaynak_klasor = r'E:\GPALL'
hedef_ana_klasor = r'E:\NEW'
paket_boyutu = 500
baslangic_numara = 71

def dosyalari_paketle():
    try:
        print("Script başladı...")
        print("Kaynak klasör var mı?:", os.path.exists(kaynak_klasor))

        dosyalar = [f for f in os.listdir(kaynak_klasor) if os.path.isfile(os.path.join(kaynak_klasor, f))]
        dosyalar.sort()

        toplam = len(dosyalar)
        print(f"Toplam {toplam} dosya bulundu.")

        for i in range(0, toplam, paket_boyutu):
            paket = dosyalar[i:i+paket_boyutu]
            klasor_numarasi = baslangic_numara + (i // paket_boyutu)
            klasor_adi = f"{klasor_numarasi:05d}"
            klasor_yolu = os.path.join(hedef_ana_klasor, klasor_adi)
            os.makedirs(klasor_yolu, exist_ok=True)

            for dosya in paket:
                kaynak_yol = os.path.join(kaynak_klasor, dosya)
                hedef_yol = os.path.join(klasor_yolu, dosya)

                if os.path.exists(hedef_yol):
                    dosya_adi, uzanti = os.path.splitext(dosya)
                    sayac = 1
                    while os.path.exists(hedef_yol):
                        yeni_ad = f"{dosya_adi}_{sayac}{uzanti}"
                        hedef_yol = os.path.join(klasor_yolu, yeni_ad)
                        sayac += 1

                shutil.move(kaynak_yol, hedef_yol)

            print(f"{len(paket)} dosya {klasor_adi} klasörüne taşındı.")

    except Exception as e:
        print("Bir hata oluştu:", str(e))

if __name__ == "__main__":
    dosyalari_paketle()
