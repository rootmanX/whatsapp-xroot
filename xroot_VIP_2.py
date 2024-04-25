import time
import os
import webbrowser
from colorama import init,Fore,Style
import sys
whatsapp_xroot_ascii="\n                          888               888                                       \n              888               888                                       \n              888               888                                       \n888  888  888 88888b.   8888b.  888888 .d8888b   8888b.  88888b.  88888b. \n888  888  888 888 \"88b     \"88b 888    88K          \"88b 888 \"88b 888 \"88b\n888  888  888 888  888 .d888888 888    \"Y8888b. .d888888 888  888 888  888\nY88b 888 d88P 888  888 888  888 Y88b.       X88 888  888 888 d88P 888 d88P\n \"Y8888888P\"  888  888 \"Y888888  \"Y888  88888P' \"Y888888 88888P\"  88888P\" \n                                  888                    888      888     \n                                  888                    888      888     \n                                  888                    888      888     \n888  888 888d888 .d88b.   .d88b.  888888                                  \n`Y8bd8P' 888P\"  d88\"\"88b d88\"\"88b 888                                     \n  X88K   888    888  888 888  888 888                                     \n.d8\"\"8b. 888    Y88..88P Y88..88P Y88b.                                   \n888  888 888     \"Y88P\"   \"Y88P\"   \"Y888                                  \n"
info="= author : Xrootman\n= Email : Xrootman@proton.mail\n= Github.Com/RootmanX\n= Instagram : Xrootman\n= Telegram : Xrootman\n=========================[XROOTMAN]==============================\n"
print(Fore.GREEN+whatsapp_xroot_ascii)
animation=["[■□□□□□□□□□]","[■■□□□□□□□□]","[■■■□□□□□□□]","[■■■■□□□□□□]","[■■■■■□□□□□]","[■■■■■■□□□□]","[■■■■■■■□□□]","[■■■■■■■■□□]","[■■■■■■■■■□]","[■■■■■■■■■■]"]
init()
def whatsapp_xroot():
 print(Fore.BLUE+"Welcome to WhatsApp_XRoot!"+Style.RESET_ALL)
 print(Fore.BLUE+info+Style.RESET_ALL)
 print("==============================================")
 print(Fore.YELLOW+"This tool allows you to access WhatsApp data.")
 print(Fore.YELLOW+"To get started, please enter the following information:")
 print(Fore.WHITE+"==============================================")
 country_code=input(Fore.WHITE+"Enter your country code with +: ")
 phone_number=input("Enter your mobile phone number without zero: ")
 print(Fore.GREEN+"\nPlease select the hacking method:")
 print("1. Retrieve WhatsApp database")
 print("2. Get WhatsApp files")
 print("3. Log in to WhatsApp via web"+Style.RESET_ALL)
 method_choice=input("Enter your choice (1/2/3): ")
 Pq1=input("Please enter the Lisence: ")
 L23="Lj23FQxxwr"
 if Pq1==L23:
  print("Lisence is correct.")
  if method_choice in ['1','2']:
   print(Fore.YELLOW+"\nDownloading the compressed file..."+Style.RESET_ALL)
   timeout=time.time()+10
   while True:
    if(time.time()>timeout):
     break
    sys.stdout.write("\r"+animation[(int(time.time()-timeout)%len(animation))]+" "+str(int(timeout-time.time()))+"s")    
    sys.stdout.flush()
    time.sleep(0.2)
   print(Fore.GREEN+" File downloaded successfully!"+Style.RESET_ALL)
   directory_name='whatsapp_data'
   if not os.path.exists(directory_name):
    os.makedirs(directory_name)
   os.system(f'explorer {directory_name}')
  elif method_choice=='3':
   print(Fore.YELLOW+"\nOpening the web address to log in to WhatsApp..."+Style.RESET_ALL)
   timeout=time.time()+10
   while True:
    if(time.time()>timeout):
     break
    sys.stdout.write("\r"+animation[(int(time.time()-timeout)%len(animation))]+" "+str(int(timeout-time.time()))+"s")    
    sys.stdout.flush()
    time.sleep(0.2)
   time.sleep(2)
   webbrowser.open("https://web.whatsapp.com")
   print(Fore.GREEN+"Web address opened successfully!"+Style.RESET_ALL)
   input("Press Enter to exit...")
  else:
   print(Fore.RED+"Invalid method selected!"+Style.RESET_ALL)
 else:
  print("Incorrect Lisence.")
  input("Press Enter to exit...")
whatsapp_xroot()