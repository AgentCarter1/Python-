i=1
while i<2:
    print("Lütfen Gerçekleştirmek İstediğiniz Dönüştürme Biçimini Seçiniz.")
    print("1-)Sıcaklık\n2-)Uzunluk\n")
    choice=input("Seçin:")
    if choice == "1":
        print("Lütfen Dönüştürmek İstediğiniz Birimi Seçiniz.")
        print("1-)Celcius\n2-)kelvin\n3-)Fahrenheit\n")
        choice1=input("Seçin:")
        if choice1=="1":
            print("Lütfen Dönüştüreceğiniz Birimi Giriniz.")
            print("1-)Kelvin\n2-)Fahrenheit")
            choice3=input("Seçin:")
            if choice3=="1":  
                celcius=float(input("Celcius Değerini Giriniz."))  
                celcius_to_kelvin=celcius+273
                print(celcius,"Celcius = ",celcius_to_kelvin,"Kelvine Eşittir.")
            elif choice3=="2":
                celcius=float(input("Celcius Değerini Giriniz:"))
                celcius_fahrenheit=(((celcius*9) / 5) + 32)
                print(celcius,"Celcius =",celcius_fahrenheit," Fahrenheite Eşittir.")
        elif choice1=="2":
            print("Lütfen Dönüştüreceğiniz Birimi Giriniz.")
            print("1-)Celcius\2-)Fahrenheit")
            choice_kelvin=input("Seçin:")
            if choice_kelvin=="1":
                kelvin=float(input("Lütfen Kelvin Değerini Giriniz:"))
                kelvin_to_celcius=kelvin-273
                print(kelvin,"Kelvin = ",kelvin_to_celcius,"Celciusa Eşittir.")
            elif choice_kelvin=="2":
                kelvin=float(input("Lütfen Kelvin Değerini Giriniz:"))
                kelvin_to_fahrenheit=(((kelvin-273)*9)/5)+32
                print(kelvin,"Kelvin = ",kelvin_to_fahrenheit,"Fahrenheite Eşittir.")
        elif choice1=="3":
            print("Lütfen Dönüştüreceğiniz Birimi Giriniz.")
            print("1-)Celcius\n2-)Kelvin")
            choice_fahrenheit=input("Seçin:")
            if choice_fahrenheit=="1":
                fahrenheit=float(input("Lütfen Fahrenheit Değerini Giriniz:"))           
                fahrenheit_to_celcius=((fahrenheit-32)*5)/9
                print(fahrenheit,"Fahrenheit = ",fahrenheit_to_celcius,"Celciusa Eşittir.")
            elif choice_fahrenheit=="2":
                fahrenheit=float(input("Lütfen Fahrenheit Değerini Giriniz:"))
                fahrenheit_to_kelvin=(((fahrenheit-32)*5)/9)+273  
                print(fahrenheit,"Fahrenheit = ",fahrenheit_to_kelvin,"Kelvine Eşittir.")
        else:
            i=i+5
            print("Yanlış Seçim Yaptınız Program Sonlandırılıyor.")   
    elif choice=="2":
        print("Lütfen Dönüştürmek İstediğiniz Birimi Giriniz.")
        print("1-)Milimetre(mm)\n2-)Santimetre(cm)\n3-)Metre(m)\n4-)Kilometre(km)")
        choice_birimler=input("Seçin:")
        if choice_birimler=="1":
            print("Lütfen Dönüştüreceğiniz Birimi Giriniz.")
            print("1-)Santimetre(cm)\n2-)Metre(m)\n3-)Kilometre(km)")
            choice_milimetre=input("Seçin:")
            if choice_milimetre=="1":
                milimetre=float(input("Lütfen Milimetre(mm) Değerini Girini:"))
                milimetre_to_cantimetre=milimetre/10
                print(milimetre,"Milimetre = ",milimetre_to_cantimetre,"Santimetredir.")
            elif choice_milimetre=="2":
                milimetre=float(input("Lütfen Milimetre(mm) Değerini Girini:"))
                milimetre_to_metre=milimetre/1000
                print(milimetre,"Milimetre = ",milimetre_to_metre,"Metredir.")
            elif choice_milimetre=="3":
                milimetre=float(input("Lütfen Milimetre(mm) Değerini Girini:"))
                milimetre_to_kilometre=milimetre/1000000
                print(milimetre,"Milimetre = ",milimetre_to_kilometre,"Kilometredir.")    
        elif choice_birimler=="2":
            print("Lütfen Dönüştüreceğiniz Birimi Giriniz.")
            print("1-)Milimetre(mm)\n2-)Metre(m)\n3-)Kilometre(km)")
            choice_santimetre=input("Seçin:")
            if choice_santimetre=="1":
                santimetre=float(input("Lütfen Santimetre(cm) Değerini Giriniz"))
                santimetre_to_milimetre=santimetre*10
                print(santimetre,"Santimetre(cm) = ",santimetre_to_milimetre,"Milimetreye(mm) Eşittir.")
            elif choice_santimetre=="2":
                santimetre=float(input("Lütfen Santimetre(cm) Değerini Giriniz"))
                santimetre_to_metre=santimetre/100
                print(santimetre,"Santimetre(cm) = ",santimetre_to_metre,"Metreye(m) Eşittir.")
            elif choice_santimetre=="3":
                santimetre=float(input("Lütfen Santimetre(cm) Değerini Giriniz"))
                santimetre_to_kilometre=santimetre/100000
                print(santimetre,"Santimetre(cm) = ",santimetre_to_kilometre,"Kilometreye(km) Eşittir.")
        elif choice_birimler=="3":
            print("Lütfen Dönüştüreceğiniz Birimi Giriniz.")
            print("1-)Milimetre(mm)\n2-)Santimetre(cm)\n4-)Kilometre(km)")
            choice_metre=input("Seçin:")
            if choice_metre=="1":
                metre=float(input("Lütfen Metre(m) Değerini Giriniz:"))
                metre_to_milimetre=metre*1000
                print(metre,"Metre(m) = ",metre_to_milimetre,"Milimetreye(mm) Eşittir.")
            elif choice_metre=="2":
                metre=float(input("Lütfen Metre(m) Değerini Giriniz:"))
                metre_to_santimetre=metre*100
                print(metre,"Metre(m) = ",metre_to_santimetre,"Santimetreye(cm) Eşittir.")  
            elif choice_metre=="3":
                metre=float(input("Lütfen Metre(m) Değerini Giriniz:"))
                metre_to_kilometre=metre/1000
                print(metre,"Metre(m) = ",metre_to_kilometre,"Kilometreye(km) Eşittir.")
        elif choice_birimler=="4":
            print("Lütfen Dönüştüreceğiniz Birimi Giriniz.")
            print("1-)Milimetre(mm)\n2-)Santimetre\n3-)Metre(m)")
            choice_kilometre=input("Seçin:")
            if choice_kilometre=="1":
                kilometre=float(input("Lütfen Kilometre(km) Değerini Giriniz."))
                kilometre_to_milimetre=kilometre*1000000
                print(kilometre,"Kilometre(km) = ",kilometre_to_milimetre,"Milimetreye(mm) Eşittir.")
            elif choice_kilometre=="2":
                kilometre=float(input("Lütfen Kilometre(km) Değerini Giriniz."))
                kilometre_to_santimetre=kilometre*100000
                print(kilometre,"Kilometre(km) = ",kilometre_to_santimetre,"Santimetreye(cm) Eşittir.")
            elif choice_kilometre=="3":
                kilometre=float(input("Lütfen Kilometre(km) Değerini Giriniz."))
                kilometre_to_metre=kilometre*1000     
                print(kilometre,"Kilometre(km) = ",kilometre_to_metre,"Metreye(m) Eşittir.") 
            else:
                i=i+5
                print("Yanlış Seçim Yaptınız Program Kapatılıyor.")     
    else:
        i=i+5
        print("Yanlış Seçim Yaptınız Program Kapatılıyor.")          
    print("Yeniden Başlatmak için 1'e \n Kapatmak İçin 0'a Basınız.")
    choice_on_of=input("Seçiniz:")
    if choice_on_of=="1":
        i=i+0
    elif choice_on_of=="0":
        i=i+5

        
         

     

    

           

                




        
         

     

    

           

                



