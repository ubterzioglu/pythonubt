"""
Instagram Reels Otomatik Yükleme Programı
Fiyat Karşılaştırma Hesabı için
"""

from instagrapi import Client
from instagrapi.types import Usertag, Location
import random
import os
from pathlib import Path
import time


class InstagramReelsBot:
    def __init__(self, username, password):
        """Instagram bot başlatıcı"""
        self.client = Client()
        self.username = username
        self.password = password

        # Fiyat karşılaştırma temalı caption'lar
        self.captions_templates = [
            "🌍 Aynı ürün, farklı fiyatlar! {urun} için ülkeler arası fiyat karşılaştırması 💰\n\n"
            "Hangi ülkede daha uygun? 🤔\n\n"
            "#fiyatkarşılaştırma #dünyafiyatları #alışveriş #tasarruf #parabiriktirme",

            "💸 {urun} almak için en uygun ülke hangisi? 🌎\n\n"
            "Fiyat farkları sizi şaşırtacak! 😱\n\n"
            "#globalprices #shopping #pricedifference #worldprices #savemoney",

            "🛒 {urun} - Ülkeler Arası Fiyat Analizi 📊\n\n"
            "Aradaki fark inanılmaz! Sizce hangi ülkede yaşamak daha avantajlı? 🤷‍♂️\n\n"
            "#fiyatanalizi #ekonomi #dünyaekonomisi #alışverişönerileri #karşılaştırma",

            "🌐 {urun} için dünya turu! Her ülkede farklı bir fiyat 💰✈️\n\n"
            "Yorumlarda sizin ülkenizdeki fiyatı paylaşın! 👇\n\n"
            "#worldtour #prices #comparison #globaleconomy #shoppingtips",

            "📍 {urun} - Nerede daha ucuz? 🔍\n\n"
            "Satın alma gücü açısından hangi ülke kazanıyor? 🏆\n\n"
            "#cheaperprices #wheretobuty #pricecomparison #smartshopping #moneysaving"
        ]

        # Popüler müzikler (Instagram müzik ID'leri)
        # Not: Gerçek müzik ID'lerini Instagram'dan almanız gerekir
        self.trending_music = [
            "trending_music_1",
            "trending_music_2",
            "trending_music_3"
        ]

    def login(self):
        """Instagram'a giriş yap"""
        try:
            print("Instagram'a giriş yapılıyor...")

            # Oturum dosyası varsa kullan
            session_file = f"{self.username}_session.json"
            if os.path.exists(session_file):
                self.client.load_settings(session_file)
                self.client.login(self.username, self.password)
                print("✓ Önceki oturum kullanılarak giriş yapıldı")
            else:
                self.client.login(self.username, self.password)
                self.client.dump_settings(session_file)
                print("✓ Yeni oturum oluşturuldu ve giriş yapıldı")

            return True
        except Exception as e:
            print(f"✗ Giriş hatası: {e}")
            return False

    def generate_caption(self, urun_adi="Bu ürün"):
        """Rastgele caption oluştur"""
        template = random.choice(self.captions_templates)
        caption = template.format(urun=urun_adi)
        return caption

    def upload_reels(self, video_path, urun_adi=None):
        """Reels yükle"""
        try:
            # Dosya kontrolü
            if not os.path.exists(video_path):
                print(f"✗ Dosya bulunamadı: {video_path}")
                return False

            print(f"\n📤 Reels yükleniyor: {video_path}")

            # Ürün adını dosya adından al (belirtilmediyse)
            if urun_adi is None:
                urun_adi = Path(video_path).stem.replace("_", " ").title()

            # Caption oluştur
            caption = self.generate_caption(urun_adi)
            print(f"\n📝 Caption:\n{caption}\n")

            # Reels yükle
            media = self.client.clip_upload(
                video_path,
                caption=caption,
            )

            print(f"✓ Reels başarıyla yüklendi!")
            print(f"✓ Media ID: {media.pk}")
            print(f"✓ Link: https://www.instagram.com/reel/{media.code}/")

            return True

        except Exception as e:
            print(f"✗ Yükleme hatası: {e}")
            return False

    def logout(self):
        """Güvenli çıkış"""
        print("\n👋 Oturum kapatılıyor...")
        # Oturum bilgileri zaten kaydedildi, ek işlem gerekmiyor


def main():
    """Ana program"""
    print("=" * 60)
    print("  INSTAGRAM REELS OTOMATİK YÜKLEME")
    print("  Fiyat Karşılaştırma Hesabı")
    print("=" * 60)

    # Instagram bilgileri
    print("\n🔐 Instagram Hesap Bilgileri")
    username = input("Kullanıcı adı: ")
    password = input("Şifre: ")

    # Bot oluştur
    bot = InstagramReelsBot(username, password)

    # Giriş yap
    if not bot.login():
        print("Program sonlandırılıyor...")
        return

    # Ana döngü
    while True:
        print("\n" + "=" * 60)
        print("📹 YENİ REELS YÜKLEME")
        print("=" * 60)

        # Video dosyası sor
        video_path = input("\nVideo dosya yolu (çıkmak için 'q'): ").strip()

        if video_path.lower() == 'q':
            break

        # Tırnak işaretlerini temizle
        video_path = video_path.strip('"').strip("'")

        # Ürün adı sor (opsiyonel)
        urun_adi = input("Ürün adı (boş bırakabilirsiniz): ").strip()
        if not urun_adi:
            urun_adi = None

        # Yükle
        bot.upload_reels(video_path, urun_adi)

        # Devam et mi?
        devam = input("\n➕ Başka video yüklemek ister misiniz? (e/h): ").lower()
        if devam != 'e':
            break

        # Instagram spam koruması için bekleme
        print("\n⏳ Güvenlik için 30 saniye bekleniyor...")
        time.sleep(30)

    # Çıkış
    bot.logout()
    print("\n✓ Program başarıyla sonlandırıldı!")


if __name__ == "__main__":
    main()