import sys, os
from termcolor import colored
import termcolor
print colored(""" 
     _____        __      _____       __ 
    / ___/__  ___/ /__   / ___/__    / / 
   / /__/ _ \/ _  / -_) / (_ / _ \_ /_/ 
   \___/\___/\_,_/\__/  \___/\___(_|_)  
""","red")
print colored("""                                           
version 1.0.0                                  
created : belalangsengat            
email   : belalangsengat@yahoo.com  
                                              
..::OPTION::..
1.lihat file yang ada 
2.buat file
3.eksekusi file
4.about me          
5.keluar""","blue")
pilih =raw_input("pilih> ")
if pilih == "1" and "lihat file yang ada":
 os.system('ls')
 pilih2 =raw_input("Apakah anda ingin mengedit file?y/n> ")
 if pilih2 == "y" and "iya":
  print colored("pilih text editor","green")
  print colored("1.nano","red")
  print colored("2.gedit*di rekomendasikan untuk ubuntu","blue")
  pilih3 =raw_input("no?> ")
  if pilih3 == "1" and "satu":
   print colored(" Anda Memilih nano","yellow")
   os.system("sh pilih4.sh")
  if pilih3 == "2" and "dua":
   print colored("anda memilih gedit","red")
   os.system("sh a1.sh")
   input("click")
   os.system("python2 codego.py")
if pilih == "2" and "buat file":
 print colored("""
                                          
   ___            __    _____ __    
  / _ )__ _____ _/ /_  / __(_) /__  
 / _  / // / _ `/ __/ / _// / / -_) 
/____/\_,_/\_,_/\__/ /_/ /_/_/\__/  
                                    ""","red")
 print colored("""        ..::CATATAN::..
...:::cara membuat file yaitu dengan menuliskan nama file beserta ekstensinya:::...
contoh : index.html
""","green")
 os.system("sudo sh buat.sh")
 print colored("""file telah terbuat""","green")
if pilih == "3" and "tiga":
 print colored("""
 __|                  |        \ \   / _ | 
 _| \ \ /   _|  |  |   _|   -_) \ \ /    | 
___| _\_\ \__| \_,_| \__| \___|  \_/    _| 
""","red")
 print colored("pilh brother","red")
 print colored("1.exe python","blue")
 print colored("2.exe php","green")
 print colored("3.exe html","red")
 print colored("[?]di versi selanjutnya akan di perbanyak lagi![?]","blue")
 pilih5 =raw_input("exe no?> ")
 if pilih5 == "1" and "exe python" and "satu":
  os.system("sh py.sh")
 if pilih5 == "2" and "exe php" and "tiga":
  print colored("[?]Anda akan menjalankan local host[?]","red")
  os.system("sleep 3")
  os.system("sh ph.sh")
 if pilih5 == "3" and "exe html" and "tiga":
  print colored("[?]jika anda sudah mengaktifkan localhost[?]","red")
  print colored("[?]anda bisa langsung ke browser dan mengetikan path[?]","red")
  print colored("[?]ex. file:///home/rezky/[?]","red")
  print colored("[?]anda bisa membatlkan opsi ini dengan ctrl+c[?]","red")
  os.system("sh ph.sh")
if pilih == "4" and "4":
 os.system("toilet --gay -f bigmono12 -t 'rezky'")
 print colored(""" PRoject name : codego.py""","blue")
 print colored(""" version      : codego.py""","green")
 print colored(""" Creator name : Muh.rezky ananda""","red")
 print colored("""Terima kasih telah meggunakan project saya 
jika nemu bug atau ingin menambahkan saran bisa langsung komen di blog saya atau email saya
dan project ini akan di kembangkan untuk memberikan lebih banyak kenyamanan
sekian dan terima kasih assalamualaikum.wr.eb
1.email
2.blog saya""","blue")
 os.system("toilet --gay -f circle -t 'copyright rezky2020'")
 pilih6 =raw_input("hai;> ")
 if pilih6 == "1" and "email" and "satu":
  os.system("xdg-email")
 if pilih6 == "2" and "blog saya" and "dua":
  os.system("xdg-open https:///anak-tik.blogspot.com")
if pilih == "5" and "lima":
 exit()
else:
 os.system("python2 codego.py")
