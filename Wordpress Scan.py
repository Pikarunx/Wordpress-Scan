#! usr/bin/env/python
#-*- coding: utf-8 -*-

import os
import time
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet  WORDPRESS SCAN")

print("""
Wordprees Tarama Tooluna Hoş Geldiniz.

1)Hızlı Tarama

2)Eklenti Tarama 

3)Tema Tarama 

4)Admin Kullanıcı Adı Arama

""")

islemno = input("İşlem Numarasını Girin :")

if (islemno == "1"):
	site = input("Site Adresini Girin: ")
	os.system("wpscan --url " + site)
	
	
elif (islemno == "2"):
	site = input("Site Adresini Girin: ")
	os.system("wpscan --url " + site + " --enumerate p ")
	
	
elif (islemno == "3" ):
	site = input("Site Adresini Girin: ")
	os.system("wpscan --url" + site + "enumerate t")
	
	
elif (islemno == "4"):
	site = input("Site Adresini Girin")
	os.system("wpscan --url " + site + "enumerate u")
	
else:
	print("Hatalı Seçim Yaptınız.Program Kapatılıyor....")
	time.sleep(0.50)				
