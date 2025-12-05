import os

ana_klasor = r"E:\0001_Photos\tarih"

# 🔢 Kullanıcıdan eşik değeri al
try:
    esik_sayi = int(input("📥 Kaç dosyadan fazla içeren klasörleri listelemek istersiniz? "))
except ValueError:
    print("❌ Lütfen geçerli bir sayı girin.")
    exit()

print(f"\n📂 '{ana_klasor}' alt klasörleri taranıyor... (>{esik_sayi} dosya)\n")

klasor_sayilari = []

# Sadece birinci seviye alt klasörler
for root, dirs, _ in os.walk(ana_klasor):
    for alt_klasor in dirs:
        alt_klasor_yolu = os.path.join(root, alt_klasor)
        dosya_sayisi = sum(len(files) for _, _, files in os.walk(alt_klasor_yolu))
        if dosya_sayisi > esik_sayi:
            klasor_sayilari.append((alt_klasor, dosya_sayisi))
    break

# Azalan sıraya göre sırala
klasor_sayilari.sort(key=lambda x: x[1], reverse=True)

# Yazdır
if klasor_sayilari:
    for isim, sayi in klasor_sayilari:
        print(f"📁 {isim:30} → {sayi} dosya")
else:
    print("⚠️ Belirtilen eşik değerinden fazla dosya içeren klasör bulunamadı.")
