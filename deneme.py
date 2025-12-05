import os
import shutil

def main():
    kaynak_klasor = r"E:\Pictures\jpg"  # 📂 Buraya dikkat: yol doğru ve var mı?
    hedef_klasor = r"E:\000allinone"  # 📂 Yeni hedef klasör

    baslangic_klasor_numarasi = 26
    dosya_sayisi_her_klasorde = 500

    if not os.path.exists(kaynak_klasor):
        print(f"❌ Kaynak klasör bulunamadı: {kaynak_klasor}")
        input("Devam etmek için Enter'a bas.")
        return

    dosyalar = sorted(os.listdir(kaynak_klasor))

    for i in range(0, len(dosyalar), dosya_sayisi_her_klasorde):
        grup = dosyalar[i:i + dosya_sayisi_her_klasorde]
        klasor_adi = f"{baslangic_klasor_numarasi:05d}"

        try:
            klasor_yolu = os.path.join(hedef_klasor, klasor_adi)

            # Debug: klasör yolu yazdır
            print(f"📂 Oluşturulacak klasör: {klasor_yolu}")

            os.makedirs(klasor_yolu, exist_ok=True)

            for dosya in grup:
                kaynak_yolu = os.path.join(kaynak_klasor, dosya)
                hedef_yolu = os.path.join(klasor_yolu, dosya)

                # Debug: taşınacak dosya yazdır
                print(f"📦 Taşınıyor: {kaynak_yolu} ➜ {hedef_yolu}")

                shutil.move(kaynak_yolu, hedef_yolu)

        except Exception as e:
            print(f"❌ HATA: klasör veya dosya işlemi sırasında sorun oluştu ➤ {e}")
            input("Hatalı dosya/klasör yolunu gördüysen Enter'a bas, devam edelim.")
            continue

        baslangic_klasor_numarasi += 1

    input("✅ Tüm dosyalar başarıyla işlendi. Çıkmak için Enter'a bas.")

if __name__ == "__main__":
    main()