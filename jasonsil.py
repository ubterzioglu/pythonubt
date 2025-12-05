import os

# 📁 Hedef klasör
hedef_klasor = r'E:\GPALL'

# 🔍 Tüm .json dosyalarını bul ve sil
def json_dosyalari_sil():
    sayac = 0
    for dosya in os.listdir(hedef_klasor):
        dosya_yolu = os.path.join(hedef_klasor, dosya)
        if dosya.endswith('.json') and os.path.isfile(dosya_yolu):
            os.remove(dosya_yolu)
            sayac += 1
            print(f"Silindi: {dosya}")

    print(f"\nToplam {sayac} .json dosyası silindi.")

if __name__ == "__main__":
    json_dosyalari_sil()
