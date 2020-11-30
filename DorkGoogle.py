#https://github.com/Xnuvers007/DorkGoogle
#usr/bin/python3.7

#player XnuversXploitXen v2.8 and v3.7

import os
import colorama
from colorama import Fore
import webbrowser

os.system("cls||clear")
img_banner = Fore.RED + """                                        
                                        
@@@@@@@    @@@@@@   @@@@@@@   @@@  @@@  
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  
@@!  @@@  @@!  @@@  @@!  @@@  @@!  !@@  
!@!  @!@  !@!  @!@  !@!  @!@  !@!  @!!  
@!@  !@!  @!@  !@!  @!@!!@!   @!@@!@!   
!@!  !!!  !@!  !!!  !!@!@!    !!@!!!    
!!:  !!!  !!:  !!!  !!: :!!   !!: :!!   
:!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  
 :::: ::  ::::: ::  ::   :::   ::  :::  
:: :  :    : :  :    :   : :   :   :::  
                                        
                                                              
 @@@@@@@@   @@@@@@    @@@@@@    @@@@@@@@  @@@       @@@@@@@@  
@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@  @@@       @@@@@@@@  
!@@        @@!  @@@  @@!  @@@  !@@        @@!       @@!       
!@!        !@!  @!@  !@!  @!@  !@!        !@!       !@!       
!@! @!@!@  @!@  !@!  @!@  !@!  !@! @!@!@  @!!       @!!!:!    
!!! !!@!!  !@!  !!!  !@!  !!!  !!! !!@!!  !!!       !!!!!:    
:!!   !!:  !!:  !!!  !!:  !!!  :!!   !!:  !!:       !!:       
:!:   !::  :!:  !:!  :!:  !:!  :!:   !::   :!:      :!:       
 ::: ::::  ::::: ::  ::::: ::   ::: ::::   :: ::::   :: ::::  
 :: :: :    : :  :    : :  :    :: :: :   : :: : :  : :: ::   
                                                              
                                    
@@@  @@@       @@@        @@@@@@@@  
@@@  @@@      @@@@        @@@@@@@@  
@@!  @@@     @@!@!             @@!  
!@!  @!@    !@!!@!            !@!   
@!@  !@!   @!! @!!           @!!    
!@!  !!!  !!!  !@!          !!!     
:!:  !!:  :!!:!:!!:        !!:      
 ::!!:!   !:::!!:::  :!:  :!:       
  ::::         :::   :::   ::       
   :           :::   :::  : :       
                                    

        Github : https://github.com/Xnuvers007/
        Coded 4study by : XnuversXploitXen / Z3thT5uN4 """


banner = Fore.CYAN+"""
        Dork4ry dork creator [DorkGoogle.py]
        Create dorks with this options
        Github: https://github.com/Xnuvers007/
        Coded 4study by: XnuversXploitXen/Z3thT5uN4
        
        Blog / Site : http://bit.ly/Mykingbee

==================================================================================

        0  ► Exit
        1  ► Files
        2  ► Words
        3  ► Title
        4  ► In Url
        5  ► Extra parameter
        6  ► In site
        25 ► Create dork
        26 ► Clear dork
        27 ► Execute With Linux / Search dork with terminal (Linux)(slow)(Block IP)
        28 ► Execute / Search Dork With Browser
        
==================================================================================
1 - 6 Itu adalah Dork, Bisa digabungkan dengan Include
7 - 24 Itu adalah Pencarian Maksimal
Tidak bisa disatukan misal : Include > 1 maka tidak bisa digabung dengan 7 - 24
==================================================================================

        7 ► Define
        8 ► Phone Book
        9 ► Maps
        10 ► book
        11 ► news
        12 ► Info
        13 ► Movie/Film
        14 ► Weather
        15 ► related
        16 ► Link
        17 ► Asterisk
        18 ► Minus
        19 ► Range
        20 ► Photo
        21 ► Personal Info
        22 ► OR
        23 ► Send Email
        24 ► Contact to Developer

==================================================================================
        CODING BY XNUVERSXPLOITXEN
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
def option_27():

        if(option==27):
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
                print("Untuk mencari Jenis File Seperti .mp4 , .mp3, .pdf\n")
                a = "Tanpa Titik ya...!!!".upper()
                print (a)
                menu = str(input(" \nFile type: "))
                options = "ext:"
                dork = f"{options}{menu}"
                time.sleep(1)
                print(" \n ► Included")
                time.sleep(0.5)

        elif(option==2):
                print("Untuk Mencari Kata yang sama Dan tepat\n")
                options = "intext:"
                menu = str(input(" \nWord: "))
                dork = f"{dork} {options+menu}"
                time.sleep(1)
                print(" \n ► Included")
                time.sleep(0.5)
        elif(option==3):
                print("Untuk Mencari Judul\n")
                options = "intitle:"
                menu = str(input(" \nTitle: "))
                dork = f"{dork} {options+menu}"
                time.sleep(1)
                print(" \n ► Included")
                time.sleep(0.5)
        elif(option==28):   
                if(dork==""):
                        func_wait()
                else:
                        webbrowser.open(f"https://www.google.com/search?q={dork}")
        
        elif(option==4):
                print("Untuk Mencari Kata kata Dalam URL/Link/Tautan\n")
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
        elif(option==7):
                print("Untuk Mencari Istilah")
                menu = input(" \nDefine: ")
                options = "define:"
                a = "https://google.com/search?q="
                print("Tunggu Sebentar...")
                time.sleep (3)
                print("Silahkan")
                webbrowser.open(a + options+menu)
        elif(option==8):
                print("Untuk Melihat/Mencari Buku Telepon dari Berbagai Negara")
                menu = input(" \nPhonebook: ")
                options = "phonebook:"
                a = "https://google.com/search?q="
                print("Tunggu sebentar...")
                time.sleep(3)
                print("Silahkan...")
                webbrowser.open( a + options+menu)
        elif(option==9):
                print("Untuk Melihat/Mencari Maps")
                menu = str(input(" \nMaps: "))
                options = "maps:"
                a = "https://google.com/search?q="
                time.sleep(3)
                print("Silahkan")
                webbrowser.open(a + options+menu)
        elif(option==10):
                print("Untuk Mencari/Melihat Buku")
                menu = input(" \nBook: ")
                options = "book:"
                a = "https://google.com/search?q="
                print("Tunggu Sebentar...")
                time.sleep(3)
                print("Silahkan")
                webbrowser.open(a + options+menu)
        elif(option==11):
                print("Untuk Melihat Berita")
                menu = input(" \nBerita\news: ")
                options = "news:"
                Xnuvers = "https://google.com/search?q="
                print("Tunggu Sebentar...")
                time.sleep(3)
                print("Silahkan")
                webbrowser.open(Xnuvers + options+menu)
        elif(option==12):
                print("Untuk Mencari Informasi")
                menu = input(" \nInfo: ")
                options = "info:"
                a = "https://google.com/search?q="
                print("Tunggu Sebentar...")
                time.sleep(3)
                print("Silahkan")
                webbrowser.open(a + options+menu)
        elif(option==13):
                print("Untuk Mencari Film/Movie")
                menu = input(" \nMovie/Film: ")
                options = "movie:"
                a = "https://google.com/search?q="
                print("tunggu Sebentar...")
                time.sleep(3)
                print("Silahkan")
                webbrowser.open(a + options+menu)
        elif(option==14):
                print("Untuk Mengetahui Cuaca")
                menu = input(" \nWeather/Cuaca: ")
                options = "weather:"
                b = "https://google.com/search?q="
                print("Tunggu Sebentar...")
                time.sleep(3)
                print("Silahkan")
                webbrowser.open(b + options+menu)
        elif(option==15):
                print("Untuk Mencari Sesuatu yang memiliki hubungan/yang sama")
                menu = input(" \nRelated/Yang berhubungan: ")
                options = "related:"
                c = "https://google.com/search?q="
                time.sleep(3)
                print("Silahkan")
                webbrowser.open(c + options+menu)
        elif(option==16):
                print("Contohnya Seperti youtube.com/ninjahatori di setiap link ada tulisan Ninja Hatori, gak Di Youtube Saja \n")
                menu = input(" \nLink: ")
                options = "link:"
                a = "https://google.com/search?q="
                time.sleep(3)
                print("Silahkan")
                webbrowser.open(a + options+menu)
        elif(option==17):
                print("berfungsi Untuk mencari kata yang hilang, Cocok untuk Mencari Lagu\n")
                a = input("Masukan Kata: ")
                b = input("Masukan Kata Selanjutnya yang dihafal: ")
                c = "https://google.com/search?q="
                d = a+" * "+b
                e = c+d
                print("Tunggu Sebentar...")
                time.sleep(2)
                webbrowser.open(e)
        elif(option==18):
                print("berfungi untuk mengecualikan kata-kata Yang tidak Tepat")
                print("\nContohnya Bahasa Pemrograman -html, maka html tidak ikut dalam pencarian \n")
                a = input("Masukan Kata: ")
                b = input("Masukan kata Yang Tidak tepat/tidak diinginkan: ")
                print("Tunggu Sebentar...")
                c = "https://google.com/search?q="
                d = a + " -" + b
                e = c+d
                time.sleep(2)
                webbrowser.open(e)
        elif(option==19):
                print("Berfungsi Sebagai Jarak, misal Sejarah Indonesia Sejak 1900 sampai 2020\n")
                print("atau presiden Indonesia 2010-2020\n")
                a = input("Masukan Kata : ")
                b = input("Dari tahun ? tanpa tanda - : ")
                c = input("Sampai Tahun ? Tanpa tanda - : ")
                print("Tunggu Sebentar")
                d = "https://google.com/search?q="
                e = a + b + ".." + c
                f = d+e
                time.sleep(2)
                webbrowser.open(f)
        elif(option==20):
                print("Berfungsi Untuk mencari Foto\n")
                ba = input ("Ingin Format Apa ? Png atau JPG ? : [P/J] ")
                if ba=="j" or ba=="J":
                        a = input("Masukan Kata : ")
                        print ("tunggu sebentar")
                        b = "https://google.com/search?q="
                        c = b + "Foto:"+a+".jpg"
                        time.sleep(3)
                        print("Silahkan...")
                        webbrowser.open(c)
                elif ba=="P" or ba=="p":
                        a = input("Masukan Kata : ")
                        print ("tunggu sebentar")
                        b = "https://google.com/search?q="
                        c = b + "Foto:"+a+".png"
                        time.sleep(3)
                        print("Silahkan...")
                        webbrowser.open(c)
                else:
                        print("Maaf tidak ada Pilihan Selain P dan J")
                        a = "P untuk png dan j untuk jpg".upper()
                        print(a)
        elif(option==21):
                print("Berfungsi untuk mencari Informasi personal\n")
                print("Contohnya Seperti Soekarno: Wikipedia atau Jokowi: Kompas.com atau bts: transtv\n")
                a = input("Masukan Kata dibagian sebelum titik dua (:) : ")
                b = input("Masukan Kata buat dibagian setelah titik dua (:) : ")
                print("Tunggu Sebentar ya...")
                c = a + ":" + b
                time.sleep(2)
                webbrowser.open(c)
        elif(option==22):
                print("Berfungsi Jika lupa atau bingung Misal Contoh Duluan ayam atau telur, atau kita lupa nama orang misal Ashe Dalmasca atau Ashelia B'nargin\n")
                a = input("Masukan Kata Pertama : ")
                b = input("Masukan Kata Kedua : ")
                c = d + a + " OR " + b
                d = "https://google.com/search?q="
                print("Tunggu Sebentar Oke ....")
                time.sleep(2)
                webbrowser.open(d)
        elif(option==23):
                print("Berfungsi untuk mengirim Email\n")
                print("Jika ada kesalahan atau Bug atau Rusak, dll Silahkan hubungi Admin developer dengan Cara memilih Nomor 24. \n")
                a = input("Masukan Alamat email : ")
                b = "mailto:" + a
                print("Tunggu Sebentar...")
                time.sleep(2)
                webbrowser.open(b)
        elif(option==24):
                print("Sedang Diarahkan Untuk Menghubungi Developer...")
                time.sleep(7)
                webbrowser.open("mailto:xnuversh1kar4@gmail.com", new=0, autoraise=True)
                print("Exit dalam 3 Detik...")
                time.sleep(3)
                exit(code=None)
        elif(option==26):
                print(' \nClearning dork...')
                time.sleep(1)
                dork = ""
                print("Dork cleaned")
                time.sleep(0.5)
        elif(option>26):
                print(" \nWithout option")
                time.sleep(1)

        elif(option==27): #//
                if(dork==""):
                        func_wait()
                else:
                        option_27()  
        os.system('cls||clear')
        if(option==25):
                
                if(dork==""):

                        print(f" \n        ► Dork without data")  
                else:
                        print(f" \n        ► Dork created → {dork} ")  

        elif(option==0):
                print(" \n         ► Exit")
                print(" \n         ► Thank you for use!")
                print(" \n         ► Github: https://github.com/Xnuvers007/")

                print ("Will Close in 3s...")
                time.sleep(3)
                exit()
        
     
