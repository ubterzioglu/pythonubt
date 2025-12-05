import os

hedef_klasor = r"E:\UD_ALL"
silinen = 0

# Tüm alt klasörleri gez (tersten → en derindeki önce silinir)
for root, dirs, files in os.walk(hedef_klasor, topdown=False):
    for d in dirs:
        klasor_yolu = os.path.join(root, d)
        try:
            if not os.listdir(klasor_yolu):  # klasör boşsa
                os.rmdir(klasor_yolu)
                silinen += 1
                print(f"🗑️ Silindi: {klasor_yolu}")
        except Exception as e:
            print(f"❌ Hata: {klasor_yolu} → {e}")

print(f"\n✅ Toplam {silinen} boş klasör silindi.")
