import os
import pyfiglet
import colorama
from colorama import Fore

os.system("cls||clear")
img_banner = pyfiglet.figlet_format("Dork Google v2.8", font='poison')

a = "Github : https://github.com/Xnuvers007/"
b = "Coded 4study by : XnuversXploitXen / Z3thT5uN4"

print (Fore.RED+img_banner)
print (Fore.CYAN+a+"\n"+b)

banner = Fore.CYAN+"""
        Dork4ry dork creator [DorkGoogle.py]
        Create dorks with this options
        Github: https://github.com/Xnuvers007/
        Coded 4study by: XnuversXploitXen/Z3thT5uN4
        
        Blog / Site : http://bit.ly/Mykingbee
        

        1  ► Files
        2  ► Words
        3  ► Title
        4  ► In Url
        5  ► Extra parameter
        6  ► In site
        7  ► Create dork
        8  ► Search dork with browser
        9  ► Search dork with terminal (Linux)(slow)(Block IP)
        10 ► Clear dork
        0  ► Exit        
"""

T = "Tanggal = "
B = "Bulan = "
Ta = "Tahun = "

import time
import datetime
from datetime import date
from datetime import datetime

hari_ini = datetime.now()
tanggal = hari_ini.strftime(T+'%d ' + B+'%m ' + Ta+'%y')

saat_ini = datetime.now()
jam = saat_ini.strftime('%H:%M:%S')

import webbrowser
create = False
dork = ""
def func_banner():
        print(f"{banner}")
        print ("=================================")
        print (tanggal)
        print ('Jam : ', jam)
        print ("=================================")
        print ("\n")
        print("[+] Include your search [+]")

def func_wait():
        if(dork==""):
                print(" \n         ► Dork without data to search")
                wait = input(' \n         ► Press [ENTER] to continue')
def option_9():

        if(option==9):
                print(" \n         ► [WARNING] - [GOOGLER NOT WORKING CORRETLY]")
                op = str(input(" \nDo you have Googler installed? Y/N: "))
                op = op.capitalize()
                if(op=='Y'):
                        up = str(input(" \nUpdate Googler?: Y/N: "))
                        up.capitalize()
                        if(up=='y'):
                                os.system("googler -u")
                        elif(up=='n'):
                                time.sleep(0.2)
                                print(" \nStarting search...");
                                search = f"googler {dork}"
                                wait = input(' \n         ► [PRESS ENTER TO CONTINUE]')
                                print(" \nMaybe your IP has been blocked by Google")
                                os.system(search)         
                elif(op=='N'):
                        op = str(input(" \nWant to install?: Y/N: "))
                        op = op.capitalize()
                        if(op=='Y'):
                                install = "sudo curl -o /usr/local/bin/googler https://raw.githubusercontent.com/jarun/googler/v2.9/googler && sudo chmod +x /usr/local/bin/googler"
                                print(" \n         ► sudo curl -o /usr/local/bin/googler https://raw.githubusercontent.com/jarun/googler/v2.9/googler && sudo chmod +x /usr/local/bin/googler")
                                wait = input(' \n         ► Press [ENTER] to continue and install')
                                os.system(install)
                               
                        else:
                                print(" \n         ► Exit")
                                exit()
print(img_banner)
time.sleep(2)
os.system('cls||clear')
while create == False:
        
        func_banner()
        option = int(input(" \n[+] ► "))
        if(option==1):
                menu = str(input(" \nFile type: "))
                options = "ext:"
                dork = f"{options}{menu}"
                time.sleep(1)
                print(" \n ► Included")
                time.sleep(0.5)

        elif(option==2):
                options = "intext:"
                menu = str(input(" \nWord: "))
                dork = f"{dork} {options+menu}"
                time.sleep(1)
                print(" \n ► Included")
                time.sleep(0.5)
        elif(option==3):
                options = "intitle:"
                menu = str(input(" \nTitle: "))
                dork = f"{dork} {options+menu}"
                time.sleep(1)
                print(" \n ► Included")
                time.sleep(0.5)
        elif(option==8):         
                if(dork==""):
                        func_wait()
                else:
                        webbrowser.open(f"https://www.google.com/search?q={dork}")
        
        elif(option==4):
                options = "inurl:"
                menu = str(input(" \nIn Url: "))
                dork = f"{dork} {options+menu}"
                time.sleep(1)
                print(" \n ► Included")
                time.sleep(0.5)
        elif(option==5):
                options = ""
                menu = str(input(" \nExtra parameter: "))
                dork = f"{dork} {options+menu}"
                time.sleep(1)
                print(" \n ► Included")
                time.sleep(0.5)
        elif(option==6):
                menu = str(input(" \nIn Site: "))
                options = "site:"
                dork = f"{dork} {options+menu}"
                time.sleep(1)
                print(" \n ► Included")
                time.sleep(0.5)
        elif(option==10):
                print(' \nClearning dork...')
                time.sleep(1)
                dork = ""
                print("Dork cleaned")
                time.sleep(0.5)
        elif(option>10):
                print(" \nWithout option")
                time.sleep(1)

        elif(option==9):
                if(dork==""):
                        func_wait()
                else:
                        option_9()  
        os.system('cls||clear')
        if(option==7):
                
                if(dork==""):

                        print(f" \n        ► Dork without data")  
                else:
                        print(f" \n        ► Dork created → {dork} ")  

        elif(option==0):
                print(" \n         ► Exit")
                print(" \n         ► Tank you for use!")
                print(" \n         ► Github: https://github.com/Xnuvers007/")

                print ("Will Close in 3s...")
                time.sleep(3)
                exit()
        
     
