import pyttsx3
import pyfiglet
from colorama import * 
import os
import sys
from rsap import AsyncRSAP
from rsap import RSAP
import json
import platform
from datetime import datetime
os.system('clear')
def start():
    os.system('clear')
    print(Fore.CYAN + """
      ___           ___           ___           ___                   __n_
     /\  \         /\__\         /\  \         /\__\      ___        /\  \  
    /::\  \       /::|  |       /::\  \       /:/  /     /\  \      /::\  \ 
   /:/\:\  \     /:|:|  |      /:/\:\  \     /:/  /      \:\  \    /:/\:\  \ 
  /::\~\:\  \   /:/|:|__|__   /::\~\:\  \   /:/  /       /::\__\  /::\~\:\  \ 
 /:/\:\ \:\__\ /:/ |::::\__\ /:/\:\ \:\__\ /:/__/     __/:/\/__/ /:/\:\ \:\__\ 
 \/__\:\/:/  / \/__/~~/:/  / \:\~\:\ \/__/ \:\  \    /\/:/  /    \/__\:\/:/  /
      \::/  /        /:/  /   \:\ \:\__\    \:\  \   \::/__/          \::/  /
      /:/  /        /:/  /     \:\ \/__/     \:\  \   \:\__\          /:/  /
     /:/  /        /:/  /       \:\__\        \:\__\   \/__/         /:/  /
     \/__/         \/__/         \/__/         \/__/                 \/__/

""")
    print(Fore.CYAN + '\n\t [+]' + Fore.YELLOW + "System Info")
    print(Fore.CYAN + '\n\t [=]' + Fore.GREEN + f"OS Detected: {platform.system()}")
    print(Fore.CYAN + '\n\t [=]' + Fore.GREEN + f"OS release : {platform.release()}")
    print(Fore.RED + '\n\t [=]' +  Fore.GREEN + ' Amelia v 1.0.0 ')
    print(Fore.RED + '\n\t [=]' +  Fore.GREEN + ' Early Access Version [Linux]')
    print(Fore.RED + '\n\n\n\t [+]' +  Fore.RED + ' Write Exit to exit ')
    print(Fore.RED + '\n\n\n\t [+]' +  Fore.RED + ' Write Chat to use the chatbot ')

    ust = input(">>")
    if "exit" in ust:
        os.system('clear')
        sys.exit()
    else:
        input('Press enter again')
init()
#engine.say("I will speak this text")
#engine.runAndWait()
def bot_reply():
    
    bot = RSAP("dX0eosnsji55", bot_name = 'Amelia', dev_name = 'Kavin Jindal', language = 'en')
    user_text = input('[.] Type your message >> ')
    if 'exit' in user_text:
        start()
    elif 'clear' in user_text:
        os.system('clear')
        chatlog = print(Fore.RED + "[sys] Cleared the chat")
        chatbot()
        bot_reply()
    elif 'help' in user_text:
        print('\n' + Fore.YELLOW + '[o] Help for Amelia' + '\n'
        + Fore.LIGHTMAGENTA_EX + '-------------------------' )
        print(Fore.CYAN + 'Some important commands for Amelia')
        print(Fore.GREEN + 'clear' + Fore.YELLOW + ' : To clear the chats')
        print(Fore.GREEN + 'exit' + Fore.YELLOW + ' : Exit the chatbot')



        

        bot_reply()
     
        
    else:
        astro_text = bot.ai_response(user_text)
        print(Fore.GREEN + f'\n[.] {astro_text}')
        
        
        f = open('chat_logs.txt', 'a')
        f.write('\n' + 'User > ' + user_text + '\n' + 'Amelia > ' + astro_text)
        f.close()
        bot_reply()
def chatbot():
    
    print(Fore.CYAN + """
      ___           ___           ___           ___                   ___
     /\  \         /\__\         /\  \         /\__\      ___        /\  \  
    /::\  \       /::|  |       /::\  \       /:/  /     /\  \      /::\  \ 
   /:/\:\  \     /:|:|  |      /:/\:\  \     /:/  /      \:\  \    /:/\:\  \ 
  /::\~\:\  \   /:/|:|__|__   /::\~\:\  \   /:/  /       /::\__\  /::\~\:\  \ 
 /:/\:\ \:\__\ /:/ |::::\__\ /:/\:\ \:\__\ /:/__/     __/:/\/__/ /:/\:\ \:\__\ 
 \/__\:\/:/  / \/__/~~/:/  / \:\~\:\ \/__/ \:\  \    /\/:/  /    \/__\:\/:/  /
      \::/  /        /:/  /   \:\ \:\__\    \:\  \   \::/__/          \::/  /
      /:/  /        /:/  /     \:\ \/__/     \:\  \   \:\__\          /:/  /
     /:/  /        /:/  /       \:\__\        \:\__\   \/__/         /:/  /
     \/__/         \/__/         \/__/         \/__/                 \/__/

    """)
  
    print(Fore.RED + '\n\t [=]' +  Fore.GREEN + ' Amelia v 1.0.0 ')
    print(Fore.RED + '\n\t [=]' +  Fore.GREEN + ' Early Access Version [Linux]')
    print(Fore.YELLOW + '\n\n\t [=]' +  Fore.CYAN + ' ChatBot Powered by Random-Stuff-API ')
    print('   ')

  
#banner = pyfiglet.figlet_format("Amelia", font = "isometric1")
#print(Fore.RED + banner)
'''
print(Fore.CYAN + """
      ___           ___           ___           ___                   ___
     /\  \         /\__\         /\  \         /\__\      ___        /\  \   
    /::\  \       /::|  |       /::\  \       /:/  /     /\  \      /::\  \ 
   /:/\:\  \     /:|:|  |      /:/\:\  \     /:/  /      \:\  \    /:/\:\  \ 
  /::\~\:\  \   /:/|:|__|__   /::\~\:\  \   /:/  /       /::\__\  /::\~\:\  \ 
 /:/\:\ \:\__\ /:/ |::::\__\ /:/\:\ \:\__\ /:/__/     __/:/\/__/ /:/\:\ \:\__\ 
 \/__\:\/:/  / \/__/~~/:/  / \:\~\:\ \/__/ \:\  \    /\/:/  /    \/__\:\/:/  /
      \::/  /        /:/  /   \:\ \:\__\    \:\  \   \::/__/          \::/  /
      /:/  /        /:/  /     \:\ \/__/     \:\  \   \:\__\          /:/  /
     /:/  /        /:/  /       \:\__\        \:\__\   \/__/         /:/  /
     \/__/         \/__/         \/__/         \/__/                 \/__/

""")
print(Fore.RED + '\n\t [=]' +  Fore.GREEN + ' Amelia v 1.0.0 ')
print(Fore.RED + '\n\t [=]' +  Fore.GREEN + ' Early Access Version ')
print(Fore.RED + '\n\n\t [+]' +  Fore.YELLOW + ' Write Menu to enter the menu ')
input(">>")
'''
start()
os.system('clear')
chatbot()
bot_reply()


